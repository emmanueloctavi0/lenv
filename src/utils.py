import os
from click import format_filename
import click


ENV_DIR = click.get_app_dir("envm")


def complete_env_vars(ctx, param, incomplete):
    envs = [f for f in os.listdir(ENV_DIR) if os.path.isfile(os.path.join(ENV_DIR, f))]
    return [format_filename(item) for item in envs if item.startswith(incomplete)]
