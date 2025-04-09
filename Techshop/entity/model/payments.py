from datetime import datetime

class Payment:
    def __init__(self, payment_id, order_id, amount, payment_method, payment_date=None):
        self._payment_id = payment_id
        self._order_id = order_id
        self._amount = amount
        self._payment_method = payment_method
        self._payment_date = payment_date or datetime.now()  # Matching PaymentDate default GETDATE()

    # Getters
    def get_payment_id(self):
        return self._payment_id

    def get_order_id(self):
        return self._order_id

    def get_amount(self):
        return self._amount

    def get_payment_method(self):
        return self._payment_method

    def get_payment_date(self):
        return self._payment_date

    # Setters
    def set_payment_id(self, payment_id):
        self._payment_id = payment_id

    def set_order_id(self, order_id):
        self._order_id = order_id

    def set_amount(self, amount):
        if amount >= 0:
            self._amount = amount
        else:
            raise ValueError("Amount must be non-negative")

    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    def set_payment_date(self, payment_date):
        self._payment_date = payment_date


class PaymentManager:
    def __init__(self):
        self.payments = []

    def record_payment(self, payment):
        self.payments.append(payment)

    def update_payment_status(self, order_id, new_status):
        for payment in self.payments:
            if payment.get_order_id() == order_id:
                # Assuming status tracking is to be added (not in schema)
                payment.status = new_status
                return
        raise ValueError("Payment not found.")
