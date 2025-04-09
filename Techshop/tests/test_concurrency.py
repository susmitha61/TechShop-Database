import unittest
from entity.services.order_service import update_order
from entity.exceptions.concurrency_exception import ConcurrencyException

class TestConcurrencyControl(unittest.TestCase):
    def test_order_update_conflict(self):
        with self.assertRaises(ConcurrencyException):
            update_order(order_id=1, new_data={})  # Simulate conflict
