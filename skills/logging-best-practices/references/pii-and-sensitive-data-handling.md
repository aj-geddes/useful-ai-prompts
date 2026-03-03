# PII and Sensitive Data Handling

## PII and Sensitive Data Handling

### Data Sanitization

```typescript
// sanitizer.ts
const SENSITIVE_FIELDS = [
  "password",
  "token",
  "apiKey",
  "ssn",
  "creditCard",
  "email", // depending on regulations
  "phone", // depending on regulations
];

function sanitize(obj: any): any {
  if (typeof obj !== "object" || obj === null) {
    return obj;
  }

  if (Array.isArray(obj)) {
    return obj.map(sanitize);
  }

  const sanitized = {};
  for (const [key, value] of Object.entries(obj)) {
    if (
      SENSITIVE_FIELDS.some((field) =>
        key.toLowerCase().includes(field.toLowerCase()),
      )
    ) {
      sanitized[key] = "[REDACTED]";
    } else if (typeof value === "object") {
      sanitized[key] = sanitize(value);
    } else {
      sanitized[key] = value;
    }
  }
  return sanitized;
}

// Usage
logger.info(
  "User data",
  sanitize({
    userId: "123",
    email: "user@example.com", // Will be redacted
    password: "secret123", // Will be redacted
    name: "John Doe", // Will be logged
  }),
);

// Output:
// {
//   "userId": "123",
//   "email": "[REDACTED]",
//   "password": "[REDACTED]",
//   "name": "John Doe"
// }
```

### Email/PII Masking

```typescript
// masking.ts
function maskEmail(email: string): string {
  const [local, domain] = email.split("@");
  const maskedLocal =
    local[0] + "*".repeat(local.length - 2) + local[local.length - 1];
  return `${maskedLocal}@${domain}`;
}

function maskPhone(phone: string): string {
  return phone.replace(/\d(?=\d{4})/g, "*");
}

function maskCreditCard(cc: string): string {
  return cc.replace(/\d(?=\d{4})/g, "*");
}

// Usage
logger.info("User registered", {
  userId: user.id,
  email: maskEmail(user.email), // u***r@example.com
  phone: maskPhone(user.phone), // ******1234
  creditCard: maskCreditCard(user.card), // ************1234
});
```
