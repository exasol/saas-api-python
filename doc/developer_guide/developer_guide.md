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
