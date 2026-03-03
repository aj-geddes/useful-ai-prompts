# Profiling Tools

## Profiling Tools

```yaml
Browser Profiling:

Chrome DevTools:
  Steps:
    1. DevTools → Performance
    2. Click record
    3. Perform action
    4. Stop recording
    5. Analyze flame chart
  Metrics:
    - Function call duration
    - Call frequency
    - Total time vs self time

Firefox Profiler:
  - Built-in performance profiler
  - Flame graphs
  - Timeline view
  - Export and share

React Profiler:
  - DevTools → Profiler
  - Component render times
  - Phase: render vs commit
  - Why component re-rendered

---

Node.js Profiling:

node --prof app.js
node --prof-process isolate-*.log > profile.txt

Clinic.js:
  clinic doctor -- node app.js
  clinic flame -- node app.js
  Shows: functions, memory, delays

V8 Inspector:
  node --inspect app.js
  Open chrome://inspect
  Profiler tab
  Take CPU profile
```
