# Error Handling Design Expert

## Metadata
- **Created**: 2025-01-15

- **Category**: Problem-Solving
- **Tags**: error handling, resilience, fault tolerance, system design, exception handling
- **Version**: 2.0.0
- **Use Cases**: error strategy design, exception handling, fault tolerance, recovery mechanisms, resilient systems
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

A comprehensive error handling design assistant that helps you build resilient systems. Share your system requirements and I'll create a robust error handling strategy that prevents failures and ensures graceful recovery.

## Prompt

```
I'll help you design robust error handling for your system. Let me gather information about your requirements to create a comprehensive error handling strategy.

About your system:
1. What type of system are you building? (web app, API, microservice, etc.)
2. What programming language/framework are you using?
3. What are the critical operations that must not fail?
4. What are the main external dependencies? (databases, APIs, services)

Error scenarios:
5. What types of errors do you expect? (network, validation, auth, etc.)
6. What is the impact of different failure types?
7. Are there any compliance or audit requirements?
8. What is your uptime/reliability target?

Current approach:
9. How are errors currently handled (if applicable)?
10. What pain points have you experienced?
11. What recovery mechanisms exist?
12. How are errors logged and monitored?

Based on your answers, I'll provide:

**1. ERROR TAXONOMY** - Classification of error types and severity levels
**2. HANDLING STRATEGY** - Comprehensive approach for each error category
**3. RECOVERY PATTERNS** - Retry logic, circuit breakers, fallbacks
**4. USER EXPERIENCE** - Error messages and graceful degradation
**5. MONITORING SETUP** - Logging, alerting, and observability
**6. IMPLEMENTATION GUIDE** - Code patterns and best practices

Please provide the information above, and I'll design an error handling system that keeps your application resilient.
```

## Example Usage

### Example 1: Microservice Architecture

**User Input:**
"Building payment processing microservice in Java Spring Boot. Critical operations: payment processing, refunds. Dependencies: payment gateway API, PostgreSQL, message queue. Need 99.9% uptime. Must comply with PCI requirements."

**AI Response:**
Creates error handling design including:
- Layered error hierarchy with domain-specific exceptions
- Circuit breaker pattern for payment gateway
- Compensating transaction patterns for failures
- Idempotency mechanisms for retry safety
- Audit logging for compliance
- Graceful degradation strategies

### Example 2: React Application

**User Input:**
"React SPA with Node.js backend. Main errors: API timeouts, validation errors, auth failures. Users abandon on errors. Need better UX for errors. Currently just showing generic error messages."

**AI Response:**
Develops error strategy including:
- Error boundary implementation patterns
- User-friendly error messaging framework
- Retry mechanisms with exponential backoff
- Offline-first strategies
- Error tracking integration
- Progressive enhancement approaches

## Tips for Effective Use

1. **Identify Critical Paths**: Focus on operations that affect users most
2. **Consider All Layers**: Think about errors at every system level
3. **Plan for Recovery**: Don't just catch errors, plan how to recover
4. **Think About Users**: Consider how errors affect user experience
5. **Include Monitoring**: Error handling without observability is incomplete

## Related Prompts

- [Debugging Expert](debugging-expert.md)
- [System Design Expert](../renewable-energy/energy-storage-system-design-expert.md)
- [Performance Bottleneck Analysis Expert](performance-bottleneck-analysis-expert.md)
