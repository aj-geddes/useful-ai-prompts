# Spring Boot Actuator-Style (Java)

## Spring Boot Actuator-Style (Java)

```java
@RestController
@RequestMapping("/actuator")
public class HealthController {

    @Autowired
    private DataSource dataSource;

    @Autowired
    private RedisTemplate<String, String> redisTemplate;

    @GetMapping("/health")
    public ResponseEntity<Map<String, Object>> health() {
        Map<String, Object> health = new HashMap<>();
        health.put("status", "UP");
        health.put("timestamp", Instant.now().toString());

        Map<String, Object> components = new HashMap<>();

        // Check database
        components.put("db", checkDatabase());

        // Check Redis
        components.put("redis", checkRedis());

        health.put("components", components);

        boolean anyDown = components.values().stream()
            .anyMatch(c -> "DOWN".equals(((Map) c).get("status")));

        if (anyDown) {
            health.put("status", "DOWN");
            return ResponseEntity.status(503).body(health);
        }

        return ResponseEntity.ok(health);
    }

    @GetMapping("/health/liveness")
    public ResponseEntity<Map<String, String>> liveness() {
        Map<String, String> response = new HashMap<>();
        response.put("status", "UP");
        return ResponseEntity.ok(response);
    }

    @GetMapping("/health/readiness")
    public ResponseEntity<Map<String, Object>> readiness() {
        Map<String, Object> readiness = new HashMap<>();

        // Check critical dependencies
        Map<String, Object> dbCheck = checkDatabase();
        readiness.put("database", dbCheck);

        boolean isReady = "UP".equals(dbCheck.get("status"));

        if (isReady) {
            readiness.put("status", "UP");
            return ResponseEntity.ok(readiness);
        } else {
            readiness.put("status", "DOWN");
            return ResponseEntity.status(503).body(readiness);
        }
    }

    private Map<String, Object> checkDatabase() {
        Map<String, Object> result = new HashMap<>();
        long startTime = System.currentTimeMillis();

        try {
            Connection conn = dataSource.getConnection();
            Statement stmt = conn.createStatement();
            ResultSet rs = stmt.executeQuery("SELECT 1");

            long duration = System.currentTimeMillis() - startTime;

            result.put("status", "UP");
            result.put("responseTime", duration + "ms");

            rs.close();
            stmt.close();
            conn.close();
        } catch (Exception e) {
            result.put("status", "DOWN");
            result.put("error", e.getMessage());
        }

        return result;
    }

    private Map<String, Object> checkRedis() {
        Map<String, Object> result = new HashMap<>();
        long startTime = System.currentTimeMillis();

        try {
            redisTemplate.opsForValue().get("health-check");
            long duration = System.currentTimeMillis() - startTime;

            result.put("status", "UP");
            result.put("responseTime", duration + "ms");
        } catch (Exception e) {
            result.put("status", "DOWN");
            result.put("error", e.getMessage());
        }

        return result;
    }
}
```
