# Webhook Sender (TypeScript)

## Webhook Sender (TypeScript)

```typescript
import crypto from "crypto";
import axios from "axios";

interface WebhookEvent {
  id: string;
  type: string;
  timestamp: number;
  data: any;
}

interface WebhookEndpoint {
  url: string;
  secret: string;
  events: string[];
  active: boolean;
}

interface DeliveryAttempt {
  attemptNumber: number;
  timestamp: number;
  statusCode?: number;
  error?: string;
  duration: number;
}

class WebhookSender {
  private maxRetries = 3;
  private retryDelays = [1000, 5000, 30000]; // Exponential backoff
  private timeout = 10000; // 10 seconds

  /**
   * Generate HMAC signature for webhook payload
   */
  private generateSignature(payload: string, secret: string): string {
    return crypto.createHmac("sha256", secret).update(payload).digest("hex");
  }

  /**
   * Send webhook to endpoint
   */
  async send(
    endpoint: WebhookEndpoint,
    event: WebhookEvent,
  ): Promise<DeliveryAttempt[]> {
    if (!endpoint.active) {
      throw new Error("Endpoint is not active");
    }

    if (!endpoint.events.includes(event.type)) {
      throw new Error(`Event type ${event.type} not subscribed`);
    }

    const payload = JSON.stringify(event);
    const signature = this.generateSignature(payload, endpoint.secret);

    const attempts: DeliveryAttempt[] = [];

    for (let attempt = 0; attempt < this.maxRetries; attempt++) {
      const startTime = Date.now();

      try {
        const response = await axios.post(endpoint.url, payload, {
          headers: {
            "Content-Type": "application/json",
            "X-Webhook-Signature": signature,
            "X-Webhook-ID": event.id,
            "X-Webhook-Timestamp": event.timestamp.toString(),
            "User-Agent": "WebhookService/1.0",
          },
          timeout: this.timeout,
          validateStatus: (status) => status >= 200 && status < 300,
        });

        const duration = Date.now() - startTime;

        attempts.push({
          attemptNumber: attempt + 1,
          timestamp: Date.now(),
          statusCode: response.status,
          duration,
        });

        console.log(
          `Webhook delivered successfully to ${endpoint.url} (attempt ${attempt + 1})`,
        );

        return attempts;
      } catch (error: any) {
        const duration = Date.now() - startTime;

        attempts.push({
          attemptNumber: attempt + 1,
          timestamp: Date.now(),
          statusCode: error.response?.status,
          error: error.message,
          duration,
        });

        console.error(
          `Webhook delivery failed to ${endpoint.url} (attempt ${attempt + 1}):`,
          error.message,
        );

        // Wait before retry (except on last attempt)
        if (attempt < this.maxRetries - 1) {
          await this.delay(this.retryDelays[attempt]);
        }
      }
    }

    throw new Error(
      `Webhook delivery failed after ${this.maxRetries} attempts`,
    );
  }

  /**
   * Batch send webhooks
   */
  async sendBatch(
    endpoints: WebhookEndpoint[],
    event: WebhookEvent,
  ): Promise<Map<string, DeliveryAttempt[]>> {
    const results = new Map<string, DeliveryAttempt[]>();

    await Promise.allSettled(
      endpoints.map(async (endpoint) => {
        try {
          const attempts = await this.send(endpoint, event);
          results.set(endpoint.url, attempts);
        } catch (error) {
          console.error(`Failed to deliver to ${endpoint.url}:`, error);
        }
      }),
    );

    return results;
  }

  private delay(ms: number): Promise<void> {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }
}

// Usage
const sender = new WebhookSender();

const endpoint: WebhookEndpoint = {
  url: "https://api.example.com/webhooks",
  secret: "your-webhook-secret",
  events: ["user.created", "user.updated"],
  active: true,
};

const event: WebhookEvent = {
  id: crypto.randomUUID(),
  type: "user.created",
  timestamp: Date.now(),
  data: {
    userId: "123",
    email: "user@example.com",
  },
};

await sender.send(endpoint, event);
```
