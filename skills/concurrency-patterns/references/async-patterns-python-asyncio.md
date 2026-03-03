# Async Patterns (Python asyncio)

## Async Patterns (Python asyncio)

```python
import asyncio
from typing import Callable, List, TypeVar, Awaitable

T = TypeVar('T')
R = TypeVar('R')

class AsyncPool:
    def __init__(self, concurrency: int):
        self.semaphore = asyncio.Semaphore(concurrency)

    async def map(
        self,
        func: Callable[[T], Awaitable[R]],
        items: List[T]
    ) -> List[R]:
        """Map async function over items with concurrency limit."""
        async def bounded_func(item: T) -> R:
            async with self.semaphore:
                return await func(item)

        return await asyncio.gather(*[
            bounded_func(item) for item in items
        ])


class AsyncQueue:
    def __init__(self, max_size: int = 0):
        self.queue = asyncio.Queue(maxsize=max_size)

    async def put(self, item):
        await self.queue.put(item)

    async def get(self):
        return await self.queue.get()

    def task_done(self):
        self.queue.task_done()

    async def join(self):
        await self.queue.join()


# Producer-Consumer pattern
async def producer(queue: AsyncQueue, items: List[int]):
    """Produce items."""
    for item in items:
        await queue.put(item)
        print(f"Produced: {item}")
        await asyncio.sleep(0.1)

async def consumer(queue: AsyncQueue, name: str):
    """Consume items."""
    while True:
        item = await queue.get()

        if item is None:
            queue.task_done()
            break

        print(f"{name} consuming: {item}")
        await asyncio.sleep(0.2)
        queue.task_done()

async def main():
    queue = AsyncQueue(max_size=10)

    # Start consumers
    consumers = [
        asyncio.create_task(consumer(queue, f"Consumer-{i}"))
        for i in range(3)
    ]

    # Start producer
    await producer(queue, list(range(20)))

    # Wait for all items to be processed
    await queue.join()

    # Stop consumers
    for _ in range(3):
        await queue.put(None)

    await asyncio.gather(*consumers)

asyncio.run(main())
```
