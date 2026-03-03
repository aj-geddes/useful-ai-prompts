# Memory Leak Detection

## Memory Leak Detection

```python
# Identify and fix memory leaks

class MemoryLeakDebug:
    def identify_leaks(self):
        """Common patterns"""
        return {
            'circular_references': {
                'problem': 'Objects reference each other, prevent GC',
                'example': 'parent.child = child; child.parent = parent',
                'solution': 'Use weak references or cleaner code'
            },
            'event_listeners': {
                'problem': 'Listeners not removed',
                'example': 'element.addEventListener(...) without removeEventListener',
                'solution': 'Always remove listeners on cleanup'
            },
            'timers': {
                'problem': 'setInterval/setTimeout not cleared',
                'example': 'setInterval(() => {}, 1000) never clearInterval',
                'solution': 'Store ID and clear on unmount'
            },
            'cache_unbounded': {
                'problem': 'Cache grows without bounds',
                'example': 'cache[key] = value (never deleted)',
                'solution': 'Implement TTL or size limits'
            },
            'dom_references': {
                'problem': 'Removed DOM elements still referenced',
                'example': 'var x = document.getElementById("removed")',
                'solution': 'Clear references after removal'
            }
        }

    def detect_in_browser(self):
        """JavaScript detection"""
        return """
// Monitor memory growth
setInterval(() => {
  const mem = performance.memory;
  const used = mem.usedJSHeapSize / 1000000;
  console.log(`Memory: ${used.toFixed(1)} MB`);
}, 1000);

// If grows over time without plateau = leak
"""
```
