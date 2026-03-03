# Payment Processor Integration (Stripe)

## Payment Processor Integration (Stripe)

```javascript
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);

class PaymentService {
  async createCharge(userId, amount, paymentMethodId) {
    try {
      const customer = await this.getOrCreateCustomer(userId);

      const charge = await stripe.charges.create({
        amount: Math.round(amount * 100), // cents
        currency: "usd",
        customer: customer.id,
        payment_method: paymentMethodId,
        confirm: true,
      });

      // Log transaction
      await Transaction.create({
        userId,
        chargeId: charge.id,
        amount,
        status: charge.status,
        createdAt: new Date(charge.created * 1000),
      });

      return {
        success: true,
        chargeId: charge.id,
        status: charge.status,
      };
    } catch (error) {
      console.error("Charge error:", error.message);

      if (error.code === "card_declined") {
        return { success: false, error: "Card declined" };
      }

      throw error;
    }
  }

  async refund(chargeId, amount = null) {
    try {
      const refund = await stripe.refunds.create({
        charge: chargeId,
        amount: amount ? Math.round(amount * 100) : undefined,
      });

      await Transaction.updateOne(
        { chargeId },
        { refundId: refund.id, status: "refunded" },
      );

      return { success: true, refundId: refund.id };
    } catch (error) {
      console.error("Refund error:", error.message);
      throw error;
    }
  }

  async getOrCreateCustomer(userId) {
    let customer = await Customer.findOne({ userId });

    if (!customer) {
      const stripeCustomer = await stripe.customers.create({
        metadata: { userId },
      });

      customer = await Customer.create({
        userId,
        stripeId: stripeCustomer.id,
      });
    }

    return customer;
  }

  async handleWebhook(event) {
    switch (event.type) {
      case "charge.succeeded":
        await this.handleChargeSucceeded(event.data.object);
        break;
      case "charge.failed":
        await this.handleChargeFailed(event.data.object);
        break;
      case "refund.created":
        await this.handleRefund(event.data.object);
        break;
    }
  }
}

// Webhook endpoint
app.post(
  "/webhooks/stripe",
  express.raw({ type: "application/json" }),
  async (req, res) => {
    const sig = req.headers["stripe-signature"];

    try {
      const event = stripe.webhooks.constructEvent(
        req.body,
        sig,
        process.env.STRIPE_WEBHOOK_SECRET,
      );

      await paymentService.handleWebhook(event);
      res.json({ received: true });
    } catch (error) {
      res.status(400).json({ error: error.message });
    }
  },
);
```
