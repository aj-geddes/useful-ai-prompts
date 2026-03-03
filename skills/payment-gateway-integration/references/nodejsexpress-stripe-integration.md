# Node.js/Express Stripe Integration

## Node.js/Express Stripe Integration

```javascript
// stripe-service.js
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
const logger = require("./logger");

class StripeService {
  async createPaymentIntent(amount, currency = "usd", metadata = {}) {
    try {
      const intent = await stripe.paymentIntents.create({
        amount: Math.round(amount * 100),
        currency: currency,
        metadata: metadata,
      });

      logger.info(`Payment intent created: ${intent.id}`);
      return {
        success: true,
        clientSecret: intent.client_secret,
        intentId: intent.id,
      };
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
        metadata: metadata,
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
        metadata: metadata,
      });

      logger.info(`Subscription created: ${subscription.id}`);
      return {
        success: true,
        subscriptionId: subscription.id,
        status: subscription.status,
      };
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
        ...(amount && { amount: Math.round(amount * 100) }),
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
const express = require("express");
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
const stripeService = require("../services/stripe-service");
const { authenticate } = require("../middleware/auth");

const router = express.Router();

router.post("/create-intent", authenticate, async (req, res) => {
  const { amount, description } = req.body;

  if (!amount || amount <= 0) {
    return res.status(400).json({ error: "Invalid amount" });
  }

  const result = await stripeService.createPaymentIntent(amount, "usd", {
    userId: req.user.id,
    description: description,
  });

  if (result.success) {
    res.json(result);
  } else {
    res.status(400).json(result);
  }
});

router.post(
  "/webhook",
  express.raw({ type: "application/json" }),
  async (req, res) => {
    const signature = req.headers["stripe-signature"];

    try {
      const event = stripe.webhooks.constructEvent(
        req.body,
        signature,
        process.env.STRIPE_WEBHOOK_SECRET,
      );

      if (event.type === "payment_intent.succeeded") {
        const intent = event.data.object;
        logger.info(`Payment succeeded: ${intent.id}`);
        // Update order status
      } else if (event.type === "customer.subscription.updated") {
        const subscription = event.data.object;
        logger.info(`Subscription updated: ${subscription.id}`);
      } else if (event.type === "invoice.payment_succeeded") {
        const invoice = event.data.object;
        logger.info(`Invoice paid: ${invoice.id}`);
      }

      res.json({ received: true });
    } catch (error) {
      logger.error(`Webhook error: ${error.message}`);
      res.status(400).send(`Webhook Error: ${error.message}`);
    }
  },
);

module.exports = router;
```
