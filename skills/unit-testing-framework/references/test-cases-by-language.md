# Test Cases by Language

## Test Cases by Language

### JavaScript/TypeScript (Jest)

```typescript
import { Calculator } from "./calculator";

describe("Calculator", () => {
  let calculator: Calculator;

  beforeEach(() => {
    calculator = new Calculator();
  });

  describe("add", () => {
    it("should add two positive numbers", () => {
      expect(calculator.add(2, 3)).toBe(5);
    });

    it("should handle negative numbers", () => {
      expect(calculator.add(-2, 3)).toBe(1);
      expect(calculator.add(-2, -3)).toBe(-5);
    });

    it("should handle zero", () => {
      expect(calculator.add(0, 5)).toBe(5);
      expect(calculator.add(5, 0)).toBe(5);
    });
  });

  describe("divide", () => {
    it("should divide numbers correctly", () => {
      expect(calculator.divide(10, 2)).toBe(5);
    });

    it("should throw error when dividing by zero", () => {
      expect(() => calculator.divide(10, 0)).toThrow("Division by zero");
    });

    it("should handle decimal results", () => {
      expect(calculator.divide(10, 3)).toBeCloseTo(3.333, 2);
    });
  });
});
```

### Python (pytest)

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

### Java (JUnit 5)

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
