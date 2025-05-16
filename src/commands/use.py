import click
import os
import shutil
from src.utils import complete_env_vars
from src.utils import ENV_DIR
from src.cli import envm


@envm.command()
@click.option('--envfile', default=".env", help='Name of the file to be saved')
@click.option('--overwrite/--no-overwrite', default=False, help='Overwrite env name')
@click.argument('name', shell_complete=complete_env_vars)
def use(envfile, name, overwrite):
    """Use the environment file in the current path.
    Default write as .env file
    """
    path = f"{ENV_DIR}/{name}"

    if not os.path.exists(path) or not os.path.isfile(path):
        click.secho(f"{name} environment is not saved", blink=True, bold=True, fg="red")
        return

    if os.path.exists(f"{envfile}") and not overwrite:
        click.confirm(f"{envfile} file actually exists in the current directory. Do you want to override?", abort=True)

    shutil.copyfile(path, f"{envfile}")
    click.secho(f"{name} written as {envfile}", fg="green")
