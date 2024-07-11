# 0.8.0 - 2024-07-11

This release fixes vulnerabilities by updating dependencies.

## Security

* Fixed vulnerabilities by updating dependencies
  * Vulnerability CVE-2024-21503 in transitive dependency via `exasol-toolbox` to `black` in versions below `24.3.0`

## Refactorings

* #68: Update to Python 3.10
* #70: Optimized logging
* n/a: Changed schedule checking if open api is outdated to 2 am
* #29: Enhanced nox task generate-api to add transitive dependencies into main `pyproject.toml`