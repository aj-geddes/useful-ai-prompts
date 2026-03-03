# Factory Pattern

## Factory Pattern

Create objects without specifying exact classes.

```python
from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass

class StripeProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # Stripe-specific logic
        return True

class PayPalProcessor(PaymentProcessor):
    def process_payment(self, amount: float) -> bool:
        # PayPal-specific logic
        return True

class PaymentProcessorFactory:
    @staticmethod
    def create_processor(processor_type: str) -> PaymentProcessor:
        if processor_type == 'stripe':
            return StripeProcessor()
        elif processor_type == 'paypal':
            return PayPalProcessor()
        else:
            raise ValueError(f'Unknown processor: {processor_type}')

# Usage
processor = PaymentProcessorFactory.create_processor('stripe')
processor.process_payment(100.00)
```
