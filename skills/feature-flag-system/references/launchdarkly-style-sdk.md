# LaunchDarkly-Style SDK

## LaunchDarkly-Style SDK

```python
from typing import Dict, Any, Optional
import hashlib
import json

class FeatureFlagClient:
    def __init__(self, sdk_key: str, config: Optional[Dict] = None):
        self.sdk_key = sdk_key
        self.config = config or {}
        self.flags: Dict[str, Dict] = {}
        self.initialize()

    def initialize(self):
        """Load flags from API or cache."""
        # In production, fetch from API
        self.flags = {
            'new-feature': {
                'enabled': True,
                'rollout': {
                    'percentage': 50
                }
            },
            'premium-feature': {
                'enabled': True,
                'targeting': {
                    'attribute': 'plan',
                    'values': ['premium', 'enterprise']
                }
            }
        }

    def variation(
        self,
        flag_key: str,
        user: Dict[str, Any],
        default: bool = False
    ) -> bool:
        """Evaluate flag for user."""
        flag = self.flags.get(flag_key)

        if not flag or not flag.get('enabled'):
            return default

        # Check targeting rules
        if 'targeting' in flag:
            if not self._evaluate_targeting(flag['targeting'], user):
                return False

        # Check percentage rollout
        if 'rollout' in flag:
            return self._evaluate_rollout(flag['rollout'], user, flag_key)

        return True

    def variation_detail(
        self,
        flag_key: str,
        user: Dict[str, Any],
        default: Any = None
    ) -> Dict[str, Any]:
        """Get flag variation with details."""
        value = self.variation(flag_key, user, default)

        return {
            'value': value,
            'variation_index': 0 if value else 1,
            'reason': {
                'kind': 'RULE_MATCH' if value else 'OFF'
            }
        }

    def _evaluate_targeting(self, targeting: Dict, user: Dict) -> bool:
        """Evaluate targeting rules."""
        attribute = targeting.get('attribute')
        values = targeting.get('values', [])

        user_value = user.get(attribute)
        return user_value in values

    def _evaluate_rollout(
        self,
        rollout: Dict,
        user: Dict,
        flag_key: str
    ) -> bool:
        """Evaluate percentage rollout."""
        percentage = rollout.get('percentage', 0)
        user_id = user.get('id', user.get('email', 'anonymous'))

        # Consistent hashing for stable rollout
        hash_value = self._hash_user(user_id, flag_key)
        bucket = hash_value % 100

        return bucket < percentage

    def _hash_user(self, user_id: str, flag_key: str) -> int:
        """Hash user ID for consistent bucketing."""
        combined = f"{flag_key}:{user_id}"
        hash_bytes = hashlib.sha256(combined.encode()).digest()
        return int.from_bytes(hash_bytes[:4], byteorder='big')

    def track(self, event_name: str, user: Dict, data: Optional[Dict] = None):
        """Track custom event."""
        # Send to analytics
        pass

    def identify(self, user: Dict):
        """Identify user."""
        # Update user context
        pass

    def flush(self):
        """Flush events."""
        pass

    def close(self):
        """Close client."""
        pass


# Usage
client = FeatureFlagClient(sdk_key='your-sdk-key')

user = {
    'id': 'user-123',
    'email': 'user@example.com',
    'plan': 'premium'
}

# Check if feature is enabled
if client.variation('new-feature', user):
    print("New feature enabled!")

# Get detailed information
detail = client.variation_detail('premium-feature', user)
print(f"Value: {detail['value']}, Reason: {detail['reason']}")

# Track event
client.track('feature-used', user, {'feature': 'new-feature'})
```
