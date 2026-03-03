# WebSocket with Reconnection

## WebSocket with Reconnection

```typescript
import { Observable, timer } from "rxjs";
import { retryWhen, tap, delayWhen } from "rxjs/operators";

function createWebSocketObservable(url: string): Observable<any> {
  return new Observable((subscriber) => {
    let ws: WebSocket;

    const connect = () => {
      ws = new WebSocket(url);

      ws.onopen = () => {
        console.log("WebSocket connected");
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          subscriber.next(data);
        } catch (error) {
          console.error("Parse error:", error);
        }
      };

      ws.onerror = (error) => {
        console.error("WebSocket error:", error);
        subscriber.error(error);
      };

      ws.onclose = () => {
        console.log("WebSocket closed");
        subscriber.error(new Error("Connection closed"));
      };
    };

    connect();

    return () => {
      if (ws) {
        ws.close();
      }
    };
  }).pipe(
    retryWhen((errors) =>
      errors.pipe(
        tap((err) => console.log("Retrying connection...", err)),
        delayWhen((_, i) => timer(Math.min(1000 * Math.pow(2, i), 30000))),
      ),
    ),
  );
}

// Usage
const ws$ = createWebSocketObservable("wss://api.example.com/ws");

ws$.subscribe({
  next: (data) => console.log("Received:", data),
  error: (err) => console.error("Error:", err),
});
```
