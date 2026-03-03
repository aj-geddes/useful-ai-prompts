# Cache Decorator (Python)

## Cache Decorator (Python)

```python
import functools
import json
import hashlib
from typing import Any, Callable, Optional
from redis import Redis
import time

class CacheDecorator:
    def __init__(self, redis_client: Redis, ttl: int = 3600):
        self.redis = redis_client
        self.ttl = ttl

    def cache_key(self, func: Callable, *args, **kwargs) -> str:
        """Generate cache key from function name and arguments."""
        # Create deterministic key from function and arguments
        key_parts = [
            func.__module__,
            func.__name__,
            str(args),
            str(sorted(kwargs.items()))
        ]
        key_string = ':'.join(key_parts)
        key_hash = hashlib.md5(key_string.encode()).hexdigest()
        return f"cache:{func.__name__}:{key_hash}"

    def __call__(self, func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Generate cache key
            cache_key = self.cache_key(func, *args, **kwargs)

            # Try to get from cache
            cached = self.redis.get(cache_key)
            if cached:
                print(f"Cache HIT: {cache_key}")
                return json.loads(cached)

            # Cache miss - execute function
            print(f"Cache MISS: {cache_key}")
            result = func(*args, **kwargs)

            # Store in cache
            self.redis.setex(
                cache_key,
                self.ttl,
                json.dumps(result)
            )

            return result

        # Add cache invalidation method
        def invalidate(*args, **kwargs):
            cache_key = self.cache_key(func, *args, **kwargs)
            self.redis.delete(cache_key)

        wrapper.invalidate = invalidate
        return wrapper


# Usage
redis = Redis(host='localhost', port=6379, db=0)
cache = CacheDecorator(redis, ttl=300)

@cache
def get_user_profile(user_id: int) -> dict:
    """Fetch user profile from database."""
    print(f"Fetching user {user_id} from database...")
    # Simulate database query
    time.sleep(1)
    return {
        'id': user_id,
        'name': 'John Doe',
        'email': 'john@example.com'
    }

# First call - cache miss
profile = get_user_profile(123)  # Takes 1 second

# Second call - cache hit
profile = get_user_profile(123)  # Instant

# Invalidate cache
get_user_profile.invalidate(123)
```
