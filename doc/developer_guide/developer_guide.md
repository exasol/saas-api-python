# SaaS API for Python &mdash; Developer Guide

## Generate the API Model

The model layer of this API has been generated from the OpenAPI specification
in JSON format of the SaaS API https://cloud.exasol.com/openapi.json using
[openapi-python-client](https://github.com/openapi-generators/openapi-python-client).

See also
[API Documentation](https://docs.exasol.com/saas/administration/rest_api/rest_api.htm)
and [Swagger UI](https://cloud.exasol.com/openapi/index.html).

In order to regenerate the model layer please use the following command line:

```shell
poetry run nox generate-api
```

### Change the Source URL of API Model JSON Definition

If you want to retrieve the JSON definition for the API model from a different
source then just edit file `noxfile.py`.

### Read JSON definition From a Local File

Use CLI option `--path` to read the JSON definition from a local file instead of a URL:

```python
"--path", "/path/to/openapi.json",
```
