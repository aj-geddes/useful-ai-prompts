# 1 Password Requirements

## 1 Password Requirements

**Minimum Requirements:**

- Length: Minimum 12 characters
- Complexity: Mix of uppercase, lowercase, numbers, and symbols
- History: Cannot reuse last 5 passwords
- Expiration: 90 days (for privileged accounts)
- Lockout: 5 failed attempts triggers 30-minute lockout

**Example Strong Password:**
```

Good: MyC0mplex!Pass#2025
Bad: password123

````

**Implementation:**

```javascript
// Password validation
function validatePassword(password) {
  const minLength = 12;
  const requirements = {
    length: password.length >= minLength,
    uppercase: /[A-Z]/.test(password),
    lowercase: /[a-z]/.test(password),
    number: /[0-9]/.test(password),
    special: /[!@#$%^&*(),.?":{}|<>]/.test(password)
  };

  return Object.values(requirements).every(Boolean);
}
````
