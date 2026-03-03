# Let's Encrypt with Cert-Manager

## Let's Encrypt with Cert-Manager

```yaml
# cert-manager-setup.yaml
apiVersion: cert-manager.io/v1
kind: ClusterIssuer
metadata:
  name: letsencrypt-prod
spec:
  acme:
    server: https://acme-v02.api.letsencrypt.org/directory
    email: admin@myapp.com
    privateKeySecretRef:
      name: letsencrypt-prod
    solvers:
      # HTTP-01 solver for standard domains
      - http01:
          ingress:
            class: nginx
        selector:
          dnsNames:
            - "myapp.com"
            - "www.myapp.com"

      # DNS-01 solver for wildcard domains
      - dns01:
          route53:
            region: us-east-1
            hostedZoneID: Z1234567890ABC
            accessKeyID: AKIAIOSFODNN7EXAMPLE
            secretAccessKeySecretRef:
              name: route53-credentials
              key: secret-access-key
        selector:
          dnsNames:
            - "*.myapp.com"

---
apiVersion: cert-manager.io/v1
kind: Certificate
metadata:
  name: myapp-tls
  namespace: production
spec:
  secretName: myapp-tls-secret
  issuerRef:
    name: letsencrypt-prod
    kind: ClusterIssuer
  commonName: myapp.com
  dnsNames:
    - myapp.com
    - www.myapp.com
    - api.myapp.com
    - "*.myapp.com"
  duration: 2160h # 90 days
  renewBefore: 720h # 30 days before expiry

---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: myapp
  namespace: production
  annotations:
    cert-manager.io/cluster-issuer: "letsencrypt-prod"
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
spec:
  ingressClassName: nginx
  tls:
    - hosts:
        - myapp.com
        - www.myapp.com
      secretName: myapp-tls-secret
  rules:
    - host: myapp.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: myapp
                port:
                  number: 80
```
