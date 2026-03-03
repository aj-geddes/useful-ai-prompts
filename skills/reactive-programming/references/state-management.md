# State Management

## State Management

```typescript
import { BehaviorSubject } from "rxjs";
import { map } from "rxjs/operators";

interface AppState {
  user: { id: string; name: string } | null;
  cart: Array<{ id: string; quantity: number }>;
  loading: boolean;
}

class StateManager {
  private state$ = new BehaviorSubject<AppState>({
    user: null,
    cart: [],
    loading: false,
  });

  // Selectors
  user$ = this.state$.pipe(
    map((state) => state.user),
    distinctUntilChanged(),
  );

  cart$ = this.state$.pipe(
    map((state) => state.cart),
    distinctUntilChanged(),
  );

  cartTotal$ = this.cart$.pipe(
    map((cart) => cart.reduce((sum, item) => sum + item.quantity, 0)),
  );

  loading$ = this.state$.pipe(map((state) => state.loading));

  // Actions
  setUser(user: AppState["user"]): void {
    this.state$.next({
      ...this.state$.value,
      user,
    });
  }

  addToCart(item: { id: string; quantity: number }): void {
    const cart = [...this.state$.value.cart];
    const existing = cart.find((i) => i.id === item.id);

    if (existing) {
      existing.quantity += item.quantity;
    } else {
      cart.push(item);
    }

    this.state$.next({
      ...this.state$.value,
      cart,
    });
  }

  setLoading(loading: boolean): void {
    this.state$.next({
      ...this.state$.value,
      loading,
    });
  }

  getState(): AppState {
    return this.state$.value;
  }
}

// Usage
const store = new StateManager();

store.user$.subscribe((user) => {
  console.log("User:", user);
});

store.cartTotal$.subscribe((total) => {
  console.log("Cart items:", total);
});

store.setUser({ id: "123", name: "John" });
store.addToCart({ id: "item1", quantity: 2 });
```
