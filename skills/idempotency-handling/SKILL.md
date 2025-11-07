---
name: idempotency-handling
description: Implement idempotency keys and handling to ensure operations can be safely retried without duplicate effects. Use when building payment systems, APIs with retries, or distributed transactions.
---

# Idempotency Handling

## Overview

Implement idempotency to ensure operations produce the same result regardless of how many times they're executed.

## When to Use

- Payment processing
- API endpoints with retries
- Webhooks and callbacks
- Message queue consumers
- Distributed transactions
- Bank transfers
- Order creation
- Email sending
- Resource creation

## Implementation Examples

### 1. **Express Idempotency Middleware**

```typescript
import express from 'express';
import Redis from 'ioredis';
import crypto from 'crypto';

interface IdempotentRequest {
  key: string;
  status: 'processing' | 'completed' | 'failed';
  response?: any;
  error?: string;
  createdAt: number;
  completedAt?: number;
}

class IdempotencyService {
  private redis: Redis;
  private ttl = 86400; // 24 hours

  constructor(redisUrl: string) {
    this.redis = new Redis(redisUrl);
  }

  async getRequest(key: string): Promise<IdempotentRequest | null> {
    const data = await this.redis.get(`idempotency:${key}`);
    return data ? JSON.parse(data) : null;
  }

  async setRequest(
    key: string,
    request: IdempotentRequest
  ): Promise<void> {
    await this.redis.setex(
      `idempotency:${key}`,
      this.ttl,
      JSON.stringify(request)
    );
  }

  async startProcessing(key: string): Promise<boolean> {
    const request: IdempotentRequest = {
      key,
      status: 'processing',
      createdAt: Date.now()
    };

    // Use SET NX to ensure only one request processes
    const result = await this.redis.set(
      `idempotency:${key}`,
      JSON.stringify(request),
      'EX',
      this.ttl,
      'NX'
    );

    return result === 'OK';
  }

  async completeRequest(
    key: string,
    response: any
  ): Promise<void> {
    const request: IdempotentRequest = {
      key,
      status: 'completed',
      response,
      createdAt: Date.now(),
      completedAt: Date.now()
    };

    await this.setRequest(key, request);
  }

  async failRequest(
    key: string,
    error: string
  ): Promise<void> {
    const request: IdempotentRequest = {
      key,
      status: 'failed',
      error,
      createdAt: Date.now(),
      completedAt: Date.now()
    };

    await this.setRequest(key, request);
  }
}

function idempotencyMiddleware(idempotency: IdempotencyService) {
  return async (
    req: express.Request,
    res: express.Response,
    next: express.NextFunction
  ) => {
    // Only apply to POST, PUT, PATCH, DELETE
    if (!['POST', 'PUT', 'PATCH', 'DELETE'].includes(req.method)) {
      return next();
    }

    const idempotencyKey = req.headers['idempotency-key'] as string;

    if (!idempotencyKey) {
      return res.status(400).json({
        error: 'Idempotency-Key header required'
      });
    }

    // Check for existing request
    const existing = await idempotency.getRequest(idempotencyKey);

    if (existing) {
      if (existing.status === 'processing') {
        return res.status(409).json({
          error: 'Request already processing',
          message: 'Please wait and retry'
        });
      }

      if (existing.status === 'completed') {
        return res.status(200).json(existing.response);
      }

      if (existing.status === 'failed') {
        return res.status(500).json({
          error: 'Previous request failed',
          message: existing.error
        });
      }
    }

    // Start processing
    const canProcess = await idempotency.startProcessing(idempotencyKey);

    if (!canProcess) {
      return res.status(409).json({
        error: 'Request already processing'
      });
    }

    // Capture response
    const originalSend = res.json.bind(res);
    res.json = (body: any) => {
      // Save response for future requests
      idempotency.completeRequest(idempotencyKey, body).catch(console.error);
      return originalSend(body);
    };

    // Handle errors
    const originalNext = next;
    next = (err?: any) => {
      if (err) {
        idempotency.failRequest(idempotencyKey, err.message).catch(console.error);
      }
      return originalNext(err);
    };

    next();
  };
}

// Usage
const app = express();
const redis = new Redis('redis://localhost:6379');
const idempotency = new IdempotencyService('redis://localhost:6379');

app.use(express.json());
app.use(idempotencyMiddleware(idempotency));

app.post('/api/payments', async (req, res) => {
  const { amount, userId } = req.body;

  // Process payment
  const payment = await processPayment(amount, userId);

  res.json(payment);
});

async function processPayment(amount: number, userId: string) {
  // Payment processing logic
  return {
    id: crypto.randomUUID(),
    amount,
    userId,
    status: 'completed'
  };
}

app.listen(3000);
```

### 2. **Database-Based Idempotency**

```typescript
import { Pool } from 'pg';

interface IdempotencyRecord {
  key: string;
  request_body: any;
  response_body?: any;
  status: string;
  error_message?: string;
  created_at: Date;
  completed_at?: Date;
}

class DatabaseIdempotency {
  constructor(private db: Pool) {
    this.createTable();
  }

  private async createTable(): Promise<void> {
    await this.db.query(`
      CREATE TABLE IF NOT EXISTS idempotency_keys (
        key VARCHAR(255) PRIMARY KEY,
        request_body JSONB NOT NULL,
        response_body JSONB,
        status VARCHAR(50) NOT NULL,
        error_message TEXT,
        created_at TIMESTAMP DEFAULT NOW(),
        completed_at TIMESTAMP,
        expires_at TIMESTAMP NOT NULL
      );

      CREATE INDEX IF NOT EXISTS idx_idempotency_expires
      ON idempotency_keys (expires_at);
    `);
  }

  async checkIdempotency(
    key: string,
    requestBody: any
  ): Promise<IdempotencyRecord | null> {
    const result = await this.db.query(
      'SELECT * FROM idempotency_keys WHERE key = $1',
      [key]
    );

    if (result.rows.length === 0) {
      return null;
    }

    const record = result.rows[0];

    // Check if request body matches
    if (JSON.stringify(record.request_body) !== JSON.stringify(requestBody)) {
      throw new Error('Request body mismatch for idempotency key');
    }

    return record;
  }

  async startProcessing(
    key: string,
    requestBody: any
  ): Promise<boolean> {
    try {
      const expiresAt = new Date(Date.now() + 86400 * 1000); // 24 hours

      await this.db.query(`
        INSERT INTO idempotency_keys (key, request_body, status, expires_at)
        VALUES ($1, $2, 'processing', $3)
      `, [key, requestBody, expiresAt]);

      return true;
    } catch (error: any) {
      if (error.code === '23505') { // Unique violation
        return false;
      }
      throw error;
    }
  }

  async completeRequest(
    key: string,
    responseBody: any
  ): Promise<void> {
    await this.db.query(`
      UPDATE idempotency_keys
      SET
        response_body = $1,
        status = 'completed',
        completed_at = NOW()
      WHERE key = $2
    `, [responseBody, key]);
  }

  async failRequest(
    key: string,
    errorMessage: string
  ): Promise<void> {
    await this.db.query(`
      UPDATE idempotency_keys
      SET
        error_message = $1,
        status = 'failed',
        completed_at = NOW()
      WHERE key = $2
    `, [errorMessage, key]);
  }

  async cleanup(): Promise<number> {
    const result = await this.db.query(`
      DELETE FROM idempotency_keys
      WHERE expires_at < NOW()
    `);

    return result.rowCount || 0;
  }
}
```

### 3. **Stripe-Style Idempotency**

```python
import hashlib
import json
from datetime import datetime, timedelta
from typing import Optional, Dict, Any
import psycopg2

class IdempotencyManager:
    def __init__(self, db_connection):
        self.db = db_connection
        self.ttl_days = 1

    def process_request(
        self,
        idempotency_key: str,
        request_data: Dict[str, Any],
        process_fn: callable
    ) -> Dict[str, Any]:
        """
        Process request with idempotency guarantee.

        Args:
            idempotency_key: Unique key for this request
            request_data: Request payload
            process_fn: Function to process the request

        Returns:
            Response data
        """
        # Check for existing request
        existing = self.get_existing_request(
            idempotency_key,
            request_data
        )

        if existing:
            if existing['status'] == 'processing':
                raise ConflictError('Request already processing')

            if existing['status'] == 'completed':
                return existing['response']

            if existing['status'] == 'failed':
                raise ProcessingError(existing['error'])

        # Start processing
        if not self.start_processing(idempotency_key, request_data):
            raise ConflictError('Request already processing')

        try:
            # Process request
            result = process_fn(request_data)

            # Store result
            self.complete_request(idempotency_key, result)

            return result

        except Exception as e:
            # Store error
            self.fail_request(idempotency_key, str(e))
            raise

    def get_existing_request(
        self,
        key: str,
        request_data: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """Get existing idempotent request."""
        cursor = self.db.cursor()

        cursor.execute("""
            SELECT status, response, error, request_hash
            FROM idempotency_requests
            WHERE idempotency_key = %s
            AND created_at > %s
        """, (key, datetime.now() - timedelta(days=self.ttl_days)))

        row = cursor.fetchone()
        cursor.close()

        if not row:
            return None

        # Verify request data matches
        request_hash = self.hash_request(request_data)
        if row[3] != request_hash:
            raise ValueError(
                'Request data does not match idempotency key'
            )

        return {
            'status': row[0],
            'response': row[1],
            'error': row[2]
        }

    def start_processing(
        self,
        key: str,
        request_data: Dict[str, Any]
    ) -> bool:
        """Mark request as processing."""
        cursor = self.db.cursor()
        request_hash = self.hash_request(request_data)

        try:
            cursor.execute("""
                INSERT INTO idempotency_requests
                (idempotency_key, request_hash, status, created_at)
                VALUES (%s, %s, 'processing', NOW())
            """, (key, request_hash))

            self.db.commit()
            cursor.close()
            return True

        except psycopg2.IntegrityError:
            self.db.rollback()
            cursor.close()
            return False

    def complete_request(
        self,
        key: str,
        response: Dict[str, Any]
    ):
        """Mark request as completed."""
        cursor = self.db.cursor()

        cursor.execute("""
            UPDATE idempotency_requests
            SET
                status = 'completed',
                response = %s,
                completed_at = NOW()
            WHERE idempotency_key = %s
        """, (json.dumps(response), key))

        self.db.commit()
        cursor.close()

    def fail_request(self, key: str, error: str):
        """Mark request as failed."""
        cursor = self.db.cursor()

        cursor.execute("""
            UPDATE idempotency_requests
            SET
                status = 'failed',
                error = %s,
                completed_at = NOW()
            WHERE idempotency_key = %s
        """, (error, key))

        self.db.commit()
        cursor.close()

    def hash_request(self, data: Dict[str, Any]) -> str:
        """Create hash of request data."""
        json_str = json.dumps(data, sort_keys=True)
        return hashlib.sha256(json_str.encode()).hexdigest()


class ConflictError(Exception):
    pass


class ProcessingError(Exception):
    pass


# Usage
def process_payment(data):
    # Process payment logic
    return {
        'payment_id': 'pay_123',
        'amount': data['amount'],
        'status': 'completed'
    }

# In your API handler
idempotency = IdempotencyManager(db_connection)

try:
    result = idempotency.process_request(
        idempotency_key='key_abc123',
        request_data={'amount': 100, 'currency': 'USD'},
        process_fn=process_payment
    )
    print(result)
except ConflictError as e:
    print(f"Conflict: {e}")
except ProcessingError as e:
    print(f"Processing error: {e}")
```

### 4. **Message Queue Idempotency**

```typescript
interface Message {
  id: string;
  data: any;
  timestamp: number;
}

class IdempotentMessageProcessor {
  private processedMessages = new Set<string>();
  private db: Pool;

  constructor(db: Pool) {
    this.db = db;
    this.loadProcessedMessages();
  }

  private async loadProcessedMessages(): Promise<void> {
    // Load recent processed message IDs
    const result = await this.db.query(`
      SELECT message_id
      FROM processed_messages
      WHERE processed_at > NOW() - INTERVAL '24 hours'
    `);

    result.rows.forEach(row => {
      this.processedMessages.add(row.message_id);
    });
  }

  async processMessage(message: Message): Promise<void> {
    // Check if already processed
    if (this.processedMessages.has(message.id)) {
      console.log(`Message ${message.id} already processed, skipping`);
      return;
    }

    // Mark as processing (atomic operation)
    const wasInserted = await this.markAsProcessing(message.id);

    if (!wasInserted) {
      console.log(`Message ${message.id} already being processed`);
      return;
    }

    try {
      // Process message
      await this.handleMessage(message);

      // Mark as completed
      await this.markAsCompleted(message.id);

      this.processedMessages.add(message.id);
    } catch (error) {
      console.error(`Failed to process message ${message.id}:`, error);
      await this.markAsFailed(message.id, (error as Error).message);
      throw error;
    }
  }

  private async markAsProcessing(messageId: string): Promise<boolean> {
    try {
      await this.db.query(`
        INSERT INTO processed_messages (message_id, status, processed_at)
        VALUES ($1, 'processing', NOW())
      `, [messageId]);

      return true;
    } catch (error: any) {
      if (error.code === '23505') {
        return false;
      }
      throw error;
    }
  }

  private async markAsCompleted(messageId: string): Promise<void> {
    await this.db.query(`
      UPDATE processed_messages
      SET status = 'completed', completed_at = NOW()
      WHERE message_id = $1
    `, [messageId]);
  }

  private async markAsFailed(
    messageId: string,
    error: string
  ): Promise<void> {
    await this.db.query(`
      UPDATE processed_messages
      SET status = 'failed', error = $2, completed_at = NOW()
      WHERE message_id = $1
    `, [messageId, error]);
  }

  private async handleMessage(message: Message): Promise<void> {
    // Actual message processing logic
    console.log('Processing message:', message);
  }
}
```

## Best Practices

### ✅ DO
- Require idempotency keys for mutations
- Store request and response together
- Set appropriate TTL for idempotency records
- Validate request body matches stored request
- Handle concurrent requests gracefully
- Return same response for duplicate requests
- Clean up old idempotency records
- Use database constraints for atomicity

### ❌ DON'T
- Apply idempotency to GET requests
- Store idempotency data forever
- Skip validation of request body
- Use non-unique idempotency keys
- Process same request concurrently
- Change response for duplicate requests

## Schema Design

```sql
CREATE TABLE idempotency_keys (
  key VARCHAR(255) PRIMARY KEY,
  request_hash VARCHAR(64) NOT NULL,
  request_body JSONB NOT NULL,
  response_body JSONB,
  status VARCHAR(20) NOT NULL CHECK (status IN ('processing', 'completed', 'failed')),
  error_message TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  completed_at TIMESTAMP,
  expires_at TIMESTAMP NOT NULL
);

CREATE INDEX idx_idempotency_expires ON idempotency_keys (expires_at);
CREATE INDEX idx_idempotency_status ON idempotency_keys (status);
```

## Resources

- [Stripe Idempotency](https://stripe.com/docs/api/idempotent_requests)
- [RFC 7807 - Problem Details](https://tools.ietf.org/html/rfc7807)
