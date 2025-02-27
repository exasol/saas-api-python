# 1.0.0 - 2025-02-27

## Summary

This release contains a potentially breaking change as class `database.Database` has been replaced with `exasol_database.ExasolDatabase`.

This release updates the Python API generated from file `openapi.json` multiple times:

In the scope of ticket #80 the updated API contains 3 additional fields for object `Schedule`:
* `createdbyID`
* `createdbyFirstName`
* `createdbyLastName`

In the scope of ticket #84 the updated API contains multiple additions and one removed field.

A `class_override` has been added to file `openapi_config.yml` to solve a conflict caused by `openapi.json` containing model class `Database` with attribute `settings`, from which Openapi Python Client` generates a module `database_settings` containing class `DatabaseSettings`.

The `class_override` replaces class `database.Database` with `exasol_database.ExasolDatabase` which potentially is a breaking change to the API.

Changes to `openapi.json` in detail:

In `paths` added
* `/api/v1/accounts/{accountId}/databases/{databaseId}/database_settings`
* `/api/v1/accounts/{accountId}/databases/{databaseId}/upgrade`

And
* In `components` / `schemas`: added `SetAutoUpdatesDatabase`
* In `components` / `schemas` / `Schedule` / `required` removed `payload`

And below `components` / `schemas`

| In | Added |
|----|-------|
| `CreateDatabase` / `properties` | `numNodes` |
| `Database` / `properties` / `settings` | `required`, `properties`, `additionalProperties` |
| `DatabaseSettings` / `required` | `autoUpdatesEnabled`, `autoUpdatesHardDisabled`, `numNodes` |
| `DatabaseSettings` / `properties` | `autoUpdatesEnabled`, `autoUpdatesHardDisabled`, `numNodes` |
| `Schedule` / `properties` / `action` / `oneOf` / `enum` | `ActionDatabaseUpgrade` |

## Refactorings

* #80: Updated `openapi.json`
* #84: Updated `openapi.json` again

## Security
 * #82: Dependencies updated, especially vitualenv (20.26.4 -> 20.29.2), jinja2 (3.1.4 -> 3.1.5)
