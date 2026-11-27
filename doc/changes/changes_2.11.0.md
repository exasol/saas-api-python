# 2.11.0 - 2026-11-27

## Summary

This release drops the support for Python 3.10.

The release also enables configurable database node counts in the handwritten database helpers, updates the project tooling to version 7.0.0, and parallelizes slow integration checks with a generated workflow matrix. It also includes the generated OpenAPI updates described below.

Since version 2.10.0, the generated Python API client has been updated from a newer SaaS API specification. The update adds database MCP status and toggle operations, expands the generated model coverage for account, billing, worksheet, support, invitation, health, and related resources, and improves endpoint parameter and response schema definitions.

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

## Security Issues

This release fixes vulnerabilities by updating dependencies:

| Dependency | Vulnerability | Affected | Fixed in |
|------------|---------------|----------|----------|
| anyio | PYSEC-2026-4024 | 4.13.0 | 4.14.2 |
| anyio | PYSEC-2026-4025 | 4.13.0 | 4.14.2 |
| black | CVE-2026-114134 | 26.3.1 | 26.10.1 |
| certifi | PYSEC-2026-4320 | 2026.2.25 | 2026.10.18 |
| cryptography | GHSA-537c-gmf6-5ccf | 46.0.6 | 48.0.1 |
| cryptography | PYSEC-2026-3552 | 46.0.6 | 50.0.0 |
| cryptography | PYSEC-2026-3553 | 46.0.6 | 49.0.0 |
| cryptography | PYSEC-2026-3554 | 46.0.6 | 49.0.0 |
| cryptography | PYSEC-2026-36 | 46.0.6 | 46.0.7 |
| filelock | CVE-2026-112907 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112909 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112910 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112913 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112915 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112935 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112936 | 3.25.2 | 4.0.9 |
| filelock | CVE-2026-112939 | 3.25.2 | 4.2.1 |
| filelock | CVE-2026-112940 | 3.25.2 | 4.2.1 |
| idna | PYSEC-2026-215 | 3.11 | 3.15 |
| msgpack | CVE-2026-114613 | 1.1.2 | 1.2.3 |
| msgpack | PYSEC-2026-3625 | 1.1.2 | 1.2.1 |
| pip | PYSEC-2026-196 | 26.0.1 | 26.1.2 |
| pip | PYSEC-2026-2875 | 26.0.1 | 26.1 |
| pip | PYSEC-2026-2876 | 26.0.1 | 26.1 |
| pip | PYSEC-2026-3721 | 26.0.1 | 26.2 |
| pip | PYSEC-2026-3721 | 26.0.1 | 26.2.0 |
| pylint | CVE-2026-114608 | 4.0.5 | 4.0.9 |
| pytest | PYSEC-2026-1845 | 7.4.4 | 9.0.3 |
| soupsieve | CVE-2026-126190 | 2.8.3 | 4.0.0 |
| soupsieve | CVE-2026-126191 | 2.8.3 | 3.0.2 |
| soupsieve | CVE-2026-126192 | 2.8.3 | 2.10.0 |
| soupsieve | CVE-2026-126193 | 2.8.3 | 3.0.2 |
| soupsieve | PYSEC-2026-3071 | 2.8.3 | 2.8.4 |
| soupsieve | PYSEC-2026-3072 | 2.8.3 | 2.8.4 |
| soupsieve | PYSEC-2026-4170 | 2.8.3 | 2.9.0 |
| soupsieve | PYSEC-2026-4171 | 2.8.3 | 2.9.0 |
| urllib3 | PYSEC-2026-141 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-142 | 2.6.3 | 2.7.0 |
| urllib3 | PYSEC-2026-4175 | 2.6.3 | 2.8.0 |
| urllib3 | PYSEC-2026-4176 | 2.6.3 | 2.8.0 |
| urllib3 | PYSEC-2026-4177 | 2.6.3 | 2.8.0 |
| virtualenv | CVE-2026-113714 | 21.2.0 | 21.14.9 |
| virtualenv | CVE-2026-113717 | 21.2.0 | 21.14.9 |
| virtualenv | CVE-2026-113718 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4011 | 21.2.0 | 21.7.12 |
| virtualenv | PYSEC-2026-4012 | 21.2.0 | 21.7.11 |
| virtualenv | PYSEC-2026-4013 | 21.2.0 | 21.7.13 |
| virtualenv | PYSEC-2026-4014 | 21.2.0 | 21.7.12 |
| virtualenv | PYSEC-2026-4372 | 21.2.0 | 21.14.10 |
| virtualenv | PYSEC-2026-4374 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4375 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4378 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4379 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4380 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4381 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4382 | 21.2.0 | 21.14.9 |
| virtualenv | PYSEC-2026-4384 | 21.2.0 | 21.14.7 |
| virtualenv | PYSEC-2026-4385 | 21.2.0 | 21.14.4 |
| virtualenv | PYSEC-2026-4386 | 21.2.0 | 21.14.2 |
| virtualenv | PYSEC-2026-4387 | 21.2.0 | 21.14.2 |

## Features

* #147: Added `num_nodes` support to the handwritten database creation helpers.

## Refactorings

* #160: Updated PTB to version 7.0.0
* #173: Parallelized slow integration checks with a generated workflow matrix.
* #175: Updated dependencies incl. PTB v12

## Dependency Updates

### `main`

* Removed dependency `ifaddr:0.2.0`
* Updated dependency `requests:2.33.1` to `2.34.2`
* Updated dependency `tenacity:9.1.4` to `9.2.1`
* Updated dependency `types-requests:2.33.0.20260402` to `2.33.0.20261030`

### `dev`

* Updated dependency `exasol-toolbox:6.1.1` to `12.0.0`
* Updated dependency `openapi-python-client:0.28.3` to `0.28.4`
* Updated dependency `pyexasol:2.2.0` to `2.4.1`
* Updated dependency `pytest:7.4.4` to `9.2.0`
* Updated dependency `pytest-mock:3.15.1` to `3.17.0`
* Updated dependency `types-python-dateutil:2.9.0.20260402` to `2.9.0.20261122`
