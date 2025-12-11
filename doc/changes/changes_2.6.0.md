# 2.6.0 - 2025-12-11

## Summary

This release changes the strategy for deleting a SaaS database instance, as required by the changed behavior of the actual SaaS backend.

Before, SAPIPY used only a fixed waiting time. In case of HTTP responses with status code 400 and their message containing "cluster is not in a proper state" SAPIPY now retries deleting the SaaS instance for max. 30 minutes.

## Bugfixes

* #125: Added retry when deleting SaaS instance
