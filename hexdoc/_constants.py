"""
* Project Constants
"""
# Standard Library Imports
from os import environ
from pathlib import Path

# Paths
CWD = Path(__file__).parent.parent
PATH_COMMON = CWD / 'common'
PATH_PROJECTS = CWD / 'projects'
PATH_MAIN = PATH_PROJECTS / 'main'
PATH_PROJECTS_YML = CWD / 'projects.yml'
PATH_MKDOCS_YML = CWD / 'mkdocs.yml'

# Site information
BASE_URL = environ.get('MKDOCS_BASE_URL', 'https://hexproof.io')
SITE_URL = BASE_URL + '/{}'
