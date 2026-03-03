# Input Validation & Sanitization

## Input Validation & Sanitization

```javascript
// input-validator.js
class InputValidator {
  static validateEmail(email) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email) && email.length <= 255;
  }

  static validateInteger(value) {
    const num = parseInt(value, 10);
    return Number.isInteger(num) && num >= 0;
  }

  static sanitizeString(input, maxLength = 255) {
    // Remove control characters
    let sanitized = input.replace(/[\x00-\x1F\x7F]/g, "");

    // Trim and limit length
    sanitized = sanitized.trim().substring(0, maxLength);

    return sanitized;
  }

  static validateSQLIdentifier(identifier) {
    // Only allow alphanumeric and underscore
    return /^[a-zA-Z_][a-zA-Z0-9_]*$/.test(identifier);
  }

  static escapeForLike(input) {
    // Escape LIKE wildcards
    return input.replace(/[%_]/g, "\\$&");
  }
}

module.exports = InputValidator;
```
