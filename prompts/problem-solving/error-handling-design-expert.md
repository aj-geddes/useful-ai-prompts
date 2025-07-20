# Error Handling Design Expert and Resilience Architecture Specialist

## Metadata

- **Category**: Problem-Solving
- **Tags**: error handling, exception design, fault tolerance, resilience patterns, defensive programming
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Master Error Handling Design Expert, Resilience Architecture Specialist
- **Use Cases**: error handling strategy, exception management, fault tolerance design, system resilience, defensive programming
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt combines expert error handling design skills with resilience architecture specialization to create robust, fault-tolerant systems that gracefully handle failures and unexpected conditions. It employs proven error handling patterns, resilience strategies, and defensive programming techniques to build systems that maintain reliability and user experience under adverse conditions.

## Prompt Template

```
You are operating as a dual-expertise error handling design system combining:

1. **Master Error Handling Design Expert** (16+ years experience)
   - Expertise: Exception design, error recovery strategies, fault tolerance patterns, graceful degradation
   - Strengths: Error classification, recovery mechanisms, user experience preservation, debugging facilitation
   - Perspective: Systematic error handling that transforms failures into manageable, recoverable situations

2. **Resilience Architecture Specialist**
   - Expertise: System resilience patterns, fault tolerance architecture, chaos engineering, failure analysis
   - Strengths: Circuit breakers, bulkheads, timeouts, retry strategies, system design for failure
   - Perspective: Building anti-fragile systems that become stronger through exposure to stressors and failures

Apply these error handling frameworks:
- **Defensive Programming**: Proactive error prevention and graceful failure handling
- **Circuit Breaker Pattern**: Automated failure detection and system protection
- **Retry Strategies**: Intelligent retry with exponential backoff and jitter
- **Bulkhead Pattern**: Failure isolation and resource protection

ERROR HANDLING CONTEXT:
- **System Type**: {{web_application_distributed_system_microservices_database_api}}
- **Error Criticality**: {{user_facing_data_integrity_security_performance_availability}}
- **Failure Tolerance**: {{zero_tolerance_low_moderate_high_graceful_degradation}}
- **Recovery Requirements**: {{immediate_fast_standard_manual_eventual}}
- **User Impact**: {{transparent_minimal_noticeable_significant_severe}}
- **System Complexity**: {{simple_moderate_complex_distributed_enterprise}}
- **Integration Dependencies**: {{none_few_many_complex_critical}}
- **Monitoring Capabilities**: {{basic_standard_advanced_comprehensive_intelligent}}
- **Recovery Automation**: {{manual_semi_automated_automated_self_healing}}
- **Business Impact**: {{minimal_moderate_significant_critical_catastrophic}}

ERROR HANDLING SCENARIO:
{{error_types_failure_modes_current_issues_improvement_requirements}}

ERROR HANDLING DESIGN FRAMEWORK:

Phase 1: ERROR ANALYSIS & CLASSIFICATION
1. Error taxonomy and failure mode analysis
2. Error impact assessment and prioritization
3. Recovery requirement definition and constraints
4. Current error handling evaluation and gap analysis

Phase 2: RESILIENCE STRATEGY DESIGN
1. Error handling strategy and pattern selection
2. Recovery mechanism design and implementation planning
3. Fault isolation and containment strategy
4. Monitoring and alerting integration design

Phase 3: IMPLEMENTATION & TESTING
1. Error handling implementation and integration
2. Resilience pattern deployment and configuration
3. Error scenario testing and validation
4. Recovery procedure testing and optimization

Phase 4: MONITORING & IMPROVEMENT
1. Error monitoring and analysis implementation
2. Recovery effectiveness measurement and optimization
3. Continuous resilience improvement and adaptation
4. Error handling knowledge and pattern evolution

DELIVER YOUR ERROR HANDLING DESIGN STRATEGY AS:
```

## COMPREHENSIVE ERROR HANDLING DESIGN STRATEGY

### ERROR HANDLING DESIGN OVERVIEW

**System**: Cloud-Native E-commerce Microservices Platform
**Error Handling Challenge**: Inconsistent error handling across 25+ microservices causing cascading failures
**Current Issues**: 15% transaction failure rate, poor user experience, difficult debugging
**Design Goal**: <2% failure rate with graceful degradation and rapid recovery

**System Architecture Context**:

- **Services**: 25 microservices with complex interdependencies
- **Traffic**: 100,000+ daily transactions across multiple geographical regions
- **Integrations**: Payment gateways, inventory systems, shipping APIs, recommendation engines
- **Infrastructure**: Kubernetes on AWS with auto-scaling and load balancing
- **Monitoring**: Basic logging with limited error correlation and analysis

**Current Error Handling Problems**:

1. **Inconsistent Error Responses**: Different error formats across services
2. **Cascading Failures**: Single service failure affecting entire user transaction
3. **Poor Error Recovery**: Limited retry logic and no circuit breaker implementation
4. **Debugging Complexity**: Insufficient error context and correlation across services
5. **User Experience Degradation**: Generic error messages and complete transaction failures

### EXECUTIVE SUMMARY

**Error Handling Design Strategy**:
Implement comprehensive error handling architecture combining systematic error classification, resilience patterns, intelligent recovery mechanisms, and proactive monitoring to create a fault-tolerant system that maintains excellent user experience despite inevitable failures.

**Resilience Architecture Approach**:

- **Error Taxonomy**: Standardized error classification and handling across all services
- **Resilience Patterns**: Circuit breakers, bulkheads, timeouts, and retry strategies
- **Graceful Degradation**: Fallback mechanisms maintaining core functionality during failures
- **Intelligent Recovery**: Automated recovery with learning and adaptation capabilities
- **Observability Integration**: Comprehensive error monitoring with correlation and analysis

**Key Design Principles**:

1. **Fail Fast, Recover Gracefully**: Quick failure detection with intelligent recovery
2. **Isolation and Containment**: Prevent error propagation across system boundaries
3. **User Experience Preservation**: Maintain functionality and communication during errors
4. **Operational Excellence**: Enable rapid debugging and problem resolution
5. **Continuous Learning**: Adapt error handling based on failure patterns and recovery effectiveness

**Expected Resilience Outcomes**:

- 85% reduction in transaction failure rate (15% to <2%)
- 90% reduction in cascading failure incidents
- 70% improvement in mean time to recovery (MTTR)
- 95% user experience preservation during service degradation
- 80% reduction in debugging and incident resolution time

### ERROR TAXONOMY AND CLASSIFICATION

#### Comprehensive Error Classification System

**Error Category Framework**:

```typescript
// Standardized Error Classification System
enum ErrorCategory {
  // Infrastructure Errors
  NETWORK_ERROR = "NETWORK_ERROR",
  TIMEOUT_ERROR = "TIMEOUT_ERROR",
  RESOURCE_EXHAUSTION = "RESOURCE_EXHAUSTION",
  SERVICE_UNAVAILABLE = "SERVICE_UNAVAILABLE",

  // Business Logic Errors
  VALIDATION_ERROR = "VALIDATION_ERROR",
  BUSINESS_RULE_VIOLATION = "BUSINESS_RULE_VIOLATION",
  AUTHORIZATION_ERROR = "AUTHORIZATION_ERROR",
  DATA_INTEGRITY_ERROR = "DATA_INTEGRITY_ERROR",

  // External Integration Errors
  PAYMENT_GATEWAY_ERROR = "PAYMENT_GATEWAY_ERROR",
  INVENTORY_SERVICE_ERROR = "INVENTORY_SERVICE_ERROR",
  SHIPPING_API_ERROR = "SHIPPING_API_ERROR",
  THIRD_PARTY_API_ERROR = "THIRD_PARTY_API_ERROR",

  // System Errors
  DATABASE_ERROR = "DATABASE_ERROR",
  CONFIGURATION_ERROR = "CONFIGURATION_ERROR",
  SECURITY_ERROR = "SECURITY_ERROR",
  UNKNOWN_ERROR = "UNKNOWN_ERROR",
}

enum ErrorSeverity {
  LOW = "LOW", // Minimal impact, system continues normally
  MEDIUM = "MEDIUM", // Noticeable impact, functionality preserved
  HIGH = "HIGH", // Significant impact, degraded functionality
  CRITICAL = "CRITICAL", // Severe impact, major functionality loss
}

enum RecoveryStrategy {
  IMMEDIATE_RETRY = "IMMEDIATE_RETRY",
  EXPONENTIAL_BACKOFF = "EXPONENTIAL_BACKOFF",
  CIRCUIT_BREAKER = "CIRCUIT_BREAKER",
  FALLBACK_SERVICE = "FALLBACK_SERVICE",
  GRACEFUL_DEGRADATION = "GRACEFUL_DEGRADATION",
  MANUAL_INTERVENTION = "MANUAL_INTERVENTION",
}
```

**Error Impact Analysis Matrix**:

```typescript
// Error Impact Assessment Framework
class ErrorImpactAnalyzer {
  private impactMatrix: Map<ErrorCategory, ErrorImpact>;

  constructor() {
    this.impactMatrix = new Map([
      [
        ErrorCategory.PAYMENT_GATEWAY_ERROR,
        {
          userImpact: "HIGH",
          businessImpact: "CRITICAL",
          systemImpact: "MEDIUM",
          recoveryPriority: "IMMEDIATE",
          fallbackAvailable: true,
          automaticRecovery: true,
        },
      ],
      [
        ErrorCategory.INVENTORY_SERVICE_ERROR,
        {
          userImpact: "MEDIUM",
          businessImpact: "HIGH",
          systemImpact: "LOW",
          recoveryPriority: "HIGH",
          fallbackAvailable: true,
          automaticRecovery: true,
        },
      ],
      [
        ErrorCategory.NETWORK_ERROR,
        {
          userImpact: "MEDIUM",
          businessImpact: "MEDIUM",
          systemImpact: "HIGH",
          recoveryPriority: "HIGH",
          fallbackAvailable: false,
          automaticRecovery: true,
        },
      ],
    ]);
  }

  assessErrorImpact(error: ApplicationError): ErrorHandlingStrategy {
    const impact = this.impactMatrix.get(error.category);

    return {
      immediateAction: this.determineImmediateAction(error, impact),
      recoveryStrategy: this.selectRecoveryStrategy(error, impact),
      userCommunication: this.designUserCommunication(error, impact),
      monitoringEnhancement: this.defineMonitoringRequirements(error, impact),
    };
  }
}
```

#### Error Context and Correlation

**Distributed Error Correlation System**:

```typescript
// Comprehensive Error Context Capture
class ErrorContextCapture {
  captureErrorContext(
    error: Error,
    request: Request,
    service: string,
  ): ErrorContext {
    return {
      // Error Details
      errorId: generateUniqueErrorId(),
      timestamp: new Date().toISOString(),
      service: service,
      errorType: error.constructor.name,
      errorMessage: error.message,
      stackTrace: error.stack,

      // Request Context
      requestId: request.headers["x-request-id"],
      correlationId: request.headers["x-correlation-id"],
      userId: request.user?.id,
      sessionId: request.sessionID,
      userAgent: request.headers["user-agent"],
      ipAddress: request.ip,

      // System Context
      serviceVersion: process.env.SERVICE_VERSION,
      environment: process.env.NODE_ENV,
      hostname: os.hostname(),
      memoryUsage: process.memoryUsage(),
      cpuUsage: process.cpuUsage(),

      // Business Context
      businessContext: this.extractBusinessContext(request),
      transactionState: this.captureTransactionState(request),
      userJourney: this.trackUserJourney(request),

      // Integration Context
      upstreamServices: this.getUpstreamServiceCalls(request),
      downstreamDependencies: this.getActiveDependencies(),
      externalApiCalls: this.getExternalApiContext(request),
    };
  }

  correlateDistributedErrors(
    errorContexts: ErrorContext[],
  ): DistributedErrorAnalysis {
    return {
      rootCauseService: this.identifyRootCause(errorContexts),
      errorPropagationPath: this.traceErrorPropagation(errorContexts),
      affectedServices: this.identifyAffectedServices(errorContexts),
      impactAssessment: this.assessDistributedImpact(errorContexts),
      recoveryRecommendations: this.generateRecoveryPlan(errorContexts),
    };
  }
}
```

### RESILIENCE PATTERNS IMPLEMENTATION

#### Circuit Breaker Pattern Implementation

**Advanced Circuit Breaker with Adaptive Thresholds**:

```typescript
// Intelligent Circuit Breaker Implementation
class AdaptiveCircuitBreaker {
  private state: CircuitState = CircuitState.CLOSED;
  private failureCount: number = 0;
  private successCount: number = 0;
  private lastFailureTime: number = 0;
  private adaptiveThreshold: AdaptiveThresholdCalculator;

  constructor(
    private config: CircuitBreakerConfig,
    private monitoring: CircuitBreakerMonitoring,
  ) {
    this.adaptiveThreshold = new AdaptiveThresholdCalculator(config);
  }

  async execute<T>(
    operation: () => Promise<T>,
    fallback?: () => Promise<T>,
  ): Promise<T> {
    // Check circuit state and decide execution strategy
    switch (this.state) {
      case CircuitState.CLOSED:
        return this.executeInClosedState(operation, fallback);

      case CircuitState.OPEN:
        return this.executeInOpenState(operation, fallback);

      case CircuitState.HALF_OPEN:
        return this.executeInHalfOpenState(operation, fallback);
    }
  }

  private async executeInClosedState<T>(
    operation: () => Promise<T>,
    fallback?: () => Promise<T>,
  ): Promise<T> {
    try {
      const result = await this.executeWithTimeout(operation);
      this.recordSuccess();
      return result;
    } catch (error) {
      this.recordFailure(error);

      // Check if threshold exceeded
      if (this.shouldOpenCircuit()) {
        this.openCircuit();
        this.monitoring.recordCircuitOpened(this.getCircuitMetrics());
      }

      if (fallback) {
        return await fallback();
      }
      throw error;
    }
  }

  private shouldOpenCircuit(): boolean {
    const currentThreshold = this.adaptiveThreshold.calculateThreshold({
      recentFailureRate: this.calculateRecentFailureRate(),
      systemLoad: this.monitoring.getCurrentSystemLoad(),
      dependencyHealth: this.monitoring.getDependencyHealth(),
      timeOfDay: new Date().getHours(),
      historicalPatterns: this.monitoring.getHistoricalFailurePatterns(),
    });

    return (
      this.failureCount >= currentThreshold.failureCount &&
      this.calculateFailureRate() >= currentThreshold.failureRate
    );
  }

  private async executeWithTimeout<T>(operation: () => Promise<T>): Promise<T> {
    return new Promise<T>((resolve, reject) => {
      const timeoutId = setTimeout(() => {
        reject(
          new TimeoutError(`Operation timeout after ${this.config.timeout}ms`),
        );
      }, this.config.timeout);

      operation()
        .then((result) => {
          clearTimeout(timeoutId);
          resolve(result);
        })
        .catch((error) => {
          clearTimeout(timeoutId);
          reject(error);
        });
    });
  }
}
```

#### Retry Strategy with Intelligent Backoff

**Advanced Retry Implementation**:

```typescript
// Intelligent Retry Strategy with Machine Learning
class IntelligentRetryStrategy {
  private retryPatternLearner: RetryPatternLearner;
  private retryMetrics: RetryMetricsCollector;

  constructor(
    private config: RetryConfig,
    private errorClassifier: ErrorClassifier,
  ) {
    this.retryPatternLearner = new RetryPatternLearner();
    this.retryMetrics = new RetryMetricsCollector();
  }

  async executeWithRetry<T>(
    operation: () => Promise<T>,
    context: OperationContext,
  ): Promise<T> {
    let lastError: Error;
    let attempt = 0;

    while (attempt < this.getMaxAttempts(context)) {
      try {
        const result = await operation();

        // Record successful retry pattern for learning
        if (attempt > 0) {
          this.retryPatternLearner.recordSuccessfulRetry({
            attempts: attempt + 1,
            context: context,
            errorTypes: this.getEncounteredErrors(),
            finalOutcome: "SUCCESS",
          });
        }

        return result;
      } catch (error) {
        lastError = error;
        attempt++;

        // Classify error to determine retry eligibility
        const errorAnalysis = this.errorClassifier.analyzeError(error);

        if (!errorAnalysis.isRetryable) {
          this.retryMetrics.recordNonRetryableError(error, context);
          throw error;
        }

        if (attempt < this.getMaxAttempts(context)) {
          const delay = this.calculateIntelligentDelay(
            attempt,
            errorAnalysis,
            context,
          );

          this.retryMetrics.recordRetryAttempt(attempt, delay, error);
          await this.delay(delay);
        }
      }
    }

    // All retries exhausted
    this.retryPatternLearner.recordFailedRetry({
      attempts: attempt,
      context: context,
      errorTypes: this.getEncounteredErrors(),
      finalOutcome: "FAILURE",
    });

    throw new RetryExhaustedException(
      `Operation failed after ${attempt} attempts`,
      lastError,
    );
  }

  private calculateIntelligentDelay(
    attempt: number,
    errorAnalysis: ErrorAnalysis,
    context: OperationContext,
  ): number {
    // Base exponential backoff
    const baseDelay = Math.min(
      this.config.baseDelay * Math.pow(2, attempt - 1),
      this.config.maxDelay,
    );

    // Apply intelligent adjustments based on error type
    const errorMultiplier = this.getErrorTypeMultiplier(
      errorAnalysis.errorType,
    );

    // Apply context-aware adjustments
    const contextMultiplier = this.getContextMultiplier(context);

    // Apply jitter to prevent thundering herd
    const jitter = Math.random() * 0.3 + 0.7; // 70-100% of calculated delay

    // Apply machine learning insights
    const mlMultiplier = this.retryPatternLearner.getOptimalDelayMultiplier(
      errorAnalysis,
      context,
    );

    return Math.round(
      baseDelay * errorMultiplier * contextMultiplier * jitter * mlMultiplier,
    );
  }
}
```

#### Bulkhead Pattern for Resource Isolation

**Resource Isolation Implementation**:

```typescript
// Bulkhead Pattern for Resource Protection
class ResourceBulkheadManager {
  private resourcePools: Map<string, ResourcePool>;
  private resourceMonitor: ResourceMonitor;

  constructor(config: BulkheadConfig) {
    this.resourcePools = new Map();
    this.resourceMonitor = new ResourceMonitor();
    this.initializeResourcePools(config);
  }

  private initializeResourcePools(config: BulkheadConfig): void {
    // Critical operations pool
    this.resourcePools.set(
      "critical",
      new ResourcePool({
        maxConcurrent: config.criticalPool.maxConcurrent,
        queueSize: config.criticalPool.queueSize,
        timeout: config.criticalPool.timeout,
        priority: Priority.HIGH,
        isolationLevel: IsolationLevel.STRICT,
      }),
    );

    // Normal operations pool
    this.resourcePools.set(
      "normal",
      new ResourcePool({
        maxConcurrent: config.normalPool.maxConcurrent,
        queueSize: config.normalPool.queueSize,
        timeout: config.normalPool.timeout,
        priority: Priority.MEDIUM,
        isolationLevel: IsolationLevel.MODERATE,
      }),
    );

    // Background operations pool
    this.resourcePools.set(
      "background",
      new ResourcePool({
        maxConcurrent: config.backgroundPool.maxConcurrent,
        queueSize: config.backgroundPool.queueSize,
        timeout: config.backgroundPool.timeout,
        priority: Priority.LOW,
        isolationLevel: IsolationLevel.FLEXIBLE,
      }),
    );
  }

  async executeInBulkhead<T>(
    operation: () => Promise<T>,
    bulkheadType: string,
    context: OperationContext,
  ): Promise<T> {
    const pool = this.resourcePools.get(bulkheadType);
    if (!pool) {
      throw new Error(`Unknown bulkhead type: ${bulkheadType}`);
    }

    // Check pool health and availability
    const poolHealth = this.resourceMonitor.assessPoolHealth(bulkheadType);
    if (poolHealth.status === PoolStatus.OVERLOADED) {
      return this.handleOverloadedPool(operation, bulkheadType, context);
    }

    return pool.execute(operation, context);
  }

  private async handleOverloadedPool<T>(
    operation: () => Promise<T>,
    bulkheadType: string,
    context: OperationContext,
  ): Promise<T> {
    // Implement overflow strategies
    switch (bulkheadType) {
      case "critical":
        // Critical operations can borrow from normal pool
        return this.executeInBulkhead(operation, "normal", context);

      case "normal":
        // Normal operations queue with back-pressure
        return this.executeWithBackPressure(operation, context);

      case "background":
        // Background operations can be deferred
        return this.deferOperation(operation, context);

      default:
        throw new BulkheadOverloadedException(
          `Bulkhead ${bulkheadType} is overloaded`,
        );
    }
  }
}
```

### GRACEFUL DEGRADATION STRATEGIES

#### Intelligent Fallback Mechanisms

**Multi-Level Fallback Implementation**:

```typescript
// Comprehensive Fallback Strategy System
class GracefulDegradationManager {
  private fallbackStrategies: Map<string, FallbackStrategy[]>;
  private featureToggleManager: FeatureToggleManager;
  private performanceMonitor: PerformanceMonitor;

  constructor() {
    this.fallbackStrategies = new Map();
    this.featureToggleManager = new FeatureToggleManager();
    this.performanceMonitor = new PerformanceMonitor();
    this.initializeFallbackStrategies();
  }

  private initializeFallbackStrategies(): void {
    // Product recommendation fallbacks
    this.fallbackStrategies.set("product-recommendations", [
      new CachedRecommendationsFallback(),
      new PopularProductsFallback(),
      new CategoryBasedFallback(),
      new StaticRecommendationsFallback(),
    ]);

    // Payment processing fallbacks
    this.fallbackStrategies.set("payment-processing", [
      new AlternatePaymentGatewayFallback(),
      new PaymentQueueingFallback(),
      new ManualPaymentProcessingFallback(),
    ]);

    // Inventory checking fallbacks
    this.fallbackStrategies.set("inventory-check", [
      new CachedInventoryFallback(),
      new EstimatedInventoryFallback(),
      new AlwaysAvailableFallback(),
    ]);
  }

  async executeWithGracefulDegradation<T>(
    primaryOperation: () => Promise<T>,
    operationType: string,
    context: OperationContext,
  ): Promise<DegradedResult<T>> {
    try {
      // Attempt primary operation
      const result = await primaryOperation();
      return {
        result: result,
        degradationLevel: DegradationLevel.NONE,
        fallbackUsed: null,
        performanceImpact: PerformanceImpact.NONE,
      };
    } catch (primaryError) {
      // Execute fallback strategies in order of preference
      const fallbacks = this.fallbackStrategies.get(operationType) || [];

      for (let i = 0; i < fallbacks.length; i++) {
        const fallback = fallbacks[i];

        try {
          // Check if fallback is available and healthy
          if (!(await fallback.isAvailable(context))) {
            continue;
          }

          const fallbackResult = await fallback.execute(context);

          // Log successful fallback usage
          this.logFallbackUsage(operationType, fallback, i + 1, context);

          return {
            result: fallbackResult,
            degradationLevel: fallback.getDegradationLevel(),
            fallbackUsed: fallback.getName(),
            performanceImpact: fallback.getPerformanceImpact(),
          };
        } catch (fallbackError) {
          // Continue to next fallback
          this.logFallbackFailure(fallback, fallbackError, context);
        }
      }

      // All fallbacks failed
      throw new GracefulDegradationFailedException(
        `All fallbacks failed for operation: ${operationType}`,
        primaryError,
      );
    }
  }

  async handlePartialServiceDegradation(
    services: string[],
    degradationLevel: DegradationLevel,
  ): Promise<DegradationPlan> {
    const degradationPlan: DegradationPlan = {
      affectedFeatures: [],
      enabledFeatures: [],
      userCommunication: "",
      estimatedRecoveryTime: null,
    };

    switch (degradationLevel) {
      case DegradationLevel.MINOR:
        // Disable non-essential features
        degradationPlan.affectedFeatures =
          this.getNonEssentialFeatures(services);
        degradationPlan.userCommunication =
          "Some features may be temporarily limited.";
        break;

      case DegradationLevel.MODERATE:
        // Enable basic functionality only
        degradationPlan.enabledFeatures = this.getEssentialFeatures(services);
        degradationPlan.userCommunication =
          "Operating in limited mode. Core features available.";
        break;

      case DegradationLevel.SEVERE:
        // Emergency mode - minimum viable functionality
        degradationPlan.enabledFeatures = this.getCriticalFeatures(services);
        degradationPlan.userCommunication =
          "System maintenance in progress. Limited functionality available.";
        break;
    }

    // Apply degradation plan
    await this.applyDegradationPlan(degradationPlan);

    return degradationPlan;
  }
}
```

### ERROR MONITORING AND OBSERVABILITY

#### Comprehensive Error Analytics

**Error Analytics and Intelligence System**:

```typescript
// Advanced Error Analytics Platform
class ErrorAnalyticsEngine {
  private errorPatternDetector: ErrorPatternDetector;
  private anomalyDetector: AnomalyDetector;
  private predictiveAnalyzer: PredictiveErrorAnalyzer;

  constructor() {
    this.errorPatternDetector = new ErrorPatternDetector();
    this.anomalyDetector = new AnomalyDetector();
    this.predictiveAnalyzer = new PredictiveErrorAnalyzer();
  }

  async analyzeErrorTrends(
    timeWindow: TimeWindow,
  ): Promise<ErrorTrendAnalysis> {
    const errorData = await this.collectErrorData(timeWindow);

    return {
      // Pattern Detection
      repeatingPatterns: this.errorPatternDetector.detectPatterns(errorData),
      emergingTrends: this.identifyEmergingTrends(errorData),
      seasonalPatterns: this.analyzeSeasonalPatterns(errorData),

      // Anomaly Detection
      anomalies: this.anomalyDetector.detectAnomalies(errorData),
      thresholdBreaches: this.identifyThresholdBreaches(errorData),
      unusualErrorTypes: this.detectUnusualErrors(errorData),

      // Predictive Analysis
      riskPrediction: this.predictiveAnalyzer.predictRisks(errorData),
      capacityForecasting: this.forecastCapacityNeeds(errorData),
      maintenanceRecommendations:
        this.generateMaintenanceRecommendations(errorData),

      // Impact Assessment
      businessImpact: this.assessBusinessImpact(errorData),
      userExperienceImpact: this.assessUserExperienceImpact(errorData),
      operationalImpact: this.assessOperationalImpact(errorData),
    };
  }

  generateErrorInsights(analysisResults: ErrorTrendAnalysis): ErrorInsights {
    return {
      prioritizedActions: this.prioritizeActions(analysisResults),
      preventiveRecommendations:
        this.generatePreventiveRecommendations(analysisResults),
      architecturalImprovements:
        this.suggestArchitecturalImprovements(analysisResults),
      processImprovements: this.suggestProcessImprovements(analysisResults),
      toolingRecommendations:
        this.recommendToolingImprovements(analysisResults),
    };
  }
}
```

#### Real-time Error Correlation

**Distributed Error Correlation System**:

```typescript
// Real-time Error Correlation Engine
class ErrorCorrelationEngine {
  private correlationRules: CorrelationRule[];
  private eventStream: EventStream;
  private correlationStore: CorrelationStore;

  constructor() {
    this.correlationRules = this.loadCorrelationRules();
    this.eventStream = new EventStream();
    this.correlationStore = new CorrelationStore();
  }

  async processErrorEvent(errorEvent: ErrorEvent): Promise<CorrelationResult> {
    // Store error event for correlation
    await this.correlationStore.storeEvent(errorEvent);

    // Find related events within time window
    const relatedEvents = await this.findRelatedEvents(errorEvent);

    // Apply correlation rules
    const correlations = this.applyCorrelationRules(errorEvent, relatedEvents);

    // Detect patterns and root causes
    const patternAnalysis = this.analyzeEventPatterns(correlations);

    // Generate correlation insights
    const insights = this.generateCorrelationInsights(patternAnalysis);

    return {
      correlationId: generateCorrelationId(),
      primaryEvent: errorEvent,
      relatedEvents: relatedEvents,
      correlations: correlations,
      rootCauseHypothesis: this.generateRootCauseHypothesis(patternAnalysis),
      impactAssessment: this.assessCorrelatedImpact(correlations),
      recommendedActions: insights.recommendedActions,
      confidenceScore: this.calculateConfidenceScore(correlations),
    };
  }

  private async findRelatedEvents(
    errorEvent: ErrorEvent,
  ): Promise<ErrorEvent[]> {
    const searchCriteria = {
      timeWindow: {
        start: errorEvent.timestamp - TimeWindow.MINUTES_30,
        end: errorEvent.timestamp + TimeWindow.MINUTES_5,
      },
      correlationKeys: [
        errorEvent.correlationId,
        errorEvent.userId,
        errorEvent.sessionId,
        errorEvent.requestId,
      ],
      serviceConnections: this.getConnectedServices(errorEvent.service),
      errorSimilarity: this.calculateErrorSimilarity(errorEvent),
    };

    return await this.correlationStore.findRelatedEvents(searchCriteria);
  }
}
```

## Usage Instructions

1. Begin with comprehensive error analysis and classification to understand failure modes
2. Design resilience architecture using proven patterns like circuit breakers and bulkheads
3. Implement intelligent error handling with context capture and correlation
4. Create graceful degradation strategies that preserve user experience during failures
5. Deploy comprehensive error monitoring and observability systems
6. Establish automated error recovery and self-healing capabilities
7. Build error analytics for pattern detection and predictive analysis
8. Continuously improve error handling based on operational insights and failure patterns

## Examples

### Example 1: Microservices Error Handling

**Input**:

```
{{system_type}}: Distributed microservices architecture
{{error_criticality}}: High - customer-facing transactions
{{integration_dependencies}}: Complex - multiple external APIs
{{failure_tolerance}}: Low - business-critical operations
{{recovery_requirements}}: Fast - sub-second recovery preferred
```

**Output**: [Microservices error handling with circuit breakers, service mesh integration, distributed tracing, and intelligent fallback strategies]

### Example 2: Database Error Handling

**Input**:

```
{{system_type}}: High-availability database system
{{error_criticality}}: Data integrity and availability critical
{{recovery_requirements}}: Immediate - zero data loss tolerance
{{monitoring_capabilities}}: Advanced - comprehensive database monitoring
{{business_impact}}: Critical - system downtime affects revenue
```

**Output**: [Database error handling with connection pooling, transaction management, data consistency checks, and automated failover strategies]

## Related Prompts

- [System Resilience Architect](/prompts/technical/system-resilience.md)
- [Fault Tolerance Designer](/prompts/technical/fault-tolerance.md)
- [Monitoring and Observability Expert](/prompts/technical/monitoring-systems.md)

## Research Notes

- Based on proven resilience patterns and fault tolerance design principles
- Integrates defensive programming with proactive error prevention strategies
- Emphasizes user experience preservation during system failures and degradation
- Focuses on observable and measurable error handling with continuous improvement
- Balances system reliability with performance and maintainability considerations
