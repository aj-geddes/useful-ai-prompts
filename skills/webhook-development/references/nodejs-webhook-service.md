# Node.js Webhook Service

## Node.js Webhook Service

```javascript
const express = require("express");
const crypto = require("crypto");
const axios = require("axios");
const Bull = require("bull");

const app = express();
app.use(express.json());

const WEBHOOK_SECRET = process.env.WEBHOOK_SECRET;
const webhookQueue = new Bull("webhooks", {
  redis: { host: "localhost", port: 6379 },
});

// Register webhook subscription
app.post("/api/webhooks/subscribe", async (req, res) => {
  const { url, events, secret } = req.body;

  // Validate URL
  try {
    new URL(url);
  } catch {
    return res.status(400).json({ error: "Invalid URL" });
  }

  const webhook = {
    id: crypto.randomBytes(16).toString("hex"),
    url,
    events,
    secret: secret || crypto.randomBytes(32).toString("hex"),
    active: true,
    createdAt: new Date(),
    failureCount: 0,
  };

  // Save to database
  await WebhookSubscription.create(webhook);

  res.status(201).json({
    id: webhook.id,
    secret: webhook.secret,
    message: "Webhook registered successfully",
  });
});

// Send webhook event
const sendWebhookEvent = async (eventType, data) => {
  const webhooks = await WebhookSubscription.find({
    events: eventType,
    active: true,
  });

  for (const webhook of webhooks) {
    const event = {
      id: `evt_${Date.now()}`,
      timestamp: new Date().toISOString(),
      event: eventType,
      version: "1.0",
      data,
      attempt: 1,
      retryable: true,
    };

    // Add to queue
    await webhookQueue.add(
      { webhook, event },
      {
        attempts: 5,
        backoff: {
          type: "exponential",
          delay: 2000,
        },
        removeOnComplete: true,
      },
    );
  }
};

// Process webhook queue
webhookQueue.process(async (job) => {
  const { webhook, event } = job.data;

  try {
    const signature = generateSignature(event, webhook.secret);

    const response = await axios.post(webhook.url, event, {
      headers: {
        "Content-Type": "application/json",
        "X-Webhook-Signature": signature,
        "X-Webhook-ID": event.id,
        "X-Webhook-Attempt": event.attempt,
      },
      timeout: 10000,
    });

    if (response.status >= 200 && response.status < 300) {
      // Success
      await WebhookDelivery.create({
        webhookId: webhook.id,
        eventId: event.id,
        status: "delivered",
        statusCode: response.status,
        deliveredAt: new Date(),
      });
      return;
    }

    throw new Error(`HTTP ${response.status}`);
  } catch (error) {
    // Retry or dead letter
    if (job.attemptsMade < 5) {
      throw error; // Retry
    } else {
      // Dead letter
      await DeadLetterQueue.create({
        webhookId: webhook.id,
        eventId: event.id,
        event,
        error: error.message,
        failedAt: new Date(),
      });

      // Update failure count
      webhook.failureCount++;
      if (webhook.failureCount >= 10) {
        webhook.active = false;
      }
      await webhook.save();
    }
  }
});

// Webhook endpoint (receiving webhooks)
app.post("/webhooks/:id", async (req, res) => {
  const signature = req.headers["x-webhook-signature"];
  const webhookId = req.params.id;
  const event = req.body;

  try {
    const webhook = await WebhookSubscription.findOne({ id: webhookId });
    if (!webhook) {
      return res.status(404).json({ error: "Webhook not found" });
    }

    // Verify signature
    const expectedSignature = generateSignature(event, webhook.secret);
    if (signature !== expectedSignature) {
      return res.status(401).json({ error: "Invalid signature" });
    }

    // Process event
    console.log("Received webhook event:", event);

    res.status(200).json({ received: true });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// Signature generation
const generateSignature = (payload, secret) => {
  const message = JSON.stringify(payload);
  return crypto.createHmac("sha256", secret).update(message).digest("hex");
};

// List webhook subscriptions
app.get("/api/webhooks", async (req, res) => {
  const webhooks = await WebhookSubscription.find({}, { secret: 0 });
  res.json(webhooks);
});

// Test webhook delivery
app.post("/api/webhooks/:id/test", async (req, res) => {
  const webhook = await WebhookSubscription.findOne({ id: req.params.id });

  const testEvent = {
    id: `evt_test_${Date.now()}`,
    timestamp: new Date().toISOString(),
    event: "webhook.test",
    data: { message: "Test event" },
  };

  await webhookQueue.add({ webhook, event: testEvent });

  res.json({ message: "Test event queued" });
});

// Retry failed deliveries
app.post("/api/webhooks/deliveries/:id/retry", async (req, res) => {
  const delivery = await WebhookDelivery.findOne({ _id: req.params.id });
  if (!delivery) {
    return res.status(404).json({ error: "Delivery not found" });
  }

  const webhook = await WebhookSubscription.findOne({ id: delivery.webhookId });
  const event = await Event.findOne({ id: delivery.eventId });

  await webhookQueue.add({ webhook, event });

  res.json({ message: "Retry queued" });
});

// List webhook deliveries
app.get("/api/webhooks/:id/deliveries", async (req, res) => {
  const deliveries = await WebhookDelivery.find({
    webhookId: req.params.id,
  }).limit(100);

  res.json(deliveries);
});

// Event trigger examples
app.post("/api/orders", async (req, res) => {
  const order = await Order.create(req.body);

  // Send webhook event
  await sendWebhookEvent("order.created", {
    orderId: order.id,
    customerId: order.customerId,
    amount: order.amount,
    status: order.status,
  });

  res.status(201).json(order);
});

app.listen(3000, () => console.log("Server on port 3000"));
```
