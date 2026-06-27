from uuid import uuid4


def _test_only_allowed_ip_cidr() -> str:
    # Avoid 0.0.0.0/0 here because the shared SaaS account accumulates old broad
    # rules and the backend does not reliably surface a fresh one by name.
    documentation_networks = ("192.0.2", "198.51.100", "203.0.113")
    token = uuid4().int
    network = documentation_networks[token % len(documentation_networks)]
    host = ((token >> 8) % 254) + 1
    return f"{network}.{host}/32"


def test_lifecycle(api_access):
    testee = api_access
    with testee.allowed_ip(
        cidr_ip=_test_only_allowed_ip_cidr(),
        ignore_delete_failure=True,
    ) as ip:
        testee.wait_until_allowed_ip_listed(ip.id)
        # verify allowed ip is listed
        assert ip.id in testee.list_allowed_ip_ids()

        # delete allowed ip and verify it is not listed anymore
        testee.delete_allowed_ip(ip.id)
        testee.wait_until_allowed_ip_deleted(ip.id)
        assert ip.id not in testee.list_allowed_ip_ids()
