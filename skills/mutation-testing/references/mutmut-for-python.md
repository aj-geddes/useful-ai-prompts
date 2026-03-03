# mutmut for Python

## mutmut for Python

```bash
# Install mutmut
pip install mutmut

# Run mutation testing
mutmut run

# Show results
mutmut results

# Show specific mutant
mutmut show 1

# Apply mutation to see what changed
mutmut apply 1
```

```python
# src/string_utils.py
def is_palindrome(s: str) -> bool:
    """Check if string is palindrome."""
    clean = ''.join(c.lower() for c in s if c.isalnum())
    return clean == clean[::-1]

def count_words(text: str) -> int:
    """Count words in text."""
    if not text:
        return 0
    return len(text.split())

def truncate(text: str, max_length: int) -> str:
    """Truncate text to max length."""
    if len(text) <= max_length:
        return text
    return text[:max_length] + "..."

# ❌ Weak tests
def test_palindrome_basic():
    """Weak: Only tests one case."""
    assert is_palindrome("racecar") == True

# ✅ Strong tests that will catch mutations
def test_is_palindrome_simple():
    assert is_palindrome("racecar") == True
    assert is_palindrome("hello") == False

def test_is_palindrome_with_spaces():
    assert is_palindrome("race car") == True
    assert is_palindrome("not a palindrome") == False

def test_is_palindrome_with_punctuation():
    assert is_palindrome("A man, a plan, a canal: Panama") == True

def test_is_palindrome_case_insensitive():
    assert is_palindrome("RaceCar") == True
    assert is_palindrome("Racecar") == True

def test_is_palindrome_empty():
    assert is_palindrome("") == True

def test_is_palindrome_single_char():
    assert is_palindrome("a") == True

def test_count_words_basic():
    assert count_words("hello world") == 2
    assert count_words("one") == 1

def test_count_words_multiple_spaces():
    assert count_words("hello  world") == 2
    assert count_words("  leading spaces") == 2

def test_count_words_empty():
    assert count_words("") == 0
    assert count_words("   ") == 0

def test_truncate_short_text():
    assert truncate("hello", 10) == "hello"

def test_truncate_exact_length():
    assert truncate("hello", 5) == "hello"

def test_truncate_long_text():
    result = truncate("hello world", 5)
    assert result == "hello..."
    assert len(result) == 8  # 5 + "..."

def test_truncate_zero_length():
    assert truncate("hello", 0) == "..."
```
