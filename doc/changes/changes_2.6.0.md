# 2.6.0 - 2025-12-08
This release changes the precondition for deleting a SaaS database instance.

Before, the SAPIPY used only a fixed waiting time. With the changed behavior of the actual SaaS instances the precondition needed to be adapted. SAPIPY now waits for the SaaS instance to be running before attempting to delete it.

## Bugfixes

* #125: Made operation delete wait for SaaS instance to enable deletion
