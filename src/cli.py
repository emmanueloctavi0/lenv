import click
import os
from src.utils import ENV_DIR


@click.group()
def envm():
    """Manage your environment variables with a simple CLI"""
    if not os.path.exists(ENV_DIR):
        os.mkdir(ENV_DIR)


# Export the group
__all__ = ['envm', 'ENV_DIR'] 
