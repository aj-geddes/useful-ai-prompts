# Debugging Techniques

## Debugging Techniques

```javascript
// Breakpoints

// Line breakpoint
// Click line number in Sources tab

// Conditional breakpoint
// Right-click line → Add conditional breakpoint
if (userId === 123) {
  // Pauses only when userId is 123
}

// DOM breakpoint
// Right-click element → Break on → subtree modifications
// Pauses when DOM changes

// Event listener breakpoint
// Sources tab → Event Listener Breakpoints
// Pauses on specific event

// Debugger statement
function problematicFunction() {
  debugger;  // Pauses here if DevTools open
  // ... rest of code
}

---

Watch Expressions

// Add variable to watch
// Updates as code executes
watch: {
  userId: 123,
  orders: [],
  total: 0
}

Call Stack
// Shows function call chain
main()
  -> processUser()
    -> validateUser()
      -> PAUSED HERE

Step Controls:
  Step over: Execute current line
  Step into: Enter function
  Step out: Exit function
  Continue: Run to next breakpoint
```
