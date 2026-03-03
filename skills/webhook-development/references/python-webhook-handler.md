# Python Webhook Handler

## Python Webhook Handler

```python
from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import hmac
import hashlib
import requests
import json
from celery import Celery
from sqlalchemy import Column, String, Boolean, DateTime, Integer

app = Flask(__name__)
celery = Celery(app.name, broker='redis://localhost:6379')

class WebhookSubscription:
    id = Column(String(100), primary_key=True)
    url = Column(String(500))
    events = Column(String(500))
    secret = Column(String(256))
    active = Column(Boolean, default=True)
    failure_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

def generate_signature(payload, secret):
    message = json.dumps(payload, sort_keys=True)
    return hmac.new(
        secret.encode(),
        message.encode(),
        hashlib.sha256
    ).hexdigest()

@app.route('/api/webhooks/subscribe', methods=['POST'])
def subscribe_webhook():
    data = request.get_json()
    url = data.get('url')
    events = data.get('events', [])
    secret = data.get('secret', os.urandom(32).hex())

    webhook = WebhookSubscription(
        id=f"wh_{secrets.token_hex(8)}",
        url=url,
        events=','.join(events),
        secret=secret,
        active=True
    )

    db.session.add(webhook)
    db.session.commit()

    return jsonify({
        'id': webhook.id,
        'secret': webhook.secret,
        'message': 'Webhook registered'
    }), 201

@celery.task(bind=True, max_retries=5)
def deliver_webhook(self, webhook_id, event):
    webhook = WebhookSubscription.query.get(webhook_id)
    if not webhook:
        return

    signature = generate_signature(event, webhook.secret)

    try:
        response = requests.post(
            webhook.url,
            json=event,
            headers={
                'Content-Type': 'application/json',
                'X-Webhook-Signature': signature,
                'X-Webhook-ID': event['id'],
                'X-Webhook-Attempt': str(event.get('attempt', 1))
            },
            timeout=10
        )

        if 200 <= response.status_code < 300:
            WebhookDelivery.create(
                webhook_id=webhook_id,
                event_id=event['id'],
                status='delivered',
                status_code=response.status_code
            )
            return

        raise Exception(f"HTTP {response.status_code}")

    except Exception as exc:
        retry_delay = 2 ** self.request.retries
        raise self.retry(exc=exc, countdown=retry_delay)

@app.route('/webhooks/<webhook_id>', methods=['POST'])
def receive_webhook(webhook_id):
    signature = request.headers.get('X-Webhook-Signature')
    event = request.get_json()

    webhook = WebhookSubscription.query.get(webhook_id)
    if not webhook:
        return jsonify({'error': 'Not found'}), 404

    expected_signature = generate_signature(event, webhook.secret)
    if signature != expected_signature:
        return jsonify({'error': 'Invalid signature'}), 401

    return jsonify({'received': True}), 200

@app.route('/api/orders', methods=['POST'])
def create_order():
    order = Order.create(request.get_json())

    # Queue webhook delivery
    event = {
        'id': f"evt_{datetime.utcnow().timestamp()}",
        'timestamp': datetime.utcnow().isoformat(),
        'event': 'order.created',
        'data': order.to_dict()
    }

    webhooks = WebhookSubscription.query.filter(
        WebhookSubscription.events.contains('order.created'),
        WebhookSubscription.active == True
    ).all()

    for webhook in webhooks:
        deliver_webhook.delay(webhook.id, event)

    return jsonify(order.to_dict()), 201

if __name__ == '__main__':
    app.run(debug=False, port=3000)
```
