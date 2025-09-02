# Comprehensive Test Strategist

## Metadata
- **Created**: 2025-07-22

- **Category**: Technical/Quality-Assurance
- **Tags**: test strategy, quality assurance, test planning, automation, test management
- **Version**: 2.0.0
- **Use Cases**: test planning, quality strategy, automation framework, test coverage
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description

This prompt helps you develop comprehensive testing strategies that ensure software quality through systematic planning, appropriate automation, and effective test coverage.

## Prompt

```
I'll help you create a comprehensive testing strategy that ensures quality throughout your development lifecycle. Let me understand your needs:

**About your project:**
1. What type of application? (web, mobile, API, desktop, embedded)
2. What's your tech stack and architecture?
3. What's the project scale? (users, complexity, criticality)
4. What are the main quality risks?

**Current testing:**
5. What testing do you currently do? (unit, integration, E2E, manual)
6. What's your test automation coverage?
7. What tools are you using?
8. How long does testing take?

**Team and process:**
9. How many QA engineers vs developers?
10. What's your development methodology? (Agile, waterfall, etc.)
11. How often do you release?
12. What are your main testing pain points?

Based on your answers, I'll provide:

**TEST STRATEGY FRAMEWORK** - Comprehensive approach to quality
**AUTOMATION ROADMAP** - What to automate and when
**TEST COVERAGE PLAN** - Ensuring nothing falls through cracks
**TOOLS & INFRASTRUCTURE** - Right tools for your needs
**METRICS & REPORTING** - Measuring testing effectiveness

Share your testing context and let's build a quality strategy!
```

## Example Usage

**User Input:**
```
1. E-commerce web platform with mobile apps (iOS/Android)
2. React frontend, Node.js microservices, PostgreSQL, Redis, Kubernetes
3. 100K daily users, payment processing, inventory management, high complexity
4. Payment failures, cart abandonment, performance issues, security breaches

5. Some unit tests (30% coverage), manual E2E testing, no integration tests
6. Almost no automation - just some unit tests
7. Jest for unit tests, manual testing with spreadsheets
8. 1 week manual regression before each release

9. 2 QA engineers, 15 developers
10. 2-week sprints, trying to be Agile but testing is waterfall
11. Monthly releases, want to go to weekly
12. Testing bottleneck, bugs in production, can't test everything
```

**Assistant Output:**

Based on your e-commerce platform needs, here's a comprehensive testing strategy:

## TEST STRATEGY FRAMEWORK

### Testing Pyramid Transformation

**Current State → Target State**
```
Current (Inverted)          Target (Healthy)
      ▼                          ▲
 ┌─────────┐                ┌─────┐
 │   E2E   │                │ E2E │ 10%
 │ Manual  │                ├─────┤
 │  (80%)  │                │ API │ 20%
 ├─────────┤                ├─────┤
 │  None   │                │ Int │ 20%
 │  (0%)   │                ├─────┤
 ├─────────┤                │Unit │ 50%
 │Unit(20%)│                └─────┘
 └─────────┘
```

### Risk-Based Testing Approach

**Critical User Journeys (P0)**:
1. Payment processing flow
2. Add to cart → Checkout
3. Inventory updates
4. User authentication
5. Order management

**Testing Priorities**:
```yaml
P0 - Business Critical (Payment, Auth):
  - 100% automated test coverage
  - Performance testing required
  - Security testing mandatory
  - Daily smoke tests

P1 - Core Features (Cart, Search):
  - 80% automated coverage
  - Weekly regression
  - Load testing

P2 - Supporting Features:
  - 50% automated coverage
  - Sprint-based testing
```

## AUTOMATION ROADMAP

### Phase 1: Foundation (Months 1-2)

**API Test Automation**
```javascript
// Example: Payment API Test with Supertest
describe('Payment Processing API', () => {
  it('should process valid payment', async () => {
    const payment = {
      amount: 99.99,
      currency: 'USD',
      card: generateTestCard(),
      orderId: 'TEST-123'
    };

    const response = await request(app)
      .post('/api/payments')
      .send(payment)
      .expect(200);

    expect(response.body).toMatchObject({
      status: 'success',
      transactionId: expect.any(String),
      amount: payment.amount
    });

    // Verify inventory updated
    const order = await getOrder(payment.orderId);
    expect(order.paymentStatus).toBe('completed');
  });
});
```

**Contract Testing Setup**
```yaml
# Pact configuration for microservices
consumer: frontend-service
provider: payment-service
pact_dir: ./pacts

interactions:
  - description: "Process payment"
    request:
      method: POST
      path: /payments
    response:
      status: 200
      body:
        status: "success"
```

### Phase 2: UI Automation (Months 2-3)

**E2E Framework Selection**: Playwright (cross-browser, fast, reliable)

```typescript
// Critical path automation example
test('Complete purchase flow', async ({ page }) => {
  // Test data setup
  const testUser = await createTestUser();
  const testProduct = await createTestProduct();

  // User journey
  await page.goto('/');
  await login(page, testUser);
  
  // Search and add to cart
  await page.fill('[data-testid="search"]', testProduct.name);
  await page.click('[data-testid="add-to-cart"]');
  
  // Checkout
  await page.click('[data-testid="checkout"]');
  await fillPaymentDetails(page, testPaymentMethod);
  await page.click('[data-testid="place-order"]');
  
  // Verify
  await expect(page).toHaveURL(/order-confirmation/);
  const orderId = await page.textContent('[data-testid="order-id"]');
  
  // API verification
  const order = await verifyOrderInAPI(orderId);
  expect(order.status).toBe('completed');
});
```

### Phase 3: Performance & Security (Months 3-4)

**Performance Testing with K6**
```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
  stages: [
    { duration: '2m', target: 100 },  // Ramp up
    { duration: '5m', target: 100 },  // Stay at 100 users
    { duration: '2m', target: 200 },  // Spike
    { duration: '2m', target: 0 },    // Ramp down
  ],
  thresholds: {
    http_req_duration: ['p(95)<500'], // 95% requests under 500ms
    http_req_failed: ['rate<0.1'],    // Error rate under 10%
  },
};

export default function() {
  // Browse products
  let products = http.get('https://api.example.com/products');
  check(products, {
    'products loaded': (r) => r.status === 200,
  });
  
  sleep(1);
  
  // Add to cart
  let cart = http.post('https://api.example.com/cart', {
    productId: 123,
    quantity: 1
  });
  check(cart, {
    'added to cart': (r) => r.status === 200,
  });
}
```

## TEST COVERAGE PLAN

### Coverage Matrix

```
Component        | Unit | Integration | API | E2E | Performance | Security
-----------------|------|-------------|-----|-----|-------------|----------
Payment Service  | 90%  | 80%        | 90% | 100%| Required    | Required
Cart Service     | 80%  | 70%        | 80% | 90% | Required    | Standard
Product Catalog  | 70%  | 60%        | 70% | 70% | Standard    | Standard
User Service     | 85%  | 75%        | 85% | 80% | Standard    | Required
Order Management | 85%  | 80%        | 85% | 90% | Required    | Standard
```

### Test Data Strategy

**Synthetic Data Generation**
```javascript
// Test data factory
class TestDataFactory {
  static async createTestScenario(scenario) {
    switch(scenario) {
      case 'happy-path-purchase':
        return {
          user: await createUser({ verified: true }),
          products: await createProducts(3),
          payment: generateValidCard(),
          shipping: generateAddress()
        };
      
      case 'payment-failure':
        return {
          user: await createUser(),
          products: await createProducts(1),
          payment: generateDeclinedCard(),
        };
    }
  }
}
```

## TOOLS & INFRASTRUCTURE

### Recommended Tech Stack

**Core Testing Tools**:
```yaml
Unit Testing:
  - Jest (JavaScript)
  - React Testing Library
  - Supertest (API)

Integration Testing:
  - Pact (Contract testing)
  - TestContainers (Database)

E2E Testing:
  - Playwright (Web)
  - Appium (Mobile)

Performance:
  - K6 (Load testing)
  - Lighthouse (Frontend performance)

Security:
  - OWASP ZAP (Scanning)
  - Snyk (Dependencies)

Infrastructure:
  - GitHub Actions (CI/CD)
  - Allure (Reporting)
  - Percy (Visual regression)
```

### CI/CD Integration

```yaml
# GitHub Actions workflow
name: Test Pipeline
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Unit Tests
        run: npm run test:unit
        
      - name: Integration Tests
        run: |
          docker-compose up -d
          npm run test:integration
          
      - name: E2E Tests
        run: |
          npm run test:e2e -- --shard=1/4
          
      - name: Performance Check
        run: |
          k6 run --quiet performance/checkout.js
          
      - name: Security Scan
        run: |
          snyk test
          npm audit
```

## METRICS & REPORTING

### KPI Dashboard

**Quality Metrics**:
```
Test Coverage:
├── Unit: 85% (Target: 80%) ✅
├── API: 75% (Target: 80%) ⚠️
├── E2E: 60% (Target: 70%) ❌

Test Execution:
├── Execution Time: 12 min
├── Flaky Tests: 2%
├── Pass Rate: 98%

Defect Metrics:
├── Defect Escape Rate: 0.5%
├── MTTR: 4 hours
├── Test Effectiveness: 92%
```

### Implementation Timeline

**Month 1-2: Foundation**
- Set up API testing framework
- Automate critical payment flows
- Establish CI/CD pipeline
- Train team on tools

**Month 3-4: Expansion**
- Add E2E automation
- Implement performance testing
- Set up monitoring
- Reduce manual testing 50%

**Month 5-6: Optimization**
- Achieve 80% automation
- Implement visual testing
- Add security scanning
- Enable continuous deployment

### Team Structure Evolution

**Current → Target**:
```
2 QA + 15 Dev → Quality Engineering Model

- Each dev team owns quality
- QA becomes "Quality Coaches"
- Developers write tests
- QA focuses on strategy, tools, complex scenarios
```

### Quick Wins (First 30 days)

1. **Automate smoke tests** - 2 hour → 10 min
2. **API test framework** - Catch integration issues
3. **Parallel test execution** - 50% faster
4. **Test data service** - Consistent test data
5. **Quality gates in CI** - Prevent bad builds

This strategy will reduce your testing time from 1 week to 2 hours while improving quality and enabling weekly releases.

## Related Prompts

- [Test Automation Expert](../../technical-workflows/robotic-process-automation-expert.md)
- [Performance Testing Specialist](../../management-leadership/performance-management-expert.md)
- [Security Testing Expert](../../problem-solving/security-vulnerability-mitigation-expert.md)
