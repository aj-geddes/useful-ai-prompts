# Analysis & Interpretation

## Analysis & Interpretation

```javascript
// Understanding profiles

Flame Graph Reading:
- Wider = more time spent
- Taller = deeper call stack
- Hot path = wide tall bars
- Idle = gaps

Self Time vs Total Time:
- Self: time in function itself
- Total: self + children
- Example:
  main() calls work() for 1s
  work() itself = 0.5s (self)
  work() itself + children = 1s (total)

Hot Spots Identification:
- Find widest bars (most time)
- Check if avoidable
- Check if optimizable
- Profile before/after changes

Example (V8 Analysis):
Function: dataProcessing
  Self time: 500ms (50%)
  Total time: 1000ms
  Calls: 1000 times
  Time per call: 0.5ms
  Optimization: Reduce call frequency
```
