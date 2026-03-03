# 2 Multi-Factor Authentication (MFA)

## 2 Multi-Factor Authentication (MFA)

**Requirements:**

- **Mandatory** for:
  - Production system access
  - Administrative accounts
  - Customer-facing applications
  - VPN access
  - Source code repositories

**Supported Methods:**

1. TOTP (Google Authenticator, Authy)
2. SMS (backup only, not primary)
3. Hardware tokens (YubiKey)
4. Biometric (fingerprint, Face ID)

**Implementation:**

```javascript
// MFA verification
async function verifyMFA(userId, token) {
  const user = await User.findById(userId);
  const secret = user.twoFactorSecret;

  // Verify TOTP token
  const isValid = speakeasy.totp.verify({
    secret,
    encoding: "base32",
    token,
    window: 2, // Allow 1 minute time drift
  });

  if (isValid) {
    await logSecurityEvent("mfa_success", userId);
    return true;
  }

  await logSecurityEvent("mfa_failure", userId);
  return false;
}
```
