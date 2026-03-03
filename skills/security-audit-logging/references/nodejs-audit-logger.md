# Node.js Audit Logger

## Node.js Audit Logger

```javascript
// audit-logger.js
const winston = require("winston");
const { ElasticsearchTransport } = require("winston-elasticsearch");

class AuditLogger {
  constructor() {
    this.logger = winston.createLogger({
      level: "info",
      format: winston.format.combine(
        winston.format.timestamp(),
        winston.format.json(),
      ),
      transports: [
        // File transport
        new winston.transports.File({
          filename: "logs/audit.log",
          maxsize: 10485760, // 10MB
          maxFiles: 30,
          tailable: true,
        }),

        // Elasticsearch transport for SIEM
        new ElasticsearchTransport({
          level: "info",
          clientOpts: {
            node: process.env.ELASTICSEARCH_URL,
          },
          index: "security-audit",
        }),
      ],
    });
  }

  /**
   * Log authentication event
   */
  logAuth(userId, action, success, metadata = {}) {
    this.logger.info({
      category: "authentication",
      userId,
      action, // login, logout, password_change
      success,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      userAgent: metadata.userAgent,
      location: metadata.location,
      mfaUsed: metadata.mfaUsed,
    });
  }

  /**
   * Log authorization event
   */
  logAuthorization(userId, resource, action, granted, metadata = {}) {
    this.logger.info({
      category: "authorization",
      userId,
      resource,
      action,
      granted,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      reason: metadata.reason,
    });
  }

  /**
   * Log data access
   */
  logDataAccess(userId, dataType, recordId, action, metadata = {}) {
    this.logger.info({
      category: "data_access",
      userId,
      dataType, // user, payment, health_record
      recordId,
      action, // read, create, update, delete
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      query: metadata.query,
      resultCount: metadata.resultCount,
    });
  }

  /**
   * Log configuration change
   */
  logConfigChange(userId, setting, oldValue, newValue, metadata = {}) {
    this.logger.info({
      category: "configuration_change",
      userId,
      setting,
      oldValue,
      newValue,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
    });
  }

  /**
   * Log security event
   */
  logSecurityEvent(eventType, severity, description, metadata = {}) {
    this.logger.warn({
      category: "security_event",
      eventType, // brute_force, suspicious_activity, data_breach
      severity, // low, medium, high, critical
      description,
      timestamp: new Date().toISOString(),
      ...metadata,
    });
  }

  /**
   * Log admin action
   */
  logAdminAction(adminId, action, targetUserId, metadata = {}) {
    this.logger.info({
      category: "admin_action",
      adminId,
      action, // user_delete, role_change, system_config
      targetUserId,
      timestamp: new Date().toISOString(),
      changes: metadata.changes,
      reason: metadata.reason,
    });
  }

  /**
   * Log API request
   */
  logAPIRequest(userId, method, endpoint, statusCode, duration, metadata = {}) {
    this.logger.info({
      category: "api_request",
      userId,
      method,
      endpoint,
      statusCode,
      duration,
      timestamp: new Date().toISOString(),
      ip: metadata.ip,
      userAgent: metadata.userAgent,
      requestId: metadata.requestId,
    });
  }
}

// Express middleware
function auditMiddleware(auditLogger) {
  return (req, res, next) => {
    const startTime = Date.now();

    // Capture response
    const originalSend = res.send;
    res.send = function (data) {
      res.send = originalSend;

      const duration = Date.now() - startTime;

      // Log API request
      auditLogger.logAPIRequest(
        req.user?.id || "anonymous",
        req.method,
        req.path,
        res.statusCode,
        duration,
        {
          ip: req.ip,
          userAgent: req.get("user-agent"),
          requestId: req.id,
        },
      );

      return res.send(data);
    };

    next();
  };
}

// Usage
const auditLogger = new AuditLogger();

// Login event
app.post("/api/login", async (req, res) => {
  const { email, password } = req.body;

  try {
    const user = await authenticateUser(email, password);

    auditLogger.logAuth(user.id, "login", true, {
      ip: req.ip,
      userAgent: req.get("user-agent"),
      mfaUsed: user.mfaEnabled,
    });

    res.json({ token: generateToken(user) });
  } catch (error) {
    auditLogger.logAuth(email, "login", false, {
      ip: req.ip,
      userAgent: req.get("user-agent"),
    });

    res.status(401).json({ error: "Invalid credentials" });
  }
});

// Data access event
app.get("/api/users/:id", authorize, async (req, res) => {
  const userId = req.params.id;

  // Check authorization
  if (req.user.id !== userId && !req.user.isAdmin) {
    auditLogger.logAuthorization(req.user.id, `user:${userId}`, "read", false, {
      ip: req.ip,
      reason: "Insufficient permissions",
    });

    return res.status(403).json({ error: "Forbidden" });
  }

  const user = await getUser(userId);

  auditLogger.logDataAccess(req.user.id, "user", userId, "read", {
    ip: req.ip,
  });

  res.json(user);
});

module.exports = { AuditLogger, auditMiddleware };
```
