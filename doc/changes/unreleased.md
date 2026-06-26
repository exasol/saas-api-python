# Unreleased

This release updates the Python API generated from file `openapi.json`.

* For endpoint `/api/v1/accounts/{accountId}/databases/{databaseId}/clusters/{clusterId}/stop`, method "put", parameter `actor` has been added.
* For many endpoints the data type "string" has been replaced by a reference to model data type.

Besides there are many formal and syntactic changes
* indent was decreased from 4 to 2 spaces
* sorting of json keys
* attribute "description" added in many places
* `"security": [ { "authorizer": [] } ]` has been removed
* `"description": "No content"` has been replaced by
 `"description": "No content", "content": {}`

## Summary

* #147: Added `num_nodes` support to the handwritten database creation helpers.

## Refactorings

* #160: Updated PTB to version 7.0.0
