# HTTP Status Codes

## HTTP Status Codes

```
Success:
200 OK              - Successful GET, PATCH, DELETE
201 Created         - Successful POST (resource created)
204 No Content      - Successful DELETE (no response body)

Client Errors:
400 Bad Request     - Invalid request format/data
401 Unauthorized    - Missing or invalid authentication
403 Forbidden       - Authenticated but not authorized
404 Not Found       - Resource doesn't exist
409 Conflict        - Resource conflict (e.g., duplicate email)
422 Unprocessable   - Validation errors
429 Too Many Requests - Rate limit exceeded

Server Errors:
500 Internal Server Error - Generic server error
503 Service Unavailable   - Temporary unavailability
```


## API Versioning

```http
# URL Path Versioning (Recommended)
GET /api/v1/users
GET /api/v2/users

# Header Versioning
GET /api/users
Accept: application/vnd.myapi.v1+json

# Query Parameter (Not recommended)
GET /api/users?version=1
```


## Authentication & Security

```http
# JWT Bearer Token
GET /api/users
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...

# API Key
GET /api/users
X-API-Key: your-api-key-here

# Always use HTTPS in production
https://api.example.com/v1/users
```


## Rate Limiting Headers

```http
HTTP/1.1 200 OK
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 995
X-RateLimit-Reset: 1642262400
```
