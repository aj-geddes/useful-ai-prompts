# Optimization Techniques

## Optimization Techniques

```yaml
Memory Optimization:

Object Pooling:
  Pattern: Reuse objects instead of creating new
  Example: GameObject pool in games
  Benefits: Reduce GC, stable memory
  Trade-off: Complexity

Lazy Loading:
  Pattern: Load data only when needed
  Example: Infinite scroll
  Benefits: Lower peak memory
  Trade-off: Complexity

Pagination:
  Pattern: Process data in chunks
  Example: 1M records → 1K per page
  Benefits: Constant memory
  Trade-off: More requests

Stream Processing:
  Pattern: Process one item at a time
  Example: fs.createReadStream()
  Benefits: Constant memory for large data
  Trade-off: Slower if cached

Memoization:
  Pattern: Cache expensive calculations
  Benefits: Faster, reuse results
  Trade-off: Memory for speed

---

Framework-Specific:

React:
  - useMemo for expensive calculations
  - useCallback to avoid creating functions
  - Code splitting / lazy loading
  - Windowing for long lists (react-window)

Node.js:
  - Stream instead of loadFile
  - Limit cluster workers
  - Set heap size: --max-old-space-size=4096
  - Monitor with clinic.js

---

GC (Garbage Collection):

Minimize:
  - Object creation
  - Large allocations
  - Frequent new objects
  - String concatenation

Example (Bad):
let result = "";
for (let i = 0; i < 1000000; i++) {
  result += i.toString() + ",";
  // Creates new string each iteration
}

Example (Good):
const result = Array.from(
  {length: 1000000},
  (_, i) => i.toString()
).join(",");
// Single allocation
```
