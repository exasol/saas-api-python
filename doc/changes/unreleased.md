# Unreleased

## Summary

This release drops the support for Python 3.10.

The release also enables configurable database node counts in the handwritten
database helpers, updates the project tooling to version 7.0.0, and
parallelizes slow integration checks with a generated workflow matrix. It also
includes the generated OpenAPI updates described below.

Since version 2.10.0, the generated Python API client has been updated from
a newer SaaS API specification. The update adds database MCP status and
toggle operations, expands the generated model coverage for account,
billing, worksheet, support, invitation, health, and related resources, and
improves endpoint parameter and response schema definitions.

The semantic API changes include:

* `GET /api/v1/accounts/{accountId}/databases/{databaseId}/mcp` retrieves the database MCP status.
* `POST /api/v1/accounts/{accountId}/databases/{databaseId}/mcp` enables or disables database MCP.
* MCP status, configuration, connection, and enable/disable action models have been added.
* Generated models for account, billing, worksheet, support, invitation, health, and related resources have been added.
* Endpoint parameters and response schemas now use explicit typed definitions in more API operations.
* API error and database schemas have been updated, including optional error fields and database MCP status information.
* For endpoint `/api/v1/accounts/{accountId}/databases/{databaseId}/clusters/{clusterId}/stop`, method "put", parameter `actor` has been added.

Besides there are many formal and syntactic changes
* indent was decreased from 4 to 2 spaces
* sorting of json keys
* attribute "description" added in many places
* `"security": [ { "authorizer": [] } ]` has been removed
* `"description": "No content"` has been replaced by `"description": "No content", "content": {}`

Additional changes when updating API again in November 2026
* Removed
  * `components` / `schemas` / `ApiError` / `properties` / `logId` / `type`
  * `components` / `schemas` / `ApiError` / `properties` / `handler` / `type`
* Modified
  * `components` / `schemas` / `PatchUserDatabases` / `properties`
  * `components` / `schemas` / `UserDatabase` / `required`
* Added
  * `paths` / `/api/v1/accounts/{accountId}/usage` / `get` / `parameters` / `"name": "yearMonth"`
  * `paths` / `/api/v1/accounts/{accountId}/usage` / `get` / `parameters` / `"name": "from"`
  * `components` / `schemas` / `from` / `type`
  * `components` / `schemas` / `to` / `type`
  * `components` / `schemas` / `RecoverAccountName` / `required`
  * `components` / `schemas` / `RecoverAccountNameResult` / `required`
  * `components` / `schemas` / `UsageCluster` / `properties` / `mainCluster` / `type`
  * `components` / `schemas` / `UsageCluster` / `properties` / `family` / `type`
  * `components` / `schemas` / `UsageDatabase` / `properties` / `region` / `type`


## Features

* #147: Added `num_nodes` support to the handwritten database creation helpers.

## Refactorings

* #160: Updated PTB to version 7.0.0
* #173: Parallelized slow integration checks with a generated workflow matrix.
* #175: Updated dependencies incl. PTB v12
