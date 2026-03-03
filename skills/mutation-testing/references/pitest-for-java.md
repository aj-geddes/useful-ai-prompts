# PITest for Java

## PITest for Java

```xml
<!-- pom.xml -->
<plugin>
    <groupId>org.pitest</groupId>
    <artifactId>pitest-maven</artifactId>
    <version>1.14.2</version>
    <configuration>
        <targetClasses>
            <param>com.example.service.*</param>
        </targetClasses>
        <targetTests>
            <param>com.example.service.*Test</param>
        </targetTests>
        <mutators>
            <mutator>DEFAULTS</mutator>
        </mutators>
        <outputFormats>
            <outputFormat>HTML</outputFormat>
            <outputFormat>XML</outputFormat>
        </outputFormats>
        <timestampedReports>false</timestampedReports>
        <mutationThreshold>80</mutationThreshold>
        <coverageThreshold>90</coverageThreshold>
    </configuration>
</plugin>
```

```bash
# Run mutation testing
mvn org.pitest:pitest-maven:mutationCoverage
```

```java
// src/main/java/OrderValidator.java
public class OrderValidator {

    public boolean isValidOrder(Order order) {
        if (order == null) {
            return false;
        }

        if (order.getItems().isEmpty()) {
            return false;
        }

        if (order.getTotal() <= 0) {
            return false;
        }

        return true;
    }

    public double calculateDiscount(double total, String customerTier) {
        if (customerTier.equals("GOLD")) {
            return total * 0.2;
        } else if (customerTier.equals("SILVER")) {
            return total * 0.1;
        }
        return 0;
    }

    public int categorizeOrderSize(int itemCount) {
        if (itemCount <= 5) {
            return 1; // Small
        } else if (itemCount <= 20) {
            return 2; // Medium
        } else {
            return 3; // Large
        }
    }
}

// ❌ Weak tests that allow mutations to survive
@Test
public void testOrderValidation_Weak() {
    OrderValidator validator = new OrderValidator();

    Order order = new Order();
    order.addItem(new Item("Product", 10.0));
    order.setTotal(10.0);

    // Only tests one scenario
    assertTrue(validator.isValidOrder(order));
}

// ✅ Strong tests that kill mutations
public class OrderValidatorTest {

    private OrderValidator validator;

    @Before
    public void setUp() {
        validator = new OrderValidator();
    }

    @Test
    public void isValidOrder_withNullOrder_returnsFalse() {
        assertFalse(validator.isValidOrder(null));
    }

    @Test
    public void isValidOrder_withEmptyItems_returnsFalse() {
        Order order = new Order();
        order.setTotal(10.0);
        assertFalse(validator.isValidOrder(order));
    }

    @Test
    public void isValidOrder_withZeroTotal_returnsFalse() {
        Order order = new Order();
        order.addItem(new Item("Product", 0));
        order.setTotal(0);
        assertFalse(validator.isValidOrder(order));
    }

    @Test
    public void isValidOrder_withNegativeTotal_returnsFalse() {
        Order order = new Order();
        order.addItem(new Item("Product", -10.0));
        order.setTotal(-10.0);
        assertFalse(validator.isValidOrder(order));
    }

    @Test
    public void isValidOrder_withValidOrder_returnsTrue() {
        Order order = new Order();
        order.addItem(new Item("Product", 10.0));
        order.setTotal(10.0);
        assertTrue(validator.isValidOrder(order));
    }

    @Test
    public void calculateDiscount_goldTier_returns20Percent() {
        assertEquals(20.0, validator.calculateDiscount(100.0, "GOLD"), 0.01);
    }

    @Test
    public void calculateDiscount_silverTier_returns10Percent() {
        assertEquals(10.0, validator.calculateDiscount(100.0, "SILVER"), 0.01);
    }

    @Test
    public void calculateDiscount_regularTier_returnsZero() {
        assertEquals(0.0, validator.calculateDiscount(100.0, "BRONZE"), 0.01);
    }

    @Test
    public void categorizeOrderSize_smallOrder() {
        assertEquals(1, validator.categorizeOrderSize(3));
        assertEquals(1, validator.categorizeOrderSize(5));
    }

    @Test
    public void categorizeOrderSize_mediumOrder() {
        assertEquals(2, validator.categorizeOrderSize(6));
        assertEquals(2, validator.categorizeOrderSize(20));
    }

    @Test
    public void categorizeOrderSize_largeOrder() {
        assertEquals(3, validator.categorizeOrderSize(21));
        assertEquals(3, validator.categorizeOrderSize(100));
    }

    // Test boundary conditions
    @Test
    public void categorizeOrderSize_boundaries() {
        assertEquals(1, validator.categorizeOrderSize(5));
        assertEquals(2, validator.categorizeOrderSize(6));
        assertEquals(2, validator.categorizeOrderSize(20));
        assertEquals(3, validator.categorizeOrderSize(21));
    }
}
```
