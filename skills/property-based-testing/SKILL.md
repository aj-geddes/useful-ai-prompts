---
name: property-based-testing
description: >
  Design property-based tests that verify code properties hold for all inputs
  using automatic test case generation. Use for property-based, QuickCheck,
  hypothesis testing, generative testing, and invariant verification.
---

# Property-Based Testing

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Hypothesis for Python](references/hypothesis-for-python.md) | Hypothesis for Python |
| [fast-check for JavaScript/TypeScript](references/fast-check-for-javascripttypescript.md) | fast-check for JavaScript/TypeScript |
| [junit-quickcheck for Java](references/junit-quickcheck-for-java.md) | junit-quickcheck for Java |

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
