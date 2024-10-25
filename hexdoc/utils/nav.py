"""
* Mkdocs Navigation Utilities
"""
# Standard Library Imports
from typing import Optional

# Third Party Imports
from omnitils.logs import logger

# Local Imports
from hexdoc.schema import DocTreeItem, Project, ProjectDocStatic, ProjectDocCollect, ProjectDocGenerate
from hexdoc.utils.markdown import collect_markdown_file, generate_markdown_file


def get_nav_item_generated(
    project: Project,
    module: str,
    dir_path: Optional[list[str]] = None
) -> Optional[str | list[dict]]:
    """Create one or more navigation items from a module-generated item.

    Args:
        project (Project): A `Project` instance.
        module (str): Path to a Python module in project source.
        dir_path (Optional[list[str]]): List tracking relative pathing to this docs item.

    Returns:
        A string or list of dictionaries representing navigation items.
    """
    if dir_path is None:
        dir_path = []

    # Get the Python source file
    src_path = project.path_repo
    for _node in module.split('.'):
        src_path = src_path / _node

    # Generate markdown for each file in directory
    if src_path.is_dir():
        _tree = []
        _modules = [n for n in src_path.iterdir() if n.is_dir()]
        _modules.extend([n for n in src_path.iterdir() if not n.is_dir()])
        for _next in sorted(_modules, key=lambda x: x.stem):
            _module = f"{module}.{_next.stem}"
            _title = _next.stem.title().replace('_', ' ').strip()
            _item = get_nav_item_generated(
                project=project,
                module=_module,
                dir_path=[*dir_path, src_path.stem])
            if _item is not None:
                _tree.append({_title: _item})
        return _tree

    # Generate markdown for a python file
    src_path = src_path.with_suffix('.py')
    if src_path.is_file():
        if src_path.name == '__init__.py':
            return
        return generate_markdown_file(
            project=project,
            module=module,
            module_path=src_path,
            dir_path=dir_path)

    # Couldn't locate module
    logger.warning(f'Module from project navigation not found: {module}')
    return


def get_nav_item(project: Project, doc_item: DocTreeItem) -> Optional[str | list[dict]]:
    """Create a navigation item to inject into a navigation tree.

    Args:
        project (Project): A `Project` instance.
        doc_item (DocTreeItem): A `DocTreeItem` instance.

    Returns:
        A string or list of dictionaries representing navigation items.
    """
    if isinstance(doc_item, ProjectDocStatic):
        # Static MD file
        return doc_item.file.lower()
    if isinstance(doc_item, ProjectDocCollect):
        # MD file collected from source
        return collect_markdown_file(
            project=project,
            file=doc_item.file)
    if isinstance(doc_item, ProjectDocGenerate):
        # MD file generated from configuration
        return get_nav_item_generated(
            project=project,
            module=doc_item.src)
    if isinstance(doc_item, dict):
        # MD files from tree node
        _tree = []
        for k, v in doc_item.items():
            _item = get_nav_item(
                project=project,
                doc_item=v)
            if _item:
                _tree.append({k: _item})
        return _tree
    # Matched no known data structure
    logger.warning(f'Nav item matched no known data structure:\n{doc_item}')
    return


def get_nav_tree(project: Project) -> list[dict[str, str | list[dict]]]:
    """Create a navigation tree for a given project to inject into an `mkdocs.yml` configuration.

    Args:
        project (Project): A `Project` instance.

    Returns:
        list[dict[str, str | list[dict]]]: A list of dictionaries representing a navigation tree.
    """
    _tree: list[dict[str, str | list[dict]]] = []
    for k, v in project.docs.items():
        _item = get_nav_item(project, v)
        if _item and isinstance(_item, dict):
            for _nav, _page in _item.items():
                if _nav == k:
                    _tree.append(_page)
                else:
                    _tree.append(_item)
        elif _item:
            _tree.append({k: _item})
    return _tree
