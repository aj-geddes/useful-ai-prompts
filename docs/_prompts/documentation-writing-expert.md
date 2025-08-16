---
category: creation
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for creation optimization and expert consultation
slug: documentation-writing-expert
tags:
- creation
title: Documentation Writing Expert
use_cases:
- creation optimization
- professional workflow enhancement
version: 3.0.0
---

# Documentation Writing Expert

## Metadata

- **Category**: Creation
- **Tags**: technical writing, documentation, API docs, user guides, knowledge management
- **Created**: 2025-07-20
- **Version**: 2.0.0
- **Use Cases**: API documentation, user manuals, developer guides, system documentation, process documentation
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A practical documentation writing assistant that helps you create clear, comprehensive, and user-friendly documentation. Provide your documentation requirements and I'll create well-structured content that helps your users accomplish their goals efficiently.

## Prompt

```
I'll help you create clear, comprehensive documentation that helps your users succeed. Let me gather information about what you need to document.

About your documentation project:
1. What are you documenting? (software, API, process, system, etc.)
2. Who will be reading this documentation? (developers, end users, administrators, etc.)
3. What's their technical skill level? (beginner, intermediate, advanced, mixed)
4. What do you want readers to accomplish after reading?

Documentation scope and format:
5. What type of documentation do you need? (user guide, API reference, tutorial, troubleshooting guide)
6. How will users access it? (website, PDF, within app, printed)
7. How detailed should it be? (quick reference, comprehensive guide, step-by-step)
8. Do you have existing documentation to build on?

Context and requirements:
9. What specific features/processes need to be covered?
10. Are there any style guidelines or standards to follow?
11. What examples or screenshots can you provide?
12. How often will this documentation need updates?

Based on your answers, I'll create:

**1. STRUCTURED DOCUMENTATION** - Clear, logical flow with appropriate headings and sections
**2. PRACTICAL EXAMPLES** - Real-world scenarios and code samples users can follow
**3. USER-FOCUSED CONTENT** - Task-oriented writing that helps users accomplish their goals
**4. VISUAL ELEMENTS** - Suggestions for diagrams, screenshots, and formatting
**5. MAINTENANCE PLAN** - Guidelines for keeping documentation current and useful

Please provide the information above, and I'll create documentation that truly serves your users' needs.
```

## Example Usage

**User Input:**
```
1. Documenting: REST API for e-commerce platform
2. Readers: Frontend developers integrating our payment system
3. Skill level: Intermediate developers familiar with APIs
4. Goal: Successfully integrate payment processing into their apps

5. Type: API reference documentation with integration guide
6. Access: Developer portal website with search functionality
7. Detail level: Comprehensive with working code examples
8. Existing docs: We have basic endpoint descriptions that need major improvement

9. Features: Payment processing, subscription management, webhook notifications
10. Style: Follow RESTful documentation standards, conversational but technical
11. Examples: Can provide Postman collection and sample responses
12. Updates: Quarterly releases with new features and endpoints
```

**Assistant Output:**

Based on your e-commerce payment API requirements, here's your comprehensive documentation:

# Payment API Documentation

## Quick Start Guide

### Get Your API Keys
1. Sign up at [developer.paymentco.com](https://developer.paymentco.com)
2. Navigate to **API Keys** in your dashboard
3. Copy your **Publishable Key** (for frontend) and **Secret Key** (for backend)

> 🔐 **Security**: Never expose your secret key in client-side code!

### Make Your First Payment
Test the API with this simple request:

```bash
curl -X POST https://api.paymentco.com/v1/payments \
  -H "Authorization: Bearer sk_test_your_secret_key" \
  -H "Content-Type: application/json" \
  -d '{
    "amount": 2000,
    "currency": "usd", 
    "payment_method": "pm_card_visa"
  }'
```

**Expected Response:**
```json
{
  "id": "pay_1234567890",
  "status": "succeeded",
  "amount": 2000,
  "currency": "usd",
  "created": 1640995200
}
```

## API Reference

### Payments

#### Create a Payment
```http
POST /v1/payments
```

Process a one-time payment.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `amount` | integer | ✓ | Amount in cents (e.g., 2000 = $20.00) |
| `currency` | string | ✓ | Three-letter ISO currency code |
| `payment_method` | string | ✓ | Payment method ID |
| `description` | string |  | Internal description |
| `metadata` | object |  | Custom key-value pairs |

**Example Request:**

```javascript
// Using fetch API
const response = await fetch('https://api.paymentco.com/v1/payments', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk_test_your_secret_key',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    amount: 2000,
    currency: 'usd',
    payment_method: 'pm_card_visa',
    description: 'T-shirt purchase',
    metadata: {
      order_id: '12345',
      customer_email: 'customer@example.com'
    }
  })
});

const payment = await response.json();
```

**Response:**
```json
{
  "id": "pay_1234567890",
  "status": "succeeded",
  "amount": 2000,
  "currency": "usd",
  "description": "T-shirt purchase",
  "payment_method": "pm_card_visa",
  "metadata": {
    "order_id": "12345",
    "customer_email": "customer@example.com"
  },
  "created": 1640995200
}
```

#### Retrieve a Payment
```http
GET /v1/payments/{PAYMENT_ID}
```

Get details about a specific payment.

```bash
curl https://api.paymentco.com/v1/payments/pay_1234567890 \
  -H "Authorization: Bearer sk_test_your_secret_key"
```

### Subscriptions

#### Create a Subscription
```http
POST /v1/subscriptions
```

Set up recurring billing for a customer.

**Parameters:**

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `customer` | string | ✓ | Customer ID |
| `price` | string | ✓ | Price ID for the subscription |
| `payment_method` | string | ✓ | Default payment method |
| `trial_period_days` | integer |  | Free trial period |

**Example:**
```javascript
const subscription = await fetch('https://api.paymentco.com/v1/subscriptions', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer sk_test_your_secret_key',
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    customer: 'cus_1234567890',
    price: 'price_monthly_plan',
    payment_method: 'pm_card_visa',
    trial_period_days: 14
  })
});
```

## Integration Guide

### Frontend Integration

#### 1. Collect Payment Information
```html
<!-- Payment form -->
<form id="payment-form">
  <input type="text" id="card-number" placeholder="Card Number">
  <input type="text" id="card-expiry" placeholder="MM/YY">
  <input type="text" id="card-cvc" placeholder="CVC">
  <button type="submit">Pay $20.00</button>
</form>

<script src="https://js.paymentco.com/v3/"></script>
<script>
  const paymentco = PaymentCo('pk_test_your_publishable_key');
  
  document.getElementById('payment-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    // Create payment method
    const {paymentMethod, error} = await paymentco.createPaymentMethod({
      type: 'card',
      card: {
        number: document.getElementById('card-number').value,
        exp_month: parseInt(document.getElementById('card-expiry').value.split('/')[0]),
        exp_year: parseInt('20' + document.getElementById('card-expiry').value.split('/')[1]),
        cvc: document.getElementById('card-cvc').value,
      }
    });
    
    if (error) {
      console.error('Payment method creation failed:', error);
      return;
    }
    
    // Send to your backend
    processPayment(paymentMethod.id);
  });
</script>
```

#### 2. Backend Processing
```javascript
// Node.js example
app.post('/process-payment', async (req, res) => {
  try {
    const payment = await fetch('https://api.paymentco.com/v1/payments', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${process.env.PAYMENTCO_SECRET_KEY}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        amount: 2000,
        currency: 'usd',
        payment_method: req.body.payment_method_id,
        confirm: true
      })
    });
    
    const result = await payment.json();
    res.json(result);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});
```

### Webhook Integration

#### Setting Up Webhooks
1. Go to your [developer dashboard](https://developer.paymentco.com/webhooks)
2. Click **Add Endpoint**  
3. Enter your endpoint URL: `https://yoursite.com/webhooks/paymentco`
4. Select events to monitor

#### Webhook Handler Example
```javascript
app.post('/webhooks/paymentco', express.raw({type: 'application/json'}), (req, res) => {
  const sig = req.headers['paymentco-signature'];
  
  try {
    // Verify webhook signature
    const event = paymentco.webhooks.constructEvent(req.body, sig, process.env.WEBHOOK_SECRET);
    
    switch (event.type) {
      case 'payment.succeeded':
        console.log('Payment successful:', event.data.object.id);
        // Update your database, send confirmation email, etc.
        break;
        
      case 'payment.failed':
        console.log('Payment failed:', event.data.object.id);
        // Handle failed payment
        break;
        
      case 'subscription.created':
        console.log('New subscription:', event.data.object.id);
        // Grant access to premium features
        break;
    }
    
    res.json({received: true});
  } catch (err) {
    console.log('Webhook signature verification failed:', err.message);
    res.status(400).send(`Webhook Error: ${err.message}`);
  }
});
```

## Error Handling

### Common Error Codes

| Code | Description | Resolution |
|------|-------------|------------|
| `card_declined` | Card was declined by bank | Ask customer to try different card |
| `insufficient_funds` | Not enough money in account | Customer needs to add funds |
| `invalid_request` | Missing or invalid parameters | Check API documentation |
| `rate_limit_exceeded` | Too many requests | Implement exponential backoff |

### Error Response Format
```json
{
  "error": {
    "type": "card_error",
    "code": "card_declined",
    "message": "Your card was declined.",
    "param": "payment_method"
  }
}
```

### Retry Logic Example
```javascript
async function createPaymentWithRetry(paymentData, maxRetries = 3) {
  for (let i = 0; i < maxRetries; i++) {
    try {
      return await createPayment(paymentData);
    } catch (error) {
      if (error.type === 'rate_limit_error' && i < maxRetries - 1) {
        await new Promise(resolve => setTimeout(resolve, Math.pow(2, i) * 1000));
        continue;
      }
      throw error;
    }
  }
}
```

## Testing

### Test Cards
Use these test card numbers in your integration:

| Card | Number | Result |
|------|--------|--------|
| Visa | `4242424242424242` | Success |
| Visa (Declined) | `4000000000000002` | Card declined |
| Mastercard | `5555555555554444` | Success |

### Test Mode
- Use `pk_test_` and `sk_test_` keys for testing
- No real charges are processed
- All test data is isolated from live data

## Rate Limits
- **Test mode**: 1000 requests/hour
- **Live mode**: 5000 requests/hour  
- Rate limits reset every hour
- Use exponential backoff when hitting limits

## Security Best Practices
✅ Always use HTTPS endpoints  
✅ Never log full card numbers  
✅ Validate webhook signatures  
✅ Use test keys during development  
✅ Follow PCI DSS guidelines  

Need help? Contact our developer support at dev-support@paymentco.com

## Related Prompts

- [API Design Specialist](./api-design-specialist.md)
- [Technical Writing Expert](./technical-writing-expert.md)
- [User Manual Creator](./user-manual-creator.md)
