# Message Queue Integration

## Message Queue Integration

```python
# tests/integration/test_message_queue.py
import pytest
from unittest.mock import patch
import json

from app.queue import MessageQueue
from app.workers import OrderProcessor

@pytest.mark.integration
class TestMessageQueueIntegration:
    @pytest.fixture
    async def queue(self):
        """Create test message queue."""
        queue = MessageQueue(url=TEST_RABBITMQ_URL)
        await queue.connect()
        yield queue
        await queue.close()

    async def test_publish_and_consume_message(self, queue):
        """Test full message lifecycle."""
        received_messages = []

        async def message_handler(message):
            received_messages.append(message)

        # Subscribe to queue
        await queue.subscribe('orders', message_handler)

        # Publish message
        order_data = {
            'order_id': '123',
            'customer': 'test@example.com',
            'total': 99.99
        }
        await queue.publish('orders', order_data)

        # Wait for message processing
        await asyncio.sleep(0.5)

        assert len(received_messages) == 1
        assert received_messages[0]['order_id'] == '123'

    async def test_order_processing_workflow(self, queue, db):
        """Test complete order processing through queue."""
        processor = OrderProcessor(queue, db)
        await processor.start()

        # Publish order
        order = await create_test_order(db, status='pending')
        await queue.publish('orders.new', {'order_id': order.id})

        # Wait for processing
        await asyncio.sleep(1)

        # Verify order was processed
        await db.refresh(order)
        assert order.status == 'processing'
        assert order.processed_at is not None
```
