# Python Threading Patterns

## Python Threading Patterns

```python
import threading
from queue import Queue
from typing import Callable, List, TypeVar, Generic
import time

T = TypeVar('T')
R = TypeVar('R')

class ThreadPool(Generic[T, R]):
    def __init__(self, num_threads: int):
        self.num_threads = num_threads
        self.tasks: Queue = Queue()
        self.results: List[R] = []
        self.lock = threading.Lock()
        self.workers: List[threading.Thread] = []

    def map(self, func: Callable[[T], R], items: List[T]) -> List[R]:
        """Map function over items using thread pool."""
        # Add tasks to queue
        for item in items:
            self.tasks.put(item)

        # Start workers
        for _ in range(self.num_threads):
            worker = threading.Thread(
                target=self._worker,
                args=(func,)
            )
            worker.start()
            self.workers.append(worker)

        # Wait for completion
        self.tasks.join()

        # Stop workers
        for _ in range(self.num_threads):
            self.tasks.put(None)

        for worker in self.workers:
            worker.join()

        return self.results

    def _worker(self, func: Callable[[T], R]):
        """Worker thread."""
        while True:
            item = self.tasks.get()

            if item is None:
                self.tasks.task_done()
                break

            try:
                result = func(item)

                with self.lock:
                    self.results.append(result)
            finally:
                self.tasks.task_done()


class Mutex:
    def __init__(self):
        self._lock = threading.Lock()

    def __enter__(self):
        self._lock.acquire()
        return self

    def __exit__(self, *args):
        self._lock.release()


class Semaphore:
    def __init__(self, max_count: int):
        self._semaphore = threading.Semaphore(max_count)

    def __enter__(self):
        self._semaphore.acquire()
        return self

    def __exit__(self, *args):
        self._semaphore.release()


# Usage
def process_item(item: int) -> int:
    time.sleep(0.1)
    return item * 2

pool = ThreadPool(num_threads=5)
items = list(range(100))
results = pool.map(process_item, items)
print(f"Processed {len(results)} items")

# Mutex example
counter = 0
mutex = Mutex()

def increment():
    global counter
    with mutex:
        current = counter
        time.sleep(0.001)
        counter = current + 1

threads = [threading.Thread(target=increment) for _ in range(100)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"Counter: {counter}")  # Should be 100

# Semaphore example
db_connections = Semaphore(max_count=10)

def query_database(query: str):
    with db_connections:
        # Execute query with limited connections
        time.sleep(0.1)
        print(f"Executing: {query}")
```
