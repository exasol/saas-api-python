# SaaS API for Python &mdash; Developer Guide

## Git Pre-Commit Hooks

saas-api-python includes a file `.pre-commit-config.yaml`.

The following command installs the pre-commit hooks, see also [framework pre-commmit](https://pre-commit.com/) and Git
documentation on [Customizing Git Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks):

```shell
poetry run pre-commit install
```

When the hooks are installed, then git will run each of the hooks on the resp. stage, e.g. before executing a commit.
