---
name: email-service-integration
description: Integrate email services with backends using SMTP, third-party providers, templates, and asynchronous sending. Use when implementing email functionality, sending transactional emails, and managing email workflows.
---

# Email Service Integration

## Overview

Build comprehensive email systems with SMTP integration, third-party email providers (SendGrid, Mailgun, AWS SES), HTML templates, email validation, retry mechanisms, and proper error handling.

## When to Use

- Sending transactional emails
- Implementing welcome/confirmation emails
- Creating password reset flows
- Sending notification emails
- Building email templates
- Managing bulk email campaigns

## Instructions

### 1. **Python/Flask with SMTP**

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
        self.app = app
        if app:
            mail.init_app(app)

    def send_email(self, recipient, subject, text_body=None, html_body=None):
        """Send email using Flask-Mail"""
        try:
            msg = Message(
                subject=subject,
                recipients=[recipient] if isinstance(recipient, str) else recipient
            )

            if text_body:
                msg.body = text_body
            if html_body:
                msg.html = html_body

            mail.send(msg)
            logger.info(f"Email sent to {recipient}: {subject}")
            return True
        except Exception as e:
            logger.error(f"Failed to send email to {recipient}: {str(e)}")
            return False

    def send_welcome_email(self, user_email, user_name):
        """Send welcome email"""
        subject = "Welcome to Our Platform!"
        html_body = render_template_string(
            '''
            <h1>Welcome, {{ name }}!</h1>
            <p>Thank you for joining us. Start exploring now!</p>
            <a href="https://example.com/dashboard">Go to Dashboard</a>
            ''',
            name=user_name
        )
        return self.send_email(user_email, subject, html_body=html_body)

    def send_password_reset_email(self, user_email, reset_token):
        """Send password reset email"""
        subject = "Reset Your Password"
        reset_url = f"https://example.com/reset-password?token={reset_token}"
        html_body = render_template_string(
            '''
            <h1>Reset Your Password</h1>
            <p>Click the link below to reset your password:</p>
            <a href="{{ reset_url }}">Reset Password</a>
            <p>This link expires in 24 hours.</p>
            ''',
            reset_url=reset_url
        )
        return self.send_email(user_email, subject, html_body=html_body)

    def send_verification_email(self, user_email, verification_token):
        """Send email verification"""
        subject = "Verify Your Email"
        verify_url = f"https://example.com/verify-email?token={verification_token}"
        html_body = render_template_string(
            '''
            <h1>Verify Your Email Address</h1>
            <p>Click the link below to verify your email:</p>
            <a href="{{ verify_url }}">Verify Email</a>
            ''',
            verify_url=verify_url
        )
        return self.send_email(user_email, subject, html_body=html_body)

    def send_notification_email(self, user_email, notification_data):
        """Send notification email"""
        subject = notification_data.get('subject', 'Notification')
        html_body = render_template_string(
            '''
            <h1>{{ title }}</h1>
            <p>{{ message }}</p>
            {{ content|safe }}
            ''',
            title=notification_data.get('title'),
            message=notification_data.get('message'),
            content=notification_data.get('html_content', '')
        )
        return self.send_email(user_email, subject, html_body=html_body)

# routes.py
from flask import Blueprint, request, jsonify
from email_service import EmailService

email_bp = Blueprint('email', __name__)
email_service = EmailService()

@email_bp.route('/api/auth/send-verification', methods=['POST'])
def send_verification():
    """Send verification email"""
    data = request.json
    user_email = data.get('email')
    verification_token = generate_token()

    success = email_service.send_verification_email(user_email, verification_token)

    if success:
        # Store token in database
        VerificationToken.create(email=user_email, token=verification_token)
        return jsonify({'message': 'Verification email sent'}), 200
    else:
        return jsonify({'error': 'Failed to send email'}), 500

@email_bp.route('/api/auth/send-reset', methods=['POST'])
def send_reset():
    """Send password reset email"""
    data = request.json
    user = User.query.filter_by(email=data['email']).first()

    if not user:
        # Don't reveal if email exists
        return jsonify({'message': 'If email exists, reset link sent'}), 200

    reset_token = generate_token()
    success = email_service.send_password_reset_email(user.email, reset_token)

    if success:
        ResetToken.create(user_id=user.id, token=reset_token)
        return jsonify({'message': 'Reset email sent'}), 200
    else:
        return jsonify({'error': 'Failed to send email'}), 500
```

### 2. **Node.js with SendGrid**

```javascript
// email-service.js
const sgMail = require('@sendgrid/mail');
const logger = require('./logger');

sgMail.setApiKey(process.env.SENDGRID_API_KEY);

class EmailService {
    async sendEmail(to, subject, htmlContent, textContent = null) {
        try {
            const msg = {
                to: Array.isArray(to) ? to : [to],
                from: process.env.MAIL_FROM || 'noreply@example.com',
                subject: subject,
                html: htmlContent,
                ...(textContent && { text: textContent })
            };

            const result = await sgMail.send(msg);
            logger.info(`Email sent to ${to}: ${subject}`);
            return { success: true, messageId: result[0].headers['x-message-id'] };
        } catch (error) {
            logger.error(`Failed to send email: ${error.message}`);
            return { success: false, error: error.message };
        }
    }

    async sendWelcomeEmail(to, userName) {
        const htmlContent = `
            <h1>Welcome, ${userName}!</h1>
            <p>Thank you for joining us.</p>
            <a href="https://example.com/dashboard">Start Exploring</a>
        `;

        return this.sendEmail(to, 'Welcome to Our Platform!', htmlContent);
    }

    async sendPasswordResetEmail(to, resetToken) {
        const resetUrl = `https://example.com/reset-password?token=${resetToken}`;
        const htmlContent = `
            <h1>Reset Your Password</h1>
            <p>Click the link below to reset your password:</p>
            <a href="${resetUrl}">Reset Password</a>
            <p>This link expires in 24 hours.</p>
        `;

        return this.sendEmail(to, 'Reset Your Password', htmlContent);
    }

    async sendVerificationEmail(to, verificationToken) {
        const verifyUrl = `https://example.com/verify-email?token=${verificationToken}`;
        const htmlContent = `
            <h1>Verify Your Email</h1>
            <p>Click the link below to verify your email:</p>
            <a href="${verifyUrl}">Verify Email</a>
        `;

        return this.sendEmail(to, 'Verify Your Email', htmlContent);
    }

    async sendBulkEmails(recipients, subject, htmlContent) {
        try {
            const personalizations = recipients.map(recipient => ({
                to: [{ email: recipient.email }],
                substitutions: {
                    '-name-': recipient.name
                }
            }));

            const msg = {
                personalizations: personalizations,
                from: process.env.MAIL_FROM || 'noreply@example.com',
                subject: subject,
                html: htmlContent
            };

            const result = await sgMail.send(msg);
            logger.info(`Bulk email sent to ${recipients.length} recipients`);
            return { success: true, sent: recipients.length };
        } catch (error) {
            logger.error(`Bulk email failed: ${error.message}`);
            return { success: false, error: error.message };
        }
    }
}

module.exports = new EmailService();

// routes.js
const express = require('express');
const emailService = require('../services/email-service');
const { generateToken } = require('../utils/token');

const router = express.Router();

router.post('/send-verification', async (req, res) => {
    try {
        const { email } = req.body;

        if (!email) {
            return res.status(400).json({ error: 'Email required' });
        }

        const verificationToken = generateToken();
        const result = await emailService.sendVerificationEmail(email, verificationToken);

        if (result.success) {
            // Store token in database
            await VerificationToken.create({ email, token: verificationToken });
            return res.json({ message: 'Verification email sent' });
        } else {
            return res.status(500).json({ error: 'Failed to send email' });
        }
    } catch (error) {
        logger.error(error);
        res.status(500).json({ error: 'Internal server error' });
    }
});

router.post('/send-reset', async (req, res) => {
    try {
        const { email } = req.body;

        const user = await User.findOne({ where: { email } });
        if (!user) {
            return res.json({ message: 'If email exists, reset link sent' });
        }

        const resetToken = generateToken();
        const result = await emailService.sendPasswordResetEmail(email, resetToken);

        if (result.success) {
            await ResetToken.create({ userId: user.id, token: resetToken });
            return res.json({ message: 'Reset email sent' });
        } else {
            return res.status(500).json({ error: 'Failed to send email' });
        }
    } catch (error) {
        res.status(500).json({ error: 'Internal server error' });
    }
});

module.exports = router;
```

### 3. **Email Templates with Mjml**

```html
<!-- templates/welcome.mjml -->
<mjml>
  <mj-body>
    <mj-container>
      <mj-section>
        <mj-column>
          <mj-image width="100px" src="https://example.com/logo.png"></mj-image>
        </mj-column>
      </mj-section>

      <mj-section background-color="#f4f4f4">
        <mj-column>
          <mj-text font-size="24px" align="center" color="#333">
            Welcome, {{ userName }}!
          </mj-text>
          <mj-text align="center" color="#666">
            Thank you for joining us. Let's get started!
          </mj-text>
        </mj-column>
      </mj-section>

      <mj-section>
        <mj-column>
          <mj-button href="https://example.com/dashboard" background-color="#007bff">
            Go to Dashboard
          </mj-button>
        </mj-column>
      </mj-section>

      <mj-section>
        <mj-column>
          <mj-text font-size="12px" align="center" color="#999">
            © 2024 Example Inc. All rights reserved.
          </mj-text>
        </mj-column>
      </mj-section>
    </mj-container>
  </mj-body>
</mjml>

<!-- Python template compilation -->
# email_templates.py
from mjml import mjml_to_html

def get_welcome_template(user_name):
    with open('templates/welcome.mjml', 'r') as f:
        mjml_content = f.read()

    mjml_content = mjml_content.replace('{{ userName }}', user_name)
    html = mjml_to_html(mjml_content)
    return html
```

### 4. **FastAPI Email with Background Tasks**

```python
# email_service.py
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    mail_server=os.getenv("MAIL_SERVER"),
    mail_port=int(os.getenv("MAIL_PORT")),
    mail_from=os.getenv("MAIL_FROM"),
    mail_password=os.getenv("MAIL_PASSWORD"),
    mail_from_name=os.getenv("MAIL_FROM_NAME", "Example App"),
    use_credentials=True,
    validate_certs=True
)

fm = FastMail(conf)

class EmailService:
    @staticmethod
    async def send_email(
        recipients: list,
        subject: str,
        body: str,
        background_tasks: BackgroundTasks = None
    ):
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype="html"
        )

        if background_tasks:
            background_tasks.add_task(fm.send_message, message)
        else:
            await fm.send_message(message)

    @staticmethod
    async def send_welcome_email(
        email: str,
        name: str,
        background_tasks: BackgroundTasks
    ):
        html_body = f"""
        <h1>Welcome, {name}!</h1>
        <p>Thank you for joining us.</p>
        <a href="https://example.com/dashboard">Start Exploring</a>
        """

        await EmailService.send_email(
            recipients=[email],
            subject="Welcome to Our Platform!",
            body=html_body,
            background_tasks=background_tasks
        )

# routes.py
from fastapi import BackgroundTasks
from email_service import EmailService

@app.post("/api/send-email")
async def send_email(
    email: str,
    background_tasks: BackgroundTasks
):
    await EmailService.send_welcome_email(email, "User", background_tasks)
    return {"message": "Email queued for sending"}
```

### 5. **Email Validation and Verification**

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

## Complete Example

```python
@app.post("/register")
async def register(
    email: str,
    password: str,
    background_tasks: BackgroundTasks
):
    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()

    background_tasks.add_task(
        send_verification_email,
        email=user.email,
        token=generate_token()
    )

    return {"message": "User registered. Check email to verify."}
```
