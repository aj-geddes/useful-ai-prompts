# Flame Graph Generation

## Flame Graph Generation

```bash
# Generate flame graph using 0x
npx 0x -o flamegraph.html node server.js

# Or using clinic.js
npx clinic doctor --on-port 'autocannon localhost:3000' -- node server.js
npx clinic flame --on-port 'autocannon localhost:3000' -- node server.js
```
