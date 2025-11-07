---
name: unit-testing-framework
description: Write comprehensive unit tests with high coverage using testing frameworks like Jest, pytest, JUnit, or RSpec. Use when writing tests for functions, classes, components, or establishing testing standards.
---

# Unit Testing Framework

## Overview

Write effective unit tests that are fast, isolated, readable, and maintainable following industry best practices and AAA (Arrange-Act-Assert) pattern.

## When to Use

- Writing tests for new code
- Improving test coverage
- Establishing testing standards
- Refactoring with test safety
- Implementing TDD (Test-Driven Development)
- Creating test utilities and mocks

## Instructions

### 1. **Test Structure (AAA Pattern)**

```javascript
// Jest/JavaScript example
describe('UserService', () => {
  describe('createUser', () => {
    it('should create user with valid data', async () => {
      // Arrange - Set up test data and dependencies
      const userData = {
        email: 'john@example.com',
        firstName: 'John',
        lastName: 'Doe'
      };
      const mockDatabase = createMockDatabase();
      const service = new UserService(mockDatabase);

      // Act - Execute the function being tested
      const result = await service.createUser(userData);

      // Assert - Verify the outcome
      expect(result.id).toBeDefined();
      expect(result.email).toBe('john@example.com');
      expect(mockDatabase.save).toHaveBeenCalledWith(
        expect.objectContaining(userData)
      );
    });
  });
});
```

### 2. **Test Cases by Language**

#### JavaScript/TypeScript (Jest)
```typescript
import { Calculator } from './calculator';

describe('Calculator', () => {
  let calculator: Calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  describe('add', () => {
    it('should add two positive numbers', () => {
      expect(calculator.add(2, 3)).toBe(5);
    });

    it('should handle negative numbers', () => {
      expect(calculator.add(-2, 3)).toBe(1);
      expect(calculator.add(-2, -3)).toBe(-5);
    });

    it('should handle zero', () => {
      expect(calculator.add(0, 5)).toBe(5);
      expect(calculator.add(5, 0)).toBe(5);
    });
  });

  describe('divide', () => {
    it('should divide numbers correctly', () => {
      expect(calculator.divide(10, 2)).toBe(5);
    });

    it('should throw error when dividing by zero', () => {
      expect(() => calculator.divide(10, 0)).toThrow('Division by zero');
    });

    it('should handle decimal results', () => {
      expect(calculator.divide(10, 3)).toBeCloseTo(3.333, 2);
    });
  });
});
```

#### Python (pytest)
```python
import pytest
from user_service import UserService, ValidationError

class TestUserService:
    @pytest.fixture
    def service(self, mock_database):
        """Fixture to create UserService instance"""
        return UserService(mock_database)

    @pytest.fixture
    def valid_user_data(self):
        return {
            'email': 'john@example.com',
            'first_name': 'John',
            'last_name': 'Doe'
        }

    def test_create_user_with_valid_data(self, service, valid_user_data):
        """Should create user with valid input"""
        # Act
        user = service.create_user(valid_user_data)

        # Assert
        assert user.id is not None
        assert user.email == 'john@example.com'
        assert user.first_name == 'John'

    def test_create_user_with_invalid_email(self, service):
        """Should raise ValidationError for invalid email"""
        invalid_data = {'email': 'invalid', 'first_name': 'John'}

        with pytest.raises(ValidationError) as exc_info:
            service.create_user(invalid_data)

        assert 'email' in str(exc_info.value)

    @pytest.mark.parametrize('email,expected', [
        ('user@example.com', True),
        ('invalid', False),
        ('', False),
        (None, False),
    ])
    def test_email_validation(self, service, email, expected):
        """Should validate email formats correctly"""
        assert service.validate_email(email) == expected
```

#### Java (JUnit 5)
```java
import org.junit.jupiter.api.*;
import static org.junit.jupiter.api.Assertions.*;
import static org.mockito.Mockito.*;

class UserServiceTest {
    private UserService userService;
    private UserRepository mockRepository;

    @BeforeEach
    void setUp() {
        mockRepository = mock(UserRepository.class);
        userService = new UserService(mockRepository);
    }

    @Test
    @DisplayName("Should create user with valid data")
    void testCreateUserWithValidData() {
        // Arrange
        UserDto userDto = new UserDto("john@example.com", "John", "Doe");
        User savedUser = new User(1L, "john@example.com", "John", "Doe");
        when(mockRepository.save(any(User.class))).thenReturn(savedUser);

        // Act
        User result = userService.createUser(userDto);

        // Assert
        assertNotNull(result.getId());
        assertEquals("john@example.com", result.getEmail());
        verify(mockRepository, times(1)).save(any(User.class));
    }

    @Test
    @DisplayName("Should throw ValidationException for invalid email")
    void testCreateUserWithInvalidEmail() {
        UserDto userDto = new UserDto("invalid", "John", "Doe");

        ValidationException exception = assertThrows(
            ValidationException.class,
            () -> userService.createUser(userDto)
        );

        assertTrue(exception.getMessage().contains("email"));
    }

    @ParameterizedTest
    @ValueSource(strings = {"user@example.com", "test@domain.co.uk"})
    @DisplayName("Should validate correct email formats")
    void testValidEmailFormats(String email) {
        assertTrue(userService.validateEmail(email));
    }

    @ParameterizedTest
    @ValueSource(strings = {"invalid", "", "no-at-sign.com"})
    @DisplayName("Should reject invalid email formats")
    void testInvalidEmailFormats(String email) {
        assertFalse(userService.validateEmail(email));
    }
}
```

### 3. **Mocking & Test Doubles**

#### Mock External Dependencies
```javascript
// Mock database
const mockDatabase = {
  save: jest.fn().mockResolvedValue({ id: '123' }),
  findById: jest.fn().mockResolvedValue({ id: '123', name: 'John' }),
  delete: jest.fn().mockResolvedValue(true)
};

// Mock HTTP client
jest.mock('axios');
axios.get.mockResolvedValue({ data: { users: [] } });

// Spy on methods
const spy = jest.spyOn(userService, 'sendEmail');
expect(spy).toHaveBeenCalledWith('john@example.com', 'Welcome');
```

#### Python Mocking
```python
from unittest.mock import Mock, patch, MagicMock

def test_send_email(mocker):
    """Test email sending with mocked SMTP"""
    # Mock the SMTP client
    mock_smtp = mocker.patch('smtplib.SMTP')
    service = EmailService()

    # Act
    service.send_email('test@example.com', 'Subject', 'Body')

    # Assert
    mock_smtp.return_value.send_message.assert_called_once()

@patch('requests.get')
def test_fetch_user_data(mock_get):
    """Test API call with mocked requests"""
    mock_get.return_value.json.return_value = {'id': 1, 'name': 'John'}

    user = fetch_user_data(1)

    assert user['name'] == 'John'
    mock_get.assert_called_with('https://api.example.com/users/1')
```

### 4. **Testing Async Code**

```javascript
// Jest async/await
it('should fetch user data', async () => {
  const user = await fetchUser('123');
  expect(user.id).toBe('123');
});

// Testing promises
it('should resolve with user data', () => {
  return fetchUser('123').then(user => {
    expect(user.id).toBe('123');
  });
});

// Testing rejection
it('should reject with error for invalid ID', async () => {
  await expect(fetchUser('invalid')).rejects.toThrow('User not found');
});
```

### 5. **Test Coverage**

```bash
# JavaScript (Jest)
npm test -- --coverage

# Python (pytest with coverage)
pytest --cov=src --cov-report=html

# Java (Maven)
mvn test jacoco:report
```

**Coverage Goals:**
- **Statements**: 80%+ covered
- **Branches**: 75%+ covered
- **Functions**: 85%+ covered
- **Lines**: 80%+ covered

### 6. **Testing Edge Cases**

```javascript
describe('Edge Cases', () => {
  it('should handle null input', () => {
    expect(processData(null)).toBeNull();
  });

  it('should handle undefined input', () => {
    expect(processData(undefined)).toBeUndefined();
  });

  it('should handle empty string', () => {
    expect(processData('')).toBe('');
  });

  it('should handle empty array', () => {
    expect(processData([])).toEqual([]);
  });

  it('should handle large numbers', () => {
    expect(calculate(Number.MAX_SAFE_INTEGER)).toBeDefined();
  });

  it('should handle special characters', () => {
    expect(sanitize('<script>alert("xss")</script>'))
      .toBe('&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;');
  });
});
```

## Best Practices

### ✅ DO
- Write tests before or alongside code (TDD)
- Test one thing per test
- Use descriptive test names
- Follow AAA pattern
- Test edge cases and error conditions
- Keep tests isolated and independent
- Use setup/teardown appropriately
- Mock external dependencies
- Aim for high coverage on critical paths
- Make tests fast (< 10ms each)
- Use parameterized tests for similar cases
- Test public interfaces, not implementation

### ❌ DON'T
- Test implementation details
- Write tests that depend on each other
- Ignore failing tests
- Test third-party library code
- Use real databases/APIs in unit tests
- Make tests too complex
- Skip edge cases
- Forget to clean up resources
- Test everything (focus on business logic)
- Write flaky tests

## Test Organization

```
src/
├── components/
│   ├── UserProfile.tsx
│   └── __tests__/
│       └── UserProfile.test.tsx
├── services/
│   ├── UserService.ts
│   └── __tests__/
│       ├── UserService.test.ts
│       └── fixtures/
│           └── users.json
└── utils/
    ├── validation.ts
    └── __tests__/
        └── validation.test.ts
```

## Common Assertions

### Jest
```javascript
expect(value).toBe(expected);              // Strict equality
expect(value).toEqual(expected);           // Deep equality
expect(value).toBeTruthy();                // Truthy check
expect(value).toBeDefined();               // Not undefined
expect(value).toBeNull();                  // Null check
expect(value).toContain(item);             // Array/string contains
expect(value).toMatch(/pattern/);          // Regex match
expect(fn).toThrow(Error);                 // Throws error
expect(fn).toHaveBeenCalled();             // Mock called
expect(fn).toHaveBeenCalledWith(arg);      // Mock called with args
```

### pytest
```python
assert value == expected
assert value is True
assert value is not None
assert item in collection
assert pattern in string
with pytest.raises(Exception):
    risky_function()
assert mock.called
assert mock.call_count == 2
```

## Example: Complete Test Suite

```typescript
// user-service.test.ts
import { UserService } from './user-service';
import { Database } from './database';
import { EmailService } from './email-service';

// Mock dependencies
jest.mock('./database');
jest.mock('./email-service');

describe('UserService', () => {
  let userService: UserService;
  let mockDatabase: jest.Mocked<Database>;
  let mockEmailService: jest.Mocked<EmailService>;

  beforeEach(() => {
    mockDatabase = new Database() as jest.Mocked<Database>;
    mockEmailService = new EmailService() as jest.Mocked<EmailService>;
    userService = new UserService(mockDatabase, mockEmailService);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe('createUser', () => {
    const validUserData = {
      email: 'john@example.com',
      firstName: 'John',
      lastName: 'Doe'
    };

    it('should create user successfully', async () => {
      // Arrange
      const savedUser = { id: '123', ...validUserData };
      mockDatabase.save.mockResolvedValue(savedUser);

      // Act
      const result = await userService.createUser(validUserData);

      // Assert
      expect(result).toEqual(savedUser);
      expect(mockDatabase.save).toHaveBeenCalledWith(
        expect.objectContaining(validUserData)
      );
      expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith(
        validUserData.email
      );
    });

    it('should throw ValidationError for invalid email', async () => {
      const invalidData = { ...validUserData, email: 'invalid' };

      await expect(userService.createUser(invalidData))
        .rejects
        .toThrow('Invalid email format');

      expect(mockDatabase.save).not.toHaveBeenCalled();
    });

    it('should handle database errors', async () => {
      mockDatabase.save.mockRejectedValue(new Error('DB Error'));

      await expect(userService.createUser(validUserData))
        .rejects
        .toThrow('Failed to create user');
    });

    it('should continue even if welcome email fails', async () => {
      const savedUser = { id: '123', ...validUserData };
      mockDatabase.save.mockResolvedValue(savedUser);
      mockEmailService.sendWelcomeEmail.mockRejectedValue(
        new Error('Email failed')
      );

      const result = await userService.createUser(validUserData);

      expect(result).toEqual(savedUser);
      // User still created even though email failed
    });
  });

  describe('getUserById', () => {
    it('should return user when found', async () => {
      const user = { id: '123', email: 'john@example.com' };
      mockDatabase.findById.mockResolvedValue(user);

      const result = await userService.getUserById('123');

      expect(result).toEqual(user);
    });

    it('should throw NotFoundError when user not found', async () => {
      mockDatabase.findById.mockResolvedValue(null);

      await expect(userService.getUserById('999'))
        .rejects
        .toThrow('User not found');
    });
  });
});
```

## Resources

- **Jest**: https://jestjs.io/docs/getting-started
- **pytest**: https://docs.pytest.org/
- **JUnit 5**: https://junit.org/junit5/docs/current/user-guide/
- **Mocha**: https://mochajs.org/
- **RSpec**: https://rspec.info/
