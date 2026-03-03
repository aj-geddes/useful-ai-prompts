# RxJS Basics

## RxJS Basics

```typescript
import {
  Observable,
  Subject,
  BehaviorSubject,
  fromEvent,
  interval,
} from "rxjs";
import {
  map,
  filter,
  debounceTime,
  distinctUntilChanged,
  switchMap,
} from "rxjs/operators";

// Create observable from array
const numbers$ = new Observable<number>((subscriber) => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);
  subscriber.complete();
});

numbers$.subscribe({
  next: (value) => console.log(value),
  error: (err) => console.error(err),
  complete: () => console.log("Done"),
});

// Subject (multicast)
const subject = new Subject<number>();

subject.subscribe((value) => console.log("Sub 1:", value));
subject.subscribe((value) => console.log("Sub 2:", value));

subject.next(1); // Both subscribers receive

// BehaviorSubject (with initial value)
const state$ = new BehaviorSubject({ count: 0 });

state$.subscribe((state) => console.log("State:", state));

state$.next({ count: 1 });
state$.next({ count: 2 });

// Operators
const source$ = interval(1000);

source$
  .pipe(
    map((n) => n * 2),
    filter((n) => n > 5),
    take(5),
  )
  .subscribe((value) => console.log(value));
```
