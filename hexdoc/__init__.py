"""
* CLI Module
"""
# Third Party Imports
from typer import Typer

# Local Imports
from hexdoc.generate import cli_gen


# Export CLI
cli_app = Typer()
cli_app.add_typer(cli_gen)
__all__ = ['cli_app']
