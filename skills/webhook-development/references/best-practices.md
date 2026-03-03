# Best Practices

## Best Practices

```
✅ DO:
- Sign all webhooks with HMAC
- Implement exponential backoff retries
- Use message queues for reliable delivery
- Track webhook deliveries for debugging
- Provide webhook test endpoints
- Document supported event types
- Use unique event IDs for deduplication
- Set appropriate timeouts (10s)
- Implement dead-letter queues
- Return 2xx quickly, process async

❌ DON'T:
- Send sensitive data without encryption
- Use weak signatures
- Synchronous webhook delivery
- Ignore signature verification
- Expose webhook URLs publicly
- Retry indefinitely
- Log webhook payloads with secrets
- Skip webhook authentication
- Forget to handle idempotency
- Send duplicate events
```


## Webhook Events

```
Standard Event Types:
- order.created
- order.updated
- order.cancelled
- payment.succeeded
- payment.failed
- user.registered
- user.updated
- invoice.issued
- shipment.created
- refund.processed
```
