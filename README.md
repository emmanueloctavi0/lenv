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
- `--direnv`: Generate `.envrc` file for automatic environment loading with direnv

```bash
$ envm use users.dev
$ envm use users.dev --envfile .env.prod
$ envm use users.dev --overwrite
$ envm use users.dev --direnv  # Automatic environment loading
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

## Automatic Environment Loading with direnv

For automatic loading/unloading of environment variables when entering/leaving directories, use the `--direnv` flag with the `use` command.

### What is direnv?
[direnv](https://direnv.net/) automatically loads environment variables based on the current directory. Variables are loaded when you enter a directory and unloaded when you leave it.

### Quick Setup
```bash
# 1. Use envm with direnv integration
$ envm use users.dev --direnv

# If direnv is not installed, envm will show installation instructions
# If direnv is installed, it will:
# - Generate .envrc file
# - Ask if you want to run 'direnv allow' automatically

# 2. That's it! Environment variables now load automatically
$ cd /your/project     # Variables loaded automatically
$ echo $DATABASE_URL   # Variable is available
$ cd /another/project  # Variables unloaded automatically
$ echo $DATABASE_URL   # Variable no longer available
```

### Manual direnv Setup
If you prefer to set up direnv manually:

1. **Install direnv:**
   ```bash
   # Ubuntu/Debian
   sudo apt install direnv
   
   # macOS
   brew install direnv
   ```

2. **Add hook to your shell:**
   ```bash
   # Bash: Add to ~/.bashrc
   eval "$(direnv hook bash)"
   
   # Zsh: Add to ~/.zshrc
   eval "$(direnv hook zsh)"
   
   # Fish: Add to ~/.config/fish/config.fish
   direnv hook fish | source
   ```

3. **Restart your terminal and use:**
   ```bash
   $ envm use users.dev --direnv
   $ direnv allow  # If not done automatically
   ```

### Benefits of direnv Integration
- ✅ **Automatic**: Variables load/unload when entering/leaving directories
- ✅ **Isolated**: Each project has its own environment scope
- ✅ **Secure**: Requires explicit permission per directory
- ✅ **Standard**: Uses industry-standard tooling
- ✅ **Team-friendly**: `.envrc` files can be shared with your team
