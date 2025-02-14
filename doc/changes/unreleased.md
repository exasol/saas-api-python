# Unreleased

## Summary

This release updates the Python API generated from file `openapi.json`.

The updated API contains 3 additional fields for object `Schedule`:
* `createdbyID`
* `createdbyFirstName`
* `createdbyLastName`

## Refactorings

* #80: Updated `openapi.json`

## Security
 * #82: Dependencies updated, especially vitualenv (20.26.4 -> 20.29.2), jinja2 (3.1.4 -> 3.1.5)