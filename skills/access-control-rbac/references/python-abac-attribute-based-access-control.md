# Python ABAC (Attribute-Based Access Control)

## Python ABAC (Attribute-Based Access Control)

```python
# abac_system.py
from typing import Dict, List, Callable, Any
from dataclasses import dataclass
from enum import Enum

class Effect(Enum):
    ALLOW = "allow"
    DENY = "deny"

@dataclass
class Policy:
    name: str
    effect: Effect
    resource: str
    action: str
    conditions: List[Callable[[Dict], bool]]

class ABACSystem:
    def __init__(self):
        self.policies: List[Policy] = []
        self.initialize_policies()

    def initialize_policies(self):
        """Initialize default policies"""

        # Allow users to read their own profile
        self.add_policy(Policy(
            name="read_own_profile",
            effect=Effect.ALLOW,
            resource="profile",
            action="read",
            conditions=[
                lambda ctx: ctx['user']['id'] == ctx['resource']['owner_id']
            ]
        ))

        # Allow users to update their own profile
        self.add_policy(Policy(
            name="update_own_profile",
            effect=Effect.ALLOW,
            resource="profile",
            action="update",
            conditions=[
                lambda ctx: ctx['user']['id'] == ctx['resource']['owner_id']
            ]
        ))

        # Allow admins to do anything
        self.add_policy(Policy(
            name="admin_all_access",
            effect=Effect.ALLOW,
            resource="*",
            action="*",
            conditions=[
                lambda ctx: 'admin' in ctx['user'].get('roles', [])
            ]
        ))

        # Allow managers to approve within their department
        self.add_policy(Policy(
            name="manager_department_approval",
            effect=Effect.ALLOW,
            resource="expense",
            action="approve",
            conditions=[
                lambda ctx: 'manager' in ctx['user'].get('roles', []),
                lambda ctx: ctx['user']['department'] == ctx['resource']['department']
            ]
        ))

        # Deny access during maintenance window
        self.add_policy(Policy(
            name="maintenance_block",
            effect=Effect.DENY,
            resource="*",
            action="*",
            conditions=[
                lambda ctx: ctx.get('system', {}).get('maintenance_mode', False)
            ]
        ))

        # Time-based access control
        self.add_policy(Policy(
            name="business_hours_only",
            effect=Effect.DENY,
            resource="sensitive_data",
            action="*",
            conditions=[
                lambda ctx: ctx['time']['hour'] < 9 or ctx['time']['hour'] > 17
            ]
        ))

    def add_policy(self, policy: Policy):
        """Add a new policy"""
        self.policies.append(policy)

    def evaluate(self, context: Dict[str, Any], resource: str, action: str) -> bool:
        """Evaluate access request against policies"""

        # Default deny
        decision = False

        for policy in self.policies:
            # Check if policy applies
            if not self._matches(policy.resource, resource):
                continue

            if not self._matches(policy.action, action):
                continue

            # Evaluate conditions
            try:
                conditions_met = all(
                    condition(context) for condition in policy.conditions
                )
            except Exception as e:
                print(f"Error evaluating policy {policy.name}: {e}")
                conditions_met = False

            if not conditions_met:
                continue

            # Apply policy effect
            if policy.effect == Effect.ALLOW:
                decision = True
            elif policy.effect == Effect.DENY:
                # Deny always takes precedence
                return False

        return decision

    def _matches(self, pattern: str, value: str) -> bool:
        """Check if pattern matches value (supports wildcards)"""
        if pattern == "*":
            return True
        return pattern == value

    def can(self, user: Dict, resource: str, action: str,
            resource_data: Dict = None, system_context: Dict = None) -> bool:
        """Check if user can perform action on resource"""

        from datetime import datetime

        context = {
            'user': user,
            'resource': resource_data or {},
            'system': system_context or {},
            'time': {
                'hour': datetime.now().hour,
                'weekday': datetime.now().weekday()
            }
        }

        return self.evaluate(context, resource, action)

# Usage
if __name__ == '__main__':
    abac = ABACSystem()

    # Test cases
    user1 = {
        'id': 'user-123',
        'roles': ['user'],
        'department': 'engineering'
    }

    user2 = {
        'id': 'user-456',
        'roles': ['admin']
    }

    user3 = {
        'id': 'user-789',
        'roles': ['manager'],
        'department': 'engineering'
    }

    # Own profile access
    print("User can read own profile:",
          abac.can(user1, 'profile', 'read',
                   resource_data={'owner_id': 'user-123'}))

    # Other's profile access
    print("User can read other's profile:",
          abac.can(user1, 'profile', 'read',
                   resource_data={'owner_id': 'user-999'}))

    # Admin access
    print("Admin can update any profile:",
          abac.can(user2, 'profile', 'update',
                   resource_data={'owner_id': 'user-999'}))

    # Manager approval
    expense = {'department': 'engineering', 'amount': 1000}
    print("Manager can approve dept expense:",
          abac.can(user3, 'expense', 'approve', resource_data=expense))

    # Different department
    other_expense = {'department': 'sales', 'amount': 1000}
    print("Manager can approve other dept expense:",
          abac.can(user3, 'expense', 'approve', resource_data=other_expense))
```
