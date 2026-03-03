---
name: email-service-integration
description: >
  Integrate email services with backends using SMTP, third-party providers,
  templates, and asynchronous sending. Use when implementing email
  functionality, sending transactional emails, and managing email workflows.
---

# Email Service Integration

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build comprehensive email systems with SMTP integration, third-party email providers (SendGrid, Mailgun, AWS SES), HTML templates, email validation, retry mechanisms, and proper error handling.

## When to Use

- Sending transactional emails
- Implementing welcome/confirmation emails
- Creating password reset flows
- Sending notification emails
- Building email templates
- Managing bulk email campaigns

## Quick Start

Minimal working example:

```python
# config.py
import os

class EmailConfig:
    MAIL_SERVER = os.getenv('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.getenv('MAIL_PORT', 587))
    MAIL_USE_TLS = os.getenv('MAIL_USE_TLS', True)
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.getenv('MAIL_DEFAULT_SENDER', 'noreply@example.com')

# email_service.py
from flask_mail import Mail, Message
from flask import render_template_string
import logging
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logger = logging.getLogger(__name__)
mail = Mail()

class EmailService:
    def __init__(self, app=None):
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Python/Flask with SMTP](references/pythonflask-with-smtp.md) | Python/Flask with SMTP |
| [Node.js with SendGrid](references/nodejs-with-sendgrid.md) | Node.js with SendGrid |
| [Email Templates with Mjml](references/email-templates-with-mjml.md) | Email Templates with Mjml |
| [FastAPI Email with Background Tasks](references/fastapi-email-with-background-tasks.md) | FastAPI Email with Background Tasks |
| [Email Validation and Verification](references/email-validation-and-verification.md) | Email Validation and Verification |

## Best Practices

### ✅ DO

- Use transactional email providers for reliability
- Implement email templates for consistency
- Add unsubscribe links (required by law)
- Use background tasks for email sending
- Implement proper error handling and retries
- Validate email addresses before sending
- Add rate limiting to prevent abuse
- Monitor email delivery and bounces
- Use SMTP authentication
- Test emails in development environment

### ❌ DON'T

- Send emails synchronously in request handlers
- Store passwords in code
- Send sensitive information in emails
- Use generic email addresses for sensitive operations
- Skip email validation
- Ignore bounce and complaint notifications
- Use HTML email with inline styles excessively
- Forget to handle failed email deliveries
- Send emails without proper templates
- Store email addresses without consent
