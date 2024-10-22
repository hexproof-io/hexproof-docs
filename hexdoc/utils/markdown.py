"""
* Utils: Markdown
"""
# Standard Library Imports
import ast
import os
import shutil
from pathlib import Path
from typing import Optional

# Third Party Imports
from omnitils.files import mkdir_full_perms
from omnitils.logs import logger

# Local Imports
from hexdoc.schema import Project


def collect_markdown_file(project: Project, file: str) -> Optional[str]:
    """Collect a markdown file from source location and place it in docs directory.

    Args:
        project (Project): A `Project` object instance.
        file (str): File path within the project and within the target docs directory.

    Returns:
        Relative string path inside doc directory.
    """
    file_to = file.lower()
    if file_to.endswith('readme.md'):
        file_to = file_to[:-9] + 'index.md'
    path_from = project.path_repo / file
    path_to = project.path_docs / file_to
    if not path_from.is_file():
        logger.warning(f'MD file from project navigation not found: {file}')
        return
    if path_to.exists():
        os.remove(path_to)
    shutil.copy2(path_from, path_to)
    return file_to


def generate_markdown_file(
    project: Project,
    module: str,
    module_path: Path,
    dir_path: list[str] | None = None
) -> str | list[dict] | None:
    """Generates a markdown file from a source file using the provided options.

    Args:
        project (Project): A `Project` object instance.
        module (str): Import path to a python module.
        module_path (Path): Path to a python module.
        dir_path (list[str]): List tracking relative pathing to this docs item.

    Returns:
        Relative string path inside doc directory.
    """
    _T = '    '
    if dir_path is None:
        dir_path = []
    if not module_path.is_file():
        return
    title = module.split('.')[-1].title().replace('_', ' ').strip()

    # Get functions and classes
    funcs, classes = [], []
    with open(module_path, 'r', encoding='utf-8') as file:
        for node in ast.parse(file.read()).body:
            if isinstance(node, ast.FunctionDef):
                funcs.append(f"{module}.{node.name}")
            elif isinstance(node, ast.ClassDef):
                classes.append(f"{module}.{node.name}")
        if not classes and not funcs:
            return

    # Only functions: Single markdown file
    if not classes:
        md_path = Path(project.path_docs, *dir_path, module_path.name).with_suffix('.md')
        _options = f'\n{_T}{_T}'.join([f"{k}: {v}" for k, v in project.options.docstrings.functions])
        if not md_path.parent.is_dir():
            mkdir_full_perms(md_path.parent)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n\n")
            for _func in funcs:
                f.write(
                    f"::: {_func}\n"
                    f"{_T}options:\n"
                    f"{_T}{_T}{_options}\n\n")
        return '/'.join([*dir_path, md_path.name])

    # Add class tree to tree
    _tree: list[dict] = []
    _parent = Path(project.path_docs, *dir_path) / module_path.stem
    if not _parent.is_dir():
        mkdir_full_perms(_parent)
    if classes:
        _classes = []
        for _cls in classes:
            _cls_name = _cls.split('.')[-1]
            _cls_path = (_parent / _cls_name.lower()).with_suffix('.md')
            _classes.append({_cls_name: '/'.join([*dir_path, module_path.stem, _cls_path.name])})
            _options = f'\n{_T}{_T}'.join([f"{k}: {v}" for k, v in project.options.docstrings.classes])
            with open(_cls_path, 'w', encoding='utf-8') as f:
                f.write(
                    f"# {_cls_name}\n\n"
                    f"::: {_cls}\n"
                    f"{_T}options:\n"
                    f"{_T}{_T}{_options}\n\n")
        _tree.append({'Classes': _classes})

    # Add functions file to tree
    if funcs:
        _func_path = _parent / 'functions.md'
        _tree.append({
            'Functions': '/'.join([*dir_path, module_path.stem, 'functions.md'])})
        _options = f'\n{_T}{_T}'.join([f"{k}: {v}" for k, v in project.options.docstrings.functions])
        with open(_func_path, 'w', encoding='utf-8') as f:
            f.write(f"# Functions\n\n")
            for _func in funcs:
                f.write(
                    f"::: {_func}\n"
                    f"{_T}options:\n"
                    f"{_T}{_T}{_options}\n"
                    f"\n---\n\n")

    # Return relative string path to doc file
    return _tree
