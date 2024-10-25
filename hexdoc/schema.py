"""
* Schemas
"""
# Standard Library Imports
from pathlib import Path
from typing import Literal
from functools import cached_property

# Third Party Imports
from omnitils.schema import Schema
from pydantic import Field, computed_field

# Local Imports
from hexdoc._constants import PATH_PROJECTS

"""
* Schemas: Project Configuration
"""


class ProjectMeta(Schema):
    """Mkdocs metadata from a defined Project."""
    repo_name: str
    repo_url: str
    remote_branch: str


class ProjectOptionTreeDocstrings(Schema):
    """Mkdocstrings option tree for a defined project."""
    classes: dict = Field(default_factory=dict)
    functions: dict = Field(default_factory=dict)


class ProjectOptionTree(Schema):
    """Option tree for a defined project."""
    docstrings: ProjectOptionTreeDocstrings = Field(default_factory=ProjectOptionTreeDocstrings)


"""
* Schemas: Doc Tree
"""


class ProjectDocCollect(Schema):
    """Collect-type Doc entry from a defined Project."""
    type: Literal['collect']
    file: str


class ProjectDocGenerate(Schema):
    """Generate-type Doc entry from a defined Project."""
    type: Literal['generate']
    src: str


class ProjectDocStatic(Schema):
    """Collect-type Doc entry from a defined Project."""
    type: Literal['static']
    file: str


"""
* Schemas: Main
"""


class Project(Schema):
    """A Project definition from `projects.yml` file."""
    title: str
    name: str
    meta: ProjectMeta
    docs: 'DocTree'
    include: list[str] = Field(default_factory=list)
    plugins: list[str | dict] = Field(default_factory=list)
    options: ProjectOptionTree = Field(default_factory=ProjectOptionTree)
    css: list[str] = Field(default_factory=list)

    @computed_field
    @cached_property
    def repo(self) -> str:
        return self.meta.repo_name

    # Top-Level Directories

    @computed_field
    @cached_property
    def path_root(self) -> Path:
        return PATH_PROJECTS / self.name

    @computed_field
    @cached_property
    def path_static(self) -> Path:
        return self.path_root / 'static'

    # Repository Directories

    @computed_field
    @cached_property
    def path_repo(self) -> Path:
        return self.path_root / 'repo'

    @computed_field
    @cached_property
    def path_docs(self) -> Path:
        return self.path_repo / 'docs'

    @computed_field
    @cached_property
    def path_site(self) -> Path:
        return self.path_repo / 'site'

    @computed_field
    @cached_property
    def path_overrides(self) -> Path:
        return self.path_repo / 'overrides'

    @computed_field
    @cached_property
    def path_mkdocs(self) -> Path:
        return self.path_repo / 'mkdocs.yml'


"""
* Types
"""


# Documentation tree
# Todo: Add support for fully recursive tree
DocTreeItem = ProjectDocCollect | ProjectDocGenerate | ProjectDocStatic
DocTree = dict[str, dict[str, DocTreeItem] | DocTreeItem]
