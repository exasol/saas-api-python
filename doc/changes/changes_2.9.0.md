# 2.9.0 - 2026-03-10

## Summary

This release fixes vulnerabilities by updating dependencies and updates `openapi-python-client` and describes naming conventions for SaaS instances in the User Guide.

Additionally the release updates the Python API generated from file `openapi.json`.

The following items have added in `openapi.json`:
* `components` / `schemas` / `Cluster` / `required` / `familyName`
* `components` / `schemas` / `Cluster` / `properties` / `familyName`

## Security

* #140: Fixed vulnerabilities by updating dependencies

## Documentation

* #145: Described SaaS instance naming conventions in the User Guide

## Refactorings

* #120: Updated openapi-python-client to version 0.26 or higher
* #141: Updated PTB to version 5 and regenerated GitHub workflows
* #148: Re-generated the SaaS API client code

## Dependency Updates

### `main`
* Updated dependency `types-requests:2.32.4.20250913` to `2.32.4.20260107`

### `dev`
* Updated dependency `exasol-toolbox:1.13.0` to `5.1.1`
* Updated dependency `openapi-python-client:0.25.3` to `0.28.2`
* Updated dependency `pyexasol:1.3.0` to `2.0.0`
* Updated dependency `types-python-dateutil:2.9.0.20251115` to `2.9.0.20260124`

## Dependency Updates

### `main`

* Updated dependency `types-requests:2.32.4.20250913` to `2.32.4.20260107`

### `dev`

* Updated dependency `exasol-toolbox:1.13.0` to `6.0.0`
* Updated dependency `openapi-python-client:0.25.3` to `0.28.3`
* Updated dependency `pyexasol:1.3.0` to `2.1.0`
* Updated dependency `types-python-dateutil:2.9.0.20251115` to `2.9.0.20260305`
