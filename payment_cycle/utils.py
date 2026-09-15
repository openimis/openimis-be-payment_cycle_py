import random
import string


def generate_payment_cycle_code(start_date=None):
    """Generate a unique YYYY plus five-digit PaymentCycle code."""
    from payment_cycle.models import PaymentCycle
    year = f"{start_date:%Y}" if start_date else ''.join(random.choices(string.digits, k=4))
    while True:
        code = f"{year}{''.join(random.choices(string.digits, k=5))}"
        if not PaymentCycle.objects.filter(code=code).exists():
            return code
