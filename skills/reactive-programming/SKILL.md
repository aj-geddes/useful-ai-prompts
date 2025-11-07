---
name: reactive-programming
description: Implement reactive programming patterns using RxJS, streams, observables, and backpressure handling. Use when building event-driven UIs, handling async data streams, or managing complex data flows.
---

# Reactive Programming

## Overview

Build responsive applications using reactive streams and observables for handling asynchronous data flows.

## When to Use

- Complex async data flows
- Real-time data updates
- Event-driven architectures
- UI state management
- WebSocket/SSE handling
- Combining multiple data sources

## Implementation Examples

### 1. **RxJS Basics**

```typescript
import { Observable, Subject, BehaviorSubject, fromEvent, interval } from 'rxjs';
import { map, filter, debounceTime, distinctUntilChanged, switchMap } from 'rxjs/operators';

// Create observable from array
const numbers$ = new Observable<number>(subscriber => {
  subscriber.next(1);
  subscriber.next(2);
  subscriber.next(3);
  subscriber.complete();
});

numbers$.subscribe({
  next: value => console.log(value),
  error: err => console.error(err),
  complete: () => console.log('Done')
});

// Subject (multicast)
const subject = new Subject<number>();

subject.subscribe(value => console.log('Sub 1:', value));
subject.subscribe(value => console.log('Sub 2:', value));

subject.next(1); // Both subscribers receive

// BehaviorSubject (with initial value)
const state$ = new BehaviorSubject({ count: 0 });

state$.subscribe(state => console.log('State:', state));

state$.next({ count: 1 });
state$.next({ count: 2 });

// Operators
const source$ = interval(1000);

source$.pipe(
  map(n => n * 2),
  filter(n => n > 5),
  take(5)
).subscribe(value => console.log(value));
```

### 2. **Search with Debounce**

```typescript
import { fromEvent } from 'rxjs';
import { debounceTime, distinctUntilChanged, switchMap, catchError } from 'rxjs/operators';
import { of } from 'rxjs';

const searchInput = document.querySelector('#search') as HTMLInputElement;

const search$ = fromEvent(searchInput, 'input').pipe(
  map((event: Event) => (event.target as HTMLInputElement).value),
  debounceTime(300), // Wait 300ms after typing
  distinctUntilChanged(), // Only if value changed
  switchMap(query => {
    if (!query) return of([]);

    return fetch(`/api/search?q=${query}`)
      .then(res => res.json())
      .catch(() => of([]));
  }),
  catchError(error => {
    console.error('Search error:', error);
    return of([]);
  })
);

search$.subscribe(results => {
  console.log('Search results:', results);
  displayResults(results);
});

function displayResults(results: any[]) {
  // Update UI
}
```

### 3. **State Management**

```typescript
import { BehaviorSubject } from 'rxjs';
import { map } from 'rxjs/operators';

interface AppState {
  user: { id: string; name: string } | null;
  cart: Array<{ id: string; quantity: number }>;
  loading: boolean;
}

class StateManager {
  private state$ = new BehaviorSubject<AppState>({
    user: null,
    cart: [],
    loading: false
  });

  // Selectors
  user$ = this.state$.pipe(
    map(state => state.user),
    distinctUntilChanged()
  );

  cart$ = this.state$.pipe(
    map(state => state.cart),
    distinctUntilChanged()
  );

  cartTotal$ = this.cart$.pipe(
    map(cart => cart.reduce((sum, item) => sum + item.quantity, 0))
  );

  loading$ = this.state$.pipe(
    map(state => state.loading)
  );

  // Actions
  setUser(user: AppState['user']): void {
    this.state$.next({
      ...this.state$.value,
      user
    });
  }

  addToCart(item: { id: string; quantity: number }): void {
    const cart = [...this.state$.value.cart];
    const existing = cart.find(i => i.id === item.id);

    if (existing) {
      existing.quantity += item.quantity;
    } else {
      cart.push(item);
    }

    this.state$.next({
      ...this.state$.value,
      cart
    });
  }

  setLoading(loading: boolean): void {
    this.state$.next({
      ...this.state$.value,
      loading
    });
  }

  getState(): AppState {
    return this.state$.value;
  }
}

// Usage
const store = new StateManager();

store.user$.subscribe(user => {
  console.log('User:', user);
});

store.cartTotal$.subscribe(total => {
  console.log('Cart items:', total);
});

store.setUser({ id: '123', name: 'John' });
store.addToCart({ id: 'item1', quantity: 2 });
```

### 4. **WebSocket with Reconnection**

```typescript
import { Observable, timer } from 'rxjs';
import { retryWhen, tap, delayWhen } from 'rxjs/operators';

function createWebSocketObservable(url: string): Observable<any> {
  return new Observable(subscriber => {
    let ws: WebSocket;

    const connect = () => {
      ws = new WebSocket(url);

      ws.onopen = () => {
        console.log('WebSocket connected');
      };

      ws.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          subscriber.next(data);
        } catch (error) {
          console.error('Parse error:', error);
        }
      };

      ws.onerror = (error) => {
        console.error('WebSocket error:', error);
        subscriber.error(error);
      };

      ws.onclose = () => {
        console.log('WebSocket closed');
        subscriber.error(new Error('Connection closed'));
      };
    };

    connect();

    return () => {
      if (ws) {
        ws.close();
      }
    };
  }).pipe(
    retryWhen(errors =>
      errors.pipe(
        tap(err => console.log('Retrying connection...', err)),
        delayWhen((_, i) => timer(Math.min(1000 * Math.pow(2, i), 30000)))
      )
    )
  );
}

// Usage
const ws$ = createWebSocketObservable('wss://api.example.com/ws');

ws$.subscribe({
  next: data => console.log('Received:', data),
  error: err => console.error('Error:', err)
});
```

### 5. **Combining Multiple Streams**

```typescript
import { combineLatest, merge, forkJoin, zip } from 'rxjs';

// combineLatest - emits when any input emits
const users$ = fetchUsers();
const settings$ = fetchSettings();

combineLatest([users$, settings$]).subscribe(([users, settings]) => {
  console.log('Users:', users);
  console.log('Settings:', settings);
});

// merge - combine multiple observables
const clicks$ = fromEvent(button1, 'click');
const hovers$ = fromEvent(button2, 'mouseover');

merge(clicks$, hovers$).subscribe(event => {
  console.log('Event:', event.type);
});

// forkJoin - wait for all to complete (like Promise.all)
forkJoin({
  users: fetchUsers(),
  posts: fetchPosts(),
  comments: fetchComments()
}).subscribe(({ users, posts, comments }) => {
  console.log('All data loaded:', { users, posts, comments });
});

// zip - combine corresponding values
const names$ = of('Alice', 'Bob', 'Charlie');
const ages$ = of(25, 30, 35);

zip(names$, ages$).subscribe(([name, age]) => {
  console.log(`${name} is ${age} years old`);
});
```

### 6. **Backpressure Handling**

```typescript
import { Subject } from 'rxjs';
import { bufferTime, throttleTime } from 'rxjs/operators';

// Buffer events
const events$ = new Subject<string>();

events$.pipe(
  bufferTime(1000), // Collect events for 1 second
  filter(buffer => buffer.length > 0)
).subscribe(events => {
  console.log('Batch:', events);
  processBatch(events);
});

// Throttle events
const clicks$ = fromEvent(button, 'click');

clicks$.pipe(
  throttleTime(1000) // Only allow one every second
).subscribe(() => {
  console.log('Click processed');
});

function processBatch(events: string[]) {
  // Process batch
}
```

### 7. **Custom Operators**

```typescript
import { Observable } from 'rxjs';

function tapLog<T>(message: string) {
  return (source: Observable<T>) => {
    return new Observable<T>(subscriber => {
      return source.subscribe({
        next: value => {
          console.log(message, value);
          subscriber.next(value);
        },
        error: err => subscriber.error(err),
        complete: () => subscriber.complete()
      });
    });
  };
}

// Usage
source$.pipe(
  tapLog('Before map:'),
  map(x => x * 2),
  tapLog('After map:')
).subscribe();
```

## Best Practices

### ✅ DO
- Unsubscribe to prevent memory leaks
- Use operators to transform data
- Handle errors properly
- Use shareReplay for expensive operations
- Combine streams when needed
- Test reactive code

### ❌ DON'T
- Subscribe multiple times to same observable
- Forget to unsubscribe
- Use nested subscriptions
- Ignore error handling
- Make observables stateful

## Common Operators

| Operator | Purpose |
|----------|---------|
| **map** | Transform values |
| **filter** | Filter values |
| **debounceTime** | Wait before emitting |
| **distinctUntilChanged** | Only emit if changed |
| **switchMap** | Switch to new observable |
| **mergeMap** | Merge multiple observables |
| **catchError** | Handle errors |
| **tap** | Side effects |
| **take** | Take n values |
| **takeUntil** | Take until condition |

## Resources

- [RxJS Documentation](https://rxjs.dev/)
- [Learn RxJS](https://www.learnrxjs.io/)
- [RxJS Marbles](https://rxmarbles.com/)
