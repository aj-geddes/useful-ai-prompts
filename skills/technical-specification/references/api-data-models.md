# API Data Models

## API Data Models

```typescript
interface User {
  id: string;
  email: string;
  emailVerified: boolean;
  twoFactorEnabled: boolean;
  createdAt: string;
  updatedAt: string;
  lastLoginAt?: string;
}

interface LoginRequest {
  email: string;
  password: string;
  twoFactorCode?: string;
}

interface LoginResponse {
  success: boolean;
  token: string;
  refreshToken: string;
  user: User;
  expiresIn: number;
}

interface RegisterRequest {
  email: string;
  password: string;
  confirmPassword: string;
}
```

---
