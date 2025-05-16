import click
import os
from click import format_filename
from src.cli import envm
from src.utils import ENV_DIR


@envm.command()
def ls():
    """List all environments saved
    """
    path = f"{ENV_DIR}"

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    files.sort()

    for _file in files:
        click.secho(f"- {format_filename(_file)}", fg="green")

    click.secho(f"\n{len(files)} environments saved", fg="green")
