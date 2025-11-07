---
name: third-party-integration
description: Integrate external APIs and services with error handling, retry logic, and data transformation. Use when connecting to payment processors, messaging services, analytics platforms, or other third-party providers.
---

# Third-Party Integration

## Overview

Build robust integrations with external services using standardized patterns for API calls, error handling, authentication, and data transformation.

## When to Use

- Integrating payment processors (Stripe, PayPal)
- Using messaging services (SendGrid, Twilio)
- Connecting to analytics platforms (Mixpanel, Segment)
- Syncing with storage services (AWS S3, Google Cloud)
- Integrating CRM systems (Salesforce, HubSpot)
- Building multi-service architectures

## Instructions

### 1. **Third-Party Client Wrapper**

```javascript
const axios = require('axios');

class ThirdPartyClient {
  constructor(config) {
    this.apiKey = config.apiKey;
    this.baseUrl = config.baseUrl;
    this.timeout = config.timeout || 30000;
    this.retryAttempts = config.retryAttempts || 3;
    this.retryDelay = config.retryDelay || 1000;
    this.client = axios.create({
      baseURL: this.baseUrl,
      timeout: this.timeout,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json'
      }
    });
  }

  async request(method, endpoint, data = null, options = {}) {
    let lastError;

    for (let attempt = 0; attempt < this.retryAttempts; attempt++) {
      try {
        const response = await this.client({
          method,
          url: endpoint,
          data,
          timeout: this.timeout,
          ...options
        });

        return {
          success: true,
          data: response.data,
          statusCode: response.status,
          headers: response.headers
        };
      } catch (error) {
        lastError = error;

        // Check if error is retryable
        if (!this.isRetryable(error) || attempt === this.retryAttempts - 1) {
          break;
        }

        // Exponential backoff
        const delay = this.retryDelay * Math.pow(2, attempt);
        await this.sleep(delay);
      }
    }

    return this.handleError(lastError);
  }

  isRetryable(error) {
    if (!error.response) return true; // Network error

    const status = error.response.status;
    // Retry on 5xx and specific 4xx errors
    return status >= 500 || [408, 429].includes(status);
  }

  handleError(error) {
    if (error.response) {
      return {
        success: false,
        error: {
          message: error.response.data?.message || error.message,
          code: error.response.data?.code || error.response.status,
          status: error.response.status,
          data: error.response.data
        }
      };
    }

    return {
      success: false,
      error: {
        message: error.message,
        code: 'NETWORK_ERROR'
      }
    };
  }

  sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
  }

  async get(endpoint) {
    return this.request('GET', endpoint);
  }

  async post(endpoint, data) {
    return this.request('POST', endpoint, data);
  }

  async put(endpoint, data) {
    return this.request('PUT', endpoint, data);
  }

  async delete(endpoint) {
    return this.request('DELETE', endpoint);
  }
}

// Usage
const stripeClient = new ThirdPartyClient({
  apiKey: process.env.STRIPE_API_KEY,
  baseUrl: 'https://api.stripe.com/v1',
  timeout: 30000,
  retryAttempts: 3
});

const result = await stripeClient.post('/charges', {
  amount: 10000,
  currency: 'usd',
  source: 'tok_visa'
});
```

### 2. **Payment Processor Integration (Stripe)**

```javascript
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);

class PaymentService {
  async createCharge(userId, amount, paymentMethodId) {
    try {
      const customer = await this.getOrCreateCustomer(userId);

      const charge = await stripe.charges.create({
        amount: Math.round(amount * 100), // cents
        currency: 'usd',
        customer: customer.id,
        payment_method: paymentMethodId,
        confirm: true
      });

      // Log transaction
      await Transaction.create({
        userId,
        chargeId: charge.id,
        amount,
        status: charge.status,
        createdAt: new Date(charge.created * 1000)
      });

      return {
        success: true,
        chargeId: charge.id,
        status: charge.status
      };
    } catch (error) {
      console.error('Charge error:', error.message);

      if (error.code === 'card_declined') {
        return { success: false, error: 'Card declined' };
      }

      throw error;
    }
  }

  async refund(chargeId, amount = null) {
    try {
      const refund = await stripe.refunds.create({
        charge: chargeId,
        amount: amount ? Math.round(amount * 100) : undefined
      });

      await Transaction.updateOne(
        { chargeId },
        { refundId: refund.id, status: 'refunded' }
      );

      return { success: true, refundId: refund.id };
    } catch (error) {
      console.error('Refund error:', error.message);
      throw error;
    }
  }

  async getOrCreateCustomer(userId) {
    let customer = await Customer.findOne({ userId });

    if (!customer) {
      const stripeCustomer = await stripe.customers.create({
        metadata: { userId }
      });

      customer = await Customer.create({
        userId,
        stripeId: stripeCustomer.id
      });
    }

    return customer;
  }

  async handleWebhook(event) {
    switch (event.type) {
      case 'charge.succeeded':
        await this.handleChargeSucceeded(event.data.object);
        break;
      case 'charge.failed':
        await this.handleChargeFailed(event.data.object);
        break;
      case 'refund.created':
        await this.handleRefund(event.data.object);
        break;
    }
  }
}

// Webhook endpoint
app.post('/webhooks/stripe', express.raw({type: 'application/json'}), async (req, res) => {
  const sig = req.headers['stripe-signature'];

  try {
    const event = stripe.webhooks.constructEvent(
      req.body,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );

    await paymentService.handleWebhook(event);
    res.json({ received: true });
  } catch (error) {
    res.status(400).json({ error: error.message });
  }
});
```

### 3. **Email Service Integration (SendGrid)**

```javascript
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

class EmailService {
  async sendEmail(to, templateId, templateData = {}) {
    try {
      const message = {
        to,
        from: process.env.FROM_EMAIL,
        templateId,
        dynamicTemplateData: {
          ...templateData,
          timestamp: new Date().toISOString()
        },
        trackingSettings: {
          clickTracking: { enabled: true },
          openTracking: { enabled: true }
        }
      };

      const response = await sgMail.send(message);

      // Log email
      await EmailLog.create({
        to,
        templateId,
        messageId: response[0].headers['x-message-id'],
        status: 'sent',
        sentAt: new Date()
      });

      return { success: true, messageId: response[0].headers['x-message-id'] };
    } catch (error) {
      console.error('Email error:', error.message);

      await EmailLog.create({
        to,
        templateId,
        error: error.message,
        status: 'failed'
      });

      throw error;
    }
  }

  async sendBulk(recipients, templateId, templateData) {
    const promises = recipients.map(recipient =>
      this.sendEmail(recipient, templateId, templateData).catch(err => ({
        recipient,
        error: err.message
      }))
    );

    return Promise.allSettled(promises);
  }

  async handleWebhook(event) {
    const { messageId, event: eventType } = event;

    await EmailLog.updateOne(
      { messageId },
      { status: eventType, updatedAt: new Date() }
    );
  }
}

// Usage
const emailService = new EmailService();

app.post('/api/send-welcome-email', async (req, res) => {
  const { email, firstName } = req.body;

  const result = await emailService.sendEmail(email, 'd-welcome-template-id', {
    firstName
  });

  res.json(result);
});
```

### 4. **Python Third-Party Integration**

```python
import requests
import time
from typing import Optional, Dict, Any
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class APIClient:
    def __init__(self, api_key: str, base_url: str, timeout: int = 30):
        self.api_key = api_key
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        })

    def request(
        self,
        method: str,
        endpoint: str,
        data: Optional[Dict] = None,
        max_retries: int = 3
    ) -> Dict[str, Any]:
        url = f"{self.base_url}/{endpoint}"
        attempt = 0

        while attempt < max_retries:
            try:
                response = self.session.request(
                    method,
                    url,
                    json=data,
                    timeout=self.timeout
                )

                if response.status_code >= 200 and response.status_code < 300:
                    return {
                        'success': True,
                        'data': response.json(),
                        'status': response.status_code
                    }

                if response.status_code >= 500 or response.status_code == 429:
                    raise requests.RequestException(f"HTTP {response.status_code}")

                return {
                    'success': False,
                    'error': response.json().get('message', 'Error'),
                    'status': response.status_code
                }

            except requests.RequestException as e:
                attempt += 1
                if attempt >= max_retries:
                    logger.error(f"API request failed: {e}")
                    return {
                        'success': False,
                        'error': str(e),
                        'status': None
                    }

                wait_time = 2 ** attempt
                time.sleep(wait_time)

        return {'success': False, 'error': 'Max retries exceeded'}

    def get(self, endpoint: str) -> Dict[str, Any]:
        return self.request('GET', endpoint)

    def post(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        return self.request('POST', endpoint, data)

    def put(self, endpoint: str, data: Dict) -> Dict[str, Any]:
        return self.request('PUT', endpoint, data)

    def delete(self, endpoint: str) -> Dict[str, Any]:
        return self.request('DELETE', endpoint)

# Payment processor example
class PaymentGateway(APIClient):
    def create_payment(self, amount: float, currency: str, customer_id: str):
        return self.post('charges', {
            'amount': int(amount * 100),
            'currency': currency,
            'customer': customer_id
        })

    def refund(self, charge_id: str, amount: Optional[float] = None):
        return self.post(f'charges/{charge_id}/refund', {
            'amount': int(amount * 100) if amount else None
        })
```

### 5. **Data Transformation**

```javascript
class DataMapper {
  static stripeChargeToTransaction(charge) {
    return {
      id: charge.id,
      amount: charge.amount / 100,
      currency: charge.currency,
      status: charge.status,
      customerId: charge.customer,
      createdAt: new Date(charge.created * 1000),
      metadata: charge.metadata
    };
  }

  static sendgridEmailToLog(event) {
    return {
      messageId: event.sg_message_id,
      email: event.email,
      eventType: event.event,
      timestamp: new Date(event.timestamp * 1000),
      metadata: event
    };
  }

  static awsS3FileToRecord(s3Object) {
    return {
      key: s3Object.Key,
      size: s3Object.Size,
      lastModified: s3Object.LastModified,
      etag: s3Object.ETag,
      bucket: s3Object.Bucket
    };
  }
}
```

## Best Practices

### ✅ DO
- Implement retry logic with exponential backoff
- Validate webhook signatures
- Log all API interactions
- Use environment variables for secrets
- Transform API responses to internal models
- Implement circuit breakers for critical services
- Monitor API quota and rate limits
- Add proper error handling
- Use timeouts appropriately
- Test with sandbox/test API keys

### ❌ DON'T
- Hardcode API keys
- Retry all errors indefinitely
- Log sensitive data
- Trust unvalidated webhook data
- Ignore rate limits
- Make synchronous blocking calls
- Expose vendor-specific details to clients
- Skip error handling
- Use production keys in tests
