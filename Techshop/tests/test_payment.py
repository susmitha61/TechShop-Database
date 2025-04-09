import unittest
from entity.services.payment_service import process_payment
from entity.exceptions.payment_failed_exception import PaymentFailedException

class TestPaymentProcessing(unittest.TestCase):
    def test_payment_declined(self):
        with self.assertRaises(PaymentFailedException):
            process_payment(order={})
