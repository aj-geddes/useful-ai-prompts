---
name: concurrency-patterns
description: Implement thread-safe code, mutexes, semaphores, async/await patterns, and concurrent data structures. Use when handling parallel operations, race conditions, or building high-performance concurrent systems.
---

# Concurrency Patterns

## Overview

Implement safe concurrent code using proper synchronization primitives and patterns for parallel execution.

## When to Use

- Multi-threaded applications
- Parallel data processing
- Race condition prevention
- Resource pooling
- Task coordination
- High-performance systems
- Async operations
- Worker pools

## Implementation Examples

### 1. **Promise Pool (TypeScript)**

```typescript
class PromisePool {
  private queue: Array<() => Promise<any>> = [];
  private active = 0;

  constructor(private concurrency: number) {}

  async add<T>(fn: () => Promise<T>): Promise<T> {
    while (this.active >= this.concurrency) {
      await this.waitForSlot();
    }

    this.active++;

    try {
      return await fn();
    } finally {
      this.active--;
    }
  }

  private async waitForSlot(): Promise<void> {
    return new Promise(resolve => {
      const checkSlot = () => {
        if (this.active < this.concurrency) {
          resolve();
        } else {
          setTimeout(checkSlot, 10);
        }
      };
      checkSlot();
    });
  }

  async map<T, R>(
    items: T[],
    fn: (item: T) => Promise<R>
  ): Promise<R[]> {
    return Promise.all(
      items.map(item => this.add(() => fn(item)))
    );
  }
}

// Usage
const pool = new PromisePool(5);

const urls = Array.from({ length: 100 }, (_, i) =>
  `https://api.example.com/item/${i}`
);

const results = await pool.map(urls, async (url) => {
  const response = await fetch(url);
  return response.json();
});
```

### 2. **Mutex and Semaphore (TypeScript)**

```typescript
class Mutex {
  private locked = false;
  private queue: Array<() => void> = [];

  async acquire(): Promise<void> {
    if (!this.locked) {
      this.locked = true;
      return;
    }

    return new Promise(resolve => {
      this.queue.push(resolve);
    });
  }

  release(): void {
    if (this.queue.length > 0) {
      const resolve = this.queue.shift()!;
      resolve();
    } else {
      this.locked = false;
    }
  }

  async runExclusive<T>(fn: () => Promise<T>): Promise<T> {
    await this.acquire();
    try {
      return await fn();
    } finally {
      this.release();
    }
  }
}

class Semaphore {
  private available: number;
  private queue: Array<() => void> = [];

  constructor(private max: number) {
    this.available = max;
  }

  async acquire(): Promise<void> {
    if (this.available > 0) {
      this.available--;
      return;
    }

    return new Promise(resolve => {
      this.queue.push(resolve);
    });
  }

  release(): void {
    if (this.queue.length > 0) {
      const resolve = this.queue.shift()!;
      resolve();
    } else {
      this.available++;
    }
  }

  async runExclusive<T>(fn: () => Promise<T>): Promise<T> {
    await this.acquire();
    try {
      return await fn();
    } finally {
      this.release();
    }
  }
}

// Usage
const mutex = new Mutex();
let counter = 0;

async function incrementCounter() {
  await mutex.runExclusive(async () => {
    const current = counter;
    await new Promise(resolve => setTimeout(resolve, 10));
    counter = current + 1;
  });
}

// Database connection pool with semaphore
const dbSemaphore = new Semaphore(10); // Max 10 concurrent connections

async function queryDatabase(query: string) {
  return dbSemaphore.runExclusive(async () => {
    // Execute query
    return executeQuery(query);
  });
}

async function executeQuery(query: string) {
  // Query logic
}
```

### 3. **Worker Pool (Node.js)**

```typescript
import { Worker } from 'worker_threads';

interface Task<T> {
  id: string;
  data: any;
  resolve: (value: T) => void;
  reject: (error: Error) => void;
}

class WorkerPool {
  private workers: Worker[] = [];
  private availableWorkers: Worker[] = [];
  private taskQueue: Task<any>[] = [];

  constructor(
    private workerScript: string,
    private poolSize: number
  ) {
    this.initializeWorkers();
  }

  private initializeWorkers(): void {
    for (let i = 0; i < this.poolSize; i++) {
      const worker = new Worker(this.workerScript);

      worker.on('message', (result) => {
        this.handleWorkerMessage(worker, result);
      });

      worker.on('error', (error) => {
        console.error('Worker error:', error);
      });

      this.workers.push(worker);
      this.availableWorkers.push(worker);
    }
  }

  async execute<T>(data: any): Promise<T> {
    return new Promise((resolve, reject) => {
      const task: Task<T> = {
        id: Math.random().toString(36),
        data,
        resolve,
        reject
      };

      this.taskQueue.push(task);
      this.processQueue();
    });
  }

  private processQueue(): void {
    while (this.taskQueue.length > 0 && this.availableWorkers.length > 0) {
      const task = this.taskQueue.shift()!;
      const worker = this.availableWorkers.shift()!;

      worker.postMessage({
        taskId: task.id,
        data: task.data
      });

      (worker as any).currentTask = task;
    }
  }

  private handleWorkerMessage(worker: Worker, result: any): void {
    const task = (worker as any).currentTask as Task<any>;

    if (!task) return;

    if (result.error) {
      task.reject(new Error(result.error));
    } else {
      task.resolve(result.data);
    }

    delete (worker as any).currentTask;
    this.availableWorkers.push(worker);
    this.processQueue();
  }

  async terminate(): Promise<void> {
    await Promise.all(
      this.workers.map(worker => worker.terminate())
    );
  }
}

// worker.js
// const { parentPort } = require('worker_threads');
//
// parentPort.on('message', async ({ taskId, data }) => {
//   try {
//     const result = await processData(data);
//     parentPort.postMessage({ taskId, data: result });
//   } catch (error) {
//     parentPort.postMessage({ taskId, error: error.message });
//   }
// });
```

### 4. **Python Threading Patterns**

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

### 5. **Async Patterns (Python asyncio)**

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

### 6. **Go-Style Channels (Simulation)**

```typescript
class Channel<T> {
  private buffer: T[] = [];
  private senders: Array<{ value: T; resolve: () => void }> = [];
  private receivers: Array<(value: T) => void> = [];
  private closed = false;

  constructor(private bufferSize: number = 0) {}

  async send(value: T): Promise<void> {
    if (this.closed) {
      throw new Error('Channel is closed');
    }

    if (this.receivers.length > 0) {
      const receiver = this.receivers.shift()!;
      receiver(value);
      return;
    }

    if (this.buffer.length < this.bufferSize) {
      this.buffer.push(value);
      return;
    }

    return new Promise(resolve => {
      this.senders.push({ value, resolve });
    });
  }

  async receive(): Promise<T | undefined> {
    if (this.buffer.length > 0) {
      const value = this.buffer.shift()!;

      if (this.senders.length > 0) {
        const sender = this.senders.shift()!;
        this.buffer.push(sender.value);
        sender.resolve();
      }

      return value;
    }

    if (this.senders.length > 0) {
      const sender = this.senders.shift()!;
      sender.resolve();
      return sender.value;
    }

    if (this.closed) {
      return undefined;
    }

    return new Promise(resolve => {
      this.receivers.push(resolve);
    });
  }

  close(): void {
    this.closed = true;
    this.receivers.forEach(receiver => receiver(undefined as any));
    this.receivers = [];
  }
}

// Usage
async function example() {
  const channel = new Channel<number>(5);

  // Producer
  async function producer() {
    for (let i = 0; i < 10; i++) {
      await channel.send(i);
      console.log(`Sent: ${i}`);
    }
    channel.close();
  }

  // Consumer
  async function consumer() {
    while (true) {
      const value = await channel.receive();
      if (value === undefined) break;
      console.log(`Received: ${value}`);
    }
  }

  await Promise.all([
    producer(),
    consumer()
  ]);
}
```

## Best Practices

### ✅ DO
- Use proper synchronization primitives
- Limit concurrency to avoid resource exhaustion
- Handle errors in concurrent operations
- Use immutable data when possible
- Test concurrent code thoroughly
- Profile concurrent performance
- Document thread-safety guarantees

### ❌ DON'T
- Share mutable state without synchronization
- Use sleep/polling for coordination
- Create unlimited threads/workers
- Ignore race conditions
- Block event loops in async code
- Forget to clean up resources

## Resources

- [Node.js Worker Threads](https://nodejs.org/api/worker_threads.html)
- [Python Threading](https://docs.python.org/3/library/threading.html)
- [Python asyncio](https://docs.python.org/3/library/asyncio.html)
