# Resilience4j-Style (Java)

## Resilience4j-Style (Java)

```java
import io.github.resilience4j.circuitbreaker.CircuitBreaker;
import io.github.resilience4j.circuitbreaker.CircuitBreakerConfig;
import io.github.resilience4j.circuitbreaker.CircuitBreakerRegistry;
import io.vavr.control.Try;

import java.time.Duration;
import java.util.function.Supplier;

public class CircuitBreakerExample {

    public static void main(String[] args) {
        // Create circuit breaker config
        CircuitBreakerConfig config = CircuitBreakerConfig.custom()
            .failureRateThreshold(50)
            .waitDurationInOpenState(Duration.ofMillis(30000))
            .permittedNumberOfCallsInHalfOpenState(2)
            .slidingWindowSize(10)
            .recordExceptions(Exception.class)
            .build();

        // Create registry
        CircuitBreakerRegistry registry = CircuitBreakerRegistry.of(config);

        // Get or create circuit breaker
        CircuitBreaker breaker = registry.circuitBreaker("apiBreaker");

        // Event handlers
        breaker.getEventPublisher()
            .onStateTransition(event ->
                System.out.println("State: " + event.getStateTransition())
            )
            .onError(event ->
                System.out.println("Error: " + event.getThrowable())
            )
            .onSuccess(event ->
                System.out.println("Success")
            );

        // Decorate supplier
        Supplier<String> decoratedSupplier = CircuitBreaker
            .decorateSupplier(breaker, this::callExternalService);

        // Execute with circuit breaker
        Try<String> result = Try.of(decoratedSupplier::get)
            .recover(throwable -> "fallback");

        System.out.println(result.get());
    }

    private String callExternalService() {
        // External service call
        return "data";
    }
}
```
