# Sliding Window Algorithm (Python)

## Sliding Window Algorithm (Python)

```python
import time
from collections import deque
from typing import Deque, Optional
import threading

class SlidingWindowRateLimiter:
    def __init__(self, max_requests: int, window_size: int):
        """
        Initialize sliding window rate limiter.

        Args:
            max_requests: Maximum number of requests allowed
            window_size: Time window in seconds
        """
        self.max_requests = max_requests
        self.window_size = window_size
        self.requests: dict[str, Deque[float]] = {}
        self.lock = threading.Lock()

    def is_allowed(self, key: str) -> tuple[bool, Optional[float]]:
        """
        Check if request is allowed.

        Returns:
            Tuple of (is_allowed, retry_after_seconds)
        """
        with self.lock:
            now = time.time()

            # Initialize or get request queue for this key
            if key not in self.requests:
                self.requests[key] = deque()

            request_queue = self.requests[key]

            # Remove expired requests
            cutoff_time = now - self.window_size
            while request_queue and request_queue[0] < cutoff_time:
                request_queue.popleft()

            # Check if limit exceeded
            if len(request_queue) >= self.max_requests:
                # Calculate retry after time
                oldest_request = request_queue[0]
                retry_after = self.window_size - (now - oldest_request)
                return False, retry_after

            # Add current request
            request_queue.append(now)
            return True, None

    def get_remaining(self, key: str) -> int:
        """Get remaining requests for key."""
        with self.lock:
            if key not in self.requests:
                return self.max_requests

            now = time.time()
            cutoff_time = now - self.window_size
            request_queue = self.requests[key]

            # Remove expired
            while request_queue and request_queue[0] < cutoff_time:
                request_queue.popleft()

            return max(0, self.max_requests - len(request_queue))

    def reset(self, key: str):
        """Reset rate limit for key."""
        with self.lock:
            if key in self.requests:
                del self.requests[key]

    def cleanup(self):
        """Remove all expired entries."""
        with self.lock:
            now = time.time()
            cutoff_time = now - self.window_size

            keys_to_delete = []
            for key, request_queue in self.requests.items():
                # Remove expired requests
                while request_queue and request_queue[0] < cutoff_time:
                    request_queue.popleft()

                # Delete empty queues
                if not request_queue:
                    keys_to_delete.append(key)

            for key in keys_to_delete:
                del self.requests[key]


# Usage
limiter = SlidingWindowRateLimiter(max_requests=100, window_size=60)

# Check if request is allowed
allowed, retry_after = limiter.is_allowed("user:123")

if not allowed:
    print(f"Rate limited. Retry after {retry_after:.2f} seconds")
else:
    # Process request
    remaining = limiter.get_remaining("user:123")
    print(f"Request allowed. {remaining} remaining")
```
