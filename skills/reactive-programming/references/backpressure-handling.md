# Backpressure Handling

## Backpressure Handling

```typescript
import { Subject } from "rxjs";
import { bufferTime, throttleTime } from "rxjs/operators";

// Buffer events
const events$ = new Subject<string>();

events$
  .pipe(
    bufferTime(1000), // Collect events for 1 second
    filter((buffer) => buffer.length > 0),
  )
  .subscribe((events) => {
    console.log("Batch:", events);
    processBatch(events);
  });

// Throttle events
const clicks$ = fromEvent(button, "click");

clicks$
  .pipe(
    throttleTime(1000), // Only allow one every second
  )
  .subscribe(() => {
    console.log("Click processed");
  });

function processBatch(events: string[]) {
  // Process batch
}
```
