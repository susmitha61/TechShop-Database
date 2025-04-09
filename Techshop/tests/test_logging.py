import unittest
from entity.services.logging_service import log_error
from entity.exceptions.io_exception import IOException

class TestLogging(unittest.TestCase):
    def test_log_error(self):
        with self.assertRaises(IOException):
            log_error("Test log message")  # Ensure this raises an IOException
