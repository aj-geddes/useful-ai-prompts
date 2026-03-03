# Python FastAPI Security

## Python FastAPI Security

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
