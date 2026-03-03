# Stripe Integration with Python/Flask

## Stripe Integration with Python/Flask

```python
# config.py
import os

class StripeConfig:
    STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_PUBLISHABLE_KEY = os.getenv('STRIPE_PUBLISHABLE_KEY')
    STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')

# stripe_service.py
import stripe
from datetime import datetime, timedelta
import logging

logger = logging.getLogger(__name__)

stripe.api_key = os.getenv('STRIPE_SECRET_KEY')

class StripePaymentService:
    @staticmethod
    def create_payment_intent(amount, currency='usd', description=None, metadata=None):
        """Create a payment intent"""
        try:
            intent = stripe.PaymentIntent.create(
                amount=int(amount * 100),  # Convert to cents
                currency=currency,
                description=description,
                metadata=metadata or {}
            )
            logger.info(f"Payment intent created: {intent.id}")
            return {
                'success': True,
                'client_secret': intent.client_secret,
                'intent_id': intent.id
            }
        except stripe.error.StripeError as e:
            logger.error(f"Stripe error: {str(e)}")
            return {'success': False, 'error': str(e)}

    @staticmethod
    def confirm_payment(intent_id):
        """Confirm payment intent"""
        try:
            intent = stripe.PaymentIntent.retrieve(intent_id)

            if intent.status == 'succeeded':
                logger.info(f"Payment confirmed: {intent_id}")
                return {'success': True, 'intent_id': intent_id, 'status': intent.status}
            else:
                return {'success': False, 'status': intent.status}

        except stripe.error.StripeError as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def create_customer(email, name=None, metadata=None):
        """Create Stripe customer"""
        try:
            customer = stripe.Customer.create(
                email=email,
                name=name,
                metadata=metadata or {}
            )
            logger.info(f"Customer created: {customer.id}")
            return {'success': True, 'customer_id': customer.id}
        except stripe.error.StripeError as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def create_subscription(customer_id, price_id, metadata=None):
        """Create recurring subscription"""
        try:
            subscription = stripe.Subscription.create(
                customer=customer_id,
                items=[{'price': price_id}],
                metadata=metadata or {}
            )
            logger.info(f"Subscription created: {subscription.id}")
            return {
                'success': True,
                'subscription_id': subscription.id,
                'status': subscription.status
            }
        except stripe.error.StripeError as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def cancel_subscription(subscription_id):
        """Cancel subscription"""
        try:
            subscription = stripe.Subscription.delete(subscription_id)
            logger.info(f"Subscription cancelled: {subscription_id}")
            return {'success': True, 'subscription_id': subscription_id}
        except stripe.error.StripeError as e:
            return {'success': False, 'error': str(e)}

    @staticmethod
    def refund_payment(payment_intent_id, amount=None):
        """Refund a payment"""
        try:
            refund = stripe.Refund.create(
                payment_intent=payment_intent_id,
                **({'amount': int(amount * 100)} if amount else {})
            )
            logger.info(f"Refund created: {refund.id}")
            return {'success': True, 'refund_id': refund.id}
        except stripe.error.StripeError as e:
            return {'success': False, 'error': str(e)}

# routes.py
from flask import Blueprint, request, jsonify
from stripe_service import StripePaymentService
from functools import wraps
import hmac
import hashlib

payment_bp = Blueprint('payments', __name__, url_prefix='/api/payments')

def verify_stripe_webhook(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        signature = request.headers.get('Stripe-Signature')
        webhook_secret = os.getenv('STRIPE_WEBHOOK_SECRET')

        try:
            event = stripe.Webhook.construct_event(
                request.data,
                signature,
                webhook_secret
            )
        except ValueError:
            return jsonify({'error': 'Invalid payload'}), 400
        except stripe.error.SignatureVerificationError:
            return jsonify({'error': 'Invalid signature'}), 403

        request.stripe_event = event
        return f(*args, **kwargs)

    return decorated_function

@payment_bp.route('/create-intent', methods=['POST'])
@token_required
def create_payment_intent():
    """Create payment intent"""
    data = request.json
    amount = data.get('amount')
    description = data.get('description')

    if not amount or amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400

    result = StripePaymentService.create_payment_intent(
        amount=amount,
        description=description,
        metadata={'user_id': current_user.id}
    )

    if result['success']:
        return jsonify(result), 200
    else:
        return jsonify(result), 400

@payment_bp.route('/confirm-payment', methods=['POST'])
@token_required
def confirm_payment():
    """Confirm payment"""
    data = request.json
    intent_id = data.get('intent_id')

    result = StripePaymentService.confirm_payment(intent_id)

    if result['success']:
        # Update user's payment status in database
        order = Order.query.filter_by(
            stripe_intent_id=intent_id,
            user_id=current_user.id
        ).first()

        if order:
            order.status = 'paid'
            db.session.commit()

        return jsonify(result), 200
    else:
        return jsonify(result), 400

@payment_bp.route('/subscribe', methods=['POST'])
@token_required
def create_subscription():
    """Create subscription"""
    data = request.json
    price_id = data.get('price_id')

    if not price_id:
        return jsonify({'error': 'Price ID required'}), 400

    # Get or create Stripe customer
    user = current_user
    if not user.stripe_customer_id:
        customer_result = StripePaymentService.create_customer(
            email=user.email,
            name=user.full_name
        )
        if not customer_result['success']:
            return jsonify(customer_result), 400
        user.stripe_customer_id = customer_result['customer_id']
        db.session.commit()

    result = StripePaymentService.create_subscription(
        customer_id=user.stripe_customer_id,
        price_id=price_id,
        metadata={'user_id': user.id}
    )

    if result['success']:
        subscription = Subscription(
            user_id=user.id,
            stripe_subscription_id=result['subscription_id'],
            status=result['status']
        )
        db.session.add(subscription)
        db.session.commit()
        return jsonify(result), 201
    else:
        return jsonify(result), 400

@payment_bp.route('/webhook', methods=['POST'])
@verify_stripe_webhook
def handle_webhook():
    """Handle Stripe webhooks"""
    event = request.stripe_event

    try:
        if event['type'] == 'payment_intent.succeeded':
            intent = event['data']['object']
            logger.info(f"Payment succeeded: {intent['id']}")
            # Update order status

        elif event['type'] == 'payment_intent.payment_failed':
            intent = event['data']['object']
            logger.error(f"Payment failed: {intent['id']}")
            # Handle failed payment

        elif event['type'] == 'customer.subscription.updated':
            subscription = event['data']['object']
            logger.info(f"Subscription updated: {subscription['id']}")

        elif event['type'] == 'customer.subscription.deleted':
            subscription = event['data']['object']
            logger.info(f"Subscription deleted: {subscription['id']}")
            # Update user's subscription status

        elif event['type'] == 'invoice.payment_succeeded':
            invoice = event['data']['object']
            logger.info(f"Invoice paid: {invoice['id']}")

        elif event['type'] == 'invoice.payment_failed':
            invoice = event['data']['object']
            logger.error(f"Invoice payment failed: {invoice['id']}")

        return jsonify({'received': True}), 200

    except Exception as e:
        logger.error(f"Webhook error: {str(e)}")
        return jsonify({'error': str(e)}), 500
```
