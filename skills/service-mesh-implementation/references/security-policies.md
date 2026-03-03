# Security Policies

## Security Policies

```yaml
# security-config.yaml
apiVersion: security.istio.io/v1beta1
kind: PeerAuthentication
metadata:
  name: default
  namespace: istio-system
spec:
  mtls:
    mode: STRICT # Enforce mTLS for all workloads

---
apiVersion: security.istio.io/v1beta1
kind: AuthorizationPolicy
metadata:
  name: api-service-authz
  namespace: production
spec:
  selector:
    matchLabels:
      app: api-service
  action: ALLOW
  rules:
    - from:
        - source:
            principals: ["cluster.local/ns/production/sa/web-service"]
      to:
        - operation:
            methods: ["GET", "POST"]
            paths: ["/api/v1/*"]

    # Allow health checks
    - to:
        - operation:
            methods: ["GET"]
            paths: ["/health"]

---
apiVersion: security.istio.io/v1beta1
kind: RequestAuthentication
metadata:
  name: api-service-authn
  namespace: production
spec:
  selector:
    matchLabels:
      app: api-service
  jwtRules:
    - issuer: https://auth.mycompany.com
      jwksUri: https://auth.mycompany.com/.well-known/jwks.json
      audiences: api-service
```
