# Database Integration Testing

## Database Integration Testing

### Spring Boot with JUnit

```java
// src/test/java/com/example/integration/UserRepositoryIntegrationTest.java
@SpringBootTest
@AutoConfigureTestDatabase(replace = AutoConfigureTestDatabase.Replace.NONE)
@TestPropertySource(locations = "classpath:application-test.properties")
class UserRepositoryIntegrationTest {

    @Autowired
    private UserRepository userRepository;

    @Autowired
    private OrderRepository orderRepository;

    @Autowired
    private TestEntityManager entityManager;

    @BeforeEach
    void setUp() {
        orderRepository.deleteAll();
        userRepository.deleteAll();
    }

    @Test
    @Transactional
    void testSaveUserWithOrders() {
        // Given
        User user = new User();
        user.setEmail("test@example.com");
        user.setName("Test User");

        Order order1 = new Order();
        order1.setTotal(new BigDecimal("99.99"));
        order1.setUser(user);

        Order order2 = new Order();
        order2.setTotal(new BigDecimal("49.99"));
        order2.setUser(user);

        user.setOrders(Arrays.asList(order1, order2));

        // When
        User savedUser = userRepository.save(user);
        entityManager.flush();
        entityManager.clear();

        // Then
        User foundUser = userRepository.findById(savedUser.getId())
            .orElseThrow();

        assertThat(foundUser.getEmail()).isEqualTo("test@example.com");
        assertThat(foundUser.getOrders()).hasSize(2);
        assertThat(foundUser.getOrders())
            .extracting(Order::getTotal)
            .containsExactlyInAnyOrder(
                new BigDecimal("99.99"),
                new BigDecimal("49.99")
            );
    }

    @Test
    void testCustomQueryWithJoins() {
        // Given
        User user = createTestUser("test@example.com");
        createTestOrder(user, new BigDecimal("150.00"));

        // When
        List<User> highValueUsers = userRepository
            .findUsersWithOrdersAbove(new BigDecimal("100.00"));

        // Then
        assertThat(highValueUsers).hasSize(1);
        assertThat(highValueUsers.get(0).getEmail())
            .isEqualTo("test@example.com");
    }
}
```
