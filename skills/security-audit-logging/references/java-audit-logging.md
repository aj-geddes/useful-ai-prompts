# Java Audit Logging

## Java Audit Logging

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
