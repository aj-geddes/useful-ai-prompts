# Rate Limiting

## Rate Limiting

| Endpoint                      | Limit      | Window     |
| ----------------------------- | ---------- | ---------- |
| POST /api/auth/login          | 5 attempts | 15 minutes |
| POST /api/auth/register       | 3 attempts | 1 hour     |
| POST /api/auth/reset-password | 3 attempts | 1 hour     |

---
