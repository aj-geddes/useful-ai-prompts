# Email Validation and Verification

## Email Validation and Verification

```python
# email_validator.py
import re
from email_validator import validate_email, EmailNotValidError
import dns.resolver

class EmailValidator:
    @staticmethod
    def validate_format(email: str) -> tuple:
        """Validate email format"""
        try:
            valid = validate_email(email)
            return True, valid.email
        except EmailNotValidError as e:
            return False, str(e)

    @staticmethod
    def check_mx_records(email: str) -> bool:
        """Check MX records for domain"""
        try:
            domain = email.split('@')[1]
            mx_records = dns.resolver.resolve(domain, 'MX')
            return len(mx_records) > 0
        except Exception:
            return False

    @staticmethod
    def validate_email_comprehensive(email: str) -> dict:
        """Comprehensive email validation"""
        # Format validation
        is_valid, message = EmailValidator.validate_format(email)
        if not is_valid:
            return {'valid': False, 'reason': 'Invalid format'}

        # MX record check
        has_mx = EmailValidator.check_mx_records(email)
        if not has_mx:
            return {'valid': False, 'reason': 'Domain has no MX records'}

        return {'valid': True, 'email': email}
```
