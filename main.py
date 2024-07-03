import click
import shutil
import os


ENV_DIR = "/home/emma/.lenv/environments"


@click.group()
def cli():
    """Manage your environment variables with a simple CLI"""
    pass


@cli.command()
@click.option('--envfile', default=".env", help='Name of the file to be saved')
@click.option('--overwrite/--no-overwrite', default=False, help='Overwrite env name')
@click.argument('name')
def save(envfile, name, overwrite):
    """Save the environment from the .env file"""
    if not os.path.exists(envfile) or not os.path.isfile(envfile):
        click.secho(f"{envfile} file is not present in the current path", blink=True, bold=True, fg="red")
        return

    if os.path.exists(f"{ENV_DIR}/{name}") and not overwrite:
        click.confirm(f"{name} env currently exists. You want to override?")

    shutil.copyfile(envfile, f"{ENV_DIR}/{name}")
    click.secho(f"{envfile} saved as {name}", fg="green")


if __name__ == '__main__':
    cli()
