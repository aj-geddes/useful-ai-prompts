# Python/Flask with SMTP

## Python/Flask with SMTP

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
