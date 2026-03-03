# fast-check for JavaScript/TypeScript

## fast-check for JavaScript/TypeScript

```typescript
// string.test.ts
import * as fc from "fast-check";

describe("String Operations", () => {
  test("reverse twice returns original", () => {
    fc.assert(
      fc.property(fc.string(), (s) => {
        const reversed = s.split("").reverse().join("");
        const doubleReversed = reversed.split("").reverse().join("");
        return s === doubleReversed;
      }),
    );
  });

  test("concatenation length", () => {
    fc.assert(
      fc.property(fc.string(), fc.string(), (s1, s2) => {
        return (s1 + s2).length === s1.length + s2.length;
      }),
    );
  });

  test("uppercase is idempotent", () => {
    fc.assert(
      fc.property(fc.string(), (s) => {
        const once = s.toUpperCase();
        const twice = once.toUpperCase();
        return once === twice;
      }),
    );
  });
});

// array.test.ts
import * as fc from "fast-check";

function quickSort(arr: number[]): number[] {
  if (arr.length <= 1) return arr;
  const pivot = arr[Math.floor(arr.length / 2)];
  const left = arr.filter((x) => x < pivot);
  const middle = arr.filter((x) => x === pivot);
  const right = arr.filter((x) => x > pivot);
  return [...quickSort(left), ...middle, ...quickSort(right)];
}

describe("Sorting Properties", () => {
  test("sorted array is ordered", () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        const sorted = quickSort(arr);
        for (let i = 0; i < sorted.length - 1; i++) {
          if (sorted[i] > sorted[i + 1]) return false;
        }
        return true;
      }),
    );
  });

  test("sorting preserves length", () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        return quickSort(arr).length === arr.length;
      }),
    );
  });

  test("sorting preserves elements", () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        const sorted = quickSort(arr);
        const originalSorted = [...arr].sort((a, b) => a - b);
        return JSON.stringify(sorted) === JSON.stringify(originalSorted);
      }),
    );
  });

  test("sorting is idempotent", () => {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        const once = quickSort(arr);
        const twice = quickSort(once);
        return JSON.stringify(once) === JSON.stringify(twice);
      }),
    );
  });
});

// object.test.ts
import * as fc from "fast-check";

interface User {
  id: number;
  name: string;
  email: string;
  age: number;
}

const userArbitrary = fc.record({
  id: fc.integer(),
  name: fc.string({ minLength: 1 }),
  email: fc.emailAddress(),
  age: fc.integer({ min: 0, max: 120 }),
});

describe("User Validation", () => {
  test("serialization round trip", () => {
    fc.assert(
      fc.property(userArbitrary, (user) => {
        const json = JSON.stringify(user);
        const parsed = JSON.parse(json);
        return JSON.stringify(parsed) === json;
      }),
    );
  });

  test("age validation", () => {
    fc.assert(
      fc.property(userArbitrary, (user) => {
        return user.age >= 0 && user.age <= 120;
      }),
    );
  });
});

// custom generators
const positiveIntegerArray = fc.array(fc.integer({ min: 1 }), { minLength: 1 });

test("sum of positives is positive", () => {
  fc.assert(
    fc.property(positiveIntegerArray, (arr) => {
      const sum = arr.reduce((a, b) => a + b, 0);
      return sum > 0;
    }),
  );
});

// test with shrinking
test("find minimum failing case", () => {
  try {
    fc.assert(
      fc.property(fc.array(fc.integer()), (arr) => {
        // This will fail for arrays with negative numbers
        return arr.every((n) => n >= 0);
      }),
    );
  } catch (error) {
    // fast-check will shrink to minimal failing case: [-1] or similar
    console.log("Minimal failing case found:", error);
  }
});
```
