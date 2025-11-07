---
name: property-based-testing
description: Design property-based tests that verify code properties hold for all inputs using automatic test case generation. Use for property-based, QuickCheck, hypothesis testing, generative testing, and invariant verification.
---

# Property-Based Testing

## Overview

Property-based testing verifies that code satisfies general properties or invariants for a wide range of automatically generated inputs, rather than testing specific examples. This approach finds edge cases and bugs that example-based tests often miss.

## When to Use

- Testing algorithms with mathematical properties
- Verifying invariants that should always hold
- Finding edge cases automatically
- Testing parsers and serializers (round-trip properties)
- Validating data transformations
- Testing sorting, searching, and data structure operations
- Discovering unexpected input combinations

## Key Concepts

- **Property**: A statement that should be true for all valid inputs
- **Generator**: Creates random test inputs
- **Shrinking**: Minimizes failing inputs to simplest case
- **Invariant**: Condition that must always be true
- **Round-trip**: Encoding then decoding returns original value

## Instructions

### 1. **Hypothesis for Python**

```python
# test_string_operations.py
import pytest
from hypothesis import given, strategies as st, assume, example

def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

class TestStringOperations:
    @given(st.text())
    def test_reverse_twice_returns_original(self, s):
        """Property: Reversing twice returns the original string."""
        assert reverse_string(reverse_string(s)) == s

    @given(st.text())
    def test_reverse_length_unchanged(self, s):
        """Property: Reverse doesn't change length."""
        assert len(reverse_string(s)) == len(s)

    @given(st.text(min_size=1))
    def test_reverse_first_becomes_last(self, s):
        """Property: First char becomes last after reverse."""
        reversed_s = reverse_string(s)
        assert s[0] == reversed_s[-1]
        assert s[-1] == reversed_s[0]

# test_sorting.py
from hypothesis import given, strategies as st

def quick_sort(items):
    """Sort items using quicksort."""
    if len(items) <= 1:
        return items
    pivot = items[len(items) // 2]
    left = [x for x in items if x < pivot]
    middle = [x for x in items if x == pivot]
    right = [x for x in items if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

class TestSorting:
    @given(st.lists(st.integers()))
    def test_sorted_list_is_ordered(self, items):
        """Property: Every element <= next element."""
        sorted_items = quick_sort(items)
        for i in range(len(sorted_items) - 1):
            assert sorted_items[i] <= sorted_items[i + 1]

    @given(st.lists(st.integers()))
    def test_sorting_preserves_length(self, items):
        """Property: Sorting doesn't add/remove elements."""
        sorted_items = quick_sort(items)
        assert len(sorted_items) == len(items)

    @given(st.lists(st.integers()))
    def test_sorting_preserves_elements(self, items):
        """Property: All elements present in result."""
        sorted_items = quick_sort(items)
        assert sorted(items) == sorted_items

    @given(st.lists(st.integers()))
    def test_sorting_is_idempotent(self, items):
        """Property: Sorting twice gives same result."""
        once = quick_sort(items)
        twice = quick_sort(once)
        assert once == twice

    @given(st.lists(st.integers(), min_size=1))
    def test_sorted_min_at_start(self, items):
        """Property: Minimum element is first."""
        sorted_items = quick_sort(items)
        assert sorted_items[0] == min(items)

    @given(st.lists(st.integers(), min_size=1))
    def test_sorted_max_at_end(self, items):
        """Property: Maximum element is last."""
        sorted_items = quick_sort(items)
        assert sorted_items[-1] == max(items)

# test_json_serialization.py
from hypothesis import given, strategies as st
import json

# Define a strategy for JSON-serializable objects
json_strategy = st.recursive(
    st.none() | st.booleans() | st.integers() | st.floats(allow_nan=False) | st.text(),
    lambda children: st.lists(children) | st.dictionaries(st.text(), children),
    max_leaves=10
)

class TestJSONSerialization:
    @given(json_strategy)
    def test_json_round_trip(self, obj):
        """Property: Encoding then decoding returns original."""
        json_str = json.dumps(obj)
        decoded = json.loads(json_str)
        assert decoded == obj

    @given(st.dictionaries(st.text(), st.integers()))
    def test_json_dict_keys_preserved(self, d):
        """Property: All dictionary keys are preserved."""
        json_str = json.dumps(d)
        decoded = json.loads(json_str)
        assert set(decoded.keys()) == set(d.keys())

# test_math_operations.py
from hypothesis import given, strategies as st, assume
import math

class TestMathOperations:
    @given(st.integers(), st.integers())
    def test_addition_commutative(self, a, b):
        """Property: a + b = b + a"""
        assert a + b == b + a

    @given(st.integers(), st.integers(), st.integers())
    def test_addition_associative(self, a, b, c):
        """Property: (a + b) + c = a + (b + c)"""
        assert (a + b) + c == a + (b + c)

    @given(st.integers())
    def test_addition_identity(self, a):
        """Property: a + 0 = a"""
        assert a + 0 == a

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_abs_non_negative(self, x):
        """Property: abs(x) >= 0"""
        assert abs(x) >= 0

    @given(st.floats(allow_nan=False, allow_infinity=False))
    def test_abs_idempotent(self, x):
        """Property: abs(abs(x)) = abs(x)"""
        assert abs(abs(x)) == abs(x)

    @given(st.integers(min_value=0))
    def test_sqrt_inverse_of_square(self, n):
        """Property: sqrt(n^2) = n for non-negative n"""
        assert math.isclose(math.sqrt(n * n), n)

# test_with_examples.py
from hypothesis import given, strategies as st, example

class TestWithExamples:
    @given(st.integers())
    @example(0)  # Ensure we test zero
    @example(-1)  # Ensure we test negative
    @example(1)  # Ensure we test positive
    def test_absolute_value(self, n):
        """Property: abs(n) >= 0, with specific examples."""
        assert abs(n) >= 0

# test_stateful.py
from hypothesis.stateful import RuleBasedStateMachine, rule, invariant
import hypothesis.strategies as st

class StackMachine(RuleBasedStateMachine):
    """Test stack data structure with stateful properties."""

    def __init__(self):
        super().__init__()
        self.stack = []

    @rule(value=st.integers())
    def push(self, value):
        """Push a value onto the stack."""
        self.stack.append(value)

    @rule()
    def pop(self):
        """Pop a value from the stack."""
        if self.stack:
            self.stack.pop()

    @invariant()
    def stack_size_non_negative(self):
        """Invariant: Stack size is never negative."""
        assert len(self.stack) >= 0

    @invariant()
    def peek_equals_last_push(self):
        """Invariant: Peek returns the last pushed value."""
        if self.stack:
            # Last item should be the most recently pushed
            assert self.stack[-1] is not None

TestStack = StackMachine.TestCase
```

### 2. **fast-check for JavaScript/TypeScript**

```typescript
// string.test.ts
import * as fc from 'fast-check';

describe('String Operations', () => {
  test('reverse twice returns original', () => {
    fc.assert(
      fc.property(fc.string(), (s) => {
        const reversed = s.split('').reverse().join('');
        const doubleReversed = reversed.split('').reverse().join('');
        return s === doubleReversed;
      })
    );
  });

  test('concatenation length', () => {
    fc.assert(
      fc.property(fc.string(), fc.string(), (s1, s2) => {
        return (s1 + s2).length === s1.length + s2.length;
      })
    );
  });

  test('uppercase is idempotent', () => {
    fc.assert(
      fc.property(fc.string(), (s) => {
        const once = s.toUpperCase();
        const twice = once.toUpperCase();
        return once === twice;
      })
    );
  });
});

// array.test.ts
import * as fc from 'fast-check';

function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = arr.filter(x => x < pivot);
  const middle = arr.filter(x => x === pivot);
  const right = arr.filter(x => x > pivot);
  return [...quickSort(left), ...middle, ...quickSort(right)];
}

describe('Sorting Properties', () => {
  test('sorted array is ordered', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        const sorted = quickSort(arr);
        for (let i = 0; i < sorted.length - 1; i++) {
          if (sorted[i] > sorted[i + 1]) return false;
        }
        return true;
      })
    );
  });

  test('sorting preserves length', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        return quickSort(arr).length === arr.length;
      })
    );
  });

  test('sorting preserves elements', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        const sorted = quickSort(arr);
        const originalSorted = [...arr].sort((a, b) => a - b);
        return JSON.stringify(sorted) === JSON.stringify(originalSorted);
      })
    );
  });

  test('sorting is idempotent', () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        const once = quickSort(arr);
        const twice = quickSort(once);
        return JSON.stringify(once) === JSON.stringify(twice);
      })
    );
  });
});

// object.test.ts
import * as fc from 'fast-check';

interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

const userArbitrary = fc.record({
  id: fc.integer(),
  name: fc.string({ minLength: 1 }),
  email: fc.emailAddress(),
  age: fc.integer({ min: 0, max: 120 }),
});

describe('User Validation', () => {
  test('serialization round trip', () => {
    fc.assert(
      fc.property(userArbitrary, (user) => {
        const json = JSON.stringify(user);
        const parsed = JSON.parse(json);
        return JSON.stringify(parsed) === json;
      })
    );
  });

  test('age validation', () => {
    fc.assert(
      fc.property(userArbitrary, (user) => {
        return user.age >= 0 && user.age <= 120;
      })
    );
  });
});

// custom generators
const positiveIntegerArray = fc.array(fc.integer({ min: 1 }), { minLength: 1 });

test('sum of positives is positive', () => {
  fc.assert(
    fc.property(positiveIntegerArray, (arr) => {
      const sum = arr.reduce((a, b) => a + b, 0);
      return sum > 0;
    })
  );
});

// test with shrinking
test('find minimum failing case', () => {
  try {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        // This will fail for arrays with negative numbers
        return arr.every(n => n >= 0);
      })
    );
  } catch (error) {
    // fast-check will shrink to minimal failing case: [-1] or similar
    console.log('Minimal failing case found:', error);
  }
});
```

### 3. **junit-quickcheck for Java**

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

## Common Properties to Test

### Universal Properties
- **Idempotence**: `f(f(x)) = f(x)`
- **Identity**: `f(x, identity) = x`
- **Commutativity**: `f(a, b) = f(b, a)`
- **Associativity**: `f(f(a, b), c) = f(a, f(b, c))`
- **Inverse**: `f(inverse_f(x)) = x`

### Data Structure Properties
- **Round-trip**: `decode(encode(x)) = x`
- **Preservation**: Operation preserves length, elements, or structure
- **Ordering**: Elements maintain required order
- **Bounds**: Values stay within valid ranges
- **Invariants**: Class invariants always hold

## Best Practices

### ✅ DO
- Focus on general properties, not specific cases
- Test mathematical properties (commutativity, associativity)
- Verify round-trip encoding/decoding
- Use shrinking to find minimal failing cases
- Combine with example-based tests for known edge cases
- Test invariants that should always hold
- Generate realistic input distributions

### ❌ DON'T
- Test properties that are tautologies
- Over-constrain input generation
- Ignore shrunk test failures
- Replace all example tests with properties
- Test implementation details
- Generate invalid inputs without constraints
- Forget to handle edge cases in generators

## Tools & Libraries

- **Python**: Hypothesis
- **JavaScript/TypeScript**: fast-check, jsverify
- **Java**: junit-quickcheck, jqwik
- **Scala**: ScalaCheck
- **Haskell**: QuickCheck (original)
- **C#**: FsCheck

## Examples

See also: test-data-generation, mutation-testing, continuous-testing for comprehensive testing strategies.
