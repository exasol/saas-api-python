# 2.4.0 - 2025-10-27
This release updates the Python API generated from file `openapi.json`.

The following items are added to `open-api.json`:

* `paths` / `/api/v1/accounts/{accountId}/databases/{databaseId}/schedules/{actionId}/state`
* `paths` / `/api/v1/accounts/{accountId}/databases/{databaseId}/schedules/{actionId}/cronRule`
* `components` / `schemas` / `Schedule`
* `components` / `schemas` / `ScheduleState`

## Refactorings

* #119: Updated Open API client

## Dependency Updates

### `main`
* Updated dependency `attrs:25.3.0` to `25.4.0`
* Updated dependency `requests:2.32.4` to `2.32.5`
* Updated dependency `types-requests:2.32.4.20250611` to `2.32.4.20250913`

### `dev`
* Updated dependency `exasol-toolbox:1.6.0` to `1.10.0`
* Updated dependency `openapi-python-client:0.25.1` to `0.25.3`
* Updated dependency `pyexasol:0.27.0` to `1.2.0`
* Updated dependency `pytest-mock:3.14.1` to `3.15.1`
* Updated dependency `types-python-dateutil:2.9.0.20250516` to `2.9.0.20251008`
