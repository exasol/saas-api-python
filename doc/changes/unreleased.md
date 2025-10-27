# Unreleased

This release updates the Python API generated from file `openapi.json`.

The following items are added to `open-api.json`:

* `paths` / `/api/v1/accounts/{accountId}/databases/{databaseId}/schedules/{actionId}/state`
* `paths` / `/api/v1/accounts/{accountId}/databases/{databaseId}/schedules/{actionId}/cronRule`
* `components` / `schemas` / `Schedule`
* `components` / `schemas` / `ScheduleState`

## Refactorings

* #119: Updated Open API client
