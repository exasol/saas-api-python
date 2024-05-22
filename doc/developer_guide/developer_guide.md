# SaaS API for Python &mdash; Developer Guide

## Git Pre-Commit Hooks

saas-api-python includes a file `.pre-commit-config.yaml`.

The following command installs the pre-commit hooks, see also [framework pre-commmit](https://pre-commit.com/) and Git documentation on [Customizing Git Git Hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks):

```shell
poetry run pre-commit install
```

When the hooks are installed, then git will run each of the hooks on the resp. stage, e.g. before executing a commit.

## Generate the API Model

The model layer of this API has been generated from the OpenAPI specification in JSON format of the SaaS API https://cloud.exasol.com/openapi.json using [openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

See also [API Documentation](https://docs.exasol.com/saas/administration/rest_api/rest_api.htm) and [Swagger UI](https://cloud.exasol.com/openapi/index.html).

In order to regenerate the model layer please use the following command line:

```shell
poetry run nox generate-api
```

### Change the Source URL of the API Model JSON Definition

If you want to retrieve the JSON definition for the API model from a different source then just edit file `noxfile.py`.

### Read JSON definition From a Local File

Use CLI option `--path` to read the JSON definition from a local file instead of a URL:

```python
"--path", "/path/to/openapi.json",
```

### Generate file `pyproject.toml`

openapi-python-client reads the JSON specification of the SaaS API and generates a python client. The generated client code requires transitive dependencies, though, which need to be added to file `pyproject.toml` to make them available for dependents of SAPIPY.

The easiest way is to make openapi-python-client create a dedicated file `pyproject.toml` and copy the transitive dependencies from there to SAPIPY's file `pyproject.toml`.

In order to create file `pyproject.toml`
* In file `noxfile.py`, function `generate_api` you need to replace mode `update` by `generate`.
* Additionally, in file `openapi_config.yml` you need to specify a non-existing top-level directory as `project_name_override` and a package that does not contain slashes, e.g.

```yaml
project_name_override: "generate"
package_name_override: saas.client.openapi
post_hooks: []
```

After generating the API,
* Copy the dependencies from file `generate/pyproject.toml` and
* Remove directory `generate`.

## Run Tests

Executing the integration tests requires the following environment variables to be set:

| Variable          | Description                                           |
|-------------------|-------------------------------------------------------|
| `SAAS_HOST`       | Host to use for requests to REST API                  |
| `SAAS_ACCOUNT_ID` | ID of the Exasol SAAS account to be used by the tests |
| `SAAS_PAT`        | Personal access token to access the SAAS API          |

## Creating a Release

### Prepare the Release

There are two scenarios for preparing a release:
* a) [You already merged your changes to branch `main`](#scenario-a-prepare-a-release-from-branch-main)
* b) [You have checked out a different branch](#scenario-b-prepare-a-release-from-another-branch)

In both scenarios the SAPIPY relies on Exasol's [python-toolbox](https://github.com/exasol/python-toolbox) for preparing a release.

The invocation depends on your setup:
* When working in a poetry shell, you need to add one double-dash `--` argument to separate arguments to the nox-session `prepare-release`.
* When calling `poetry` directly for one-time usage, then you need to add _two_ double-dashes `-- --` to terminate arguments to poetry and nox before arguments to the nox-session.

```shell
poetry run nox -s prepare-release -- -- <version>
```

#### Scenario a) Prepare a Release from Branch `main`

Note that this scenario requires all your changes to be merged to branch `main` and no uncommited changes to be present in your local file tree.

Nox session `prepare-release` will
* Create a branch, e.g. `prepare-release/1.2.3` starting from `main`
* Checkout this new branch
* Update the version in files `pyproject.toml` and `version.py`
* Update changes documentation
  * Rename file `doc/unreleased.md` to `doc/changes_<version>.md` and add the current date as date of the release
  * Create a new file `doc/unreleased.md`
  * Update the file `doc/changelog.md`
* Commit and push the changes
* Create a pull request on GitHub

Please note that creating a pull request on GitHub requires
* Executable `gh` to be installed and in your `$PATH` variable
* You must be authenticated towards GitHub via gh, use `gh auth` for that
* In case you are using a GitHub token, the token must have permission `org:read`

##### Manually Create a Pull Request

If you prefer to create the pull request manually or cannot provide one of the prerequisites, you can add command line option `--no-pr`:

```shell
poetry run nox -s prepare-release -- -- <version> --no-pr
```

#### Scenario b) Prepare a Release from Another Branch

In case you currently are already working on a branch other than `main`, please ensure to have all changes commited and add command line option `--no-branch`:

```shell
poetry run nox -s prepare-release -- -- <version> --no-pr --no-branch
```

### Finalize and Publish the Release

When all workflows triggered by merging the pull request to `main` have succeeded, you can create a new release by
* Switching to branch `main`
* Creating a git tag and
* Pushing it to `origin`

```shell
TAG="${1}"
git tag "${TAG}"
git push origin "${TAG}"
```

This will trigger additional GitHub workflows
* Running some checks
* Creating a GitHub release on https://github.com/exasol/saas-api-python/releases and
* Publishing the release on [pypi](https://pypi.org/project/exasol-saas-api)
