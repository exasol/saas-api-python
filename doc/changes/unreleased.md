# Unreleased

## Summary

This release updates the Python API generated from file `openapi.json`.

Changes to `open-api.json` in detail:

Added `streamDescription` to the models below `components` / `schemas`:

* `Database` / `properties` / `settings` / `required`
* `Database` / `properties` / `settings` / `properties`
* `DatabaseSettings` / `required`
* `DatabaseSettings` / `properties`

## Refactorings

* #90: Updated open API client 2025-04-15

## Security

* #92: Dependencies updated, especially jinja2 (3.1.5 -> 3.1.6)