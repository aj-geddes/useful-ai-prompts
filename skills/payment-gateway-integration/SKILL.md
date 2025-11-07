---
name: payment-gateway-integration
description: Integrate payment gateways like Stripe, PayPal, and Square with backends for payment processing, subscription management, and webhook handling. Use when building e-commerce platforms, implementing billing systems, and handling payments securely.
---

# Payment Gateway Integration

## Overview

Build secure payment processing systems with major payment providers (Stripe, PayPal, Square), handling transactions, subscriptions, webhooks, PCI compliance, and error scenarios across different backend frameworks.

## When to Use

- Processing customer payments
- Implementing subscription billing
- Building e-commerce platforms
- Handling refunds and disputes
- Managing recurring charges
- Integrating payment webhooks

## Instructions

### 1. **Stripe Integration with Python/Flask**

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

### 2. **Node.js/Express Stripe Integration**

```javascript
// stripe-service.js
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const logger = require('./logger');

class StripeService {
    async createPaymentIntent(amount, currency = 'usd', metadata = {}) {
        try {
            const intent = await stripe.paymentIntents.create({
                amount: Math.round(amount * 100),
                currency: currency,
                metadata: metadata
            });

            logger.info(`Payment intent created: ${intent.id}`);
            return { success: true, clientSecret: intent.client_secret, intentId: intent.id };
        } catch (error) {
            logger.error(`Stripe error: ${error.message}`);
            return { success: false, error: error.message };
        }
    }

    async createCustomer(email, name, metadata = {}) {
        try {
            const customer = await stripe.customers.create({
                email: email,
                name: name,
                metadata: metadata
            });

            logger.info(`Customer created: ${customer.id}`);
            return { success: true, customerId: customer.id };
        } catch (error) {
            return { success: false, error: error.message };
        }
    }

    async createSubscription(customerId, priceId, metadata = {}) {
        try {
            const subscription = await stripe.subscriptions.create({
                customer: customerId,
                items: [{ price: priceId }],
                metadata: metadata
            });

            logger.info(`Subscription created: ${subscription.id}`);
            return { success: true, subscriptionId: subscription.id, status: subscription.status };
        } catch (error) {
            return { success: false, error: error.message };
        }
    }

    async cancelSubscription(subscriptionId) {
        try {
            await stripe.subscriptions.del(subscriptionId);
            logger.info(`Subscription cancelled: ${subscriptionId}`);
            return { success: true };
        } catch (error) {
            return { success: false, error: error.message };
        }
    }

    async refundPayment(paymentIntentId, amount = null) {
        try {
            const refund = await stripe.refunds.create({
                payment_intent: paymentIntentId,
                ...(amount && { amount: Math.round(amount * 100) })
            });

            logger.info(`Refund created: ${refund.id}`);
            return { success: true, refundId: refund.id };
        } catch (error) {
            return { success: false, error: error.message };
        }
    }
}

module.exports = new StripeService();

// routes.js
const express = require('express');
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
const stripeService = require('../services/stripe-service');
const { authenticate } = require('../middleware/auth');

const router = express.Router();

router.post('/create-intent', authenticate, async (req, res) => {
    const { amount, description } = req.body;

    if (!amount || amount <= 0) {
        return res.status(400).json({ error: 'Invalid amount' });
    }

    const result = await stripeService.createPaymentIntent(amount, 'usd', {
        userId: req.user.id,
        description: description
    });

    if (result.success) {
        res.json(result);
    } else {
        res.status(400).json(result);
    }
});

router.post('/webhook', express.raw({ type: 'application/json' }), async (req, res) => {
    const signature = req.headers['stripe-signature'];

    try {
        const event = stripe.webhooks.constructEvent(
            req.body,
            signature,
            process.env.STRIPE_WEBHOOK_SECRET
        );

        if (event.type === 'payment_intent.succeeded') {
            const intent = event.data.object;
            logger.info(`Payment succeeded: ${intent.id}`);
            // Update order status

        } else if (event.type === 'customer.subscription.updated') {
            const subscription = event.data.object;
            logger.info(`Subscription updated: ${subscription.id}`);

        } else if (event.type === 'invoice.payment_succeeded') {
            const invoice = event.data.object;
            logger.info(`Invoice paid: ${invoice.id}`);
        }

        res.json({ received: true });
    } catch (error) {
        logger.error(`Webhook error: ${error.message}`);
        res.status(400).send(`Webhook Error: ${error.message}`);
    }
});

module.exports = router;
```

### 3. **PayPal Integration**

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

### 4. **Subscription Management**

```python
# subscription_service.py
class SubscriptionService:
    @staticmethod
    def create_subscription(user_id, plan_id, payment_method_id):
        """Create user subscription"""
        try:
            result = StripePaymentService.create_subscription(
                customer_id=user.stripe_customer_id,
                price_id=plan_id
            )

            if result['success']:
                subscription = Subscription(
                    user_id=user_id,
                    stripe_subscription_id=result['subscription_id'],
                    plan_id=plan_id,
                    status='active',
                    started_at=datetime.utcnow(),
                    renewal_date=datetime.utcnow() + timedelta(days=30)
                )
                db.session.add(subscription)
                db.session.commit()

                logger.info(f"Subscription created for user {user_id}")
                return {'success': True, 'subscription_id': subscription.id}

        except Exception as e:
            logger.error(f"Failed to create subscription: {str(e)}")
            return {'success': False, 'error': str(e)}

    @staticmethod
    def cancel_subscription(subscription_id):
        """Cancel subscription"""
        subscription = Subscription.query.get(subscription_id)
        if not subscription:
            return {'success': False, 'error': 'Subscription not found'}

        result = StripePaymentService.cancel_subscription(subscription.stripe_subscription_id)

        if result['success']:
            subscription.status = 'cancelled'
            subscription.cancelled_at = datetime.utcnow()
            db.session.commit()

            logger.info(f"Subscription cancelled: {subscription_id}")
            return {'success': True}

        return result
```

## Best Practices

### ✅ DO
- Use official payment SDK libraries
- Verify webhook signatures
- Store minimal payment information
- Never store full credit card numbers
- Use HTTPS for all payment routes
- Implement proper error handling
- Test with sandbox environments
- Handle payment failures gracefully
- Implement PCI compliance
- Log all payment transactions
- Use idempotency keys
- Implement retry logic

### ❌ DON'T
- Handle raw card data
- Store sensitive payment information
- Log sensitive details
- Trust client-side validation only
- Ignore webhook events
- Hardcode API keys
- Use test keys in production
- Skip SSL/TLS verification
- Forget to validate amounts
- Store payment tokens without encryption

## Complete Example

```python
@app.post("/pay")
async def process_payment(amount: float, current_user: dict = Depends(get_current_user)):
    result = StripePaymentService.create_payment_intent(amount)
    if result['success']:
        return result
    raise HTTPException(status_code=400, detail=result['error'])
```
