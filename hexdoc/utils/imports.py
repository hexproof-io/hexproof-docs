"""
* Handles Importing Files
"""
# Standard Library Imports
from pathlib import Path
from shutil import rmtree, copytree, copy2, SameFileError

# Local Imports
from hexdoc._constants import PATH_COMMON
from hexdoc.schema import Project
from omnitils.logs import logger


def import_defaults(root_dir: Path) -> None:
    """Removes previously generated doc files and imports common and static files to a project.

    Args:
        root_dir (Path): Root directory of the project.
    """
    _overrides_dir = root_dir / 'overrides'
    _static_dir = root_dir / 'static'
    _docs_dir = root_dir / 'docs'

    # Remove current docs and overrides
    if _docs_dir.is_dir():
        rmtree(_docs_dir)
    if _overrides_dir.is_dir():
        rmtree(_overrides_dir)

    # Add common files
    copytree(
        PATH_COMMON,
        root_dir,
        dirs_exist_ok=True)

    # Add docs files
    if _static_dir.is_dir():
        copytree(
            _static_dir,
            root_dir,
            dirs_exist_ok=True)


def import_includes(project: Project) -> None:
    """Import included files from project repository.

    Args:
        project (Project): A `Project` instance.
    """

    # Check for includes
    if project.include:
        for _item in project.include:
            _from = project.path_repo / _item
            _to = project.path_docs / _item
            try:
                if _from.is_dir():
                    copytree(_from, _to, dirs_exist_ok=True)
                elif _from.is_file():
                    copy2(_from, _to)
                else:
                    logger.warning(f"Defined inclusion doesn't match any files: {_from}")
            except (PermissionError, FileExistsError, IOError, SameFileError):
                logger.warning(f"Couldn't import item from list of inclusions: {_from}")
