# Unreleased

This release updates the Python API generated from file `openapi.json`.

The following changes actually are breaking changes:
* removed `components` / `schemas` / `Database` / `required` / `settings`
* removed `components` / `schemas` / `Database` / `properties` / `settings`

However, as these changes are transparant to users of the SAPIPY the release only
increases the minor version.

Other changes to `open-api.json` are:
* added `paths` / `/api/v1/accounts/{accountId}/databases/{databaseId}/dlhc-activate`
* added `components` / `schemas` / `DlhcActivateStatus`

## Bugfixes

* #115: Fixed SaaS API throws "stream Type should be provided"

## Refactorings

* #110: Updated exasol-toolbox to 1.6.0 & activated sonar
* #112: Updated open API client
