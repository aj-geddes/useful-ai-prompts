---
name: refactor-legacy-code
description: Modernize and improve legacy codebases while maintaining functionality. Use when you need to refactor old code, reduce technical debt, modernize deprecated patterns, or improve code maintainability without breaking existing behavior.
---

# Refactor Legacy Code

## Overview

This skill helps you systematically refactor legacy code to improve maintainability, readability, and performance while preserving existing functionality. It follows industry best practices for safe refactoring with comprehensive testing.

## When to Use

- Modernizing outdated code patterns or deprecated APIs
- Reducing technical debt in existing codebases
- Improving code readability and maintainability
- Extracting reusable components from monolithic code
- Upgrading to newer language features or frameworks
- Preparing code for new feature development

## Instructions

### 1. **Code Assessment**

First, analyze the legacy code to understand:

```bash
# Review the codebase structure
tree -L 3 -I 'node_modules|dist|build'

# Check for outdated dependencies
npm outdated  # or pip list --outdated, composer outdated, etc.

# Identify code complexity hotspots
# Use tools like:
# - SonarQube for code smells
# - eslint for JavaScript
# - pylint for Python
# - RuboCop for Ruby
```

**Assessment Checklist:**
- [ ] Identify deprecated patterns and APIs
- [ ] Locate tightly coupled components
- [ ] Find duplicated code blocks
- [ ] Review test coverage gaps
- [ ] Document current behavior and edge cases
- [ ] Identify performance bottlenecks

### 2. **Establish Safety Net**

Before refactoring, ensure you have comprehensive tests:

```javascript
// Add characterization tests to lock in current behavior
describe('LegacyFeature', () => {
  it('should preserve existing behavior during refactoring', () => {
    // Test current implementation behavior
    const input = { /* realistic test data */ };
    const result = legacyFunction(input);

    // Document expected output
    expect(result).toEqual({ /* current actual output */ });
  });
});
```

**Testing Strategy:**
- Add unit tests for critical paths
- Create integration tests for component interactions
- Document edge cases and error scenarios
- Set up test coverage monitoring
- Run tests before each refactoring step

### 3. **Incremental Refactoring**

Apply refactoring patterns systematically:

#### Extract Function/Method
```javascript
// BEFORE: Long, complex function
function processUserData(user) {
  // 50 lines of mixed validation, transformation, and business logic
  if (!user.email || !user.email.includes('@')) return null;
  const normalized = user.email.toLowerCase().trim();
  // ... more complex logic
}

// AFTER: Extracted, focused functions
function validateEmail(email) {
  return email && email.includes('@');
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

#### Replace Conditionals with Polymorphism
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

#### Introduce Parameter Object
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
  zip: string
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

### 4. **Modernize Patterns**

Replace outdated patterns with modern equivalents:

#### Promises over Callbacks
```javascript
// BEFORE: Callback hell
function fetchUserData(userId, callback) {
  db.query('SELECT * FROM users WHERE id = ?', [userId], (err, user) => {
    if (err) return callback(err);
    db.query('SELECT * FROM orders WHERE user_id = ?', [userId], (err, orders) => {
      if (err) return callback(err);
      callback(null, { user, orders });
    });
  });
}

// AFTER: Async/await
async function fetchUserData(userId) {
  const user = await db.query('SELECT * FROM users WHERE id = ?', [userId]);
  const orders = await db.query('SELECT * FROM orders WHERE user_id = ?', [userId]);
  return { user, orders };
}
```

#### Modern Language Features
```javascript
// BEFORE: var and string concatenation
var userName = user.firstName + ' ' + user.lastName;
var isActive = user.status === 'active' ? true : false;

// AFTER: const/let and template literals
const userName = `${user.firstName} ${user.lastName}`;
const isActive = user.status === 'active';
```

### 5. **Reduce Dependencies**

Break tight coupling:

```python
# BEFORE: Tight coupling to specific implementation
class OrderProcessor:
    def __init__(self):
        self.db = MySQLDatabase()  # Tightly coupled
        self.email = SendGridEmail()  # Tightly coupled

    def process_order(self, order):
        self.db.save(order)
        self.email.send(order.customer_email, "Order confirmed")

# AFTER: Dependency injection
class OrderProcessor:
    def __init__(self, database, email_service):
        self.db = database  # Any database implementation
        self.email = email_service  # Any email service

    def process_order(self, order):
        self.db.save(order)
        self.email.send(order.customer_email, "Order confirmed")

# Easy to test with mocks
processor = OrderProcessor(MockDatabase(), MockEmailService())
```

### 6. **Documentation**

Document refactoring decisions:

```markdown
## Refactoring Log

### 2025-01-15: Extract Payment Processing
**Rationale**: Payment logic was embedded in order controller (500 lines)
**Changes**:
- Extracted PaymentService with single responsibility
- Introduced PaymentGateway interface for flexibility
- Added comprehensive unit tests (95% coverage)
**Breaking Changes**: None (internal refactoring only)
**Performance Impact**: 15% improvement in order processing time

### 2025-01-16: Replace Callback with Async/Await
**Rationale**: Callback hell in user authentication flow
**Changes**:
- Converted all authentication methods to async/await
- Simplified error handling with try/catch
- Improved readability (reduced from 150 to 80 lines)
**Breaking Changes**: Function signatures changed (requires updates in calling code)
**Migration**: Updated all 12 call sites in controllers
```

## Best Practices

### ✅ DO

- **Refactor incrementally**: Small, testable changes
- **Run tests frequently**: After each refactoring step
- **Commit often**: Create logical, atomic commits
- **Keep existing tests passing**: Don't break functionality
- **Use IDE refactoring tools**: Safer than manual edits
- **Review code coverage**: Ensure tests cover refactored code
- **Document decisions**: Why, not just what
- **Seek peer review**: Fresh eyes catch issues

### ❌ DON'T

- **Mix refactoring with new features**: Separate concerns
- **Refactor without tests**: Recipe for breaking changes
- **Change behavior**: Refactoring should preserve functionality
- **Refactor large chunks**: Increases risk and review difficulty
- **Ignore code smells**: Address them systematically
- **Skip documentation**: Future maintainers need context

## Common Pitfalls

### 1. **Over-Engineering**
```javascript
// ❌ Too complex for simple case
class UserNameFormatterFactory {
  createFormatter(type) {
    return new UserNameFormatter(new FormattingStrategy(type));
  }
}

// ✅ Appropriate for simple case
function formatUserName(firstName, lastName) {
  return `${firstName} ${lastName}`;
}
```

### 2. **Premature Optimization**
Focus on readability first, then optimize bottlenecks identified by profiling.

### 3. **Breaking Backward Compatibility**
Use deprecation warnings before removing public APIs:

```typescript
/** @deprecated Use createUser(userData) instead. Will be removed in v2.0 */
function createUserOld(firstName: string, lastName: string, email: string) {
  console.warn('createUserOld is deprecated. Use createUser(userData)');
  return createUser({ firstName, lastName, email });
}
```

## Testing Strategy

### Unit Tests
```javascript
describe('Refactored User Service', () => {
  describe('validateEmail', () => {
    it('should accept valid email formats', () => {
      expect(validateEmail('user@example.com')).toBe(true);
    });

    it('should reject invalid email formats', () => {
      expect(validateEmail('invalid')).toBe(false);
      expect(validateEmail('')).toBe(false);
      expect(validateEmail(null)).toBe(false);
    });
  });
});
```

### Integration Tests
```python
def test_refactored_order_processing():
    """Ensure refactored code maintains end-to-end behavior"""
    # Arrange
    order = create_test_order()
    processor = OrderProcessor(test_database, test_email_service)

    # Act
    result = processor.process_order(order)

    # Assert
    assert result.status == 'completed'
    assert test_database.orders.count() == 1
    assert test_email_service.sent_count == 1
```

### Regression Tests
Run full test suite to ensure no unintended side effects.

## Refactoring Patterns Reference

### Common Patterns

1. **Extract Method/Function**: Break long functions into smaller ones
2. **Extract Class**: Group related functionality
3. **Inline Method**: Remove unnecessary indirection
4. **Move Method**: Place method in appropriate class
5. **Rename**: Use descriptive names
6. **Replace Magic Numbers**: Use named constants
7. **Replace Conditional with Polymorphism**: Use inheritance
8. **Introduce Parameter Object**: Group related parameters
9. **Remove Duplication**: DRY principle
10. **Simplify Conditional Logic**: Reduce complexity

## Tools & Resources

### Static Analysis Tools
- **JavaScript/TypeScript**: ESLint, TSLint, SonarQube
- **Python**: Pylint, Flake8, Bandit
- **Java**: SonarQube, PMD, Checkstyle
- **Ruby**: RuboCop, Reek
- **PHP**: PHPStan, Psalm

### IDE Refactoring Support
- **VS Code**: Built-in refactoring commands
- **JetBrains IDEs**: Comprehensive refactoring tools
- **Eclipse**: Automated refactorings
- **Vim/Neovim**: Language server refactoring actions

### Recommended Reading
- "Refactoring" by Martin Fowler
- "Working Effectively with Legacy Code" by Michael Feathers
- "Clean Code" by Robert C. Martin

## Examples

### Complete Refactoring Example

#### Before
```javascript
// legacy-user-service.js - 200 lines of complex, coupled code
var UserService = {
  createUser: function(fn, ln, em, ph, addr) {
    if (!em || em.indexOf('@') === -1) {
      return { error: 'Invalid email' };
    }
    var conn = mysql.createConnection(config);
    conn.connect();
    conn.query(
      'INSERT INTO users (first_name, last_name, email, phone, address) VALUES (?, ?, ?, ?, ?)',
      [fn, ln, em.toLowerCase(), ph, addr],
      function(err, result) {
        if (err) {
          console.log(err);
          return { error: 'Database error' };
        }
        // Send welcome email
        var nodemailer = require('nodemailer');
        var transporter = nodemailer.createTransport(emailConfig);
        transporter.sendMail({
          to: em,
          subject: 'Welcome!',
          html: '<h1>Welcome ' + fn + '!</h1>'
        }, function(err, info) {
          if (err) console.log(err);
        });
        conn.end();
        return { id: result.insertId };
      }
    );
  }
};
```

#### After
```typescript
// user-service.ts - Clean, testable, maintainable
interface UserData {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  address: string;
}

class UserService {
  constructor(
    private database: Database,
    private emailService: EmailService,
    private validator: Validator
  ) {}

  async createUser(userData: UserData): Promise<User> {
    this.validator.validateEmail(userData.email);

    const normalizedData = this.normalizeUserData(userData);
    const user = await this.database.users.create(normalizedData);

    await this.sendWelcomeEmail(user);

    return user;
  }

  private normalizeUserData(data: UserData): UserData {
    return {
      ...data,
      email: data.email.toLowerCase().trim()
    };
  }

  private async sendWelcomeEmail(user: User): Promise<void> {
    await this.emailService.send({
      to: user.email,
      subject: 'Welcome!',
      template: 'welcome',
      data: { firstName: user.firstName }
    });
  }
}

// validator.ts
class Validator {
  validateEmail(email: string): void {
    if (!email || !email.includes('@')) {
      throw new ValidationError('Invalid email format');
    }
  }
}

// Easy to test
describe('UserService', () => {
  it('should create user with valid data', async () => {
    const mockDb = createMockDatabase();
    const mockEmail = createMockEmailService();
    const service = new UserService(mockDb, mockEmail, new Validator());

    const user = await service.createUser({
      firstName: 'John',
      lastName: 'Doe',
      email: 'john@example.com',
      phone: '555-0123',
      address: '123 Main St'
    });

    expect(user.id).toBeDefined();
    expect(mockDb.users.create).toHaveBeenCalled();
    expect(mockEmail.send).toHaveBeenCalledWith(
      expect.objectContaining({ to: 'john@example.com' })
    );
  });
});
```

### Benefits Achieved
- ✅ **Testability**: Dependencies injected, easy to mock
- ✅ **Readability**: Clear, focused methods
- ✅ **Maintainability**: Single responsibility principle
- ✅ **Type Safety**: TypeScript interfaces prevent bugs
- ✅ **Reusability**: Components can be used independently
- ✅ **Error Handling**: Proper exception handling
- ✅ **Modern Patterns**: Async/await, dependency injection

## Checklist

Before considering refactoring complete:

- [ ] All existing tests pass
- [ ] New tests added for refactored code
- [ ] Code coverage maintained or improved
- [ ] No breaking changes to public APIs (or properly documented)
- [ ] Performance benchmarks show no regression
- [ ] Code review completed
- [ ] Documentation updated
- [ ] Refactoring decisions documented
- [ ] CI/CD pipeline passes
- [ ] Staged deployment to verify in production-like environment

## Support

For complex refactoring scenarios, consider:
- Seeking peer review early and often
- Using feature flags for gradual rollouts
- Creating a refactoring plan document
- Scheduling dedicated refactoring time
- Monitoring production metrics after deployment
