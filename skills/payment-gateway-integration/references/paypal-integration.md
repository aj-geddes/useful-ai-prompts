# PayPal Integration

## PayPal Integration

```python
# paypal_service.py
import paypalrestsdk
import os

paypalrestsdk.configure({
    "mode": os.getenv("PAYPAL_MODE", "sandbox"),
    "client_id": os.getenv("PAYPAL_CLIENT_ID"),
    "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
})

class PayPalService:
    @staticmethod
    def create_payment(amount, currency='USD', return_url=None, cancel_url=None):
        """Create PayPal payment"""
        payment = paypalrestsdk.Payment({
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "redirect_urls": {
                "return_url": return_url or "https://example.com/return",
                "cancel_url": cancel_url or "https://example.com/cancel"
            },
            "transactions": [{
                "amount": {
                    "total": str(amount),
                    "currency": currency,
                    "details": {
                        "subtotal": str(amount)
                    }
                },
                "description": "Payment"
            }]
        })

        if payment.create():
            logger.info(f"PayPal payment created: {payment.id}")
            approval_url = None
            for link in payment.links:
                if link['rel'] == 'approval_url':
                    approval_url = link['href']

            return {
                'success': True,
                'payment_id': payment.id,
                'approval_url': approval_url
            }
        else:
            logger.error(f"PayPal error: {payment.error}")
            return {'success': False, 'error': payment.error}

    @staticmethod
    def execute_payment(payment_id, payer_id):
        """Execute approved payment"""
        payment = paypalrestsdk.Payment.find(payment_id)

        if payment.execute({"payer_id": payer_id}):
            logger.info(f"Payment executed: {payment.id}")
            return {'success': True, 'transaction_id': payment.transactions[0].related_resources[0].sale.id}
        else:
            logger.error(f"Execution error: {payment.error}")
            return {'success': False, 'error': payment.error}
```
