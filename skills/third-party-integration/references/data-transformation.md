# Data Transformation

## Data Transformation

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
      metadata: charge.metadata,
    };
  }

  static sendgridEmailToLog(event) {
    return {
      messageId: event.sg_message_id,
      email: event.email,
      eventType: event.event,
      timestamp: new Date(event.timestamp * 1000),
      metadata: event,
    };
  }

  static awsS3FileToRecord(s3Object) {
    return {
      key: s3Object.Key,
      size: s3Object.Size,
      lastModified: s3Object.LastModified,
      etag: s3Object.ETag,
      bucket: s3Object.Bucket,
    };
  }
}
```
