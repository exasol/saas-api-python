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
* In file `noxfile.py` you need to replace mode `update` by `generate`
* Additionally in file `openapi_config.yml` you need to specify a non-existing top-level directory as `name` and a package that does not contain slashes, e.g.

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

