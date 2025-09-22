# Unreleased

This release updates the Python API generated from file `openapi.json`.

Changes to `open-api.json` in detail:
* added `paths` / `/api/v1/accounts/{accountId}/databases/{databaseId}/dlhc-activate`
* added `components` / `schemas` / `DlhcActivateStatus`
* removed `components` / `schemas` / `Database` / `required` / `settings`
* removed `components` / `schemas` / `Database` / `properties` / `settings`

## Bugfixes

* #115: Fixed SaaS API throws "stream Type should be provided"

## Refactorings

* #110: Updated exasol-toolbox to 1.6.0 & activated sonar
* #112: Updated open API client
