# Hypothesis for Python

## Hypothesis for Python

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
