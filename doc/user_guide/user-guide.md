# SaaS API for Python User Guide

## Raise Error on Response Status Code Other Than 200

The default behavior of the API client is to return a response with a status code and optionally an attribute `parsed` containing the returned data.

If you want the client to raise an exception for each response with a status other than 200 then please provide optional keyword argument `raise_on_unexpected_status=True`:

```python
from exasol.saas.client.openapi.api.databases import list_databases

client = AuthenticatedClient(host, token, raise_on_unexpected_status=True)
databases = list_databases.sync(client)
````
