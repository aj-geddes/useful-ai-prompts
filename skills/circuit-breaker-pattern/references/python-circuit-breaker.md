# Python Circuit Breaker

## Python Circuit Breaker

```python
from enum import Enum
from typing import Callable, Optional, TypeVar, Generic
import time
import threading

T = TypeVar('T')

class CircuitState(Enum):
    CLOSED = "CLOSED"
    OPEN = "OPEN"
    HALF_OPEN = "HALF_OPEN"

class CircuitBreaker(Generic[T]):
    def __init__(
        self,
        failure_threshold: int = 5,
        success_threshold: int = 2,
        timeout: float = 3.0,
        reset_timeout: float = 60.0
    ):
        self.failure_threshold = failure_threshold
        self.success_threshold = success_threshold
        self.timeout = timeout
        self.reset_timeout = reset_timeout

        self.state = CircuitState.CLOSED
        self.failures = 0
        self.successes = 0
        self.last_failure_time = None
        self.next_attempt = time.time()
        self.lock = threading.Lock()

    def call(
        self,
        func: Callable[[], T],
        fallback: Optional[Callable[[], T]] = None
    ) -> T:
        """Execute function with circuit breaker protection."""
        with self.lock:
            if self.state == CircuitState.OPEN:
                if time.time() < self.next_attempt:
                    print("Circuit breaker OPEN")
                    if fallback:
                        return fallback()
                    raise Exception("Circuit breaker is OPEN")

                # Try to recover
                self.state = CircuitState.HALF_OPEN
                print("Circuit breaker entering HALF_OPEN")

        try:
            result = func()
            self._on_success()
            return result
        except Exception as e:
            self._on_failure()
            if fallback:
                return fallback()
            raise

    def _on_success(self):
        """Handle successful request."""
        with self.lock:
            self.failures = 0
            self.successes += 1

            if self.state == CircuitState.HALF_OPEN:
                if self.successes >= self.success_threshold:
                    print("Circuit breaker CLOSED")
                    self.state = CircuitState.CLOSED
                    self.successes = 0

    def _on_failure(self):
        """Handle failed request."""
        with self.lock:
            self.failures += 1
            self.successes = 0
            self.last_failure_time = time.time()

            if self.state == CircuitState.HALF_OPEN:
                print("Circuit breaker OPEN after failed recovery")
                self._trip()
            elif self.failures >= self.failure_threshold:
                print(f"Circuit breaker OPEN after {self.failures} failures")
                self._trip()

    def _trip(self):
        """Open the circuit."""
        self.state = CircuitState.OPEN
        self.next_attempt = time.time() + self.reset_timeout

    def get_state(self) -> CircuitState:
        """Get current circuit state."""
        return self.state

    def reset(self):
        """Manually reset the circuit breaker."""
        with self.lock:
            self.state = CircuitState.CLOSED
            self.failures = 0
            self.successes = 0


# Usage
import requests

breaker = CircuitBreaker(
    failure_threshold=5,
    success_threshold=2,
    timeout=3.0,
    reset_timeout=60.0
)

def call_api():
    response = requests.get('https://api.example.com/data', timeout=3)
    response.raise_for_status()
    return response.json()

def fallback():
    return {"data": "cached or default"}

# Execute with circuit breaker
try:
    result = breaker.call(call_api, fallback)
    print(result)
except Exception as e:
    print(f"Error: {e}")
```
