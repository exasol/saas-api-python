<style type="text/css">
var {
  font-style: italic;
  color: #840;
}
</style>
# SaaS API for Python User Guide

## Naming SaaS instances

SAPIPY offers function `timestamp_name()` to name database instances.

In case of left over SaaS instances, the generated name is intended to identify who created the database, when, and for which project.

Exasol SaaS limits database names to max 20 characters.

SAPIPY function `timestamp_name()` uses the following format: <var>&lt;time>&lt;random>&lt;pst>`-`&lt;user></var>

* <var>&lt;time></var> 5 characters hex `0-9a-f` encoding the minutes since new year UTC.
* <var>&lt;random></var> 5 random hex characters `0-9a-f` to avoid duplicate names.
* <var>&lt;pst></var> optional project short tag, truncated to not exceed the maximum name length.
* <var>&lt;user></var> name of the current user. On GitHub runners typically "runner", also truncated.

Example: `10aa5dd99cSAPIPY-run`, was generated from
* <var>&lt;time></var> `10aa5`<sub>hex</sub> = `68261`<sub>dec</sub> minutes since new year = February, 17 09:41
* <var>&lt;random></var> `dd99c`
* <var>&lt;pst></var> `SAPIPY`
* <var>&lt;user></var> `run`, probably truncated from `runner`

## Raise Error on Response Status Code Other Than 200

The default behavior of the API client is to return a response with a status code and optionally an attribute `parsed` containing the returned data.

If you want the client to raise an exception for each response with a status other than 200 then please provide optional keyword argument `raise_on_unexpected_status=True`:

```python
from exasol.saas.client.openapi.api.databases import list_databases

client = AuthenticatedClient(host, token, raise_on_unexpected_status=True)
databases = list_databases.sync(client)
````
