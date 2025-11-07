---
name: security-audit-logging
description: Implement comprehensive security audit logging for compliance, forensics, and SIEM integration. Use when building audit trails, compliance logging, or security monitoring systems.
---

# Security Audit Logging

## Overview

Implement comprehensive audit logging for security events, user actions, and system changes with structured logging, retention policies, and SIEM integration.

## When to Use

- Compliance requirements (SOC 2, HIPAA, PCI-DSS)
- Security monitoring
- Forensic investigations
- User activity tracking
- System change auditing
- Breach detection

## Implementation Examples

### 1. **Node.js Audit Logger**

```javascript
// audit-logger.js
const winston = require('winston');
const { ElasticsearchTransport } = require('winston-elasticsearch');

class AuditLogger {
  constructor() {
    this.logger = winston.createLogger({
      level: 'info',
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json()
      ),
      transports: [
        // File transport
        new winston.transports.File({
          filename: 'logs/audit.log',
          maxsize: 10485760, // 10MB
          maxFiles: 30,
          tailable: true
        }),

        // Elasticsearch transport for SIEM
        new ElasticsearchTransport({
          level: 'info',
          clientOpts: {
            node: process.env.ELASTICSEARCH_URL
          },
          index: 'security-audit'
        })
      ]
    });
  }

  /**
   * Log authentication event
   */
  logAuth(userId, action, success, metadata = {}) {
    this.logger.info({
      category: 'authentication',
      userId,
      action, // login, logout, password_change
      success,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      userAgent: metadata.userAgent,
      location: metadata.location,
      mfaUsed: metadata.mfaUsed
    });
  }

  /**
   * Log authorization event
   */
  logAuthorization(userId, resource, action, granted, metadata = {}) {
    this.logger.info({
      category: 'authorization',
      userId,
      resource,
      action,
      granted,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      reason: metadata.reason
    });
  }

  /**
   * Log data access
   */
  logDataAccess(userId, dataType, recordId, action, metadata = {}) {
    this.logger.info({
      category: 'data_access',
      userId,
      dataType, // user, payment, health_record
      recordId,
      action, // read, create, update, delete
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      query: metadata.query,
      resultCount: metadata.resultCount
    });
  }

  /**
   * Log configuration change
   */
  logConfigChange(userId, setting, oldValue, newValue, metadata = {}) {
    this.logger.info({
      category: 'configuration_change',
      userId,
      setting,
      oldValue,
      newValue,
      timestamp: new Date().toISOString(),
      ip: metadata.ip
    });
  }

  /**
   * Log security event
   */
  logSecurityEvent(eventType, severity, description, metadata = {}) {
    this.logger.warn({
      category: 'security_event',
      eventType, // brute_force, suspicious_activity, data_breach
      severity, // low, medium, high, critical
      description,
      timestamp: new Date().toISOString(),
      ...metadata
    });
  }

  /**
   * Log admin action
   */
  logAdminAction(adminId, action, targetUserId, metadata = {}) {
    this.logger.info({
      category: 'admin_action',
      adminId,
      action, // user_delete, role_change, system_config
      targetUserId,
      timestamp: new Date().toISOString(),
      changes: metadata.changes,
      reason: metadata.reason
    });
  }

  /**
   * Log API request
   */
  logAPIRequest(userId, method, endpoint, statusCode, duration, metadata = {}) {
    this.logger.info({
      category: 'api_request',
      userId,
      method,
      endpoint,
      statusCode,
      duration,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      userAgent: metadata.userAgent,
      requestId: metadata.requestId
    });
  }
}

// Express middleware
function auditMiddleware(auditLogger) {
  return (req, res, next) => {
    const startTime = Date.now();

    // Capture response
    const originalSend = res.send;
    res.send = function(data) {
      res.send = originalSend;

      const duration = Date.now() - startTime;

      // Log API request
      auditLogger.logAPIRequest(
        req.user?.id || 'anonymous',
        req.method,
        req.path,
        res.statusCode,
        duration,
        {
          ip: req.ip,
          userAgent: req.get('user-agent'),
          requestId: req.id
        }
      );

      return res.send(data);
    };

    next();
  };
}

// Usage
const auditLogger = new AuditLogger();

// Login event
app.post('/api/login', async (req, res) => {
  const { email, password } = req.body;

  try {
    const user = await authenticateUser(email, password);

    auditLogger.logAuth(
      user.id,
      'login',
      true,
      {
        ip: req.ip,
        userAgent: req.get('user-agent'),
        mfaUsed: user.mfaEnabled
      }
    );

    res.json({ token: generateToken(user) });
  } catch (error) {
    auditLogger.logAuth(
      email,
      'login',
      false,
      {
        ip: req.ip,
        userAgent: req.get('user-agent')
      }
    );

    res.status(401).json({ error: 'Invalid credentials' });
  }
});

// Data access event
app.get('/api/users/:id', authorize, async (req, res) => {
  const userId = req.params.id;

  // Check authorization
  if (req.user.id !== userId && !req.user.isAdmin) {
    auditLogger.logAuthorization(
      req.user.id,
      `user:${userId}`,
      'read',
      false,
      {
        ip: req.ip,
        reason: 'Insufficient permissions'
      }
    );

    return res.status(403).json({ error: 'Forbidden' });
  }

  const user = await getUser(userId);

  auditLogger.logDataAccess(
    req.user.id,
    'user',
    userId,
    'read',
    {
      ip: req.ip
    }
  );

  res.json(user);
});

module.exports = { AuditLogger, auditMiddleware };
```

### 2. **Python Audit Logging System**

```python
# audit_logging.py
import logging
import json
from datetime import datetime
from typing import Dict, Any, Optional
import structlog
from elasticsearch import Elasticsearch

class AuditLogger:
    def __init__(self):
        # Configure structured logging
        structlog.configure(
            processors=[
                structlog.processors.TimeStamper(fmt="iso"),
                structlog.processors.JSONRenderer()
            ]
        )

        self.logger = structlog.get_logger()

        # File handler
        file_handler = logging.FileHandler('logs/audit.log')
        file_handler.setLevel(logging.INFO)

        # Elasticsearch for SIEM
        self.es = Elasticsearch([{'host': 'localhost', 'port': 9200}])

    def _log(self, category: str, event_data: Dict[str, Any]):
        """Internal logging method"""
        log_entry = {
            'category': category,
            'timestamp': datetime.utcnow().isoformat(),
            **event_data
        }

        # Log to file
        self.logger.info(json.dumps(log_entry))

        # Send to Elasticsearch
        try:
            self.es.index(
                index='security-audit',
                document=log_entry
            )
        except Exception as e:
            print(f"Failed to send to Elasticsearch: {e}")

    def log_auth(self, user_id: str, action: str, success: bool,
                  ip: str = None, user_agent: str = None, **kwargs):
        """Log authentication event"""
        self._log('authentication', {
            'user_id': user_id,
            'action': action,
            'success': success,
            'ip': ip,
            'user_agent': user_agent,
            **kwargs
        })

    def log_authorization(self, user_id: str, resource: str, action: str,
                         granted: bool, reason: str = None, **kwargs):
        """Log authorization decision"""
        self._log('authorization', {
            'user_id': user_id,
            'resource': resource,
            'action': action,
            'granted': granted,
            'reason': reason,
            **kwargs
        })

    def log_data_access(self, user_id: str, data_type: str, record_id: str,
                       action: str, **kwargs):
        """Log data access event"""
        self._log('data_access', {
            'user_id': user_id,
            'data_type': data_type,
            'record_id': record_id,
            'action': action,
            **kwargs
        })

    def log_security_event(self, event_type: str, severity: str,
                          description: str, **kwargs):
        """Log security event"""
        self._log('security_event', {
            'event_type': event_type,
            'severity': severity,
            'description': description,
            **kwargs
        })

    def log_config_change(self, user_id: str, setting: str,
                         old_value: Any, new_value: Any, **kwargs):
        """Log configuration change"""
        self._log('configuration_change', {
            'user_id': user_id,
            'setting': setting,
            'old_value': str(old_value),
            'new_value': str(new_value),
            **kwargs
        })

# Flask integration
from flask import Flask, request, g
from functools import wraps

app = Flask(__name__)
audit_logger = AuditLogger()

@app.before_request
def before_request():
    g.request_start_time = datetime.now()

@app.after_request
def after_request(response):
    if hasattr(g, 'request_start_time'):
        duration = (datetime.now() - g.request_start_time).total_seconds() * 1000

        audit_logger._log('api_request', {
            'user_id': getattr(g, 'user_id', 'anonymous'),
            'method': request.method,
            'endpoint': request.path,
            'status_code': response.status_code,
            'duration_ms': duration,
            'ip': request.remote_addr,
            'user_agent': request.user_agent.string
        })

    return response

def audit_data_access(data_type: str):
    """Decorator for data access logging"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            result = f(*args, **kwargs)

            audit_logger.log_data_access(
                user_id=g.user_id,
                data_type=data_type,
                record_id=kwargs.get('id', 'unknown'),
                action=request.method.lower(),
                ip=request.remote_addr
            )

            return result

        return decorated_function
    return decorator

@app.route('/api/users/<user_id>', methods=['GET'])
@audit_data_access('user')
def get_user(user_id):
    # Fetch user
    return jsonify({'id': user_id})

if __name__ == '__main__':
    app.run()
```

### 3. **Java Audit Logging**

```java
// AuditLogger.java
package com.example.security;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.time.Instant;
import java.util.HashMap;
import java.util.Map;

public class AuditLogger {
    private static final Logger logger = LoggerFactory.getLogger("AUDIT");
    private static final ObjectMapper objectMapper = new ObjectMapper();

    public enum Category {
        AUTHENTICATION,
        AUTHORIZATION,
        DATA_ACCESS,
        CONFIGURATION_CHANGE,
        SECURITY_EVENT,
        ADMIN_ACTION
    }

    public enum Severity {
        LOW, MEDIUM, HIGH, CRITICAL
    }

    public void logAuth(String userId, String action, boolean success,
                       String ip, Map<String, Object> metadata) {
        Map<String, Object> logEntry = new HashMap<>();
        logEntry.put("category", Category.AUTHENTICATION);
        logEntry.put("userId", userId);
        logEntry.put("action", action);
        logEntry.put("success", success);
        logEntry.put("ip", ip);
        logEntry.put("timestamp", Instant.now().toString());
        logEntry.putAll(metadata);

        log(logEntry);
    }

    public void logDataAccess(String userId, String dataType, String recordId,
                             String action, String ip) {
        Map<String, Object> logEntry = new HashMap<>();
        logEntry.put("category", Category.DATA_ACCESS);
        logEntry.put("userId", userId);
        logEntry.put("dataType", dataType);
        logEntry.put("recordId", recordId);
        logEntry.put("action", action);
        logEntry.put("ip", ip);
        logEntry.put("timestamp", Instant.now().toString());

        log(logEntry);
    }

    public void logSecurityEvent(String eventType, Severity severity,
                                String description, Map<String, Object> metadata) {
        Map<String, Object> logEntry = new HashMap<>();
        logEntry.put("category", Category.SECURITY_EVENT);
        logEntry.put("eventType", eventType);
        logEntry.put("severity", severity);
        logEntry.put("description", description);
        logEntry.put("timestamp", Instant.now().toString());
        logEntry.putAll(metadata);

        log(logEntry);
    }

    private void log(Map<String, Object> logEntry) {
        try {
            String json = objectMapper.writeValueAsString(logEntry);
            logger.info(json);

            // Send to SIEM/Elasticsearch
            // siemClient.send(logEntry);
        } catch (Exception e) {
            logger.error("Failed to log audit event", e);
        }
    }
}

// Spring Boot Filter
@Component
public class AuditFilter extends OncePerRequestFilter {

    @Autowired
    private AuditLogger auditLogger;

    @Override
    protected void doFilterInternal(HttpServletRequest request,
                                   HttpServletResponse response,
                                   FilterChain filterChain)
            throws ServletException, IOException {

        long startTime = System.currentTimeMillis();

        filterChain.doFilter(request, response);

        long duration = System.currentTimeMillis() - startTime;

        String userId = SecurityContextHolder.getContext()
            .getAuthentication()
            .getName();

        Map<String, Object> metadata = new HashMap<>();
        metadata.put("method", request.getMethod());
        metadata.put("endpoint", request.getRequestURI());
        metadata.put("statusCode", response.getStatus());
        metadata.put("duration", duration);
        metadata.put("userAgent", request.getHeader("User-Agent"));

        auditLogger.logAuth(userId, "api_request", true,
                           request.getRemoteAddr(), metadata);
    }
}
```

## Best Practices

### ✅ DO
- Log all security events
- Use structured logging
- Include timestamps (UTC)
- Log user context
- Implement log retention
- Encrypt sensitive logs
- Monitor log integrity
- Send to SIEM
- Include request IDs

### ❌ DON'T
- Log passwords/secrets
- Log sensitive PII unnecessarily
- Skip failed attempts
- Allow log tampering
- Store logs insecurely
- Ignore log analysis

## Events to Log

- **Authentication**: Login, logout, password changes
- **Authorization**: Access granted/denied
- **Data Access**: CRUD operations
- **Configuration**: System changes
- **Security Events**: Suspicious activity
- **Admin Actions**: Privileged operations

## Log Retention

- **SOC 2**: 1 year minimum
- **HIPAA**: 6 years
- **PCI-DSS**: 1 year online, 3 years archive
- **GDPR**: As needed for purpose

## Resources

- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [NIST Audit Logging Guide](https://csrc.nist.gov/publications/detail/sp/800-92/final)
- [Elastic Stack](https://www.elastic.co/elastic-stack)
