# 🔒 Security

## 🔒 Security

- **TLS 1.3 Required:** Dropped support for TLS 1.2
- **JWT Expiry:** Tokens now expire after 1 hour (was 24 hours)
- **Rate Limiting:** Stricter limits on authentication endpoints
- **CORS:** Updated allowed origins (see security policy)
- **Input Validation:** Enhanced validation on all endpoints

---


## 🗑️ Deprecated

### Deprecation Schedule

| Feature               | Deprecated | Removal Date | Replacement                |
| --------------------- | ---------- | ------------ | -------------------------- |
| API Token Auth        | v3.0.0     | 2025-06-01   | JWT Bearer tokens          |
| XML Response Format   | v3.0.0     | 2025-04-01   | JSON only                  |
| `/api/v1/*` endpoints | v3.0.0     | 2025-03-01   | `/api/v3/*`                |
| Query param `filter`  | v3.0.0     | 2025-05-01   | Use `filters[field]=value` |

**Deprecation Warnings:**

All deprecated features return a warning header:

```http
HTTP/1.1 200 OK
Deprecation: true
Sunset: Sat, 01 Jun 2025 00:00:00 GMT
Link: <https://docs.example.com/migration/v2-to-v3>; rel="deprecation"
```

---


## 📊 Version Support Policy

| Version | Status      | Release Date | End of Support |
| ------- | ----------- | ------------ | -------------- |
| v3.x    | Current     | 2025-01-15   | TBD            |
| v2.x    | Maintenance | 2024-01-01   | 2025-07-01     |
| v1.x    | End of Life | 2023-01-01   | 2024-12-31     |

**Support Levels:**

- **Current:** Full support, new features
- **Maintenance:** Bug fixes and security patches only
- **End of Life:** No support, upgrade required

---
