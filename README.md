CLI to manage environment variables. This tool was created to simplify working with multiple .env files across different projects and environments (development, staging, and local).

## Installation

To install the package, simply run:

```bash
pip install envm
```

## Commands

### save
Save the current .env file to the environments database:
```bash
$ envm save users.dev
```

### ls
List all your saved environment files:
```bash
$ envm ls
```

### use
Create a .env file in the current directory:
```bash
$ envm use users.dev
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
