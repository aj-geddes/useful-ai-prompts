# Custom Operators

## Custom Operators

```typescript
import { Observable } from "rxjs";

function tapLog<T>(message: string) {
  return (source: Observable<T>) => {
    return new Observable<T>((subscriber) => {
      return source.subscribe({
        next: (value) => {
          console.log(message, value);
          subscriber.next(value);
        },
        error: (err) => subscriber.error(err),
        complete: () => subscriber.complete(),
      });
    });
  };
}

// Usage
source$
  .pipe(
    tapLog("Before map:"),
    map((x) => x * 2),
    tapLog("After map:"),
  )
  .subscribe();
```
