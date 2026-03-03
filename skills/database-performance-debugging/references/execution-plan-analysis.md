# Execution Plan Analysis

## Execution Plan Analysis

```yaml
EXPLAIN Output Understanding:

Seq Scan (Full Table Scan):
  - Reads entire table
  - Slowest method
  - Fix: Add index

Index Scan:
  - Uses index
  - Fast
  - Ideal

Bitmap Index Scan:
  - Partial index scan
  - Converts to heap scan
  - Moderate speed

Nested Loop:
  - For each row in left, scan right
  - O(n*m) complexity
  - Slow for large tables

Hash Join:
  - Build hash table of smaller table
  - Probe with larger table
  - Faster than nested loop

Merge Join:
  - Sort both tables, merge
  - Fastest for large sorted data
  - Requires sort operation

---

Reading EXPLAIN ANALYZE:

Node: Seq Scan on orders (actual 8023.456 ms)
  - Seq Scan = Full table scan
  - actual time = real execution time
  - 8023 ms = TOO SLOW

Rows: 1000000 (estimated) 1000000 (actual)
  - Match = planner accurate
  - Mismatch = update statistics

Node: Index Scan (actual 15.234 ms)
  - Index Scan = Fast
  - 15 ms = ACCEPTABLE
```
