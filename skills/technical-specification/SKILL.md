---
name: technical-specification
description: Create detailed technical specifications, requirements documents, design documents, and system architecture specs. Use when writing technical specs, requirements docs, or design documents.
---

# Technical Specification

## Overview

Create comprehensive technical specifications that define system requirements, architecture, implementation details, and acceptance criteria for software projects.

## When to Use

- Feature specifications
- System design documents
- Requirements documentation (PRD)
- Architecture decision records (ADR)
- Technical proposals
- RFC (Request for Comments)
- API design specs
- Database schema designs

## Technical Specification Template

```markdown
# Technical Specification: [Feature Name]

**Document Status:** Draft | Review | Approved | Implemented
**Version:** 1.0
**Author:** John Doe
**Date:** 2025-01-15
**Reviewers:** Jane Smith, Bob Johnson
**Last Updated:** 2025-01-15

## Executive Summary

Brief 2-3 sentence overview of what this spec covers and why it's being built.

**Problem:** What problem are we solving?
**Solution:** High-level description of the solution
**Impact:** Expected business/user impact

---

## 1. Background

### Context

Provide background on why this feature is needed:
- What's the current situation?
- What pain points exist?
- What's driving this change?

### Goals

- **Primary Goal:** Main objective of this feature
- **Secondary Goals:** Additional benefits
- **Success Metrics:** How we'll measure success
  - Metric 1: [Description] - Target: [Value]
  - Metric 2: [Description] - Target: [Value]

### Non-Goals

What this specification explicitly does NOT cover:
- Non-goal 1
- Non-goal 2
- Future considerations (out of scope for v1)

---

## 2. Requirements

### Functional Requirements

#### FR-1: User Authentication
**Priority:** P0 (Must Have)
**Description:** Users must be able to authenticate using email/password

**Acceptance Criteria:**
- [ ] User can register with email and password
- [ ] User can log in with credentials
- [ ] User receives email verification
- [ ] User can reset forgotten password
- [ ] Session expires after 7 days of inactivity

**Dependencies:** None

#### FR-2: Social Login
**Priority:** P1 (Should Have)
**Description:** Users can authenticate using OAuth providers

**Acceptance Criteria:**
- [ ] Support Google OAuth
- [ ] Support GitHub OAuth
- [ ] Link social accounts to existing accounts
- [ ] Unlink social accounts

**Dependencies:** FR-1

#### FR-3: Two-Factor Authentication
**Priority:** P2 (Nice to Have)
**Description:** Optional 2FA for enhanced security

**Acceptance Criteria:**
- [ ] Enable/disable 2FA in settings
- [ ] Support TOTP (Google Authenticator, Authy)
- [ ] Backup codes generation
- [ ] Recovery process if device is lost

**Dependencies:** FR-1

### Non-Functional Requirements

#### Performance
- **Response Time:** API endpoints < 200ms p95
- **Throughput:** Support 1000 requests/second
- **Database Queries:** < 50ms p95
- **Page Load:** First contentful paint < 1.5s

#### Scalability
- **Concurrent Users:** Support 100,000 simultaneous users
- **Data Growth:** Handle 10M user records
- **Horizontal Scaling:** Support 10 application instances

#### Security
- **Authentication:** JWT-based with refresh tokens
- **Password Hashing:** bcrypt with 12 rounds
- **Rate Limiting:** 100 requests/hour per IP
- **Data Encryption:** AES-256 at rest, TLS 1.3 in transit

#### Availability
- **Uptime:** 99.9% SLA
- **Recovery Time:** RTO < 4 hours, RPO < 1 hour
- **Backup:** Daily automated backups, 30-day retention

#### Compliance
- GDPR compliant (data export/deletion)
- SOC 2 Type II requirements
- PCI DSS (if handling payments)

---

## 3. System Architecture

### High-Level Architecture

```
┌─────────────┐
│   Client    │
│ (React App) │
└──────┬──────┘
       │
       ▼
┌─────────────┐     ┌──────────────┐
│ API Gateway │────▶│ Auth Service │
│  (Express)  │     │   (Node.js)  │
└──────┬──────┘     └──────┬───────┘
       │                   │
       ▼                   ▼
┌─────────────┐     ┌──────────────┐
│User Service │     │   Database   │
│  (Node.js)  │────▶│ (PostgreSQL) │
└─────────────┘     └──────────────┘
       │
       ▼
┌─────────────┐
│    Cache    │
│   (Redis)   │
└─────────────┘
```

### Component Diagram

#### Frontend (React)
- **Login Page:** Email/password and social login
- **Registration Page:** User signup with validation
- **Settings Page:** Manage 2FA and connected accounts
- **Components:** Reusable auth components

#### Backend (Node.js/Express)
- **Auth Controller:** Handle authentication requests
- **User Controller:** Manage user data
- **Auth Middleware:** Validate JWT tokens
- **Rate Limiter:** Prevent abuse

#### Database (PostgreSQL)
- **users table:** User account data
- **sessions table:** Active sessions
- **oauth_connections table:** Social login links

#### Cache (Redis)
- Session storage
- Rate limit counters
- Temporary tokens (password reset, email verification)

---

## 4. Data Model

### Database Schema

```sql
-- Users table
CREATE TABLE users (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  email VARCHAR(255) UNIQUE NOT NULL,
  password_hash VARCHAR(255),
  email_verified BOOLEAN DEFAULT FALSE,
  two_factor_enabled BOOLEAN DEFAULT FALSE,
  two_factor_secret VARCHAR(32),
  created_at TIMESTAMP DEFAULT NOW(),
  updated_at TIMESTAMP DEFAULT NOW(),
  last_login_at TIMESTAMP
);

-- OAuth connections
CREATE TABLE oauth_connections (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  provider VARCHAR(50) NOT NULL, -- 'google', 'github'
  provider_user_id VARCHAR(255) NOT NULL,
  access_token TEXT,
  refresh_token TEXT,
  created_at TIMESTAMP DEFAULT NOW(),
  UNIQUE(provider, provider_user_id)
);

-- Sessions
CREATE TABLE sessions (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  user_id UUID REFERENCES users(id) ON DELETE CASCADE,
  token VARCHAR(255) UNIQUE NOT NULL,
  expires_at TIMESTAMP NOT NULL,
  created_at TIMESTAMP DEFAULT NOW(),
  ip_address INET,
  user_agent TEXT
);

-- Indexes
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_sessions_token ON sessions(token);
CREATE INDEX idx_sessions_user_id ON sessions(user_id);
CREATE INDEX idx_oauth_user_id ON oauth_connections(user_id);
```

### API Data Models

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

## 5. API Design

### Authentication Endpoints

#### POST /api/auth/register
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

#### POST /api/auth/login
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

### Rate Limiting

| Endpoint | Limit | Window |
|----------|-------|--------|
| POST /api/auth/login | 5 attempts | 15 minutes |
| POST /api/auth/register | 3 attempts | 1 hour |
| POST /api/auth/reset-password | 3 attempts | 1 hour |

---

## 6. Implementation Plan

### Phase 1: Core Authentication (Week 1-2)
- [ ] Database schema setup
- [ ] User registration endpoint
- [ ] Email/password login
- [ ] JWT token generation
- [ ] Password hashing
- [ ] Basic frontend forms

### Phase 2: Email Verification (Week 3)
- [ ] Email service integration
- [ ] Verification token generation
- [ ] Verification endpoint
- [ ] Email templates
- [ ] Resend verification email

### Phase 3: Social Login (Week 4)
- [ ] OAuth integration (Google)
- [ ] OAuth integration (GitHub)
- [ ] Account linking
- [ ] Frontend OAuth buttons

### Phase 4: Security Features (Week 5)
- [ ] Two-factor authentication
- [ ] Password reset flow
- [ ] Rate limiting
- [ ] Session management
- [ ] Security headers

### Phase 5: Testing & Polish (Week 6)
- [ ] Unit tests
- [ ] Integration tests
- [ ] E2E tests
- [ ] Security audit
- [ ] Performance testing
- [ ] Documentation

---

## 7. Testing Strategy

### Unit Tests
- Password hashing/verification
- JWT token generation/validation
- Input validation
- Business logic

**Coverage Target:** 90%

### Integration Tests
- API endpoint testing
- Database operations
- OAuth flow
- Email sending

**Coverage Target:** 80%

### E2E Tests
- Complete registration flow
- Login with email/password
- Social login flow
- Password reset flow
- 2FA setup and verification

**Coverage Target:** Critical paths only

### Performance Tests
- Load testing: 1000 concurrent logins
- Stress testing: Find breaking point
- Database query performance

---

## 8. Security Considerations

### Threats

| Threat | Mitigation |
|--------|------------|
| Brute force | Rate limiting, account lockout |
| SQL injection | Parameterized queries, ORM |
| XSS | Input sanitization, CSP headers |
| CSRF | CSRF tokens, SameSite cookies |
| Session hijacking | Secure cookies, HTTPS only |
| Password leaks | bcrypt hashing, password strength |

### Security Checklist
- [ ] HTTPS enforced
- [ ] Security headers configured
- [ ] Rate limiting implemented
- [ ] Input validation on all endpoints
- [ ] SQL injection prevention
- [ ] XSS prevention
- [ ] CSRF protection
- [ ] Secure password storage
- [ ] Audit logging

---

## 9. Monitoring & Observability

### Metrics
- **Authentication success rate**
- **Failed login attempts**
- **Average login time**
- **Active sessions**
- **2FA adoption rate**

### Alerts
- Failed login rate > 10%
- Database connection errors
- Email sending failures
- Rate limit exceeded > 100 times/hour

### Logging
```javascript
// Log structure
{
  "timestamp": "2025-01-15T14:30:00Z",
  "level": "info",
  "event": "user_login",
  "userId": "550e8400-...",
  "ip": "192.168.1.1",
  "userAgent": "Mozilla/5.0...",
  "success": true,
  "duration": 125
}
```

---

## 10. Risks & Mitigation

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| OAuth provider downtime | Medium | High | Fallback to email login |
| Database migration issues | Low | High | Test thoroughly in staging |
| Performance under load | Medium | Medium | Load testing, caching |
| Security vulnerabilities | Low | Critical | Security audit, pen testing |

---

## 11. Open Questions

1. Should we support passwordless authentication?
2. What's the session timeout policy?
3. Do we need magic link login?
4. Should we implement remember me functionality?

---

## 12. Alternatives Considered

### Alternative 1: Use Auth0
**Pros:** Faster implementation, proven security
**Cons:** Cost, vendor lock-in, less customization
**Decision:** Build in-house for flexibility

### Alternative 2: Session-based auth instead of JWT
**Pros:** Simpler revocation, less token size
**Cons:** Harder to scale, CORS issues
**Decision:** Use JWT for stateless scaling

---

## 13. Success Criteria

### Launch Criteria
- [ ] All P0 requirements implemented
- [ ] Security audit passed
- [ ] Load testing passed (1000 concurrent users)
- [ ] Documentation complete
- [ ] 90% test coverage achieved

### Post-Launch Metrics (Week 1)
- < 1% authentication error rate
- < 500ms average login time
- > 95% user satisfaction (surveys)
- Zero security incidents

---

## 14. References

- [OWASP Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [JWT Best Practices](https://tools.ietf.org/html/rfc8725)
- [OAuth 2.0 Spec](https://oauth.net/2/)
- Internal: Authentication RFC #123
```

## Best Practices

### ✅ DO
- Include acceptance criteria for each requirement
- Provide architecture diagrams
- Document API contracts
- Specify performance requirements
- List risks and mitigations
- Include implementation timeline
- Add success metrics
- Document security considerations
- Version your specs
- Get stakeholder review

### ❌ DON'T
- Be vague about requirements
- Skip non-functional requirements
- Forget about security
- Ignore alternatives
- Skip testing strategy
- Forget monitoring/observability
- Leave questions unanswered

## Resources

- [Google Design Docs](https://www.industrialempathy.com/posts/design-docs-at-google/)
- [RFC Template](https://github.com/philips/template-rfcs)
- [Architecture Decision Records](https://adr.github.io/)
- [Amazon Press Release / FAQ](https://www.productplan.com/glossary/working-backward-amazon-method/)
