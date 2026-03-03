# junit-quickcheck for Java

## junit-quickcheck for Java

```java
// ArrayOperationsTest.java
import com.pholser.junit.quickcheck.Property;
import com.pholser.junit.quickcheck.runner.JUnitQuickcheck;
import com.pholser.junit.quickcheck.generator.InRange;
import org.junit.runner.RunWith;
import static org.junit.Assert.*;
import java.util.*;

@RunWith(JUnitQuickcheck.class)
public class ArrayOperationsTest {

    @Property
    public void sortingPreservesLength(List<Integer> list) {
        List<Integer> sorted = new ArrayList<>(list);
        Collections.sort(sorted);
        assertEquals(list.size(), sorted.size());
    }

    @Property
    public void sortedListIsOrdered(List<Integer> list) {
        List<Integer> sorted = new ArrayList<>(list);
        Collections.sort(sorted);

        for (int i = 0; i < sorted.size() - 1; i++) {
            assertTrue(sorted.get(i) <= sorted.get(i + 1));
        }
    }

    @Property
    public void sortingIsIdempotent(List<Integer> list) {
        List<Integer> onceSorted = new ArrayList<>(list);
        Collections.sort(onceSorted);

        List<Integer> twiceSorted = new ArrayList<>(onceSorted);
        Collections.sort(twiceSorted);

        assertEquals(onceSorted, twiceSorted);
    }

    @Property
    public void reverseReverseIsIdentity(List<String> list) {
        List<String> once = new ArrayList<>(list);
        Collections.reverse(once);

        List<String> twice = new ArrayList<>(once);
        Collections.reverse(twice);

        assertEquals(list, twice);
    }
}

// StringOperationsTest.java
@RunWith(JUnitQuickcheck.class)
public class StringOperationsTest {

    @Property
    public void concatenationLength(String s1, String s2) {
        assertEquals(s1.length() + s2.length(), (s1 + s2).length());
    }

    @Property
    public void uppercaseIsIdempotent(String s) {
        String once = s.toUpperCase();
        String twice = once.toUpperCase();
        assertEquals(once, twice);
    }

    @Property
    public void trimRemovesWhitespace(String s) {
        String trimmed = s.trim();
        if (!trimmed.isEmpty()) {
            assertFalse(Character.isWhitespace(trimmed.charAt(0)));
            assertFalse(Character.isWhitespace(trimmed.charAt(trimmed.length() - 1)));
        }
    }
}

// MathOperationsTest.java
@RunWith(JUnitQuickcheck.class)
public class MathOperationsTest {

    @Property
    public void additionCommutative(int a, int b) {
        assertEquals(a + b, b + a);
    }

    @Property
    public void additionAssociative(int a, int b, int c) {
        assertEquals((a + b) + c, a + (b + c));
    }

    @Property
    public void absoluteValueNonNegative(int n) {
        assertTrue(Math.abs(n) >= 0);
    }

    @Property
    public void absoluteValueIdempotent(int n) {
        assertEquals(Math.abs(n), Math.abs(Math.abs(n)));
    }

    @Property
    public void divisionByNonZero(
        int dividend,
        @InRange(minInt = 1, maxInt = Integer.MAX_VALUE) int divisor
    ) {
        int result = dividend / divisor;
        assertTrue(result * divisor <= dividend + divisor);
    }
}
```
