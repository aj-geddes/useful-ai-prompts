---
name: application-logging
description: Implement structured logging across applications with log aggregation and centralized analysis. Use when setting up application logging, implementing ELK stack, or analyzing application behavior.
---

# Application Logging

## Overview

Implement comprehensive structured logging with proper levels, context, and centralized aggregation for effective debugging and monitoring.

## When to Use

- Application debugging
- Audit trail creation
- Performance analysis
- Compliance requirements
- Centralized log aggregation

## Instructions

### 1. **Node.js Structured Logging with Winston**

```javascript
// logger.js
const winston = require('winston');

const logFormat = winston.format.combine(
  winston.format.timestamp({ format: 'YYYY-MM-DD HH:mm:ss' }),
  winston.format.errors({ stack: true }),
  winston.format.json()
);

const logger = winston.createLogger({
  level: process.env.LOG_LEVEL || 'info',
  format: logFormat,
  defaultMeta: {
    service: 'api-service',
    environment: process.env.NODE_ENV || 'development'
  },
  transports: [
    new winston.transports.Console({
      format: winston.format.combine(
        winston.format.colorize(),
        winston.format.simple()
      )
    }),
    new winston.transports.File({
      filename: 'logs/error.log',
      level: 'error'
    }),
    new winston.transports.File({
      filename: 'logs/combined.log'
    })
  ]
});

module.exports = logger;
```

### 2. **Express HTTP Request Logging**

```javascript
// Express middleware
const express = require('express');
const expressWinston = require('express-winston');
const logger = require('./logger');

const app = express();

app.use(expressWinston.logger({
  transports: [
    new winston.transports.Console(),
    new winston.transports.File({ filename: 'logs/http.log' })
  ],
  format: winston.format.combine(
    winston.format.timestamp(),
    winston.format.json()
  ),
  meta: true,
  msg: 'HTTP {{req.method}} {{req.url}}',
  expressFormat: true
}));

app.get('/api/users/:id', (req, res) => {
  const requestId = req.headers['x-request-id'] || Math.random().toString();

  logger.info('User request started', { requestId, userId: req.params.id });

  try {
    const user = { id: req.params.id, name: 'John Doe' };
    logger.debug('User data retrieved', { requestId, user });
    res.json(user);
  } catch (error) {
    logger.error('User retrieval failed', {
      requestId,
      error: error.message,
      stack: error.stack
    });
    res.status(500).json({ error: 'Internal server error' });
  }
});
```

### 3. **Python Structured Logging**

```python
# logger_config.py
import logging
import json
from pythonjsonlogger import jsonlogger
import sys

class CustomJsonFormatter(jsonlogger.JsonFormatter):
    def add_fields(self, log_record, record, message_dict):
        super().add_fields(log_record, record, message_dict)
        log_record['timestamp'] = self.formatTime(record)
        log_record['service'] = 'api-service'
        log_record['level'] = record.levelname

def setup_logging():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler(sys.stdout)
    formatter = CustomJsonFormatter()
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger

logger = setup_logging()
```

### 4. **Flask Integration**

```python
# Flask app
from flask import Flask, request, g
import uuid
import time

app = Flask(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()
    g.request_id = request.headers.get('X-Request-ID', str(uuid.uuid4()))

@app.after_request
def after_request(response):
    duration = time.time() - g.start_time
    logger.info('HTTP Request', extra={
        'method': request.method,
        'path': request.path,
        'status_code': response.status_code,
        'duration_ms': duration * 1000,
        'request_id': g.request_id
    })
    return response

@app.route('/api/orders/<order_id>')
def get_order(order_id):
    logger.info('Order request', extra={
        'order_id': order_id,
        'request_id': g.request_id
    })

    try:
        order = db.query(f'SELECT * FROM orders WHERE id = {order_id}')
        logger.debug('Order retrieved', extra={'order_id': order_id})
        return {'order': order}
    except Exception as e:
        logger.error('Order retrieval failed', extra={
            'order_id': order_id,
            'error': str(e),
            'request_id': g.request_id
        }, exc_info=True)
        return {'error': 'Internal server error'}, 500
```

### 5. **ELK Stack Setup**

```yaml
# docker-compose.yml
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.0.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms512m -Xmx512m"
    ports:
      - "9200:9200"
    volumes:
      - elasticsearch_data:/usr/share/elasticsearch/data

  logstash:
    image: docker.elastic.co/logstash/logstash:8.0.0
    ports:
      - "5000:5000"
    volumes:
      - ./logstash.conf:/usr/share/logstash/pipeline/logstash.conf
    depends_on:
      - elasticsearch

  kibana:
    image: docker.elastic.co/kibana/kibana:8.0.0
    ports:
      - "5601:5601"
    environment:
      ELASTICSEARCH_HOSTS: http://elasticsearch:9200
    depends_on:
      - elasticsearch

volumes:
  elasticsearch_data:
```

### 6. **Logstash Configuration**

```conf
# logstash.conf
input {
  tcp {
    port => 5000
    codec => json
  }
}

filter {
  date {
    match => [ "timestamp", "YYYY-MM-dd HH:mm:ss" ]
    target => "@timestamp"
  }

  mutate {
    add_field => { "[@metadata][index_name]" => "logs-%{+YYYY.MM.dd}" }
  }
}

output {
  elasticsearch {
    hosts => ["elasticsearch:9200"]
    index => "%{[@metadata][index_name]}"
  }
}
```

## Best Practices

### ✅ DO
- Use structured JSON logging
- Include request IDs for tracing
- Log at appropriate levels
- Add context to error logs
- Implement log rotation
- Use timestamps consistently
- Aggregate logs centrally
- Filter sensitive data

### ❌ DON'T
- Log passwords or secrets
- Log at INFO for every operation
- Use unstructured messages
- Ignore log storage limits
- Skip context information
- Log to stdout in production
- Create unbounded log files

## Log Levels

- **ERROR**: Application error requiring immediate attention
- **WARN**: Potential issues requiring investigation
- **INFO**: Significant application events
- **DEBUG**: Detailed diagnostic information
