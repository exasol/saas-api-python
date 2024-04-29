from exasol.saas.client import openapi


def test_lifecycle(api_testee):
    """
    This integration test uses the database created and provided by pytest
    fixture ``saas_database`` to verify

    - initial status and number of clusters of the created database
    - list_databases includes the new database
    - delete_database deletes the database
    - list_databases does not include the deleted database anymore
    """

    testee = api_testee
    with testee.database(ignore_delete_failure=True) as db:
        # verify state and clusters of created database
        assert db.status == openapi.models.Status.TOCREATE and \
            db.clusters.total == 1

        # verify database is listed
        assert db.id in testee.list_database_ids()

        # delete database and verify database is not listed anymore
        testee.delete_database(db.id)
        assert db.id not in testee.list_database_ids()
