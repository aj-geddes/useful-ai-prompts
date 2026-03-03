# Soak/Endurance Testing

## Soak/Endurance Testing

```python
# soak_test.py
import asyncio
import aiohttp
import time
from datetime import datetime, timedelta
import psutil
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SoakTest:
    """Run sustained load test to detect memory leaks and degradation."""

    def __init__(self, url, duration_hours=4, requests_per_second=50):
        self.url = url
        self.duration = timedelta(hours=duration_hours)
        self.rps = requests_per_second
        self.metrics = {
            'requests': 0,
            'errors': 0,
            'response_times': [],
            'memory_usage': [],
        }

    async def make_request(self, session):
        """Make single request and record metrics."""
        start = time.time()
        try:
            async with session.get(self.url) as response:
                await response.read()
                duration = time.time() - start

                self.metrics['requests'] += 1
                self.metrics['response_times'].append(duration)

                if response.status >= 400:
                    self.metrics['errors'] += 1
                    logger.warning(f"Error: {response.status}")

        except Exception as e:
            self.metrics['errors'] += 1
            logger.error(f"Request failed: {e}")

    async def worker(self, session):
        """Worker that makes requests at target rate."""
        while self.running:
            await self.make_request(session)
            await asyncio.sleep(1 / self.rps)

    def monitor_resources(self):
        """Monitor system resources."""
        process = psutil.Process()
        return {
            'memory_mb': process.memory_info().rss / 1024 / 1024,
            'cpu_percent': process.cpu_percent(),
            'timestamp': datetime.now(),
        }

    async def run(self):
        """Execute soak test."""
        start_time = datetime.now()
        end_time = start_time + self.duration
        self.running = True

        logger.info(f"Starting soak test for {self.duration}")
        logger.info(f"Target: {self.rps} req/s to {self.url}")

        async with aiohttp.ClientSession() as session:
            # Start workers
            workers = [
                asyncio.create_task(self.worker(session))
                for _ in range(10)  # 10 concurrent workers
            ]

            # Monitor resources periodically
            while datetime.now() < end_time:
                await asyncio.sleep(60)  # Check every minute

                resources = self.monitor_resources()
                self.metrics['memory_usage'].append(resources)

                # Log progress
                elapsed = (datetime.now() - start_time).total_seconds()
                error_rate = self.metrics['errors'] / max(self.metrics['requests'], 1)
                avg_response = sum(self.metrics['response_times'][-1000:]) / 1000

                logger.info(
                    f"Elapsed: {elapsed:.0f}s | "
                    f"Requests: {self.metrics['requests']} | "
                    f"Error Rate: {error_rate:.2%} | "
                    f"Avg Response: {avg_response:.3f}s | "
                    f"Memory: {resources['memory_mb']:.1f}MB"
                )

                # Check for memory leak
                if len(self.metrics['memory_usage']) > 10:
                    initial_mem = self.metrics['memory_usage'][0]['memory_mb']
                    current_mem = resources['memory_mb']
                    growth = current_mem - initial_mem

                    if growth > 500:  # 500MB growth
                        logger.warning(f"Possible memory leak: +{growth:.1f}MB")

            # Stop workers
            self.running = False
            await asyncio.gather(*workers, return_exceptions=True)

        self.report()

    def report(self):
        """Generate test report."""
        total_requests = self.metrics['requests']
        error_rate = self.metrics['errors'] / total_requests if total_requests > 0 else 0
        response_times = self.metrics['response_times']

        print("\n" + "="*60)
        print("SOAK TEST RESULTS")
        print("="*60)
        print(f"Total Requests: {total_requests:,}")
        print(f"Total Errors: {self.metrics['errors']:,}")
        print(f"Error Rate: {error_rate:.2%}")
        print(f"\nResponse Times:")
        print(f"  Min: {min(response_times):.3f}s")
        print(f"  Max: {max(response_times):.3f}s")
        print(f"  Mean: {sum(response_times)/len(response_times):.3f}s")
        print(f"  P95: {sorted(response_times)[int(len(response_times)*0.95)]:.3f}s")

        # Memory analysis
        if self.metrics['memory_usage']:
            initial_mem = self.metrics['memory_usage'][0]['memory_mb']
            final_mem = self.metrics['memory_usage'][-1]['memory_mb']
            growth = final_mem - initial_mem

            print(f"\nMemory Usage:")
            print(f"  Initial: {initial_mem:.1f}MB")
            print(f"  Final: {final_mem:.1f}MB")
            print(f"  Growth: {growth:.1f}MB ({growth/initial_mem*100:.1f}%)")

            if growth > 200:
                print("  ⚠️  Possible memory leak detected!")

        print("="*60)

# Run soak test
if __name__ == '__main__':
    test = SoakTest(
        url='http://api.example.com/products',
        duration_hours=4,
        requests_per_second=50
    )
    asyncio.run(test.run())
```
