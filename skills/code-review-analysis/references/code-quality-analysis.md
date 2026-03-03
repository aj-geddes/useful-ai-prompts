# Code Quality Analysis

## Code Quality Analysis

### Readability

```python
# ❌ Poor readability
def p(u,o):
    return u['t']*o['q'] if u['s']=='a' else 0

# ✅ Good readability
def calculate_order_total(user: User, order: Order) -> float:
    """Calculate order total with user-specific pricing."""
    if user.status == 'active':
        return user.tier_price * order.quantity
    return 0
```

### Complexity

```javascript
// ❌ High cognitive complexity
function processData(data) {
  if (data) {
    if (data.type === "user") {
      if (data.status === "active") {
        if (data.permissions && data.permissions.length > 0) {
          // deeply nested logic
        }
      }
    }
  }
}

// ✅ Reduced complexity with early returns
function processData(data) {
  if (!data) return null;
  if (data.type !== "user") return null;
  if (data.status !== "active") return null;
  if (!data.permissions?.length) return null;

  // main logic at top level
}
```
