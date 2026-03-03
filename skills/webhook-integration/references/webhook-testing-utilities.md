# Webhook Testing Utilities

## Webhook Testing Utilities

```typescript
import express from "express";
import crypto from "crypto";

class WebhookTester {
  private app: express.Application;
  private receivedEvents: WebhookEvent[] = [];

  constructor() {
    this.app = express();
    this.setupTestEndpoint();
  }

  private setupTestEndpoint(): void {
    this.app.use(express.json());

    this.app.post("/test-webhook", (req, res) => {
      const event = req.body;

      // Validate signature if provided
      const signature = req.headers["x-webhook-signature"] as string;
      if (signature) {
        // Verify signature here
      }

      // Store received event
      this.receivedEvents.push(event);

      console.log("Received webhook:", event);

      // Respond based on test scenario
      res.status(200).json({
        received: true,
        eventId: event.id,
      });
    });

    // Endpoint that simulates failures
    this.app.post("/test-webhook/fail", (req, res) => {
      const failureType = req.query.type;

      switch (failureType) {
        case "timeout":
          // Don't respond (simulates timeout)
          break;
        case "server-error":
          res.status(500).json({ error: "Internal server error" });
          break;
        case "unauthorized":
          res.status(401).json({ error: "Unauthorized" });
          break;
        default:
          res.status(400).json({ error: "Bad request" });
      }
    });
  }

  start(port: number): void {
    this.app.listen(port, () => {
      console.log(`Webhook test server running on port ${port}`);
    });
  }

  getReceivedEvents(): WebhookEvent[] {
    return this.receivedEvents;
  }

  clearEvents(): void {
    this.receivedEvents = [];
  }

  /**
   * Create mock webhook event
   */
  static createMockEvent(type: string, data: any): WebhookEvent {
    return {
      id: crypto.randomUUID(),
      type,
      timestamp: Date.now(),
      data,
    };
  }
}

// Testing
const tester = new WebhookTester();
tester.start(3001);

// Send test webhook
const mockEvent = WebhookTester.createMockEvent("user.created", {
  userId: "123",
  email: "test@example.com",
});

const sender = new WebhookSender();
await sender.send(
  {
    url: "http://localhost:3001/test-webhook",
    secret: "test-secret",
    events: ["user.created"],
    active: true,
  },
  mockEvent,
);

// Verify received
const received = tester.getReceivedEvents();
console.log("Received events:", received);
```
