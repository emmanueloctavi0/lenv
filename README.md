CLI to manage environment variables. This tool was created to simplify working with multiple .env files across different projects and environments (development, staging, and local).

## Installation

To install the package, simply run:

```bash
pip install envm
```

## Commands

### save
Save the current environment file to the environments database. By default, it looks for a `.env` file in the current directory.

Options:
- `--envfile`: Specify a different environment file name (default: `.env`)
- `--overwrite/--no-overwrite`: Overwrite existing environment if it exists (default: false)

```bash
$ envm save users.dev
$ envm save users.dev --envfile .env.prod
$ envm save users.dev --overwrite
```

### ls
List all your saved environment files. Shows a count of total environments at the end.

```bash
$ envm ls
```

### use
Create an environment file in the current directory from a saved environment. By default, it creates a `.env` file.

Options:
- `--envfile`: Specify a different output file name (default: `.env`)
- `--overwrite/--no-overwrite`: Overwrite existing file if it exists (default: false)

```bash
$ envm use users.dev
$ envm use users.dev --envfile .env.prod
$ envm use users.dev --overwrite
```

### delete
Delete a saved environment file. Use `--force` to skip confirmation:
```bash
$ envm delete users.dev
$ envm delete users.dev --force
```

## Enable Shell Completion

Enable autocompletion for your environment variable files

### zsh
```shell
curl https://raw.githubusercontent.com/emmanueloctavi0/envm/refs/heads/main/src/completion/envm_complete.zsh >> ~/.zshrc
```

### bash
```shell
curl https://raw.githubusercontent.com/emmanueloctavi0/envm/refs/heads/main/src/completion/envm_complete.bash >> ~/.bashrc
```
