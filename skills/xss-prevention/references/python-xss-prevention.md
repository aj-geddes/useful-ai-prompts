# Python XSS Prevention

## Python XSS Prevention

```python
# xss_prevention.py
import html
import bleach
from urllib.parse import urlparse, quote
import re

class XSSPrevention:
    # Allowed HTML tags for rich content
    ALLOWED_TAGS = [
        'p', 'br', 'strong', 'em', 'u', 'h1', 'h2', 'h3',
        'ul', 'ol', 'li', 'a', 'blockquote', 'code'
    ]

    ALLOWED_ATTRIBUTES = {
        'a': ['href', 'title'],
        'img': ['src', 'alt']
    }

    @staticmethod
    def encode_html(text: str) -> str:
        """HTML entity encoding - safest for text content"""
        return html.escape(text, quote=True)

    @staticmethod
    def sanitize_html(dirty_html: str) -> str:
        """Sanitize HTML - for rich content"""
        return bleach.clean(
            dirty_html,
            tags=XSSPrevention.ALLOWED_TAGS,
            attributes=XSSPrevention.ALLOWED_ATTRIBUTES,
            strip=True
        )

    @staticmethod
    def sanitize_strict(dirty_html: str) -> str:
        """Strict sanitization - strip all HTML"""
        return bleach.clean(
            dirty_html,
            tags=[],
            attributes={},
            strip=True
        )

    @staticmethod
    def strip_html(text: str) -> str:
        """Remove all HTML tags"""
        return re.sub(r'<[^>]*>', '', text)

    @staticmethod
    def sanitize_url(url: str) -> str:
        """Validate and sanitize URLs"""
        try:
            parsed = urlparse(url)

            # Only allow safe protocols
            if parsed.scheme not in ['http', 'https', 'mailto']:
                return ''

            return url
        except:
            return ''

    @staticmethod
    def encode_for_javascript(text: str) -> str:
        """Encode for JavaScript context"""
        escape_map = {
            '<': '\\x3C',
            '>': '\\x3E',
            '"': '\\x22',
            "'": '\\x27',
            '&': '\\x26',
            '/': '\\x2F'
        }

        return ''.join(escape_map.get(char, char) for char in text)

    @staticmethod
    def encode_url_param(text: str) -> str:
        """Encode for URL parameters"""
        return quote(text, safe='')

# Flask integration
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)

def sanitize_input(f):
    """Decorator to sanitize all request inputs"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if request.is_json:
            data = request.get_json()
            request._cached_json = sanitize_dict(data)

        return f(*args, **kwargs)

    return decorated_function

def sanitize_dict(data: dict) -> dict:
    """Recursively sanitize dictionary values"""
    sanitized = {}

    for key, value in data.items():
        if isinstance(value, str):
            sanitized[key] = XSSPrevention.strip_html(value)
        elif isinstance(value, dict):
            sanitized[key] = sanitize_dict(value)
        elif isinstance(value, list):
            sanitized[key] = [
                sanitize_dict(item) if isinstance(item, dict)
                else XSSPrevention.strip_html(item) if isinstance(item, str)
                else item
                for item in value
            ]
        else:
            sanitized[key] = value

    return sanitized

@app.route('/api/comments', methods=['POST'])
@sanitize_input
def create_comment():
    data = request.get_json()
    comment = data.get('comment', '')

    # Additional rich content sanitization
    safe_comment = XSSPrevention.sanitize_html(comment)

    return jsonify({'comment': safe_comment})

# Django template filter
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='sanitize_html')
def sanitize_html_filter(value):
    """Django template filter for HTML sanitization"""
    sanitized = XSSPrevention.sanitize_html(value)
    return mark_safe(sanitized)

# Usage in templates:
# {{ user_content|sanitize_html }}
```
