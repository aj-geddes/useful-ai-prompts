# Common Memory Leak Patterns

## Common Memory Leak Patterns

```typescript
// BAD: Event listener leak
class BadComponent {
  constructor() {
    window.addEventListener("resize", this.handleResize);
  }

  handleResize = () => {
    // Handler logic
  };

  // Missing cleanup!
}

// GOOD: Proper cleanup
class GoodComponent {
  constructor() {
    window.addEventListener("resize", this.handleResize);
  }

  handleResize = () => {
    // Handler logic
  };

  destroy() {
    window.removeEventListener("resize", this.handleResize);
  }
}

// BAD: Timer leak
function badFunction() {
  setInterval(() => {
    doSomething();
  }, 1000);
  // Interval never cleared!
}

// GOOD: Clear timer
function goodFunction() {
  const intervalId = setInterval(() => {
    doSomething();
  }, 1000);

  return () => clearInterval(intervalId);
}

// BAD: Closure leak
function createClosure() {
  const largeData = new Array(1000000).fill("data");

  return function () {
    // largeData kept in memory even if unused
    console.log("closure");
  };
}

// GOOD: Don't capture unnecessary data
function createClosure() {
  const needed = "small data";

  return function () {
    console.log(needed);
  };
}

// BAD: Global variable accumulation
let cache = [];

function addToCache(item: any) {
  cache.push(item);
  // Cache grows indefinitely!
}

// GOOD: Bounded cache
class BoundedCache {
  private cache: any[] = [];
  private maxSize = 1000;

  add(item: any) {
    this.cache.push(item);
    if (this.cache.length > this.maxSize) {
      this.cache.shift();
    }
  }
}
```
