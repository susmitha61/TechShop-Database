from entity.exceptions.payment_failed_exception import PaymentFailedException

def process_payment(order):
    payment_successful = False  # Simulate payment processing logic
    if not payment_successful:
        raise PaymentFailedException("Payment was declined. Please try again.")
