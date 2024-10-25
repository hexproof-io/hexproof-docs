"""
* Commands: Generate Docs
"""
# Standard Library Imports
import os
import subprocess
from os import rmdir
from shutil import rmtree

# Third Party Imports
from omnitils.api.github import gh_download_repository
from omnitils.files import load_data_file, dump_data_file, mkdir_full_perms
from omnitils.logs import logger
from pathlib import Path
from typer import Typer

# Local Imports
from hexdoc._constants import PATH_PROJECTS_YML, PATH_MKDOCS_YML, SITE_URL, PATH_MAIN, BASE_URL
from hexdoc.schema import Project
from hexdoc.utils.imports import import_defaults, import_includes
from hexdoc.utils.nav import get_nav_tree

cli_gen = Typer(name='gen')

"""
* Commands
"""


@cli_gen.command('.')
def generate_all() -> None:
    """Generates Markdown docs for all projects defined in `projects.yml`."""

    # Generate docs for each project
    logger.info('Generating docs for all projects ...')
    [generate_project(n) for n in load_data_file(PATH_PROJECTS_YML).keys()]

    # Generate docs for the top-level site
    generate_main()


@cli_gen.command('main')
def generate_main() -> None:
    """Generates Markdown docs for the 'main' top-level site."""
    logger.info('Generating docs for main site ...')

    # Inject our site URL
    _cfg = load_data_file(PATH_MKDOCS_YML)
    _cfg['site_url'] = BASE_URL
    _repo_dir = PATH_MAIN / 'repo'

    # Remove repo if present
    if _repo_dir.is_dir():
        rmtree(_repo_dir)
        if _repo_dir.is_dir():
            rmdir(_repo_dir)
    mkdir_full_perms(_repo_dir)
    dump_data_file(_cfg, Path(_repo_dir, 'mkdocs.yml'))

    # Import Files
    import_defaults(PATH_MAIN)

    # Build static site
    subprocess.call(f'cd projects/main/repo && mkdocs build -f mkdocs.yml', shell=True)
    logger.success('Documentation generated!')


@cli_gen.command('project')
def generate_project(project: str) -> None:
    """Generates Markdown docs for a specific project, based on the configuration provided in `projects.yml`.

    Args:
        project (str): The name of the project.
    """
    project_name = project.lower().strip()
    logger.info(f'Generating docs: {project_name} ...')
    if project_name == 'main':
        return logger.error('A project cannot be named "main" as this conflicts with the top-level site!')

    # Load project configuration
    cfg_projects = load_data_file(PATH_PROJECTS_YML)
    if project_name not in cfg_projects:
        return logger.warning(f"Project '{project}' not found in projects.yml!")
    try:
        project = Project(name=project_name, **cfg_projects[project_name])
    except Exception as e:
        logger.error((str(e)))
        return logger.warning(f'Failed to generate schema for project: {project_name}')

    # Load main config, import defaults
    cfg_mkdocs = load_data_file(PATH_MKDOCS_YML)

    # Remove repo if present
    """if project.path_repo.is_dir():
        rmtree(project.path_repo)
        if project.path_repo.is_dir():
            rmdir(project.path_repo)

    # Clone repo
    try:
        user, repo = project.repo.split('/')
        _repo = gh_download_repository(user, repo, path=project.path_root)
        os.rename(_repo, _repo.with_name('repo'))
    except Exception as e:
        logger.error(f"Failed to download repository: {e}")
    """
    import_defaults(project.path_root)

    # Update mkdocs metadata
    cfg_mkdocs.update(dict(
        **project.meta.model_dump(),
        site_url=SITE_URL.format(project_name)
    ))

    # Update mkdocstrings plugin path
    for _plugin in cfg_mkdocs['plugins']:
        if 'mkdocstrings' in _plugin:
            _plugin['mkdocstrings']['handlers']['python']['paths'] = ['repo']

    # Add additional plugins
    cfg_mkdocs.setdefault('plugins', []).extend(project.plugins)

    # Add CSS
    cfg_mkdocs.setdefault('extra_css', []).extend(project.css)

    # Update navigation
    _found = False
    for _nav_item in cfg_mkdocs['nav']:

        # Replace main navigation
        if 'About' in _nav_item:
            _nav_item['About'] = '/../'

        # Replace project navigation
        if not _found and project.title in _nav_item:
            _nav_item[project.title] = get_nav_tree(project)
            _found = True

    # Log missing
    if not _found:
        logger.warning('Project not found in main `mkdocs.yml` navigation tree!')

    # Import repo-included files
    import_includes(project)

    # Save mkdocs configuration file
    dump_data_file(cfg_mkdocs, project.path_mkdocs, config=dict(sort_keys=False))

    # Build static site
    subprocess.call(f'cd ./projects/{project.name}/repo && mkdocs build -f mkdocs.yml', shell=True)
    logger.success('Documentation generated!')
