# Breaking Point Analysis

## Breaking Point Analysis

```python
# find_breaking_point.py
import requests
import threading
import time
from collections import defaultdict

class BreakingPointTest:
    """Find system breaking point by gradually increasing load."""

    def __init__(self, url):
        self.url = url
        self.results = defaultdict(lambda: {'success': 0, 'errors': 0, 'times': []})
        self.running = True

    def worker(self, vusers):
        """Worker thread that makes requests."""
        while self.running:
            start = time.time()
            try:
                response = requests.get(self.url, timeout=10)
                duration = time.time() - start

                if response.status_code == 200:
                    self.results[vusers]['success'] += 1
                    self.results[vusers]['times'].append(duration)
                else:
                    self.results[vusers]['errors'] += 1

            except Exception as e:
                self.results[vusers]['errors'] += 1

            time.sleep(0.1)

    def test_load_level(self, vusers, duration=60):
        """Test system with specific number of virtual users."""
        print(f"\nTesting with {vusers} concurrent users...")

        threads = []
        for _ in range(vusers):
            t = threading.Thread(target=self.worker, args=(vusers,))
            t.start()
            threads.append(t)

        time.sleep(duration)

        self.running = False
        for t in threads:
            t.join()

        self.running = True

        # Analyze results
        stats = self.results[vusers]
        total = stats['success'] + stats['errors']
        error_rate = stats['errors'] / total if total > 0 else 0
        avg_time = sum(stats['times']) / len(stats['times']) if stats['times'] else 0

        print(f"  Requests: {total}")
        print(f"  Success: {stats['success']}")
        print(f"  Errors: {stats['errors']}")
        print(f"  Error Rate: {error_rate:.1%}")
        print(f"  Avg Response: {avg_time:.3f}s")

        # System is breaking if error rate > 5% or avg response > 5s
        is_breaking = error_rate > 0.05 or avg_time > 5.0

        return not is_breaking

    def find_breaking_point(self):
        """Binary search to find breaking point."""
        min_users = 10
        max_users = 1000
        breaking_point = None

        while min_users < max_users:
            mid = (min_users + max_users) // 2

            if self.test_load_level(mid):
                # System handles this load, try higher
                min_users = mid + 10
            else:
                # System breaking, found upper limit
                breaking_point = mid
                max_users = mid - 10

        print(f"\n{'='*60}")
        print(f"Breaking point: ~{breaking_point} concurrent users")
        print(f"{'='*60}")

        return breaking_point

# Run
test = BreakingPointTest('http://api.example.com/products')
test.find_breaking_point()
```
