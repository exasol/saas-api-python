# SaaS API for Python &mdash; Software Design

## Design decision: Generated API Interface

We prefer a generated API interface as
* It includes the complete API without additional overhead.
* It allows to update the generated code with low effort.
* It allows to check if the current client is outdated in an automated way,

## Design decision: Selected Client Generator

The following generators have been considered
* O1) https://github.com/openapi-generators/openapi-python-client (python based)
* O2) https://github.com/OpenAPITools/openapi-generator (used by SaaS, but java based)
* O3) https://github.com/swagger-api/swagger-codegen (java based)

The developers decided to use (O1) [openapi-python-client](https://github.com/openapi-generators/openapi-python-client) with the following rationale:

* It can be used as simple dependency in `pyproject.toml`, hence avoids
  * Extra tooling for developers (mvn, jre)
  * Additional dependencies in CI builds
* Its feature set is rated to be sufficient.
* Warnings are accepted.

The mentioned warnings are due to the generator (O1)'s limited OpenAPI specification support. In particular, the generator does not support a "default" response, which is used for default errors in the [JSON spec](https://cloud.exasol.com/openapi.json) of the Exasol SaaS REST API. In the generated code such default is just parsed into `None` or raises an exception (if `client.raise_on_unexpected_status` is set). This design document states to not lose any information and functionality from those warnings. Analysis indicated, that this is the only warning.

