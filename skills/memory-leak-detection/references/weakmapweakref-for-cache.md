# WeakMap/WeakRef for Cache

## WeakMap/WeakRef for Cache

```typescript
class WeakCache<K extends object, V> {
  private cache = new WeakMap<K, V>();

  set(key: K, value: V): void {
    this.cache.set(key, value);
  }

  get(key: K): V | undefined {
    return this.cache.get(key);
  }

  has(key: K): boolean {
    return this.cache.has(key);
  }

  delete(key: K): void {
    this.cache.delete(key);
  }
}

// Objects can be garbage collected even if in cache
const cache = new WeakCache<object, string>();
let obj = { id: 1 };

cache.set(obj, "data");

// When obj is no longer referenced, it can be GC'd
obj = null as any;
```
