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


class ProjectOptionTreeDocstringsKeys(Schema):
    """Keys for the Mkdocstrings option tree in a defined project."""
    show_root_members_full_path: bool = False
    show_category_heading: bool = True
    show_root_full_path: bool = False
    show_root_heading: bool = True


class ProjectOptionTreeDocstrings(Schema):
    """Mkdocstrings option tree for a defined project."""
    classes: ProjectOptionTreeDocstringsKeys = Field(default_factory=ProjectOptionTreeDocstringsKeys)
    functions: ProjectOptionTreeDocstringsKeys = Field(default_factory=ProjectOptionTreeDocstringsKeys)


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
    def path_root(self) -> Path:
        return Path(PATH_PROJECTS, self.name)

    @computed_field
    @cached_property
    def path_docs(self) -> Path:
        return Path(self.path_root, 'docs')

    @computed_field
    @cached_property
    def path_repo(self) -> Path:
        return Path(self.path_root, 'repo')

    @computed_field
    @cached_property
    def path_site(self) -> Path:
        return Path(self.path_root, 'site')

    @computed_field
    @cached_property
    def path_overrides(self) -> Path:
        return Path(self.path_root, 'overrides')

    @computed_field
    @cached_property
    def path_static(self) -> Path:
        return Path(self.path_root, 'static')

    @computed_field
    @cached_property
    def repo(self) -> str:
        return self.meta.repo_name


"""
* Types
"""


# Documentation tree
# Todo: Add support for fully recursive tree
DocTreeItem = ProjectDocCollect | ProjectDocGenerate | ProjectDocStatic
DocTree = dict[str, dict[str, DocTreeItem] | DocTreeItem]
