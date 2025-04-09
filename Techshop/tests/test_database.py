import unittest
from entity.services.database_service import execute_query
from entity.exceptions.database_access_exception import DatabaseAccessException

class TestDatabaseAccess(unittest.TestCase):
    def test_query_failure(self):
        with self.assertRaises(DatabaseAccessException):
            execute_query("SELECT * FROM non_existing_table")  # Simulate failure
