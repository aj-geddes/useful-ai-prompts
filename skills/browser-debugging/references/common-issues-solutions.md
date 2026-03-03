# Common Issues & Solutions

## Common Issues & Solutions

```yaml
Issue: JavaScript Error in Console

Error Message: "Uncaught TypeError: Cannot read property 'map' of undefined"

Solution Steps:
  1. Note line number from error
  2. Click line to go to Sources tab
  3. Set breakpoint before error
  4. Check variable values
  5. Trace how undefined value occurred

Example:
  const data = await fetchData();
  const items = data.results.map(x => x.name);
  // Error if results is undefined
  // Add check: const items = data?.results?.map(...)

---

Issue: Element Not Showing (Hidden)

Debug:
  1. Right-click element → Inspect
  2. Check display: none in CSS
  3. Check visibility: hidden
  4. Check opacity: 0
  5. Check position off-screen
  6. Check z-index buried
  7. Check parent hidden

---

Issue: CSS Not Applying

Debug:
  1. Inspect element
  2. View Styles panel
  3. Find CSS rule
  4. Check if crossed out (overridden)
  5. Check specificity
  6. Check media queries
  7. Check !important usage

---

Issue: Memory Leak

Detect:
  1. Memory tab
  2. Take heap snapshot
  3. Perform action
  4. Take another snapshot
  5. Compare (delta)
  6. Objects retained? (leaked)
  7. Check detached DOM nodes

Fix:
  - Remove event listeners
  - Clear timers
  - Release object references
  - Cleanup subscriptions
```
