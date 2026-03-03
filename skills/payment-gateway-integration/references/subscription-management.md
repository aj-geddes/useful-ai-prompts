# Subscription Management

## Subscription Management

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
