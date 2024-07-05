import click
from click import format_filename
import shutil
import os

import click.shell_completion


ENV_DIR = click.get_app_dir("lenv")


@click.group()
def lenv():
    """Manage your environment variables with a simple CLI"""
    if not os.path.exists(ENV_DIR):
        os.mkdir(ENV_DIR) 


@lenv.command()
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


def complete_env_vars(ctx, param, incomplete):
    envs = [f for f in os.listdir(ENV_DIR) if os.path.isfile(os.path.join(ENV_DIR, f))]
    return [format_filename(item) for item in envs if item.startswith(incomplete)]


@lenv.command()
@click.option('--envfile', default=".env", help='Name of the file to be saved')
@click.option('--overwrite/--no-overwrite', default=False, help='Overwrite env name')
@click.argument('name', shell_complete=complete_env_vars)
def write(envfile, name, overwrite):
    """Write the environment file in the current path.
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


@lenv.command()
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


@lenv.command()
def ls():
    """List all environments saved
    """
    path = f"{ENV_DIR}"

    files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

    for _file in files:
        click.secho(f"- {format_filename(_file)}", fg="green")

    click.secho(f"\n{len(files)} environments saved", fg="green")


if __name__ == '__main__':
    lenv()
