# 1.1.0 - 2025-04-07

## Summary

This release updates the Python API generated from file `openapi.json`.

Changes to `open-api.json` in detail:

Endpoint was renamed
* from `/api/v1/accounts/{accountId}/databases/{databaseId}/database_settings`
* to `/api/v1/accounts/{accountId}/databases/{databaseId}/settings`

Method `GET` was added for endpoint
* `/api/v1/accounts/{accountId}/databases/{databaseId}/upgrade`

Changes to models below `components` / `schemas`:

Attribute `streamType` was added to
* `CreateDatabase` / `properties`
* `Database` / `properties` / `settings` / `required`
* `Database` / `properties` / `settings` / `properties`
* `DatabaseSettings` / `required`
* `DatabaseSettings` / `properties`

Model `DatabaseUpgradeInfo` was added.

* Refactorings

* #88: Updated `openapi.json`
