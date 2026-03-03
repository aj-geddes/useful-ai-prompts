# Python Zero Trust Policy Engine

## Python Zero Trust Policy Engine

```python
# zero_trust_policy.py
from dataclasses import dataclass
from typing import List, Dict, Any
from datetime import datetime
import jwt

@dataclass
class ZeroTrustContext:
    user_id: str
    device_id: str
    location: Dict[str, Any]
    risk_score: int
    timestamp: datetime

class ZeroTrustPolicy:
    def __init__(self):
        self.policies = self.load_policies()

    def load_policies(self) -> List[Dict]:
        """Load Zero Trust policies"""
        return [
            {
                'name': 'high_risk_block',
                'condition': lambda ctx: ctx.risk_score >= 8,
                'action': 'deny',
                'reason': 'High risk score'
            },
            {
                'name': 'require_mfa',
                'condition': lambda ctx: ctx.risk_score >= 5,
                'action': 'step_up_auth',
                'reason': 'Elevated risk requires MFA'
            },
            {
                'name': 'untrusted_device',
                'condition': lambda ctx: not self.is_device_trusted(ctx.device_id),
                'action': 'deny',
                'reason': 'Untrusted device'
            },
            {
                'name': 'unusual_location',
                'condition': lambda ctx: self.is_unusual_location(ctx),
                'action': 'step_up_auth',
                'reason': 'Unusual location detected'
            }
        ]

    def evaluate(self, context: ZeroTrustContext, resource: str, action: str) -> Dict:
        """Evaluate Zero Trust policies"""
        for policy in self.policies:
            if policy['condition'](context):
                return {
                    'allowed': policy['action'] != 'deny',
                    'action': policy['action'],
                    'reason': policy['reason'],
                    'policy': policy['name']
                }

        # Check resource-specific permissions
        if self.has_permission(context.user_id, resource, action):
            return {
                'allowed': True,
                'action': 'allow',
                'reason': 'User has required permissions'
            }

        return {
            'allowed': False,
            'action': 'deny',
            'reason': 'No matching policy allows access'
        }

    def is_device_trusted(self, device_id: str) -> bool:
        # Check device trust status
        return True

    def is_unusual_location(self, context: ZeroTrustContext) -> bool:
        # Check if location is unusual for user
        return False

    def has_permission(self, user_id: str, resource: str, action: str) -> bool:
        # Check user permissions
        return False

# Flask integration
from flask import Flask, request, jsonify, g
from functools import wraps

app = Flask(__name__)
zt_policy = ZeroTrustPolicy()

def zero_trust_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Build Zero Trust context
        context = ZeroTrustContext(
            user_id=g.user_id,
            device_id=request.headers.get('X-Device-ID', 'unknown'),
            location={
                'ip': request.remote_addr,
                'country': 'US'  # From GeoIP
            },
            risk_score=calculate_risk_score(request),
            timestamp=datetime.utcnow()
        )

        # Evaluate policies
        result = zt_policy.evaluate(
            context,
            request.path,
            request.method
        )

        if not result['allowed']:
            return jsonify({
                'error': 'forbidden',
                'reason': result['reason'],
                'action_required': result['action']
            }), 403

        return f(*args, **kwargs)

    return decorated_function

def calculate_risk_score(request) -> int:
    """Calculate risk score based on request context"""
    score = 0

    # Check for suspicious patterns
    if not request.headers.get('X-Device-ID'):
        score += 2

    # Add more risk factors
    return min(score, 10)

@app.route('/api/sensitive', methods=['GET'])
@zero_trust_required
def get_sensitive_data():
    return jsonify({'data': 'sensitive information'})
```
