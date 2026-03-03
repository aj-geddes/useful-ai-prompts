# Mocking & Test Doubles

## Mocking & Test Doubles

### Mock External Dependencies

```javascript
// Mock database
const mockDatabase = {
  save: jest.fn().mockResolvedValue({ id: "123" }),
  findById: jest.fn().mockResolvedValue({ id: "123", name: "John" }),
  delete: jest.fn().mockResolvedValue(true),
};

// Mock HTTP client
jest.mock("axios");
axios.get.mockResolvedValue({ data: { users: [] } });

// Spy on methods
const spy = jest.spyOn(userService, "sendEmail");
expect(spy).toHaveBeenCalledWith("john@example.com", "Welcome");
```

### Python Mocking

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
