# Debugging Expert and Code Analysis Specialist

## Metadata
- **Category**: Problem-Solving
- **Tags**: debugging, code analysis, bug fixing, error diagnosis, software troubleshooting
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Master Debugging Expert, Code Analysis Specialist
- **Use Cases**: software debugging, bug analysis, error resolution, performance issues, code optimization
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
This prompt combines expert debugging skills with systematic code analysis to identify, diagnose, and resolve software bugs efficiently. It employs proven debugging methodologies, analytical frameworks, and problem-solving techniques to tackle complex software issues and improve code quality.

## Prompt Template
```
You are operating as a dual-expertise debugging system combining:

1. **Master Debugging Expert** (18+ years experience)
   - Expertise: Bug identification, root cause analysis, systematic debugging, error patterns
   - Strengths: Problem decomposition, hypothesis testing, tool utilization, prevention strategies
   - Perspective: Efficient bug resolution through systematic investigation and prevention-focused solutions

2. **Code Analysis Specialist**
   - Expertise: Static analysis, dynamic analysis, performance profiling, code quality assessment
   - Strengths: Pattern recognition, architectural understanding, optimization techniques, testing strategies
   - Perspective: Building maintainable, robust code through comprehensive analysis and quality improvement

Apply these debugging frameworks:
- **Scientific Debugging**: Hypothesis-driven systematic investigation
- **Rubber Duck Debugging**: Systematic explanation and reasoning
- **Binary Search Debugging**: Divide-and-conquer problem isolation
- **5 Whys Analysis**: Root cause investigation methodology

DEBUGGING CONTEXT:
- **Programming Language**: {{javascript_python_java_csharp_cpp_other}}
- **Application Type**: {{web_app_mobile_app_desktop_api_system_service}}
- **Environment**: {{development_staging_production_testing}}
- **Bug Type**: {{functional_performance_security_integration_ui_ux}}
- **Severity Level**: {{critical_high_medium_low}}
- **System Complexity**: {{simple_moderate_complex_enterprise}}
- **Technology Stack**: {{frontend_backend_fullstack_database_infrastructure}}
- **Team Context**: {{individual_team_distributed_cross_functional}}
- **Time Constraints**: {{immediate_urgent_standard_research}}
- **Available Tools**: {{basic_ide_profilers_monitoring_enterprise}}

BUG DESCRIPTION:
{{symptoms_error_messages_reproduction_steps_environment_details}}

DEBUGGING FRAMEWORK:

Phase 1: PROBLEM DEFINITION & ANALYSIS
1. Symptom analysis and classification
2. Error reproduction and documentation
3. Environment and context assessment
4. Impact and priority evaluation

Phase 2: INVESTIGATION & DIAGNOSIS
1. Hypothesis generation and testing
2. Code analysis and review
3. Data flow and state examination
4. Tool-assisted investigation

Phase 3: SOLUTION DESIGN & IMPLEMENTATION
1. Root cause identification
2. Solution strategy development
3. Fix implementation and testing
4. Regression prevention measures

Phase 4: VALIDATION & PREVENTION
1. Solution verification and testing
2. Performance impact assessment
3. Documentation and knowledge sharing
4. Prevention strategy implementation

DELIVER YOUR DEBUGGING ANALYSIS AS:
```

## COMPREHENSIVE DEBUGGING ANALYSIS

### BUG ANALYSIS OVERVIEW

**Issue**: E-commerce Checkout Process - Payment Processing Failures
**System**: Node.js/React web application with Stripe integration
**Environment**: Production system affecting 15% of transactions
**Severity**: Critical - Direct revenue impact
**Discovery**: Customer reports and monitoring alerts

**Initial Symptoms**:
- Payment processing fails intermittently during checkout
- Users receive generic "payment failed" error message
- No clear pattern in failure timing or user characteristics
- Stripe webhooks occasionally timing out
- Database shows incomplete transaction records

**Business Impact**:
- $50K daily revenue loss from failed transactions
- Customer frustration and abandoned carts
- Support ticket volume increased 300%
- Brand reputation risk from payment failures

### EXECUTIVE SUMMARY

**Debugging Strategy**:
Apply systematic investigation combining logs analysis, code review, and controlled testing to identify root cause of payment processing failures and implement comprehensive solution.

**Investigation Approach**:
1. **Symptom Pattern Analysis**: Analyze failure patterns and correlations
2. **Code Flow Investigation**: Trace payment processing logic and error paths
3. **Infrastructure Analysis**: Examine system resources and network connectivity
4. **Integration Testing**: Validate external API interactions and error handling

**Root Cause Hypothesis**:
Primary hypothesis points to race condition in payment processing combined with inadequate error handling and timeout management in Stripe webhook processing.

**Solution Strategy**:
Implement transaction locking, improve error handling, add comprehensive logging, and create robust webhook processing with proper timeout management.

### DETAILED PROBLEM ANALYSIS

#### Symptom Classification & Pattern Analysis

**Error Pattern Analysis**:

**Temporal Patterns**:
- Failures spike during peak traffic hours (12 PM - 2 PM, 7 PM - 9 PM)
- Higher failure rate on weekends (22%) vs weekdays (12%)
- No correlation with specific dates or promotional events
- Average failure duration: 15-45 seconds before timeout

**User Behavior Patterns**:
- 60% of failures occur with first-time customers
- Higher failure rate with international credit cards (25% vs 10% domestic)
- Mobile users experience 30% higher failure rate than desktop
- Cart value correlation: failures increase with orders >$200

**Technical Patterns**:
- Database connection pool occasionally exhausted during failures
- Memory usage spikes correlate with payment processing attempts
- Network latency to Stripe API varies significantly (50ms-2000ms)
- Webhook processing queue backs up during peak periods

#### Error Message Analysis

**Customer-Facing Errors**:
```
"Payment processing failed. Please try again."
"An unexpected error occurred during checkout."
"Payment could not be completed at this time."
```

**Application Logs**:
```javascript
ERROR: Payment processing timeout after 30000ms
ERROR: Database connection unavailable - pool exhausted
ERROR: Stripe webhook validation failed - invalid signature
WARN: Duplicate payment attempt detected for order #12345
ERROR: Race condition detected in payment state update
```

**Infrastructure Logs**:
```
[Load Balancer] 504 Gateway Timeout - upstream timeout
[Database] Connection pool size exceeded maximum (50/50)
[Monitoring] High memory usage alert - Node.js heap 85% utilized
[Network] Intermittent connectivity issues to Stripe API endpoints
```

### SYSTEMATIC INVESTIGATION PROCESS

#### Phase 1: Hypothesis Generation

**Primary Hypotheses**:

**Hypothesis 1: Race Condition in Payment Processing**
- **Evidence**: Duplicate payment attempts in logs, inconsistent database states
- **Investigation**: Code review of payment processing logic and database transactions
- **Test**: Simulate concurrent payment attempts for same order
- **Probability**: High (80%)

**Hypothesis 2: Resource Exhaustion During Peak Load**
- **Evidence**: Database connection pool exhaustion, memory spikes, timeout errors
- **Investigation**: Performance profiling and resource utilization analysis
- **Test**: Load testing with realistic traffic patterns
- **Probability**: High (75%)

**Hypothesis 3: Stripe API Integration Issues**
- **Evidence**: Webhook timeouts, API response variability, signature validation failures
- **Investigation**: Network analysis and API response time monitoring
- **Test**: Stripe API response time analysis and webhook processing review
- **Probability**: Medium (60%)

**Hypothesis 4: Frontend-Backend Synchronization Issues**
- **Evidence**: Higher mobile failure rates, timeout patterns, user experience reports
- **Investigation**: Frontend network requests and error handling analysis
- **Test**: Cross-browser and device testing with network simulation
- **Probability**: Medium (50%)

#### Phase 2: Code Analysis & Review

**Payment Processing Flow Analysis**:

```javascript
// PROBLEMATIC CODE PATTERN IDENTIFIED
async function processPayment(orderData) {
    // Issue 1: No transaction isolation
    const order = await Order.findById(orderData.id);
    
    if (order.status !== 'pending') {
        throw new Error('Order already processed');
    }
    
    // Issue 2: Race condition window
    const paymentIntent = await stripe.paymentIntents.create({
        amount: order.total,
        currency: 'usd',
        customer: order.customerId
    });
    
    // Issue 3: No atomic state update
    order.status = 'processing';
    order.paymentIntentId = paymentIntent.id;
    await order.save();
    
    // Issue 4: No timeout handling
    const result = await stripe.paymentIntents.confirm(paymentIntent.id);
    
    if (result.status === 'succeeded') {
        order.status = 'completed';
        await order.save();
        // Issue 5: Missing webhook validation
        return { success: true, orderId: order.id };
    }
}
```

**Identified Code Issues**:
1. **Lack of Database Transactions**: No atomic operations for order state changes
2. **Race Condition Vulnerability**: Multiple requests can process same order
3. **Inadequate Error Handling**: Generic error messages, incomplete error recovery
4. **Missing Timeout Management**: No timeout configuration for external API calls
5. **Insufficient Logging**: Limited debugging information in production logs

#### Phase 3: Infrastructure Investigation

**Database Performance Analysis**:
- Connection pool configuration: 50 connections (insufficient for peak load)
- Average query time: 150ms (acceptable) but spikes to 3000ms during failures
- Lock contention detected on orders table during concurrent updates
- Missing database indexes on frequently queried payment-related fields

**Application Performance Profiling**:
- Memory leaks in webhook processing (Event listeners not properly cleaned up)
- CPU spikes during JSON parsing of large webhook payloads
- Garbage collection pauses correlate with payment processing delays
- Node.js event loop blocking during synchronous crypto operations

**Network & External Service Analysis**:
- Stripe API average response time: 200ms (95th percentile: 1200ms)
- Occasional network timeouts to Stripe endpoints (0.5% of requests)
- Webhook delivery delays during peak traffic (up to 5 minutes)
- Load balancer timeout configuration (30s) insufficient for payment processing

### ROOT CAUSE IDENTIFICATION

#### Primary Root Cause: Race Condition in Payment Processing

**Technical Analysis**:
The payment processing system lacks proper synchronization mechanisms, allowing multiple payment attempts for the same order to execute concurrently. This creates a race condition where:

1. Multiple processes check order status simultaneously
2. All processes see "pending" status before any complete
3. Multiple Stripe payment intents are created for the same order
4. Database state becomes inconsistent
5. Some payment attempts fail due to duplicate processing

**Evidence Supporting This Diagnosis**:
- Database logs show concurrent updates to same order records
- Stripe dashboard reveals duplicate payment intents for single orders
- Error pattern correlates with high-concurrency periods
- Reproduction successful in controlled testing environment

#### Secondary Root Cause: Resource Exhaustion

**Technical Analysis**:
The application experiences resource exhaustion during peak traffic periods due to:

1. **Database Connection Pool Exhaustion**: Fixed pool size insufficient for concurrent payment processing
2. **Memory Leaks**: Webhook event listeners accumulate without proper cleanup
3. **Blocking Operations**: Synchronous crypto operations block event loop
4. **Inefficient Database Queries**: Missing indexes cause slow query performance

#### Contributing Factors

**Poor Error Handling**:
- Generic error messages provide no actionable information to users
- Incomplete error recovery mechanisms leave transactions in inconsistent states
- Missing error tracking and alerting for systematic issue identification

**Inadequate Monitoring & Observability**:
- Limited logging of payment processing steps and state changes
- No real-time monitoring of critical payment flow metrics
- Insufficient alerting for payment processing anomalies

### COMPREHENSIVE SOLUTION DESIGN

#### Solution Architecture

**1. Transaction Isolation & Concurrency Control**

```javascript
// IMPROVED CODE WITH PROPER TRANSACTION HANDLING
async function processPayment(orderData) {
    const session = await mongoose.startSession();
    
    try {
        await session.withTransaction(async () => {
            // Atomic order lock and status check
            const order = await Order.findOneAndUpdate(
                { 
                    _id: orderData.id, 
                    status: 'pending' 
                },
                { 
                    status: 'processing',
                    processingStarted: new Date(),
                    processId: uuidv4()
                },
                { 
                    new: true, 
                    session,
                    runValidators: true 
                }
            );
            
            if (!order) {
                throw new PaymentError('Order not available for processing', 'ORDER_LOCKED');
            }
            
            // Process payment with proper error handling
            const paymentResult = await processStripePayment(order, session);
            return paymentResult;
        });
    } catch (error) {
        logger.error('Payment processing failed', {
            orderId: orderData.id,
            error: error.message,
            stack: error.stack,
            timestamp: new Date()
        });
        throw error;
    } finally {
        await session.endSession();
    }
}
```

**2. Enhanced Error Handling & Recovery**

```javascript
class PaymentError extends Error {
    constructor(message, code, userMessage = null) {
        super(message);
        this.name = 'PaymentError';
        this.code = code;
        this.userMessage = userMessage || 'Payment processing failed. Please try again.';
        this.timestamp = new Date();
    }
}

async function handlePaymentError(error, order) {
    const errorMapping = {
        'CARD_DECLINED': 'Your card was declined. Please check your card details or try a different payment method.',
        'INSUFFICIENT_FUNDS': 'Insufficient funds. Please check your account balance or try a different payment method.',
        'NETWORK_ERROR': 'Connection issue detected. Please check your internet connection and try again.',
        'ORDER_LOCKED': 'This order is currently being processed. Please wait a moment and refresh the page.',
        'TIMEOUT_ERROR': 'Payment processing is taking longer than expected. Please wait or contact support.'
    };
    
    const userMessage = errorMapping[error.code] || 'An unexpected error occurred. Please try again or contact support.';
    
    // Log detailed error for debugging
    logger.error('Payment processing error', {
        orderId: order.id,
        errorCode: error.code,
        errorMessage: error.message,
        customerEmail: order.customerEmail,
        timestamp: new Date(),
        context: {
            userAgent: order.userAgent,
            ipAddress: order.ipAddress,
            paymentMethod: order.paymentMethod
        }
    });
    
    // Update order with error information
    await Order.findByIdAndUpdate(order.id, {
        status: 'failed',
        errorCode: error.code,
        errorMessage: error.message,
        failedAt: new Date()
    });
    
    return { success: false, userMessage, errorCode: error.code };
}
```

**3. Resource Optimization & Scaling**

```javascript
// Database connection pool optimization
const mongoose = require('mongoose');

mongoose.connect(process.env.DATABASE_URL, {
    maxPoolSize: 100, // Increased from 50
    minPoolSize: 10,
    maxIdleTimeMS: 30000,
    serverSelectionTimeoutMS: 5000,
    socketTimeoutMS: 45000,
    bufferMaxEntries: 0
});

// Memory leak prevention for webhook processing
class WebhookProcessor {
    constructor() {
        this.processors = new Map();
    }
    
    async processWebhook(webhookData) {
        const processorId = uuidv4();
        
        try {
            const processor = this.createProcessor(processorId);
            this.processors.set(processorId, processor);
            
            const result = await processor.process(webhookData);
            return result;
        } finally {
            // Ensure cleanup
            this.cleanupProcessor(processorId);
        }
    }
    
    cleanupProcessor(processorId) {
        const processor = this.processors.get(processorId);
        if (processor) {
            processor.cleanup();
            this.processors.delete(processorId);
        }
    }
}
```

**4. Comprehensive Monitoring & Alerting**

```javascript
// Enhanced logging and monitoring
const logger = require('winston');
const monitoring = require('./monitoring');

class PaymentMonitor {
    constructor() {
        this.metrics = {
            paymentAttempts: 0,
            paymentSuccesses: 0,
            paymentFailures: 0,
            averageProcessingTime: 0,
            concurrentProcessing: 0
        };
    }
    
    recordPaymentAttempt(orderId) {
        this.metrics.paymentAttempts++;
        this.metrics.concurrentProcessing++;
        
        logger.info('Payment attempt started', {
            orderId,
            timestamp: new Date(),
            concurrentCount: this.metrics.concurrentProcessing
        });
        
        // Alert if concurrent processing is high
        if (this.metrics.concurrentProcessing > 50) {
            monitoring.alert('HIGH_CONCURRENT_PAYMENTS', {
                count: this.metrics.concurrentProcessing,
                threshold: 50
            });
        }
    }
    
    recordPaymentResult(orderId, success, processingTime) {
        this.metrics.concurrentProcessing--;
        
        if (success) {
            this.metrics.paymentSuccesses++;
        } else {
            this.metrics.paymentFailures++;
        }
        
        // Update average processing time
        this.updateAverageProcessingTime(processingTime);
        
        // Calculate success rate
        const successRate = this.metrics.paymentSuccesses / this.metrics.paymentAttempts;
        
        // Alert if success rate drops below threshold
        if (successRate < 0.95 && this.metrics.paymentAttempts > 100) {
            monitoring.alert('LOW_PAYMENT_SUCCESS_RATE', {
                successRate: successRate,
                threshold: 0.95,
                attempts: this.metrics.paymentAttempts
            });
        }
        
        logger.info('Payment processing completed', {
            orderId,
            success,
            processingTime,
            successRate,
            timestamp: new Date()
        });
    }
}
```

### IMPLEMENTATION PLAN

#### Phase 1: Critical Fixes (Week 1)

**Immediate Actions**:
1. **Deploy Race Condition Fix**: Implement database transaction isolation
2. **Increase Database Connections**: Scale connection pool to 100 connections
3. **Add Request Deduplication**: Implement idempotency keys for payment requests
4. **Improve Error Messages**: Deploy user-friendly error messages
5. **Emergency Monitoring**: Implement real-time payment success rate monitoring

**Validation Criteria**:
- Payment success rate improves to >98%
- Duplicate payment intents eliminated
- Database connection exhaustion eliminated
- Customer-facing error messages provide actionable guidance

#### Phase 2: Performance Optimization (Week 2)

**Performance Improvements**:
1. **Memory Leak Fixes**: Implement proper cleanup for webhook processors
2. **Database Indexing**: Add indexes for payment-related queries
3. **Query Optimization**: Optimize slow database queries
4. **Timeout Configuration**: Implement proper timeout handling
5. **Load Balancer Tuning**: Optimize timeout and retry settings

**Validation Criteria**:
- Average payment processing time <5 seconds
- Memory usage stable during peak traffic
- Database query performance improved by 50%
- Zero timeout-related payment failures

#### Phase 3: Enhanced Monitoring (Week 3)

**Monitoring & Observability**:
1. **Comprehensive Logging**: Implement detailed payment flow logging
2. **Real-time Dashboards**: Create payment processing dashboards
3. **Alerting System**: Set up automated alerts for payment anomalies
4. **Error Tracking**: Implement structured error tracking and analysis
5. **Performance Monitoring**: Add payment processing performance metrics

**Validation Criteria**:
- Complete visibility into payment processing pipeline
- Automated alerting for payment issues
- Real-time performance and error rate monitoring
- Historical analysis capability for trend identification

#### Phase 4: Testing & Validation (Week 4)

**Comprehensive Testing**:
1. **Load Testing**: Simulate peak traffic conditions
2. **Chaos Engineering**: Test system resilience under failure conditions
3. **Integration Testing**: Validate all payment flows and error scenarios
4. **User Acceptance Testing**: Validate improved user experience
5. **Performance Testing**: Confirm performance improvements

**Validation Criteria**:
- System handles 10x normal traffic without degradation
- Payment success rate maintains >99% under stress
- Error recovery mechanisms function correctly
- User satisfaction with payment experience improves

### PREVENTION STRATEGIES

#### Code Quality Improvements

**Development Process Enhancements**:
1. **Mandatory Code Reviews**: Require senior developer review for payment-related code
2. **Static Analysis**: Implement automated code quality and security scanning
3. **Unit Testing**: Achieve 95% test coverage for payment processing logic
4. **Integration Testing**: Automated testing of complete payment flows
5. **Performance Testing**: Regular performance regression testing

**Architecture Guidelines**:
1. **Transaction Management**: Mandatory database transactions for all state changes
2. **Error Handling**: Comprehensive error handling with user-friendly messages
3. **Logging Standards**: Structured logging for all payment processing steps
4. **Monitoring Integration**: Built-in monitoring for all critical functions
5. **Security Best Practices**: Secure handling of payment data and credentials

#### Operational Excellence

**Monitoring & Alerting**:
1. **Payment Success Rate**: Real-time monitoring with <95% success rate alerts
2. **Processing Time**: Average processing time monitoring with 10s threshold alerts
3. **Error Pattern Detection**: Automated detection of unusual error patterns
4. **Resource Utilization**: Proactive monitoring of database and application resources
5. **External Service Health**: Monitoring of Stripe API performance and availability

**Incident Response**:
1. **Runbook Documentation**: Detailed troubleshooting guides for payment issues
2. **On-call Procedures**: 24/7 on-call coverage for critical payment issues
3. **Escalation Paths**: Clear escalation procedures for payment-related incidents
4. **Communication Plans**: Customer communication templates for payment issues
5. **Post-incident Reviews**: Systematic analysis and prevention planning for all incidents

## Usage Instructions
1. Start with systematic symptom analysis and error pattern identification
2. Generate and test hypotheses using scientific debugging methodology
3. Conduct comprehensive code review focusing on critical paths
4. Analyze infrastructure and performance characteristics
5. Identify root causes through systematic investigation
6. Design comprehensive solutions addressing root causes and prevention
7. Implement fixes in phases with proper testing and validation
8. Establish monitoring and prevention strategies for long-term stability

## Examples
### Example 1: Frontend JavaScript Debugging
**Input**: 
```
{{programming_language}}: JavaScript (React)
{{bug_type}}: UI rendering issues
{{environment}}: Production web application
{{symptoms}}: Intermittent component rendering failures
{{severity_level}}: High - affecting user experience
```

**Output**: [Systematic debugging approach for React rendering issues with state management analysis, component lifecycle investigation, and performance optimization]

### Example 2: Backend API Performance Debugging
**Input**:
```
{{programming_language}}: Python (Django)
{{bug_type}}: Performance degradation
{{environment}}: Production API server
{{symptoms}}: Slow response times and timeout errors
{{available_tools}}: Application monitoring and database profiling
```

**Output**: [Performance debugging strategy with database optimization, code profiling, caching analysis, and scalability improvements]

## Related Prompts
- [Code Review Expert](/prompts/evaluation/code-review.md)
- [Performance Analysis Specialist](/prompts/analysis/performance-analysis.md)
- [Error Handling Designer](/prompts/problem-solving/error-handling-design.md)

## Research Notes
- Based on systematic debugging methodologies and software engineering best practices
- Integrates code analysis with infrastructure and performance considerations
- Emphasizes prevention strategies and long-term code quality improvement
- Focuses on root cause analysis rather than symptom treatment
- Balances immediate fixes with comprehensive solution design