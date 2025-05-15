
Command to manage environments variables, the idea is because everyday I have to work with .env files with different projects and environments like dev, staging and local.

Examples:

1. Save the current .env (environment) file in the database environments
```bash
$ lenv save users.dev
```

2. Use a file called .env in my current path:
```bash
$ lenv use users.dev
```

3. (WIP) The next command should "export" the environments in my current shell session:
```bash
lenv export users.dev
```

4. (WIP) Clean my current env space (--lenv flag is optional)
```bash
lenv clean --lenv users.prod
```
