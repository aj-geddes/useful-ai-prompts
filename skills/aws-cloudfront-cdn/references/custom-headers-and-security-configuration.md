# Custom Headers and Security Configuration

## Custom Headers and Security Configuration

```bash
# Add custom headers for security
aws cloudfront create-response-headers-policy \
  --response-headers-policy-config '{
    "Name": "SecurityHeadersPolicy",
    "SecurityHeadersConfig": {
      "StrictTransportSecurity": {
        "Enabled": true,
        "AccessControlMaxAgeSec": 63072000,
        "IncludeSubdomains": true,
        "Preload": true
      },
      "ContentTypeOptions": {
        "Enabled": true
      },
      "XSSProtection": {
        "Enabled": true,
        "ModeBlock": true
      },
      "ReferrerPolicy": {
        "Enabled": true,
        "ReferrerPolicy": "strict-origin-when-cross-origin"
      },
      "FrameOptions": {
        "Enabled": true,
        "FrameOption": "DENY"
      }
    }
  }'
```
