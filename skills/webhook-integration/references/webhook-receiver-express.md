# Webhook Receiver (Express)

## Webhook Receiver (Express)

```typescript
import express from "express";
import crypto from "crypto";
import { body, validationResult } from "express-validator";

interface WebhookConfig {
  secret: string;
  signatureHeader: string;
  timestampTolerance: number; // seconds
}

class WebhookReceiver {
  constructor(private config: WebhookConfig) {}

  /**
   * Verify webhook signature
   */
  verifySignature(payload: string, signature: string): boolean {
    const expectedSignature = crypto
      .createHmac("sha256", this.config.secret)
      .update(payload)
      .digest("hex");

    return crypto.timingSafeEqual(
      Buffer.from(signature),
      Buffer.from(expectedSignature),
    );
  }

  /**
   * Verify timestamp to prevent replay attacks
   */
  verifyTimestamp(timestamp: number): boolean {
    const now = Date.now();
    const diff = Math.abs(now - timestamp) / 1000;

    return diff <= this.config.timestampTolerance;
  }

  /**
   * Middleware for webhook verification
   */
  createMiddleware() {
    return async (
      req: express.Request,
      res: express.Response,
      next: express.NextFunction,
    ) => {
      try {
        const signature = req.headers[this.config.signatureHeader] as string;
        const timestamp = parseInt(
          req.headers["x-webhook-timestamp"] as string,
        );

        if (!signature) {
          return res.status(401).json({
            error: "Missing signature",
          });
        }

        // Verify timestamp
        if (!this.verifyTimestamp(timestamp)) {
          return res.status(401).json({
            error: "Invalid timestamp",
          });
        }

        // Get raw body for signature verification
        const payload = JSON.stringify(req.body);

        // Verify signature
        if (!this.verifySignature(payload, signature)) {
          return res.status(401).json({
            error: "Invalid signature",
          });
        }

        next();
      } catch (error) {
        console.error("Webhook verification error:", error);
        res.status(500).json({
          error: "Verification failed",
        });
      }
    };
  }
}

// Setup Express app
const app = express();

// Use raw body parser for signature verification
app.use(
  express.json({
    verify: (req: any, res, buf) => {
      req.rawBody = buf.toString();
    },
  }),
);

const receiver = new WebhookReceiver({
  secret: process.env.WEBHOOK_SECRET!,
  signatureHeader: "x-webhook-signature",
  timestampTolerance: 300, // 5 minutes
});

// Webhook endpoint
app.post(
  "/webhooks",
  receiver.createMiddleware(),
  [body("id").isString(), body("type").isString(), body("data").isObject()],
  async (req, res) => {
    // Validate request
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
      return res.status(400).json({ errors: errors.array() });
    }

    const { id, type, data } = req.body;

    try {
      // Process webhook event
      await processWebhookEvent(type, data);

      // Respond immediately
      res.status(200).json({
        received: true,
        eventId: id,
      });

      // Process asynchronously if needed
      processEventAsync(type, data).catch(console.error);
    } catch (error) {
      console.error("Webhook processing error:", error);
      res.status(500).json({
        error: "Processing failed",
      });
    }
  },
);

async function processWebhookEvent(type: string, data: any): Promise<void> {
  switch (type) {
    case "user.created":
      await handleUserCreated(data);
      break;
    case "payment.success":
      await handlePaymentSuccess(data);
      break;
    default:
      console.log(`Unknown event type: ${type}`);
  }
}

async function processEventAsync(type: string, data: any): Promise<void> {
  // Heavy processing that doesn't need to block the response
}

async function handleUserCreated(data: any): Promise<void> {
  console.log("User created:", data);
}

async function handlePaymentSuccess(data: any): Promise<void> {
  console.log("Payment successful:", data);
}

app.listen(3000, () => {
  console.log("Webhook receiver listening on port 3000");
});
```
