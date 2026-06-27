def test_create_database_with_two_nodes(api_access, local_name):
    """
    This integration test verifies that the handwritten helper forwards
    `num_nodes` and the created database reports that setting back.
    """
    with api_access.database(
        local_name,
        ignore_delete_failure=True,
        num_nodes=2,
    ) as db:
        settings = api_access.get_database_settings(db.id)

        assert settings is not None
        assert settings.num_nodes == 2
