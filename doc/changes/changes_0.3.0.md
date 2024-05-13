# Saas API Python 0.3.0, released 2024-05-14

## Summary

This release renamed the package published on pypi from `saas-api` to `exasol-saas-api`. The old package has been removed to avoid confusion.

Additionally, this release adds integration tests for the most important calls to SaaS API.

## Refactorings

* #21: Added integration test for operation "create database"
* #23: Added integration test for operation "add IP to whitelist"

## Feature

* #14: Added fixture waiting until SaaS database is running
* #25: Fixed transitive dependencies required by generated API client

## Bugfixes

* #34: Fixed handling secrets in CI/CD build
* #28: Renamed pypi package from `saas-api` to `exasol-saas-api`
