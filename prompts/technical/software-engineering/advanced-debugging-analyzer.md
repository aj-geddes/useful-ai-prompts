# Advanced Debugging Analyzer

## Metadata
- **Created**: 2025-07-15

- **Category**: Technical/Software-Engineering
- **Tags**: debugging, troubleshooting, root cause analysis, performance debugging, diagnostics
- **Version**: 2.0.0
- **Use Cases**: bug diagnosis, performance issues, memory leaks, system debugging
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you systematically debug complex software issues through structured analysis, hypothesis testing, and root cause identification.

## Prompt

```
I'll help you debug this issue systematically. Let me gather information to understand the problem:

**About the issue:**
1. What's the specific problem or error you're experiencing?
2. When did it start happening? (after a deployment, randomly, specific time)
3. How frequently does it occur? (always, intermittently, under load)
4. What's the impact? (crashes, wrong output, performance degradation)

**Environment details:**
5. What's your tech stack? (languages, frameworks, databases)
6. What environment? (production, staging, local)
7. Has anything changed recently? (code, config, infrastructure)
8. Can you reproduce it consistently?

**Diagnostic data:**
9. What error messages or logs do you have?
10. Any metrics or monitoring data available?
11. What have you already tried?
12. Any patterns you've noticed?

Based on your answers, I'll provide:

**ROOT CAUSE ANALYSIS** - Systematic investigation approach
**DEBUGGING STRATEGY** - Step-by-step troubleshooting plan
**DIAGNOSTIC TOOLS** - Specific tools and commands to use
**SOLUTION OPTIONS** - Potential fixes with trade-offs
**PREVENTION PLAN** - How to avoid similar issues

Share your debugging challenge and let's solve it together!
```

## Example Usage

**User Input:**
```
1. API endpoints randomly return 502 errors, but retry usually works
2. Started 3 days ago after deploying new feature with database queries
3. Happens ~5% of requests, spikes during high traffic (>1000 req/min)
4. Users see errors, have to retry, affecting checkout conversion

5. Node.js API, PostgreSQL database, Redis cache, nginx reverse proxy, AWS ECS
6. Production only - can't reproduce in staging even with load tests
7. Deployed new recommendation engine that queries user history
8. No - it's intermittent and seems load-dependent

9. Nginx logs: "upstream timed out (110: Connection timed out)"
10. CPU normal, memory stable, but database connections spike to max (100)
11. Increased connection pool to 150, added indexes, still happening
12. Correlates with recommendation API calls, worse during flash sales
```

**Assistant Output:**

Based on your 502 timeout issues, here's a systematic debugging approach:

## ROOT CAUSE ANALYSIS

### Hypothesis Ranking
1. **Connection pool exhaustion** (90% confidence)
   - New feature creates N+1 query problem
   - Connections held too long under load
   
2. **Slow queries blocking pool** (70% confidence)
   - Missing indexes on recommendation queries
   - Lock contention on hot rows

3. **Resource leak** (40% confidence)
   - Connections not properly released
   - Transaction not committed/rolled back

### Evidence Analysis
- **Timing**: Issue started with recommendation engine ✓
- **Pattern**: Load-dependent, connection spike ✓
- **Symptom**: 502s = nginx timeout waiting for backend ✓
- **Key clue**: Retries work = transient resource issue ✓

## DEBUGGING STRATEGY

### Step 1: Immediate Diagnostics (Do Now)

**Database Connection Analysis**:
```sql
-- Current connections by state
SELECT state, count(*) 
FROM pg_stat_activity 
GROUP BY state;

-- Long-running queries
SELECT pid, now() - query_start AS duration, query 
FROM pg_stat_activity 
WHERE state != 'idle' 
ORDER BY duration DESC;

-- Connections per application
SELECT application_name, count(*) 
FROM pg_stat_activity 
GROUP BY application_name;
```

**Application-Level Debugging**:
```javascript
// Add connection pool monitoring
const poolStats = {
  available: pool.availableCount,
  waiting: pool.waitingCount,
  total: pool.totalCount
};
console.log('Pool stats:', poolStats);

// Log slow queries
db.on('query', (query) => {
  const start = Date.now();
  query.on('end', () => {
    const duration = Date.now() - start;
    if (duration > 1000) {
      console.error('Slow query:', duration, query.sql);
    }
  });
});
```

### Step 2: Deep Dive Analysis

**Query Performance Check**:
```sql
-- Find slow queries from recommendations
SELECT 
  query,
  calls,
  mean_exec_time,
  total_exec_time
FROM pg_stat_statements
WHERE query LIKE '%recommendation%'
ORDER BY mean_exec_time DESC
LIMIT 10;
```

**Connection Leak Detection**:
```javascript
// Track connection lifecycle
let activeConnections = new Map();

db.on('acquire', (connection) => {
  activeConnections.set(connection.id, {
    acquired: new Date(),
    stack: new Error().stack
  });
});

db.on('release', (connection) => {
  activeConnections.delete(connection.id);
});

// Log connections held >5 seconds
setInterval(() => {
  const now = Date.now();
  activeConnections.forEach((info, id) => {
    if (now - info.acquired > 5000) {
      console.error('Long-held connection:', id, info.stack);
    }
  });
}, 5000);
```

### Step 3: Load Testing with Monitoring

**Reproduce in Staging**:
```bash
# Monitor connections while load testing
watch -n1 "psql -c \"SELECT count(*) FROM pg_stat_activity WHERE state = 'active'\""

# In another terminal, gradually increase load
for rate in 100 500 1000 1500; do
  echo "Testing at $rate req/min"
  artillery run -t https://staging-api.com \
    --rate $rate \
    --duration 300 \
    loadtest.yml
  sleep 60
done
```

## DIAGNOSTIC TOOLS

### Essential Commands

**1. Database Diagnostics**:
```bash
# Real-time query monitoring
pg_stat_activity | grep -v idle

# Connection pool efficiency
SELECT 
  datname,
  numbackends,
  xact_commit,
  xact_rollback,
  blks_read,
  blks_hit
FROM pg_stat_database;

# Lock monitoring
SELECT 
  blocked_locks.pid AS blocked_pid,
  blocking_locks.pid AS blocking_pid,
  blocked_activity.query AS blocked_query,
  blocking_activity.query AS blocking_query
FROM pg_catalog.pg_locks blocked_locks
JOIN pg_catalog.pg_stat_activity blocked_activity 
  ON blocked_activity.pid = blocked_locks.pid
JOIN pg_catalog.pg_locks blocking_locks 
  ON blocking_locks.locktype = blocked_locks.locktype
  AND blocking_locks.pid != blocked_locks.pid
JOIN pg_catalog.pg_stat_activity blocking_activity 
  ON blocking_activity.pid = blocking_locks.pid;
```

**2. Application Performance Monitoring**:
```javascript
// Add APM instrumentation
const apm = require('elastic-apm-node').start({
  serviceName: 'api',
  secretToken: process.env.APM_TOKEN
});

// Trace recommendation queries
async function getRecommendations(userId) {
  const span = apm.startSpan('recommendations.fetch');
  try {
    // Your query logic
    return results;
  } finally {
    span.end();
  }
}
```

## SOLUTION OPTIONS

### Option 1: Query Optimization (Recommended)
**Implementation**:
```javascript
// Before: N+1 query problem
async function getRecommendations(userId) {
  const user = await db.query('SELECT * FROM users WHERE id = $1', [userId]);
  const history = await db.query('SELECT * FROM orders WHERE user_id = $1', [userId]);
  
  for (const order of history) {
    const items = await db.query('SELECT * FROM order_items WHERE order_id = $1', [order.id]);
    // More queries...
  }
}

// After: Optimized single query
async function getRecommendations(userId) {
  const result = await db.query(`
    WITH user_history AS (
      SELECT oi.product_id, COUNT(*) as purchase_count
      FROM orders o
      JOIN order_items oi ON o.id = oi.order_id
      WHERE o.user_id = $1
      GROUP BY oi.product_id
    )
    SELECT p.*, uh.purchase_count
    FROM products p
    JOIN user_history uh ON p.id = uh.product_id
    ORDER BY uh.purchase_count DESC
    LIMIT 10
  `, [userId]);
  
  return result.rows;
}
```

**Pros**: Fixes root cause, dramatic performance improvement
**Cons**: Requires code changes, testing

### Option 2: Connection Pool Tuning
```javascript
// Implement connection queueing and timeouts
const pool = new Pool({
  max: 100,
  idleTimeoutMillis: 30000,
  connectionTimeoutMillis: 5000,
  queueLimit: 200,  // Queue requests instead of failing
  acquireTimeoutMillis: 10000  // Wait up to 10s for connection
});
```

### Option 3: Circuit Breaker Pattern
```javascript
const CircuitBreaker = require('opossum');

const options = {
  timeout: 3000,
  errorThresholdPercentage: 10,
  resetTimeout: 30000
};

const breaker = new CircuitBreaker(getRecommendations, options);

breaker.fallback(() => {
  // Return cached or default recommendations
  return getCachedRecommendations();
});
```

## PREVENTION PLAN

### 1. Query Performance Budget
```javascript
// Enforce query time limits
db.setQueryTimeout(1000); // 1 second max

// Alert on slow queries
if (queryTime > 500) {
  metrics.increment('slow_query', { query: queryName });
}
```

### 2. Load Testing in CI/CD
```yaml
# .github/workflows/load-test.yml
- name → Load Test
  run: |
    artillery run load-test.yml
    artillery report --output report.html
    
- name → Check Performance
  run: |
    p95_response_time=$(jq '.aggregate.latency.p95' report.json)
    if [ $p95_response_time -gt 1000 ]; then
      echo "P95 response time too high: ${p95_response_time}ms"
      exit 1
    fi
```

### 3. Connection Pool Monitoring
```javascript
// Add Prometheus metrics
const poolMetrics = new client.Gauge({
  name: 'db_pool_connections',
  help: 'Database connection pool stats',
  labelNames: ['state']
});

setInterval(() => {
  poolMetrics.set({ state: 'active' }, pool.totalCount);
  poolMetrics.set({ state: 'idle' }, pool.idleCount);
  poolMetrics.set({ state: 'waiting' }, pool.waitingCount);
}, 5000);
```

### Next Steps
1. Run the connection analysis queries immediately
2. Deploy connection monitoring code to production
3. Implement query optimization for recommendations
4. Set up alerts for connection pool saturation
5. Add circuit breaker for graceful degradation

The root cause is likely the N+1 query pattern in your recommendation engine. Fix that first, then implement the monitoring to prevent future issues.

## Related Prompts

- [Performance Optimization Expert](../../management-leadership/performance-management-expert.md)
- [Database Query Optimizer](../../technical-workflows/database-schema-development-expert.md)
- [System Architecture Reviewer](../../technical-workflows/system-architecture-design-expert.md)
