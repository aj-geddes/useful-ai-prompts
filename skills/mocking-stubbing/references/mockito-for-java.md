# Mockito for Java

## Mockito for Java

```java
// service/UserService.java
public class UserService {
    private final UserRepository userRepository;
    private final EmailService emailService;
    private final AuditLogger auditLogger;

    public UserService(
        UserRepository userRepository,
        EmailService emailService,
        AuditLogger auditLogger
    ) {
        this.userRepository = userRepository;
        this.emailService = emailService;
        this.auditLogger = auditLogger;
    }

    public User createUser(UserDto userDto) {
        User user = userRepository.save(mapToUser(userDto));
        emailService.sendWelcomeEmail(user.getEmail());
        auditLogger.log("User created: " + user.getId());
        return user;
    }

    public Optional<User> getUserWithOrders(Long userId) {
        return userRepository.findByIdWithOrders(userId);
    }
}

// test/UserServiceTest.java
import static org.mockito.Mockito.*;
import static org.junit.jupiter.api.Assertions.*;

@ExtendWith(MockitoExtension.class)
class UserServiceTest {

    @Mock
    private UserRepository userRepository;

    @Mock
    private EmailService emailService;

    @Mock
    private AuditLogger auditLogger;

    @InjectMocks
    private UserService userService;

    @Test
    void createUser_shouldSaveAndSendEmail() {
        // Arrange
        UserDto userDto = new UserDto("test@example.com", "Test User");
        User savedUser = new User(1L, "test@example.com", "Test User");

        when(userRepository.save(any(User.class))).thenReturn(savedUser);
        doNothing().when(emailService).sendWelcomeEmail(anyString());

        // Act
        User result = userService.createUser(userDto);

        // Assert
        assertNotNull(result);
        assertEquals(1L, result.getId());

        verify(userRepository, times(1)).save(any(User.class));
        verify(emailService, times(1)).sendWelcomeEmail("test@example.com");
        verify(auditLogger, times(1)).log(contains("User created"));
    }

    @Test
    void createUser_shouldThrowExceptionWhenEmailFails() {
        // Arrange
        UserDto userDto = new UserDto("test@example.com", "Test User");
        User savedUser = new User(1L, "test@example.com", "Test User");

        when(userRepository.save(any(User.class))).thenReturn(savedUser);
        doThrow(new EmailException("SMTP error"))
            .when(emailService)
            .sendWelcomeEmail(anyString());

        // Act & Assert
        assertThrows(EmailException.class, () -> {
            userService.createUser(userDto);
        });

        verify(userRepository).save(any(User.class));
        verify(emailService).sendWelcomeEmail("test@example.com");
    }

    @Test
    void getUserWithOrders_shouldReturnUserWhenExists() {
        // Arrange
        User user = new User(1L, "test@example.com", "Test User");
        when(userRepository.findByIdWithOrders(1L))
            .thenReturn(Optional.of(user));

        // Act
        Optional<User> result = userService.getUserWithOrders(1L);

        // Assert
        assertTrue(result.isPresent());
        assertEquals(user, result.get());

        verify(userRepository).findByIdWithOrders(1L);
    }

    @Test
    void getUserWithOrders_shouldReturnEmptyWhenNotExists() {
        // Arrange
        when(userRepository.findByIdWithOrders(999L))
            .thenReturn(Optional.empty());

        // Act
        Optional<User> result = userService.getUserWithOrders(999L);

        // Assert
        assertFalse(result.isPresent());
    }

    @Captor
    private ArgumentCaptor<User> userCaptor;

    @Test
    void createUser_shouldSaveUserWithCorrectData() {
        // Arrange
        UserDto userDto = new UserDto("test@example.com", "Test User");
        when(userRepository.save(any(User.class)))
            .thenReturn(new User(1L, "test@example.com", "Test User"));

        // Act
        userService.createUser(userDto);

        // Assert - Capture and verify the saved user
        verify(userRepository).save(userCaptor.capture());
        User capturedUser = userCaptor.getValue();

        assertEquals("test@example.com", capturedUser.getEmail());
        assertEquals("Test User", capturedUser.getName());
    }
}
```
