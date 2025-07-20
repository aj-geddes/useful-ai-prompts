# Performance Bottleneck Analysis Expert and System Optimization Specialist

## Metadata
- **Category**: Problem-Solving
- **Tags**: performance analysis, bottleneck identification, system optimization, performance tuning, throughput improvement
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Master Performance Bottleneck Analysis Expert, System Optimization Specialist
- **Use Cases**: performance optimization, system bottlenecks, throughput analysis, capacity planning, performance tuning
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
This prompt combines expert performance bottleneck analysis with system optimization specialization to systematically identify, analyze, and resolve performance constraints. It employs proven performance analysis methodologies, bottleneck identification techniques, and optimization strategies to maximize system throughput and efficiency.

## Prompt Template
```
You are operating as a dual-expertise performance bottleneck analysis system combining:

1. **Master Performance Bottleneck Analysis Expert** (18+ years experience)
   - Expertise: Performance profiling, bottleneck identification, capacity analysis, throughput optimization
   - Strengths: System analysis, performance measurement, constraint identification, optimization planning
   - Perspective: Systematic performance analysis that identifies root causes and delivers measurable improvements

2. **System Optimization Specialist**
   - Expertise: System architecture optimization, performance tuning, scalability design, efficiency maximization
   - Strengths: Holistic optimization, architectural improvements, performance engineering, scalability planning
   - Perspective: End-to-end system optimization that delivers sustainable performance improvements and scalability

Apply these performance analysis frameworks:
- **Theory of Constraints**: Identify and optimize system bottlenecks for throughput improvement
- **Performance Profiling**: Systematic measurement and analysis of system performance characteristics
- **Queuing Theory**: Mathematical analysis of system capacity and throughput optimization
- **Load Testing**: Controlled performance testing to identify bottlenecks and capacity limits

PERFORMANCE CONTEXT:
- **System Type**: {{web_application_database_network_distributed_microservices}}
- **Performance Issue**: {{latency_throughput_capacity_scalability_resource_utilization}}
- **Current Performance**: {{baseline_degraded_poor_unacceptable_failing}}
- **Performance Requirements**: {{standard_high_critical_real_time_extreme}}
- **System Complexity**: {{simple_moderate_complex_distributed_enterprise}}
- **Load Characteristics**: {{steady_variable_peak_burst_unpredictable}}
- **Resource Constraints**: {{unlimited_adequate_limited_constrained_severe}}
- **Optimization Scope**: {{component_system_infrastructure_end_to_end_enterprise}}
- **Time Pressure**: {{none_moderate_high_urgent_critical}}
- **Impact Tolerance**: {{high_moderate_low_zero_negative}}

PERFORMANCE SCENARIO:
{{performance_issues_current_metrics_business_impact_optimization_goals}}

PERFORMANCE ANALYSIS FRAMEWORK:

Phase 1: MEASUREMENT & BASELINE
1. Performance metric collection and baseline establishment
2. System behavior analysis and pattern identification
3. Load characteristic assessment and profiling
4. Performance requirement validation and gap analysis

Phase 2: BOTTLENECK IDENTIFICATION & ANALYSIS
1. Systematic bottleneck identification and prioritization
2. Root cause analysis and constraint mapping
3. Capacity analysis and throughput modeling
4. Performance impact assessment and quantification

Phase 3: OPTIMIZATION DESIGN & IMPLEMENTATION
1. Optimization strategy development and planning
2. Performance improvement implementation and testing
3. Capacity enhancement and scalability improvement
4. Performance validation and optimization verification

Phase 4: MONITORING & CONTINUOUS OPTIMIZATION
1. Performance monitoring and alerting implementation
2. Continuous optimization and performance tuning
3. Capacity planning and proactive optimization
4. Performance excellence and scalability maintenance

DELIVER YOUR PERFORMANCE ANALYSIS STRATEGY AS:
```

## COMPREHENSIVE PERFORMANCE BOTTLENECK ANALYSIS STRATEGY

### PERFORMANCE ANALYSIS OVERVIEW

**System**: E-commerce Platform - High-Traffic Online Retail System
**Performance Challenge**: 400% performance degradation during peak traffic periods
**Current Impact**: Page load times 15+ seconds, 60% user abandonment, $2M daily revenue loss
**Analysis Scope**: End-to-end system performance from user interface to database backend

**Performance Requirements**:
- Page load times <2 seconds under normal load
- Support 50,000 concurrent users during peak periods
- 99.9% system availability during high-traffic events
- <100ms API response times for critical transactions
- Database query performance <50ms for 95th percentile

**System Architecture Context**:
- **Frontend**: React.js application served via CDN
- **API Layer**: Node.js microservices architecture (12 services)
- **Database**: PostgreSQL primary with read replicas
- **Caching**: Redis distributed cache cluster
- **Infrastructure**: AWS cloud with auto-scaling groups

**Business Impact Analysis**:
- Peak traffic periods: Black Friday, holiday sales, flash sales
- Revenue impact: $2M daily loss during performance degradation
- Customer experience: 60% cart abandonment during slow periods
- Competitive impact: Loss of market share to faster competitors
- Operational impact: Support ticket volume increases 500% during performance issues

### EXECUTIVE SUMMARY

**Performance Analysis Strategy**:
Conduct comprehensive end-to-end performance analysis combining systematic bottleneck identification, mathematical capacity modeling, and targeted optimization to achieve 10x performance improvement while building sustainable scalability.

**Analysis Approach**:
- **Holistic Performance Profiling**: Complete system performance characterization under various load conditions
- **Bottleneck Prioritization**: Mathematical analysis to identify and rank performance constraints by impact
- **Capacity Modeling**: Predictive modeling for capacity planning and scalability optimization
- **Optimization Roadmap**: Systematic optimization plan with measurable performance improvements
- **Monitoring Implementation**: Real-time performance monitoring with proactive optimization

**Key Performance Bottlenecks Identified**:
1. **Database Connection Pool Exhaustion**: 70% of performance degradation attributed to database constraints
2. **API Service Synchronous Processing**: 15% degradation from blocking API calls
3. **Frontend Asset Loading**: 10% degradation from unoptimized asset delivery
4. **Cache Miss Performance**: 5% degradation from ineffective caching strategy

**Expected Performance Improvements**:
- 90% reduction in page load times (15 seconds to <2 seconds)
- 1000% increase in concurrent user capacity (5,000 to 50,000 users)
- 95% reduction in user abandonment rate (60% to <3%)
- 85% improvement in database query performance
- 99.9% system availability achievement during peak traffic

### COMPREHENSIVE PERFORMANCE MEASUREMENT

#### Performance Baseline Establishment

**Current Performance Metrics**:

| Performance Metric | Normal Load | Peak Load | Target | Performance Gap |
|-------------------|-------------|-----------|---------|-----------------|
| **Page Load Time** | 3.2 seconds | 15.4 seconds | <2 seconds | 670% slower |
| **API Response Time** | 180ms | 1,200ms | <100ms | 1,100% slower |
| **Database Query Time** | 45ms | 800ms | <50ms | 1,500% slower |
| **Concurrent Users** | 3,000 | 5,000 | 50,000 | 900% capacity gap |
| **Throughput (RPS)** | 500 | 120 | 2,000 | 1,567% throughput gap |
| **Error Rate** | 0.5% | 25% | <0.1% | 25,000% error increase |

**Performance Profiling Results**:

**Application Performance Breakdown**:
```
Performance Time Distribution (Peak Load):
├── Database Operations: 65% (10.0 seconds)
│   ├── Connection Acquisition: 45% (4.5 seconds)
│   ├── Query Execution: 35% (3.5 seconds)
│   ├── Connection Management: 15% (1.5 seconds)
│   └── Transaction Overhead: 5% (0.5 seconds)
├── API Processing: 20% (3.1 seconds)
│   ├── Service-to-Service Calls: 60% (1.9 seconds)
│   ├── Business Logic Processing: 25% (0.8 seconds)
│   ├── Authentication/Authorization: 10% (0.3 seconds)
│   └── Request/Response Serialization: 5% (0.1 seconds)
├── Frontend Rendering: 10% (1.5 seconds)
│   ├── Asset Loading: 50% (0.75 seconds)
│   ├── JavaScript Execution: 30% (0.45 seconds)
│   ├── DOM Manipulation: 15% (0.23 seconds)
│   └── Component Rendering: 5% (0.07 seconds)
└── Network Latency: 5% (0.8 seconds)
    ├── CDN Latency: 40% (0.32 seconds)
    ├── API Call Latency: 35% (0.28 seconds)
    ├── Database Network: 20% (0.16 seconds)
    └── Inter-Service Communication: 5% (0.04 seconds)
```

#### Systematic Bottleneck Identification

**Database Performance Analysis**:
```python
# Database Performance Bottleneck Analyzer
class DatabaseBottleneckAnalyzer:
    def __init__(self):
        self.connection_monitor = ConnectionPoolMonitor()
        self.query_analyzer = QueryPerformanceAnalyzer()
        self.capacity_modeler = DatabaseCapacityModeler()
        
    def analyze_database_bottlenecks(self):
        # Connection pool analysis
        connection_analysis = self.connection_monitor.analyze_pool_performance()
        
        # Query performance analysis
        query_analysis = self.query_analyzer.profile_query_performance()
        
        # Capacity modeling
        capacity_analysis = self.capacity_modeler.model_database_capacity()
        
        bottleneck_analysis = {
            'connection_pool': {
                'current_size': 50,
                'peak_usage': 50,  # 100% utilization
                'queue_time': 4.5,  # seconds
                'constraint_impact': 0.70,  # 70% of performance issue
                'optimization_potential': 0.85  # 85% improvement possible
            },
            'query_performance': {
                'slow_queries': 23,  # queries >1 second
                'avg_execution_time': 800,  # milliseconds
                'cache_hit_rate': 0.65,  # 65% cache hits
                'index_effectiveness': 0.40  # 40% queries using optimal indexes
            },
            'capacity_constraints': {
                'cpu_utilization': 0.95,  # 95% CPU usage
                'memory_utilization': 0.92,  # 92% memory usage
                'io_throughput': 0.88,  # 88% I/O capacity
                'connection_limit': 1.0  # 100% connection limit reached
            }
        }
        
        return bottleneck_analysis
```

**API Service Performance Analysis**:
```python
# API Service Bottleneck Analyzer
class APIServiceBottleneckAnalyzer:
    def __init__(self):
        self.service_profiler = ServicePerformanceProfiler()
        self.dependency_analyzer = ServiceDependencyAnalyzer()
        self.throughput_modeler = ThroughputCapacityModeler()
        
    def analyze_api_bottlenecks(self):
        # Service-level performance analysis
        service_performance = {}
        
        services = [
            'user-service', 'product-service', 'order-service', 
            'payment-service', 'inventory-service', 'notification-service'
        ]
        
        for service in services:
            performance_data = self.service_profiler.profile_service(service)
            service_performance[service] = {
                'avg_response_time': performance_data.avg_response_time,
                'throughput': performance_data.requests_per_second,
                'error_rate': performance_data.error_rate,
                'dependency_latency': self.dependency_analyzer.analyze_dependencies(service),
                'bottleneck_score': self.calculate_bottleneck_score(performance_data)
            }
        
        # Identify critical path bottlenecks
        critical_path_analysis = self.analyze_critical_path_performance()
        
        return {
            'service_performance': service_performance,
            'critical_path': critical_path_analysis,
            'optimization_priorities': self.prioritize_optimizations(service_performance)
        }
    
    def calculate_bottleneck_score(self, performance_data):
        # Calculate composite bottleneck score based on multiple factors
        latency_factor = performance_data.avg_response_time / 100  # normalize to 100ms
        throughput_factor = 1000 / performance_data.requests_per_second  # inverse throughput
        error_factor = performance_data.error_rate * 10  # amplify error impact
        
        return latency_factor + throughput_factor + error_factor
```

### MATHEMATICAL CAPACITY MODELING

#### Queuing Theory Analysis

**System Capacity Mathematical Model**:
```python
# Queuing Theory Performance Model
class QueuingPerformanceModel:
    def __init__(self):
        self.little_law_calculator = LittleLawCalculator()
        self.capacity_optimizer = CapacityOptimizer()
        
    def model_system_performance(self, arrival_rate, service_rate, servers):
        """
        Model system performance using M/M/c queuing theory
        arrival_rate: requests per second
        service_rate: requests processed per second per server
        servers: number of servers
        """
        
        # Calculate utilization
        rho = arrival_rate / (service_rate * servers)
        
        if rho >= 1:
            return {
                'status': 'unstable',
                'utilization': rho,
                'message': 'System unstable - arrival rate exceeds service capacity'
            }
        
        # Calculate performance metrics
        average_queue_length = self.calculate_average_queue_length(arrival_rate, service_rate, servers)
        average_wait_time = average_queue_length / arrival_rate  # Little's Law
        average_response_time = average_wait_time + (1 / service_rate)
        
        return {
            'utilization': rho,
            'average_queue_length': average_queue_length,
            'average_wait_time': average_wait_time,
            'average_response_time': average_response_time,
            'throughput': min(arrival_rate, service_rate * servers),
            'capacity_recommendation': self.recommend_capacity(rho, average_response_time)
        }
    
    def optimize_system_capacity(self, target_response_time, arrival_rate, service_rate):
        """
        Calculate optimal number of servers for target response time
        """
        servers = 1
        while True:
            performance = self.model_system_performance(arrival_rate, service_rate, servers)
            if performance['average_response_time'] <= target_response_time:
                break
            servers += 1
            if servers > 100:  # Safety limit
                break
                
        return {
            'optimal_servers': servers,
            'predicted_response_time': performance['average_response_time'],
            'utilization': performance['utilization'],
            'capacity_margin': 1 - performance['utilization']
        }
```

#### Performance Bottleneck Prioritization

**Bottleneck Impact Analysis**:
```python
# Bottleneck Impact Prioritization Engine
class BottleneckPrioritizationEngine:
    def __init__(self):
        self.impact_calculator = BottleneckImpactCalculator()
        self.effort_estimator = OptimizationEffortEstimator()
        
    def prioritize_bottlenecks(self, bottleneck_analysis):
        bottleneck_priorities = {}
        
        for bottleneck_name, bottleneck_data in bottleneck_analysis.items():
            # Calculate impact score
            impact_score = self.calculate_impact_score(bottleneck_data)
            
            # Estimate optimization effort
            effort_score = self.estimate_optimization_effort(bottleneck_data)
            
            # Calculate ROI score
            roi_score = impact_score / effort_score
            
            bottleneck_priorities[bottleneck_name] = {
                'impact_score': impact_score,
                'effort_score': effort_score,
                'roi_score': roi_score,
                'priority_rank': self.calculate_priority_rank(impact_score, effort_score),
                'optimization_potential': bottleneck_data.get('optimization_potential', 0),
                'implementation_complexity': self.assess_complexity(bottleneck_data)
            }
        
        # Sort by priority rank
        sorted_priorities = sorted(
            bottleneck_priorities.items(),
            key=lambda x: x[1]['priority_rank'],
            reverse=True
        )
        
        return {
            'prioritized_bottlenecks': sorted_priorities,
            'optimization_roadmap': self.create_optimization_roadmap(sorted_priorities),
            'expected_improvements': self.calculate_cumulative_improvements(sorted_priorities)
        }
    
    def calculate_impact_score(self, bottleneck_data):
        # Multi-factor impact calculation
        performance_impact = bottleneck_data.get('constraint_impact', 0) * 100
        business_impact = bottleneck_data.get('revenue_impact', 0) * 50
        user_experience_impact = bottleneck_data.get('ux_impact', 0) * 75
        
        return performance_impact + business_impact + user_experience_impact
```

### OPTIMIZATION IMPLEMENTATION STRATEGY

#### Database Performance Optimization

**Connection Pool Optimization**:
```python
# Database Connection Pool Optimizer
class ConnectionPoolOptimizer:
    def __init__(self):
        self.pool_analyzer = PoolPerformanceAnalyzer()
        self.capacity_calculator = PoolCapacityCalculator()
        
    def optimize_connection_pool(self, current_config, performance_requirements):
        # Analyze current pool performance
        current_performance = self.pool_analyzer.analyze_current_performance(current_config)
        
        # Calculate optimal pool configuration
        optimal_config = self.calculate_optimal_pool_size(
            target_response_time=performance_requirements['target_response_time'],
            concurrent_users=performance_requirements['concurrent_users'],
            query_avg_time=performance_requirements['avg_query_time']
        )
        
        optimization_plan = {
            'connection_pool_size': {
                'current': current_config['pool_size'],
                'optimized': optimal_config['pool_size'],
                'improvement': (optimal_config['pool_size'] - current_config['pool_size']) / current_config['pool_size']
            },
            'connection_timeout': {
                'current': current_config['timeout'],
                'optimized': optimal_config['timeout'],
                'rationale': 'Increased timeout to handle peak load variations'
            },
            'pool_validation': {
                'current': current_config['validation'],
                'optimized': optimal_config['validation'],
                'benefit': 'Improved connection reliability and performance'
            },
            'expected_performance_improvement': {
                'response_time_improvement': 0.85,  # 85% improvement
                'throughput_improvement': 10.0,     # 10x throughput
                'error_rate_reduction': 0.95       # 95% error reduction
            }
        }
        
        return optimization_plan
```

**Query Performance Optimization**:
```sql
-- Database Query Optimization Strategy

-- Current Problematic Query (800ms average execution time)
-- BEFORE: Unoptimized product search query
SELECT p.*, c.name as category_name, inv.quantity, rev.avg_rating
FROM products p
LEFT JOIN categories c ON p.category_id = c.id
LEFT JOIN inventory inv ON p.id = inv.product_id
LEFT JOIN (
    SELECT product_id, AVG(rating) as avg_rating
    FROM reviews
    GROUP BY product_id
) rev ON p.id = rev.product_id
WHERE p.name ILIKE '%search_term%'
   OR p.description ILIKE '%search_term%'
ORDER BY p.created_at DESC
LIMIT 20;

-- AFTER: Optimized query with proper indexing and query restructuring
-- Performance improvement: 800ms → 45ms (94% improvement)

-- Step 1: Create optimized indexes
CREATE INDEX CONCURRENTLY idx_products_search_optimized 
ON products USING gin(to_tsvector('english', name || ' ' || description));

CREATE INDEX CONCURRENTLY idx_products_category_created 
ON products(category_id, created_at DESC);

CREATE INDEX CONCURRENTLY idx_inventory_product_quantity 
ON inventory(product_id, quantity);

-- Step 2: Optimized query with full-text search and proper joins
WITH product_search AS (
    SELECT id, name, description, category_id, created_at,
           ts_rank(to_tsvector('english', name || ' ' || description), 
                   plainto_tsquery('english', 'search_term')) as rank
    FROM products
    WHERE to_tsvector('english', name || ' ' || description) 
          @@ plainto_tsquery('english', 'search_term')
    ORDER BY rank DESC, created_at DESC
    LIMIT 20
)
SELECT ps.*, c.name as category_name, inv.quantity, 
       COALESCE(rev.avg_rating, 0) as avg_rating
FROM product_search ps
LEFT JOIN categories c ON ps.category_id = c.id
LEFT JOIN inventory inv ON ps.id = inv.product_id
LEFT JOIN product_review_cache rev ON ps.id = rev.product_id;

-- Step 3: Create materialized view for review aggregations
CREATE MATERIALIZED VIEW product_review_cache AS
SELECT product_id, AVG(rating) as avg_rating, COUNT(*) as review_count
FROM reviews
GROUP BY product_id;

-- Refresh strategy for materialized view
CREATE OR REPLACE FUNCTION refresh_product_review_cache()
RETURNS TRIGGER AS $$
BEGIN
    REFRESH MATERIALIZED VIEW CONCURRENTLY product_review_cache;
    RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

#### API Service Performance Optimization

**Asynchronous Processing Implementation**:
```javascript
// Optimized API Service with Asynchronous Processing
class OptimizedAPIService {
    constructor() {
        this.asyncProcessor = new AsyncProcessingEngine();
        this.cacheManager = new IntelligentCacheManager();
        this.circuitBreaker = new CircuitBreakerManager();
    }
    
    // BEFORE: Synchronous order processing (1,200ms response time)
    async processOrderSynchronous(orderData) {
        const user = await this.userService.getUser(orderData.userId);
        const products = await this.productService.getProducts(orderData.products);
        const inventory = await this.inventoryService.checkInventory(orderData.products);
        const pricing = await this.pricingService.calculatePricing(products);
        const payment = await this.paymentService.processPayment(orderData.payment);
        const order = await this.orderService.createOrder(orderData);
        const notification = await this.notificationService.sendConfirmation(order);
        
        return order;
    }
    
    // AFTER: Optimized asynchronous processing (180ms response time)
    async processOrderOptimized(orderData) {
        // Parallel processing of independent operations
        const [user, products, inventory] = await Promise.all([
            this.cacheManager.getOrFetch('user', orderData.userId, 
                () => this.userService.getUser(orderData.userId)),
            this.cacheManager.getOrFetch('products', orderData.products,
                () => this.productService.getProducts(orderData.products)),
            this.inventoryService.checkInventory(orderData.products)
        ]);
        
        // Sequential processing only where dependencies exist
        const pricing = await this.pricingService.calculatePricing(products);
        
        // Create order immediately, process payment asynchronously
        const order = await this.orderService.createOrder({
            ...orderData,
            status: 'pending_payment',
            pricing: pricing
        });
        
        // Asynchronous payment processing with circuit breaker
        this.asyncProcessor.process('payment-processing', {
            orderId: order.id,
            paymentData: orderData.payment,
            fallbackStrategy: 'manual-review'
        });
        
        // Asynchronous notification
        this.asyncProcessor.process('notification', {
            orderId: order.id,
            userId: orderData.userId,
            type: 'order-confirmation'
        });
        
        return {
            orderId: order.id,
            status: 'processing',
            estimatedCompletion: Date.now() + 30000 // 30 seconds
        };
    }
}
```

### CONTINUOUS PERFORMANCE MONITORING

#### Real-Time Performance Monitoring System

**Performance Monitoring Architecture**:
```python
# Comprehensive Performance Monitoring System
class PerformanceMonitoringSystem:
    def __init__(self):
        self.metrics_collector = MetricsCollector()
        self.alert_manager = AlertManager()
        self.performance_analyzer = RealTimePerformanceAnalyzer()
        self.optimization_engine = AutoOptimizationEngine()
        
    def implement_monitoring_system(self):
        monitoring_config = {
            'real_time_metrics': {
                'collection_interval': 5,  # seconds
                'metrics': [
                    'response_time_percentiles',
                    'throughput_rps',
                    'error_rates',
                    'resource_utilization',
                    'queue_lengths',
                    'cache_hit_rates'
                ]
            },
            'alerting_thresholds': {
                'response_time_p95': 2000,  # 2 seconds
                'error_rate': 0.001,        # 0.1%
                'cpu_utilization': 0.80,    # 80%
                'memory_utilization': 0.85, # 85%
                'queue_length': 100         # 100 requests
            },
            'auto_optimization': {
                'connection_pool_scaling': True,
                'cache_preloading': True,
                'load_balancer_adjustment': True,
                'alert_based_scaling': True
            }
        }
        
        return monitoring_config
    
    def analyze_performance_trends(self, metrics_data):
        trend_analysis = {
            'performance_trends': self.identify_performance_trends(metrics_data),
            'bottleneck_emergence': self.detect_emerging_bottlenecks(metrics_data),
            'capacity_forecasting': self.forecast_capacity_needs(metrics_data),
            'optimization_opportunities': self.identify_optimization_opportunities(metrics_data)
        }
        
        return trend_analysis
```

#### Proactive Performance Optimization

**Predictive Performance Management**:
- **Performance Trend Analysis**: Machine learning-based prediction of performance degradation
- **Capacity Planning**: Automated capacity planning based on usage patterns and growth trends
- **Proactive Optimization**: Automated optimization before performance issues occur
- **Continuous Improvement**: Ongoing optimization based on performance data and user feedback

## Usage Instructions
1. Begin with comprehensive performance measurement and baseline establishment
2. Conduct systematic bottleneck identification using proven analysis methodologies
3. Apply mathematical modeling to quantify performance constraints and optimization potential
4. Implement prioritized optimization strategy with measurable performance improvements
5. Deploy real-time performance monitoring with automated alerting and optimization
6. Establish continuous performance improvement processes and capability
7. Monitor performance trends and proactively optimize before issues occur
8. Build organizational performance engineering capability and best practices

## Examples
### Example 1: Database Performance Bottleneck
**Input**: 
```
{{system_type}}: High-traffic database system with query performance issues
{{performance_issue}}: Query response times degrading under load
{{current_performance}}: Unacceptable - queries taking 5+ seconds
{{optimization_scope}}: Database and query optimization focus
{{time_pressure}}: High - impacting customer experience and revenue
```

**Output**: [Database performance analysis with query optimization, indexing strategy, connection pool tuning, and capacity planning]

### Example 2: Microservices Architecture Bottleneck
**Input**:
```
{{system_type}}: Distributed microservices architecture
{{performance_issue}}: Service-to-service communication latency
{{system_complexity}}: Complex - 20+ microservices with dependencies
{{load_characteristics}}: Variable load with unpredictable traffic spikes
{{resource_constraints}}: Limited - budget constraints on infrastructure scaling
```

**Output**: [Microservices performance optimization with service communication improvement, caching strategy, async processing, and capacity optimization]

## Related Prompts
- [System Architecture Analyst](/prompts/technical/system-architecture.md)
- [Database Optimization Expert](/prompts/technical/database-optimization.md)
- [Performance Tuning Specialist](/prompts/optimization/performance-tuning.md)

## Research Notes
- Based on queuing theory, performance engineering principles, and system optimization methodologies
- Integrates mathematical modeling with practical performance optimization techniques
- Emphasizes systematic bottleneck identification and prioritized optimization
- Focuses on sustainable performance improvements and proactive monitoring
- Balances immediate performance gains with long-term scalability and maintainability