# Worker Pool (Node.js)

## Worker Pool (Node.js)

```typescript
import { Worker } from "worker_threads";

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
    private poolSize: number,
  ) {
    this.initializeWorkers();
  }

  private initializeWorkers(): void {
    for (let i = 0; i < this.poolSize; i++) {
      const worker = new Worker(this.workerScript);

      worker.on("message", (result) => {
        this.handleWorkerMessage(worker, result);
      });

      worker.on("error", (error) => {
        console.error("Worker error:", error);
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
        reject,
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
        data: task.data,
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
    await Promise.all(this.workers.map((worker) => worker.terminate()));
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
