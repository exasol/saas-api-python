def test_lifecycle(api_access):
    testee = api_access
    with testee.allowed_ip(ignore_delete_failure=True) as ip:
        testee.wait_until_allowed_ip_listed(ip.id)
        # verify allowed ip is listed
        assert ip.id in testee.list_allowed_ip_ids()

        # delete allowed ip and verify it is not listed anymore
        testee.delete_allowed_ip(ip.id)
        testee.wait_until_allowed_ip_deleted(ip.id)
        assert ip.id not in testee.list_allowed_ip_ids()
