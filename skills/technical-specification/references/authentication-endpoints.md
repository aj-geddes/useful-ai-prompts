# Authentication Endpoints

## Authentication Endpoints

### POST /api/auth/register

**Description:** Register a new user account

**Request:**

```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "confirmPassword": "SecurePass123!"
}
```

**Response (201):**

```json
{
  "success": true,
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com",
    "emailVerified": false
  },
  "message": "Verification email sent"
}
```

**Errors:**

- 400: Invalid email format
- 409: Email already exists
- 422: Password too weak

### POST /api/auth/login

**Description:** Authenticate user and return JWT token

**Request:**

```json
{
  "email": "user@example.com",
  "password": "SecurePass123!",
  "twoFactorCode": "123456"
}
```

**Response (200):**

```json
{
  "success": true,
  "token": "eyJhbGciOiJIUzI1NiIs...",
  "refreshToken": "eyJhbGciOiJIUzI1NiIs...",
  "user": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "email": "user@example.com"
  },
  "expiresIn": 3600
}
```

**Errors:**

- 401: Invalid credentials
- 403: Account locked
- 428: 2FA code required
