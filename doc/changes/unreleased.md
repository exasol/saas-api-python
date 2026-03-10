# Unreleased

## Summary

This release fixes vulnerabilities by updating dependencies and updates `openapi-python-client` and describes naming conventions for SaaS instances in the User Guide.

Additionally the release updates the Python API generated from file `openapi.json`.

The following items have added in `open-api.json`:
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
