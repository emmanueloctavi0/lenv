import click
import os
import shutil
from src.cli import envm
from src.utils import ENV_DIR


@envm.command()
@click.option('--envfile', default=".env", help='Name of the file to be saved')
@click.option('--overwrite/--no-overwrite', default=False, help='Overwrite env name')
@click.argument('name')
def save(envfile, name, overwrite):
    """Save the environment from the .env file"""
    if not os.path.exists(envfile) or not os.path.isfile(envfile):
        click.secho(f"{envfile} file is not present in the current path", blink=True, bold=True, fg="red")
        return

    path = f"{ENV_DIR}/{name}"

    if os.path.exists(path) and not overwrite:
        click.confirm(f"{name} env currently exists. You want to override?", abort=True)

    shutil.copyfile(envfile, path)
    click.secho(f"{envfile} saved as {name}", fg="green")
