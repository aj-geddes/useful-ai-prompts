# Incremental Refactoring

## Incremental Refactoring

Apply refactoring patterns systematically:

### Extract Function/Method

```javascript
// BEFORE: Long, complex function
function processUserData(user) {
  // 50 lines of mixed validation, transformation, and business logic
  if (!user.email || !user.email.includes("@")) return null;
  const normalized = user.email.toLowerCase().trim();
  // ... more complex logic
}

// AFTER: Extracted, focused functions
function validateEmail(email) {
  return email && email.includes("@");
}

function normalizeEmail(email) {
  return email.toLowerCase().trim();
}

function processUserData(user) {
  if (!validateEmail(user.email)) return null;
  const email = normalizeEmail(user.email);
  // Clear, readable flow
}
```

### Replace Conditionals with Polymorphism

```python
# BEFORE: Complex conditional logic
def calculate_price(customer_type, base_price):
    if customer_type == 'regular':
        return base_price
    elif customer_type == 'premium':
        return base_price * 0.9
    elif customer_type == 'vip':
        return base_price * 0.8
    else:
        return base_price

# AFTER: Polymorphic approach
class PricingStrategy:
    def calculate(self, base_price):
        return base_price

class RegularPricing(PricingStrategy):
    pass

class PremiumPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price * 0.9

class VIPPricing(PricingStrategy):
    def calculate(self, base_price):
        return base_price * 0.8

# Usage
pricing = pricing_strategies[customer_type]
price = pricing.calculate(base_price)
```

### Introduce Parameter Object

```typescript
// BEFORE: Long parameter lists
function createUser(
  firstName: string,
  lastName: string,
  email: string,
  phone: string,
  address: string,
  city: string,
  state: string,
  zip: string,
) {
  // ...
}

// AFTER: Parameter object
interface UserData {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  address: Address;
}

interface Address {
  street: string;
  city: string;
  state: string;
  zip: string;
}

function createUser(userData: UserData) {
  // ...
}
```
