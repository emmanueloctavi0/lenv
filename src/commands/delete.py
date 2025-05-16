import os
import click
from src.cli import envm
from src.utils import complete_env_vars
from src.utils import ENV_DIR


@envm.command()
@click.option('--force/--no-force', default=False, help='force delete')
@click.argument('name', shell_complete=complete_env_vars)
def delete(name, force):
    """Delete the environment
    """
    path = f"{ENV_DIR}/{name}"

    if not os.path.exists(path) or not os.path.isfile(path):
        click.secho(f"{name} environment does not exist", blink=True, bold=True, fg="red")
        return

    if os.path.exists(f"{path}") and not force:
        click.confirm(f"Do you want to delete {name} environment?", abort=True)

    os.remove(path)
    click.secho(f"{name} deleted", fg="green")
