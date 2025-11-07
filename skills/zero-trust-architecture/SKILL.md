---
name: zero-trust-architecture
description: Implement Zero Trust security model with identity verification, microsegmentation, least privilege access, and continuous monitoring. Use when building secure cloud-native applications.
---

# Zero Trust Architecture

## Overview

Implement comprehensive Zero Trust security architecture based on "never trust, always verify" principle with identity-centric security, microsegmentation, and continuous verification.

## When to Use

- Cloud-native applications
- Microservices architecture
- Remote workforce security
- API security
- Multi-cloud deployments
- Legacy modernization
- Compliance requirements

## Implementation Examples

### 1. **Zero Trust Gateway**

```javascript
// zero-trust-gateway.js
const jwt = require('jsonwebtoken');
const axios = require('axios');

class ZeroTrustGateway {
  constructor() {
    this.identityProvider = process.env.IDENTITY_PROVIDER_URL;
    this.deviceRegistry = new Map();
    this.sessionContext = new Map();
  }

  /**
   * Verify identity - Who are you?
   */
  async verifyIdentity(token) {
    try {
      // Verify JWT token
      const decoded = jwt.verify(token, process.env.JWT_PUBLIC_KEY, {
        algorithms: ['RS256']
      });

      // Check token hasn't been revoked
      const revoked = await this.checkTokenRevocation(decoded.jti);
      if (revoked) {
        throw new Error('Token has been revoked');
      }

      return {
        valid: true,
        userId: decoded.sub,
        roles: decoded.roles,
        permissions: decoded.permissions
      };
    } catch (error) {
      return { valid: false, error: error.message };
    }
  }

  /**
   * Verify device - What device are you using?
   */
  async verifyDevice(deviceId, deviceFingerprint) {
    const registered = this.deviceRegistry.get(deviceId);

    if (!registered) {
      return {
        trusted: false,
        reason: 'Device not registered'
      };
    }

    // Check device fingerprint matches
    if (registered.fingerprint !== deviceFingerprint) {
      return {
        trusted: false,
        reason: 'Device fingerprint mismatch'
      };
    }

    // Check device compliance
    const compliance = await this.checkDeviceCompliance(deviceId);

    return {
      trusted: compliance.compliant,
      reason: compliance.reason,
      riskScore: compliance.riskScore
    };
  }

  /**
   * Verify location - Where are you?
   */
  async verifyLocation(ip, expectedCountry) {
    try {
      // Get geolocation data
      const geoData = await this.getGeoLocation(ip);

      // Check for impossible travel
      const lastLocation = this.getLastKnownLocation(ip);
      if (lastLocation) {
        const impossibleTravel = this.detectImpossibleTravel(
          lastLocation,
          geoData,
          Date.now() - lastLocation.timestamp
        );

        if (impossibleTravel) {
          return {
            valid: false,
            reason: 'Impossible travel detected',
            riskScore: 9
          };
        }
      }

      // Check against allowed locations
      if (expectedCountry && geoData.country !== expectedCountry) {
        return {
          valid: false,
          reason: 'Unexpected location',
          riskScore: 7
        };
      }

      return {
        valid: true,
        location: geoData,
        riskScore: 1
      };
    } catch (error) {
      return {
        valid: false,
        reason: 'Location verification failed',
        riskScore: 5
      };
    }
  }

  /**
   * Verify authorization - What can you access?
   */
  async verifyAuthorization(userId, resource, action, context) {
    // Get user permissions
    const user = await this.getUserPermissions(userId);

    // Check direct permissions
    if (this.hasPermission(user, resource, action)) {
      return { authorized: true, reason: 'Direct permission' };
    }

    // Check role-based permissions
    for (const role of user.roles) {
      if (this.hasRolePermission(role, resource, action)) {
        return { authorized: true, reason: `Role: ${role}` };
      }
    }

    // Check attribute-based policies
    const abacResult = await this.evaluateABAC(user, resource, action, context);
    if (abacResult.allowed) {
      return { authorized: true, reason: 'ABAC policy' };
    }

    return {
      authorized: false,
      reason: 'Insufficient permissions'
    };
  }

  /**
   * Calculate risk score
   */
  calculateRiskScore(factors) {
    let score = 0;

    // Identity factors
    if (!factors.mfaUsed) score += 3;
    if (factors.newDevice) score += 2;

    // Location factors
    if (factors.unusualLocation) score += 3;
    if (factors.vpnDetected) score += 1;

    // Behavior factors
    if (factors.unusualTime) score += 2;
    if (factors.rapidRequests) score += 2;

    // Device factors
    if (!factors.deviceCompliant) score += 4;
    if (factors.jailbroken) score += 5;

    return Math.min(score, 10);
  }

  /**
   * Continuous verification middleware
   */
  middleware() {
    return async (req, res, next) => {
      const startTime = Date.now();

      try {
        // Extract authentication token
        const token = req.headers.authorization?.replace('Bearer ', '');
        if (!token) {
          return res.status(401).json({
            error: 'unauthorized',
            message: 'No authentication token provided'
          });
        }

        // Step 1: Verify identity
        const identity = await this.verifyIdentity(token);
        if (!identity.valid) {
          return res.status(401).json({
            error: 'unauthorized',
            message: 'Invalid identity'
          });
        }

        // Step 2: Verify device
        const deviceId = req.headers['x-device-id'];
        const deviceFingerprint = req.headers['x-device-fingerprint'];

        if (deviceId && deviceFingerprint) {
          const device = await this.verifyDevice(deviceId, deviceFingerprint);
          if (!device.trusted) {
            return res.status(403).json({
              error: 'forbidden',
              message: device.reason
            });
          }
        }

        // Step 3: Verify location
        const location = await this.verifyLocation(req.ip);
        if (!location.valid) {
          // Require step-up authentication
          return res.status(403).json({
            error: 'forbidden',
            message: 'Additional authentication required',
            requiresStepUp: true
          });
        }

        // Step 4: Calculate risk score
        const riskScore = this.calculateRiskScore({
          mfaUsed: identity.mfaUsed,
          newDevice: !deviceId,
          unusualLocation: location.riskScore > 5,
          deviceCompliant: true
        });

        // Step 5: Verify authorization
        const authorization = await this.verifyAuthorization(
          identity.userId,
          req.path,
          req.method,
          {
            ip: req.ip,
            riskScore,
            time: new Date()
          }
        );

        if (!authorization.authorized) {
          return res.status(403).json({
            error: 'forbidden',
            message: authorization.reason
          });
        }

        // Add context to request
        req.zeroTrust = {
          userId: identity.userId,
          roles: identity.roles,
          riskScore,
          verificationTime: Date.now() - startTime
        };

        // Log access
        this.logAccess(req, identity, riskScore);

        next();
      } catch (error) {
        console.error('Zero Trust verification failed:', error);
        return res.status(500).json({
          error: 'internal_error',
          message: 'Security verification failed'
        });
      }
    };
  }

  async checkTokenRevocation(jti) {
    // Check against revocation list
    return false;
  }

  async checkDeviceCompliance(deviceId) {
    // Check device meets security requirements
    return {
      compliant: true,
      reason: 'Device meets requirements',
      riskScore: 1
    };
  }

  async getGeoLocation(ip) {
    // Get geolocation from IP
    return {
      country: 'US',
      city: 'San Francisco',
      lat: 37.7749,
      lon: -122.4194
    };
  }

  getLastKnownLocation(ip) {
    return null;
  }

  detectImpossibleTravel(lastLocation, currentLocation, timeDiff) {
    // Calculate if travel is physically possible
    return false;
  }

  async getUserPermissions(userId) {
    // Fetch user permissions
    return {
      roles: ['user'],
      permissions: []
    };
  }

  hasPermission(user, resource, action) {
    return false;
  }

  hasRolePermission(role, resource, action) {
    return false;
  }

  async evaluateABAC(user, resource, action, context) {
    return { allowed: false };
  }

  logAccess(req, identity, riskScore) {
    console.log({
      timestamp: new Date().toISOString(),
      userId: identity.userId,
      resource: req.path,
      method: req.method,
      riskScore,
      ip: req.ip
    });
  }
}

// Express setup
const express = require('express');
const app = express();

const ztGateway = new ZeroTrustGateway();

// Apply Zero Trust middleware
app.use(ztGateway.middleware());

// Protected endpoint
app.get('/api/sensitive-data', (req, res) => {
  res.json({
    message: 'Access granted',
    riskScore: req.zeroTrust.riskScore
  });
});

module.exports = ZeroTrustGateway;
```

### 2. **Service Mesh - Microsegmentation**

```yaml
# istio-zero-trust.yaml
# Istio configuration for Zero Trust microsegmentation

apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: production
spec:
  mtls:
    mode: STRICT  # Require mutual TLS

---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: deny-all
  namespace: production
spec:
  {} # Deny all by default

---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-frontend-to-backend
  namespace: production
spec:
  selector:
    matchLabels:
      app: backend
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/production/sa/frontend"]
    to:
    - operation:
        methods: ["GET", "POST"]
        paths: ["/api/*"]

---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: allow-backend-to-database
  namespace: production
spec:
  selector:
    matchLabels:
      app: database
  action: ALLOW
  rules:
  - from:
    - source:
        principals: ["cluster.local/ns/production/sa/backend"]
    to:
    - operation:
        methods: ["*"]

---
# JWT authentication
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: jwt-auth
  namespace: production
spec:
  selector:
    matchLabels:
      app: backend
  jwtRules:
  - issuer: "https://auth.example.com"
    jwksUri: "https://auth.example.com/.well-known/jwks.json"
    audiences:
    - "api.example.com"

---
# Network policy - additional defense layer
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: backend-network-policy
  namespace: production
spec:
  podSelector:
    matchLabels:
      app: backend
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - podSelector:
        matchLabels:
          app: database
    ports:
    - protocol: TCP
      port: 5432
```

### 3. **Python Zero Trust Policy Engine**

```python
# zero_trust_policy.py
from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime
import jwt

@dataclass
class ZeroTrustContext:
    user_id: str
    device_id: str
    location: Dict[str, Any]
    risk_score: int
    timestamp: datetime

class ZeroTrustPolicy:
    def __init__(self):
        self.policies = self.load_policies()

    def load_policies(self) -> List[Dict]:
        """Load Zero Trust policies"""
        return [
            {
                'name': 'high_risk_block',
                'condition': lambda ctx: ctx.risk_score >= 8,
                'action': 'deny',
                'reason': 'High risk score'
            },
            {
                'name': 'require_mfa',
                'condition': lambda ctx: ctx.risk_score >= 5,
                'action': 'step_up_auth',
                'reason': 'Elevated risk requires MFA'
            },
            {
                'name': 'untrusted_device',
                'condition': lambda ctx: not self.is_device_trusted(ctx.device_id),
                'action': 'deny',
                'reason': 'Untrusted device'
            },
            {
                'name': 'unusual_location',
                'condition': lambda ctx: self.is_unusual_location(ctx),
                'action': 'step_up_auth',
                'reason': 'Unusual location detected'
            }
        ]

    def evaluate(self, context: ZeroTrustContext, resource: str, action: str) -> Dict:
        """Evaluate Zero Trust policies"""
        for policy in self.policies:
            if policy['condition'](context):
                return {
                    'allowed': policy['action'] != 'deny',
                    'action': policy['action'],
                    'reason': policy['reason'],
                    'policy': policy['name']
                }

        # Check resource-specific permissions
        if self.has_permission(context.user_id, resource, action):
            return {
                'allowed': True,
                'action': 'allow',
                'reason': 'User has required permissions'
            }

        return {
            'allowed': False,
            'action': 'deny',
            'reason': 'No matching policy allows access'
        }

    def is_device_trusted(self, device_id: str) -> bool:
        # Check device trust status
        return True

    def is_unusual_location(self, context: ZeroTrustContext) -> bool:
        # Check if location is unusual for user
        return False

    def has_permission(self, user_id: str, resource: str, action: str) -> bool:
        # Check user permissions
        return False

# Flask integration
from flask import Flask, request, jsonify, g
from functools import wraps

app = Flask(__name__)
zt_policy = ZeroTrustPolicy()

def zero_trust_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Build Zero Trust context
        context = ZeroTrustContext(
            user_id=g.user_id,
            device_id=request.headers.get('X-Device-ID', 'unknown'),
            location={
                'ip': request.remote_addr,
                'country': 'US'  # From GeoIP
            },
            risk_score=calculate_risk_score(request),
            timestamp=datetime.utcnow()
        )

        # Evaluate policies
        result = zt_policy.evaluate(
            context,
            request.path,
            request.method
        )

        if not result['allowed']:
            return jsonify({
                'error': 'forbidden',
                'reason': result['reason'],
                'action_required': result['action']
            }), 403

        return f(*args, **kwargs)

    return decorated_function

def calculate_risk_score(request) -> int:
    """Calculate risk score based on request context"""
    score = 0

    # Check for suspicious patterns
    if not request.headers.get('X-Device-ID'):
        score += 2

    # Add more risk factors
    return min(score, 10)

@app.route('/api/sensitive', methods=['GET'])
@zero_trust_required
def get_sensitive_data():
    return jsonify({'data': 'sensitive information'})
```

## Zero Trust Principles

1. **Verify Explicitly**: Always authenticate and authorize
2. **Least Privilege**: Minimal access required
3. **Assume Breach**: Limit blast radius
4. **Microsegmentation**: Network segmentation
5. **Continuous Monitoring**: Real-time security
6. **Device Trust**: Verify device compliance
7. **Data Protection**: Encrypt everything

## Implementation Layers

- **Identity Layer**: Strong authentication (MFA, SSO)
- **Device Layer**: Device compliance, certificates
- **Network Layer**: Microsegmentation, mTLS
- **Application Layer**: API gateway, authorization
- **Data Layer**: Encryption, DLP

## Zero Trust Maturity Model

1. **Traditional**: Perimeter-based security
2. **Advanced**: Some segmentation
3. **Optimal**: Full Zero Trust
4. **Progressive**: Continuous improvement

## Best Practices

### ✅ DO
- Verify every request
- Implement MFA everywhere
- Use microsegmentation
- Monitor continuously
- Encrypt all communications
- Implement least privilege
- Log all access
- Regular audits

### ❌ DON'T
- Trust network location
- Use implicit trust
- Skip device verification
- Allow lateral movement
- Use static credentials

## Resources

- [NIST Zero Trust Architecture](https://csrc.nist.gov/publications/detail/sp/800-207/final)
- [Google BeyondCorp](https://cloud.google.com/beyondcorp)
- [Zero Trust Implementation Guide](https://www.microsoft.com/en-us/security/business/zero-trust)
