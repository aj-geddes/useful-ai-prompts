# Go-Style Channels (Simulation)

## Go-Style Channels (Simulation)

```typescript
class Channel<T> {
  private buffer: T[] = [];
  private senders: Array<{ value: T; resolve: () => void }> = [];
  private receivers: Array<(value: T) => void> = [];
  private closed = false;

  constructor(private bufferSize: number = 0) {}

  async send(value: T): Promise<void> {
    if (this.closed) {
      throw new Error("Channel is closed");
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

    return new Promise((resolve) => {
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

    return new Promise((resolve) => {
      this.receivers.push(resolve);
    });
  }

  close(): void {
    this.closed = true;
    this.receivers.forEach((receiver) => receiver(undefined as any));
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

  await Promise.all([producer(), consumer()]);
}
```
