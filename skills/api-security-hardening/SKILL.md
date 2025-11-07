---
name: api-security-hardening
description: Secure REST APIs with authentication, rate limiting, CORS, input validation, and security middleware. Use when building or hardening API endpoints against common attacks.
---

# API Security Hardening

## Overview

Implement comprehensive API security measures including authentication, authorization, rate limiting, input validation, and attack prevention to protect against common vulnerabilities.

## When to Use

- New API development
- Security audit remediation
- Production API hardening
- Compliance requirements
- High-traffic API protection
- Public API exposure

## Implementation Examples

### 1. **Node.js/Express API Security**

```javascript
// secure-api.js - Comprehensive API security
const express = require('express');
const helmet = require('helmet');
const rateLimit = require('express-rate-limit');
const mongoSanitize = require('express-mongo-sanitize');
const xss = require('xss-clean');
const hpp = require('hpp');
const cors = require('cors');
const jwt = require('jsonwebtoken');
const validator = require('validator');

class SecureAPIServer {
  constructor() {
    this.app = express();
    this.setupSecurityMiddleware();
    this.setupRoutes();
  }

  setupSecurityMiddleware() {
    // 1. Helmet - Set security headers
    this.app.use(helmet({
      contentSecurityPolicy: {
        directives: {
          defaultSrc: ["'self'"],
          styleSrc: ["'self'", "'unsafe-inline'"],
          scriptSrc: ["'self'"],
          imgSrc: ["'self'", "data:", "https:"]
        }
      },
      hsts: {
        maxAge: 31536000,
        includeSubDomains: true,
        preload: true
      }
    }));

    // 2. CORS configuration
    const corsOptions = {
      origin: (origin, callback) => {
        const whitelist = [
          'https://example.com',
          'https://app.example.com'
        ];

        if (!origin || whitelist.includes(origin)) {
          callback(null, true);
        } else {
          callback(new Error('Not allowed by CORS'));
        }
      },
      credentials: true,
      optionsSuccessStatus: 200,
      methods: ['GET', 'POST', 'PUT', 'DELETE'],
      allowedHeaders: ['Content-Type', 'Authorization']
    };

    this.app.use(cors(corsOptions));

    // 3. Rate limiting
    const generalLimiter = rateLimit({
      windowMs: 15 * 60 * 1000, // 15 minutes
      max: 100, // limit each IP to 100 requests per windowMs
      message: 'Too many requests from this IP',
      standardHeaders: true,
      legacyHeaders: false,
      handler: (req, res) => {
        res.status(429).json({
          error: 'rate_limit_exceeded',
          message: 'Too many requests, please try again later',
          retryAfter: req.rateLimit.resetTime
        });
      }
    });

    const authLimiter = rateLimit({
      windowMs: 15 * 60 * 1000,
      max: 5, // Stricter limit for auth endpoints
      skipSuccessfulRequests: true
    });

    this.app.use('/api/', generalLimiter);
    this.app.use('/api/auth/', authLimiter);

    // 4. Body parsing with size limits
    this.app.use(express.json({ limit: '10kb' }));
    this.app.use(express.urlencoded({ extended: true, limit: '10kb' }));

    // 5. NoSQL injection prevention
    this.app.use(mongoSanitize());

    // 6. XSS protection
    this.app.use(xss());

    // 7. HTTP Parameter Pollution prevention
    this.app.use(hpp());

    // 8. Request ID for tracking
    this.app.use((req, res, next) => {
      req.id = require('crypto').randomUUID();
      res.setHeader('X-Request-ID', req.id);
      next();
    });

    // 9. Security logging
    this.app.use(this.securityLogger());
  }

  securityLogger() {
    return (req, res, next) => {
      const startTime = Date.now();

      res.on('finish', () => {
        const duration = Date.now() - startTime;

        const logEntry = {
          timestamp: new Date().toISOString(),
          requestId: req.id,
          method: req.method,
          path: req.path,
          statusCode: res.statusCode,
          duration,
          ip: req.ip,
          userAgent: req.get('user-agent')
        };

        // Log suspicious activity
        if (res.statusCode === 401 || res.statusCode === 403) {
          console.warn('Security event:', logEntry);
        }

        if (res.statusCode >= 500) {
          console.error('Server error:', logEntry);
        }
      });

      next();
    };
  }

  // JWT authentication middleware
  authenticateJWT() {
    return (req, res, next) => {
      const authHeader = req.headers.authorization;

      if (!authHeader || !authHeader.startsWith('Bearer ')) {
        return res.status(401).json({
          error: 'unauthorized',
          message: 'Missing or invalid authorization header'
        });
      }

      const token = authHeader.substring(7);

      try {
        const decoded = jwt.verify(token, process.env.JWT_SECRET, {
          algorithms: ['HS256'],
          issuer: 'api.example.com',
          audience: 'api.example.com'
        });

        req.user = decoded;
        next();
      } catch (error) {
        if (error.name === 'TokenExpiredError') {
          return res.status(401).json({
            error: 'token_expired',
            message: 'Token has expired'
          });
        }

        return res.status(401).json({
          error: 'invalid_token',
          message: 'Invalid token'
        });
      }
    };
  }

  // Input validation middleware
  validateInput(schema) {
    return (req, res, next) => {
      const errors = [];

      // Validate request body
      if (schema.body) {
        for (const [field, rules] of Object.entries(schema.body)) {
          const value = req.body[field];

          if (rules.required && !value) {
            errors.push(`${field} is required`);
            continue;
          }

          if (value) {
            // Type validation
            if (rules.type === 'email' && !validator.isEmail(value)) {
              errors.push(`${field} must be a valid email`);
            }

            if (rules.type === 'uuid' && !validator.isUUID(value)) {
              errors.push(`${field} must be a valid UUID`);
            }

            if (rules.type === 'url' && !validator.isURL(value)) {
              errors.push(`${field} must be a valid URL`);
            }

            // Length validation
            if (rules.minLength && value.length < rules.minLength) {
              errors.push(`${field} must be at least ${rules.minLength} characters`);
            }

            if (rules.maxLength && value.length > rules.maxLength) {
              errors.push(`${field} must be at most ${rules.maxLength} characters`);
            }

            // Pattern validation
            if (rules.pattern && !rules.pattern.test(value)) {
              errors.push(`${field} format is invalid`);
            }
          }
        }
      }

      if (errors.length > 0) {
        return res.status(400).json({
          error: 'validation_error',
          message: 'Input validation failed',
          details: errors
        });
      }

      next();
    };
  }

  // Authorization middleware
  authorize(...roles) {
    return (req, res, next) => {
      if (!req.user) {
        return res.status(401).json({
          error: 'unauthorized',
          message: 'Authentication required'
        });
      }

      if (roles.length > 0 && !roles.includes(req.user.role)) {
        return res.status(403).json({
          error: 'forbidden',
          message: 'Insufficient permissions'
        });
      }

      next();
    };
  }

  setupRoutes() {
    // Public endpoint
    this.app.get('/api/health', (req, res) => {
      res.json({ status: 'healthy' });
    });

    // Protected endpoint with validation
    this.app.post('/api/users',
      this.authenticateJWT(),
      this.authorize('admin'),
      this.validateInput({
        body: {
          email: { required: true, type: 'email' },
          name: { required: true, minLength: 2, maxLength: 100 },
          password: { required: true, minLength: 8 }
        }
      }),
      async (req, res) => {
        try {
          // Sanitized and validated input
          const { email, name, password } = req.body;

          // Process request
          res.status(201).json({
            message: 'User created successfully',
            userId: '123'
          });
        } catch (error) {
          res.status(500).json({
            error: 'internal_error',
            message: 'An error occurred'
          });
        }
      }
    );

    // Error handling middleware
    this.app.use((err, req, res, next) => {
      console.error('Unhandled error:', err);

      res.status(500).json({
        error: 'internal_error',
        message: 'An unexpected error occurred',
        requestId: req.id
      });
    });
  }

  start(port = 3000) {
    this.app.listen(port, () => {
      console.log(`Secure API server running on port ${port}`);
    });
  }
}

// Usage
const server = new SecureAPIServer();
server.start(3000);
```

### 2. **Python FastAPI Security**

```python
# secure_api.py
from fastapi import FastAPI, HTTPException, Depends, Security, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from pydantic import BaseModel, EmailStr, validator, Field
import jwt
from datetime import datetime, timedelta
import re
from typing import Optional, List
import secrets

app = FastAPI()
security = HTTPBearer()
limiter = Limiter(key_func=get_remote_address)

# Rate limiting
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://example.com",
        "https://app.example.com"
    ],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Content-Type", "Authorization"],
    max_age=3600
)

# Trusted hosts
app.add_middleware(
    TrustedHostMiddleware,
    allowed_hosts=["example.com", "*.example.com"]
)

# Security headers middleware
@app.middleware("http")
async def add_security_headers(request, call_next):
    response = await call_next(request)

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "strict-origin-when-cross-origin"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"

    return response

# Input validation models
class CreateUserRequest(BaseModel):
    email: EmailStr
    name: str = Field(..., min_length=2, max_length=100)
    password: str = Field(..., min_length=8)

    @validator('password')
    def validate_password(cls, v):
        if not re.search(r'[A-Z]', v):
            raise ValueError('Password must contain uppercase letter')
        if not re.search(r'[a-z]', v):
            raise ValueError('Password must contain lowercase letter')
        if not re.search(r'\d', v):
            raise ValueError('Password must contain digit')
        if not re.search(r'[!@#$%^&*]', v):
            raise ValueError('Password must contain special character')
        return v

    @validator('name')
    def validate_name(cls, v):
        # Prevent XSS in name field
        if re.search(r'[<>]', v):
            raise ValueError('Name contains invalid characters')
        return v

class APIKeyRequest(BaseModel):
    name: str = Field(..., max_length=100)
    expires_in_days: int = Field(30, ge=1, le=365)

# JWT token verification
def verify_token(credentials: HTTPAuthorizationCredentials = Security(security)):
    try:
        token = credentials.credentials

        payload = jwt.decode(
            token,
            "your-secret-key",
            algorithms=["HS256"],
            audience="api.example.com",
            issuer="api.example.com"
        )

        return payload

    except jwt.ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token has expired"
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token"
        )

# Role-based authorization
def require_role(required_roles: List[str]):
    def role_checker(token_payload: dict = Depends(verify_token)):
        user_role = token_payload.get('role')

        if user_role not in required_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Insufficient permissions"
            )

        return token_payload

    return role_checker

# API key authentication
def verify_api_key(api_key: str):
    # Constant-time comparison to prevent timing attacks
    if not secrets.compare_digest(api_key, "expected-api-key"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid API key"
        )
    return True

# Endpoints
@app.get("/api/health")
@limiter.limit("100/minute")
async def health_check():
    return {"status": "healthy"}

@app.post("/api/users")
@limiter.limit("10/minute")
async def create_user(
    user: CreateUserRequest,
    token_payload: dict = Depends(require_role(["admin"]))
):
    """Create new user (admin only)"""

    # Hash password before storing
    # hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

    return {
        "message": "User created successfully",
        "user_id": "123"
    }

@app.post("/api/keys")
@limiter.limit("5/hour")
async def create_api_key(
    request: APIKeyRequest,
    token_payload: dict = Depends(verify_token)
):
    """Generate API key"""

    # Generate secure random API key
    api_key = secrets.token_urlsafe(32)

    expires_at = datetime.now() + timedelta(days=request.expires_in_days)

    return {
        "api_key": api_key,
        "expires_at": expires_at.isoformat(),
        "name": request.name
    }

@app.get("/api/protected")
async def protected_endpoint(token_payload: dict = Depends(verify_token)):
    return {
        "message": "Access granted",
        "user_id": token_payload.get("sub")
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, ssl_certfile="cert.pem", ssl_keyfile="key.pem")
```

### 3. **API Gateway Security Configuration**

```yaml
# nginx-api-gateway.conf
# Nginx API Gateway with security hardening

http {
    # Security headers
    add_header X-Frame-Options "DENY" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header Content-Security-Policy "default-src 'self'" always;

    # Rate limiting zones
    limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;
    limit_req_zone $binary_remote_addr zone=auth_limit:10m rate=1r/s;
    limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

    # Request body size limit
    client_max_body_size 10M;
    client_body_buffer_size 128k;

    # Timeout settings
    client_body_timeout 12;
    client_header_timeout 12;
    send_timeout 10;

    server {
        listen 443 ssl http2;
        server_name api.example.com;

        # SSL configuration
        ssl_certificate /etc/ssl/certs/api.example.com.crt;
        ssl_certificate_key /etc/ssl/private/api.example.com.key;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;

        # API endpoints
        location /api/ {
            # Rate limiting
            limit_req zone=api_limit burst=20 nodelay;
            limit_conn conn_limit 10;

            # CORS headers
            add_header Access-Control-Allow-Origin "https://app.example.com" always;
            add_header Access-Control-Allow-Methods "GET, POST, PUT, DELETE" always;
            add_header Access-Control-Allow-Headers "Authorization, Content-Type" always;

            # Block common exploits
            if ($request_method !~ ^(GET|POST|PUT|DELETE|HEAD)$ ) {
                return 444;
            }

            # Proxy to backend
            proxy_pass http://backend:3000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;

            # Timeouts
            proxy_connect_timeout 60s;
            proxy_send_timeout 60s;
            proxy_read_timeout 60s;
        }

        # Auth endpoints with stricter limits
        location /api/auth/ {
            limit_req zone=auth_limit burst=5 nodelay;

            proxy_pass http://backend:3000;
        }

        # Block access to sensitive files
        location ~ /\. {
            deny all;
            return 404;
        }
    }
}
```

## Best Practices

### ✅ DO
- Use HTTPS everywhere
- Implement rate limiting
- Validate all inputs
- Use security headers
- Log security events
- Implement CORS properly
- Use strong authentication
- Version your APIs

### ❌ DON'T
- Expose stack traces
- Return detailed errors
- Trust user input
- Use HTTP for APIs
- Skip input validation
- Ignore rate limiting

## Security Checklist

- [ ] HTTPS enforced
- [ ] Authentication required
- [ ] Authorization implemented
- [ ] Rate limiting active
- [ ] Input validation
- [ ] CORS configured
- [ ] Security headers set
- [ ] Error handling secure
- [ ] Logging enabled
- [ ] API versioning

## Resources

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [API Security Best Practices](https://github.com/shieldfy/API-Security-Checklist)
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)
