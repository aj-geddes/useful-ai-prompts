# Specification Creation Expert and Requirements Engineering Architect

## Metadata
- **Category**: Creation
- **Tags**: technical specifications, requirements engineering, system design, documentation, standards
- **Created**: 2025-07-20
- **Version**: 1.0.0
- **Personas**: Senior Specification Creation Expert, Requirements Engineering Architect
- **Use Cases**: software specifications, API specs, hardware requirements, system architecture, technical standards
- **Compatible Models**: GPT-4, Claude 3, Gemini Pro, GPT-3.5

## Description
This prompt combines expert specification creation skills with requirements engineering architecture to develop comprehensive, unambiguous technical specifications. It employs industry standards, formal methods, and stakeholder analysis to create specifications that bridge business needs with technical implementation.

## Prompt Template
```
You are operating as a dual-expertise specification system combining:

1. **Senior Specification Creation Expert** (15+ years experience)
   - Expertise: Technical writing, requirements analysis, system modeling, standards compliance
   - Strengths: Precision, completeness, traceability, validation methods, stakeholder communication
   - Perspective: Specifications must be unambiguous, testable, and implementable

2. **Requirements Engineering Architect**
   - Expertise: Requirements elicitation, analysis patterns, formal methods, verification strategies
   - Strengths: Stakeholder management, conflict resolution, priority frameworks, change management
   - Perspective: Building specifications that evolve while maintaining system integrity

Apply these specification frameworks:
- **IEEE 830**: Software Requirements Specifications standard
- **SWEBOK**: Software Engineering Body of Knowledge
- **MoSCoW**: Prioritization method (Must/Should/Could/Won't)
- **SMART**: Specific, Measurable, Achievable, Relevant, Time-bound

SPECIFICATION CONTEXT:
- **Specification Type**: {{software_API_hardware_system_integration_protocol}}
- **Domain**: {{industry_application_area_technical_domain}}
- **Stakeholders**: {{developers_users_business_regulatory_operations}}
- **System Scope**: {{component_module_system_enterprise}}
- **Standards Required**: {{IEEE_ISO_industry_specific_regulatory}}
- **Development Method**: {{agile_waterfall_hybrid_iterative}}
- **Technical Constraints**: {{platform_performance_security_compatibility}}
- **Timeline**: {{MVP_phases_milestones_deadlines}}
- **Integration Points**: {{APIs_databases_external_systems_hardware}}
- **Success Criteria**: {{acceptance_tests_metrics_compliance}}

SPECIFICATION REQUIREMENTS:
{{functional_non_functional_constraints_interfaces_assumptions}}

SPECIFICATION FRAMEWORK:

Phase 1: REQUIREMENTS GATHERING
1. Stakeholder analysis
2. Requirements elicitation
3. Domain modeling
4. Constraint identification

Phase 2: ANALYSIS & DESIGN
1. Requirements classification
2. Architecture definition
3. Interface specification
4. Behavior modeling

Phase 3: DOCUMENTATION
1. Structured writing
2. Diagram creation
3. Traceability matrix
4. Review cycles

Phase 4: VALIDATION
1. Completeness check
2. Consistency validation
3. Testability review
4. Stakeholder approval

DELIVER YOUR SPECIFICATION AS:
```

## COMPREHENSIVE SPECIFICATION PACKAGE

### SPECIFICATION OVERVIEW

**Project**: SmartInventory - AI-Powered Inventory Management System
**Version**: 2.0.0
**Date**: January 20, 2025
**Status**: Draft for Review
**Authors**: Technical Architecture Team

**Document Purpose**:
This Software Requirements Specification (SRS) defines the functional and non-functional requirements for SmartInventory 2.0, an AI-powered inventory management system designed to optimize stock levels, predict demand, and automate reordering processes.

**Intended Audience**:
- Development Team
- QA Engineers
- Product Management
- System Integrators
- Operations Team
- Executive Stakeholders

### 1. INTRODUCTION

#### 1.1 Purpose
SmartInventory 2.0 revolutionizes inventory management through artificial intelligence and real-time analytics. This specification defines all requirements for building a system that reduces inventory costs by 30% while improving stock availability to 99.5%.

#### 1.2 Scope
**In Scope**:
- Real-time inventory tracking across multiple locations
- AI-based demand prediction engine
- Automated reordering system
- Integration with existing ERP systems
- Mobile and web interfaces
- Analytics and reporting dashboard

**Out of Scope**:
- Financial accounting features
- HR management capabilities
- Manufacturing execution
- Direct customer-facing e-commerce

#### 1.3 Definitions, Acronyms, and Abbreviations

| Term | Definition |
|------|------------|
| **SKU** | Stock Keeping Unit - Unique identifier for each product variant |
| **ML** | Machine Learning - AI algorithms for prediction |
| **API** | Application Programming Interface |
| **FIFO** | First In, First Out - Inventory rotation method |
| **SLA** | Service Level Agreement |
| **ROI** | Return on Investment |
| **B2B** | Business to Business |

#### 1.4 References
- IEEE Std 830-1998: Recommended Practice for Software Requirements Specifications
- REST API Design Guidelines v2.0
- Company Security Standards v3.1
- GDPR Compliance Framework

#### 1.5 Overview
This document is organized into:
- Section 2: Overall system description
- Section 3: Specific functional requirements
- Section 4: Non-functional requirements
- Section 5: Interface requirements
- Section 6: System architecture
- Section 7: Validation criteria

### 2. OVERALL DESCRIPTION

#### 2.1 Product Perspective

```
┌─────────────────────────────────────────────────────┐
│                  SmartInventory 2.0                 │
├─────────────────┬───────────────┬──────────────────┤
│   Web Portal    │  Mobile Apps  │   API Gateway    │
├─────────────────┴───────────────┴──────────────────┤
│              Application Services Layer              │
├──────────┬──────────┬──────────┬──────────────────┤
│Inventory │Prediction│ Ordering │Analytics         │
│Service   │Engine    │Service   │Service           │
├──────────┴──────────┴──────────┴──────────────────┤
│                 Data Layer                          │
├──────────┬──────────┬──────────┬──────────────────┤
│PostgreSQL│ Redis    │ ML Models│ Data Lake        │
└──────────┴──────────┴──────────┴──────────────────┘
                           │
                           ├── ERP Integration
                           ├── Supplier APIs
                           └── IoT Sensors
```

#### 2.2 Product Functions

**Core Capabilities**:
1. **Real-time Inventory Tracking**
   - Multi-location visibility
   - Barcode/RFID scanning
   - Automatic stock level updates
   - Low stock alerts

2. **Demand Prediction**
   - Historical data analysis
   - Seasonal pattern recognition
   - External factor integration
   - Accuracy tracking

3. **Automated Ordering**
   - Reorder point calculation
   - Supplier integration
   - Order optimization
   - Approval workflows

4. **Analytics & Reporting**
   - Inventory turnover metrics
   - Cost analysis
   - Performance dashboards
   - Custom report builder

#### 2.3 User Classes and Characteristics

| User Class | Description | Technical Skill | Usage Frequency |
|------------|-------------|-----------------|-----------------|
| **Warehouse Manager** | Oversees daily operations | Medium | Daily, 4-6 hours |
| **Inventory Analyst** | Analyzes trends and optimizes | High | Daily, full-time |
| **Purchasing Agent** | Manages supplier orders | Medium | Daily, 2-3 hours |
| **Executive** | Reviews KPIs and metrics | Low | Weekly, 30 min |
| **System Admin** | Maintains system | Very High | As needed |
| **API Consumer** | External system integration | High | Continuous |

#### 2.4 Operating Environment

**Client Requirements**:
- Web: Chrome 90+, Firefox 88+, Safari 14+, Edge 90+
- Mobile: iOS 14+, Android 10+
- Screen resolution: 1366x768 minimum
- Network: Broadband internet (10 Mbps+)

**Server Requirements**:
- Cloud: AWS preferred, Azure compatible
- Compute: Auto-scaling EC2/containers
- Database: PostgreSQL 14+
- Cache: Redis 6+
- ML Platform: SageMaker or equivalent

#### 2.5 Design and Implementation Constraints

**Technical Constraints**:
- Must integrate with SAP ERP system
- Response time < 2 seconds for queries
- Support 10,000 concurrent users
- 99.9% uptime SLA
- GDPR compliant data handling

**Business Constraints**:
- Development budget: $2.5M
- Go-live date: Q3 2025
- Phased rollout required
- Minimal disruption to operations

#### 2.6 Assumptions and Dependencies

**Assumptions**:
- Stable internet connectivity at all locations
- Users have basic computer skills
- Existing data can be migrated
- Suppliers will provide API access

**Dependencies**:
- ERP system availability
- Third-party ML libraries
- Cloud service providers
- Barcode scanner hardware

### 3. SPECIFIC REQUIREMENTS

#### 3.1 Functional Requirements

##### 3.1.1 Inventory Management

**REQ-INV-001: Real-time Stock Tracking**
- **Description**: System shall track inventory levels in real-time across all locations
- **Input**: Barcode scan, manual entry, API update
- **Processing**: Validate SKU, update quantity, log transaction
- **Output**: Updated stock level, confirmation message
- **Priority**: Must Have

```
Use Case: Update Stock Level
Actor: Warehouse Worker
Precondition: User logged in with appropriate permissions
Main Flow:
1. User scans item barcode
2. System displays current quantity
3. User enters new quantity or adjustment
4. System validates input
5. System updates database
6. System displays confirmation
Alternate Flow:
3a. If barcode not found:
    - System prompts for manual SKU entry
    - Continue from step 2
4a. If validation fails:
    - System displays error message
    - Return to step 3
```

**REQ-INV-002: Multi-location Inventory**
- **Description**: Support inventory tracking across unlimited locations
- **Acceptance Criteria**:
  - Each location has unique identifier
  - Transfer between locations tracked
  - Location-specific reorder points
  - Consolidated view available

**REQ-INV-003: Inventory Categorization**
- **Description**: Organize inventory in hierarchical categories
- **Requirements**:
  - Minimum 5 levels of categorization
  - Multiple category assignment
  - Custom attributes per category
  - Bulk categorization tools

##### 3.1.2 Demand Prediction

**REQ-ML-001: Demand Forecasting Algorithm**
- **Description**: ML model predicts future demand with 85%+ accuracy
- **Inputs**:
  - Historical sales data (min 24 months)
  - Seasonal patterns
  - Promotional calendars
  - Economic indicators
- **Outputs**:
  - 30/60/90 day forecasts
  - Confidence intervals
  - Contributing factors
- **Model Requirements**:
  - Retrain weekly
  - A/B testing capability
  - Explainable AI features

**REQ-ML-002: Anomaly Detection**
- **Description**: Identify unusual demand patterns
- **Triggers**:
  - Demand spike > 3 standard deviations
  - New pattern emergence
  - Data quality issues
- **Actions**:
  - Alert relevant users
  - Flag for manual review
  - Adjust predictions

##### 3.1.3 Automated Ordering

**REQ-ORD-001: Reorder Point Calculation**
```python
# Pseudocode for reorder point calculation
def calculate_reorder_point(sku):
    lead_time = get_supplier_lead_time(sku)
    daily_usage = calculate_average_daily_usage(sku)
    safety_stock = calculate_safety_stock(sku)
    
    reorder_point = (lead_time * daily_usage) + safety_stock
    
    # Apply business rules
    if sku.is_critical:
        reorder_point *= 1.2  # 20% buffer
    
    return round(reorder_point)
```

**REQ-ORD-002: Purchase Order Generation**
- **Description**: Automatically generate POs when reorder point reached
- **Workflow**:
  1. System detects stock below reorder point
  2. Calculate optimal order quantity (EOQ)
  3. Check supplier availability
  4. Generate draft PO
  5. Route for approval based on amount
  6. Send to supplier upon approval

**REQ-ORD-003: Supplier Integration**
- **Description**: Real-time integration with supplier systems
- **Protocols**: REST API, EDI, Email
- **Data Exchange**:
  - Product catalogs
  - Pricing updates
  - Availability status
  - Order confirmation
  - Shipping notifications

#### 3.2 Non-Functional Requirements

##### 3.2.1 Performance Requirements

**REQ-PERF-001: Response Time**
| Operation | Target Time | Maximum Time |
|-----------|-------------|--------------|
| Page Load | < 1 second | 3 seconds |
| Search Query | < 500ms | 2 seconds |
| Report Generation | < 5 seconds | 30 seconds |
| Data Import (1M records) | < 10 minutes | 30 minutes |

**REQ-PERF-002: Throughput**
- Concurrent users: 10,000
- Transactions per second: 1,000
- API calls per second: 5,000
- Data ingestion: 100,000 records/minute

**REQ-PERF-003: Resource Usage**
- CPU utilization: < 70% average
- Memory usage: < 80% peak
- Database connections: < 1000
- Network bandwidth: < 100 Mbps

##### 3.2.2 Security Requirements

**REQ-SEC-001: Authentication & Authorization**
```yaml
authentication:
  methods:
    - username_password:
        min_length: 12
        complexity: uppercase, lowercase, number, special
        expiry: 90 days
    - multi_factor:
        required_for: [admin, financial_approve]
        methods: [sms, authenticator_app, hardware_token]
    - single_sign_on:
        protocol: SAML 2.0
        providers: [okta, azure_ad]

authorization:
  model: role_based_access_control
  roles:
    - warehouse_worker:
        permissions: [view_inventory, update_stock, create_transfer]
    - manager:
        permissions: [all_warehouse_worker, approve_transfer, view_reports]
    - admin:
        permissions: [all_permissions]
```

**REQ-SEC-002: Data Encryption**
- At rest: AES-256
- In transit: TLS 1.3
- Database: Transparent Data Encryption
- Backups: Encrypted with separate keys

**REQ-SEC-003: Audit Trail**
- All data modifications logged
- User, timestamp, before/after values
- Immutable audit log
- 7-year retention policy

##### 3.2.3 Reliability Requirements

**REQ-REL-001: Availability**
- Uptime SLA: 99.9% (8.76 hours downtime/year)
- Planned maintenance windows: Sunday 2-6 AM
- Disaster recovery: RTO < 4 hours, RPO < 1 hour

**REQ-REL-002: Fault Tolerance**
- No single point of failure
- Automatic failover for all services
- Graceful degradation for non-critical features
- Circuit breakers for external dependencies

##### 3.2.4 Usability Requirements

**REQ-USE-001: User Interface Standards**
- Consistent with company design system
- Mobile-first responsive design
- Accessibility: WCAG 2.1 Level AA
- Internationalization: 10 languages

**REQ-USE-002: User Efficiency**
- Common tasks: < 3 clicks
- Keyboard shortcuts for power users
- Bulk operations supported
- Customizable dashboards

### 4. INTERFACE REQUIREMENTS

#### 4.1 User Interfaces

**Web Portal Wireframes**:

```
Dashboard Layout:
┌─────────────────────────────────────────────┐
│ SmartInventory  [Search...] [🔔] [User ▼]  │
├─────────────┬───────────────────────────────┤
│             │  Inventory Level: 87%         │
│  Navigation │  Low Stock Items: 23          │
│             │  Pending Orders: 5            │
│  Dashboard  │                               │
│  Inventory  │  [Stock Levels Graph]         │
│  Orders     │                               │
│  Analytics  │  Recent Activity:             │
│  Settings   │  • SKU-1234 received 500 units│
│             │  • Order PO-5678 approved     │
└─────────────┴───────────────────────────────┘
```

**Mobile App Screens**:
- Scanner view with overlay information
- Quick action buttons for common tasks
- Swipe gestures for quantity adjustments
- Offline mode with sync capability

#### 4.2 Hardware Interfaces

**Barcode Scanner Integration**:
```javascript
// Scanner interface specification
interface BarcodeScanner {
  // Initialize scanner connection
  connect(): Promise<boolean>;
  
  // Start scanning
  startScan(): void;
  
  // Scanner events
  onScan(callback: (data: ScanData) => void): void;
  onError(callback: (error: Error) => void): void;
  
  // Disconnect scanner
  disconnect(): void;
}

interface ScanData {
  barcode: string;
  type: 'EAN13' | 'QR' | 'Code128';
  timestamp: Date;
  location?: GPSCoordinates;
}
```

**RFID Reader Support**:
- Protocol: EPC Gen2
- Frequency: 860-960 MHz
- Read range: 10 meters
- Bulk reading: 1000 tags/second

#### 4.3 Software Interfaces

**ERP Integration API**:
```json
{
  "endpoint": "https://erp.company.com/api/v2",
  "authentication": {
    "type": "oauth2",
    "token_endpoint": "/auth/token",
    "scope": "inventory.read inventory.write"
  },
  "operations": {
    "get_products": {
      "method": "GET",
      "path": "/products",
      "params": ["sku", "category", "location"]
    },
    "update_stock": {
      "method": "POST",
      "path": "/inventory/update",
      "body": {
        "sku": "string",
        "location": "string",
        "quantity": "number",
        "transaction_type": "enum"
      }
    }
  }
}
```

**External APIs**:
1. **Weather API**: For demand prediction
2. **Shipping APIs**: FedEx, UPS, DHL
3. **Supplier APIs**: Various formats
4. **Analytics APIs**: Google Analytics, Mixpanel

#### 4.4 Communication Interfaces

**Message Queue Specification**:
- Protocol: AMQP (RabbitMQ)
- Exchanges: inventory.updates, orders.events
- Message format: JSON with schema validation
- Retry policy: Exponential backoff

**Webhook Support**:
```yaml
webhooks:
  events:
    - inventory.low_stock
    - order.created
    - order.shipped
    - prediction.anomaly
  
  payload:
    event: string
    timestamp: ISO8601
    data: object
    signature: HMAC-SHA256
  
  delivery:
    timeout: 30s
    retries: 3
    backoff: exponential
```

### 5. SYSTEM ARCHITECTURE

#### 5.1 High-Level Architecture

```
┌──────────────────────────────────────────────────────┐
│                    Load Balancer                      │
└──────────────────────┬───────────────────────────────┘
                       │
┌──────────────────────┴───────────────────────────────┐
│                   API Gateway                         │
│              (Authentication, Rate Limiting)          │
└──────────────────────┬───────────────────────────────┘
                       │
        ┌──────────────┴──────────────┐
        │                             │
┌───────┴────────┐           ┌───────┴────────┐
│  Web Services  │           │   ML Services   │
│   (REST API)   │           │  (Prediction)   │
└───────┬────────┘           └───────┬────────┘
        │                             │
        └──────────────┬──────────────┘
                       │
              ┌────────┴────────┐
              │  Message Queue  │
              └────────┬────────┘
                       │
     ┌─────────────────┼─────────────────┐
     │                 │                 │
┌────┴─────┐    ┌─────┴──────┐   ┌─────┴──────┐
│Primary DB│    │  Cache      │   │ Analytics  │
│PostgreSQL│    │  Redis      │   │ Data Lake  │
└──────────┘    └────────────┘   └────────────┘
```

#### 5.2 Component Specifications

**Inventory Service**:
```yaml
service: inventory-service
type: microservice
technology: Node.js + TypeScript
database: PostgreSQL
api:
  - GET /inventory/{sku}
  - PUT /inventory/{sku}
  - POST /inventory/transfer
  - GET /inventory/search
dependencies:
  - auth-service
  - notification-service
scaling:
  min_instances: 3
  max_instances: 50
  metric: cpu_utilization
  target: 70%
```

**ML Prediction Engine**:
```python
class DemandPredictor:
    def __init__(self):
        self.model = load_model('demand_forecast_v2')
        self.feature_pipeline = FeaturePipeline()
    
    def predict(self, sku: str, horizon: int = 30) -> PredictionResult:
        features = self.feature_pipeline.extract(sku)
        prediction = self.model.predict(features, horizon)
        
        return PredictionResult(
            sku=sku,
            predictions=prediction.values,
            confidence_intervals=prediction.intervals,
            feature_importance=self.explain(features)
        )
    
    def retrain(self, training_data: DataFrame):
        # Retraining logic with validation
        pass
```

### 6. VALIDATION & TESTING

#### 6.1 Test Scenarios

**Functional Test Cases**:

| Test ID | Description | Input | Expected Output | Priority |
|---------|-------------|-------|-----------------|----------|
| TC-001 | Stock update via barcode | Scan valid barcode, enter quantity 100 | Stock updated to 100, confirmation shown | Critical |
| TC-002 | Low stock alert | Stock falls below reorder point | Alert generated, notification sent | High |
| TC-003 | Demand prediction accuracy | Historical data for SKU-123 | Prediction within 15% of actual | High |
| TC-004 | Automated PO generation | Stock below reorder point | PO created with correct quantity | Critical |

**Performance Test Scenarios**:
1. **Load Test**: 10,000 concurrent users
2. **Stress Test**: 2x expected peak load
3. **Endurance Test**: 72-hour continuous operation
4. **Spike Test**: Sudden 10x traffic increase

#### 6.2 Acceptance Criteria

**System-Level Acceptance**:
- [ ] All critical requirements implemented
- [ ] Performance targets met in production-like environment
- [ ] Security penetration test passed
- [ ] User acceptance testing completed
- [ ] Documentation complete and approved
- [ ] Training materials prepared

**Go-Live Checklist**:
1. Data migration completed successfully
2. All integrations tested end-to-end
3. Disaster recovery plan tested
4. Support team trained
5. Rollback plan prepared
6. Executive sign-off obtained

### 7. APPENDICES

#### Appendix A: Glossary
[Comprehensive glossary of all technical and business terms]

#### Appendix B: Data Model
```sql
-- Core inventory table
CREATE TABLE inventory (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    sku VARCHAR(50) NOT NULL,
    location_id UUID NOT NULL,
    quantity INTEGER NOT NULL CHECK (quantity >= 0),
    reorder_point INTEGER,
    reorder_quantity INTEGER,
    last_counted TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (location_id) REFERENCES locations(id),
    UNIQUE(sku, location_id)
);

-- Audit trail for all changes
CREATE TABLE inventory_audit (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    inventory_id UUID NOT NULL,
    user_id UUID NOT NULL,
    action VARCHAR(50) NOT NULL,
    old_quantity INTEGER,
    new_quantity INTEGER,
    reason TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (inventory_id) REFERENCES inventory(id),
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```

#### Appendix C: API Documentation
[Complete OpenAPI 3.0 specification - see separate document]

#### Appendix D: Compliance Matrix

| Requirement | Source | Implementation | Verification Method |
|-------------|--------|----------------|---------------------|
| GDPR Article 17 | EU Regulation | Data deletion API | Automated testing |
| SOC 2 Type II | Audit requirement | Access controls | Annual audit |
| HIPAA | Healthcare products | Encryption at rest | Security scan |

### VERSION CONTROL

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 0.1 | 2024-11-01 | J. Smith | Initial draft |
| 0.2 | 2024-11-15 | M. Johnson | Added ML requirements |
| 1.0 | 2024-12-01 | Team | First complete version |
| 2.0 | 2025-01-20 | A. Williams | Major update for v2.0 |

### APPROVAL

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Product Owner | Sarah Chen | _______ | _____ |
| Technical Lead | Michael Brown | _______ | _____ |
| QA Manager | Lisa Wang | _______ | _____ |
| Security Officer | David Kim | _______ | _____ |

## Usage Instructions
1. Start with clear understanding of business objectives and constraints
2. Engage all stakeholders early in requirements gathering
3. Use formal methods for critical system requirements
4. Create traceable links between requirements and tests
5. Include both functional and non-functional requirements
6. Provide clear acceptance criteria for each requirement
7. Version control all specification changes
8. Review and approve with all stakeholders

## Examples
### Example 1: API Specification
**Input**: 
```
{{specification_type}}: RESTful API specification
{{domain}}: Payment processing system
{{stakeholders}}: Frontend developers, mobile teams, partners
{{standards}}: OpenAPI 3.0, PCI-DSS compliance
{{success_criteria}}: <100ms response time, 99.99% uptime
```

**Output**: [Complete OpenAPI specification with endpoints, schemas, authentication, error codes, rate limits, and example requests/responses]

### Example 2: IoT Device Specification
**Input**:
```
{{specification_type}}: Hardware/firmware specification
{{domain}}: Smart home temperature sensor
{{stakeholders}}: Hardware engineers, firmware developers, app teams
{{constraints}}: Battery life 2 years, -20°C to 50°C operation
{{integration}}: MQTT, Bluetooth LE, OTA updates
```

**Output**: [Detailed hardware requirements, communication protocols, power specifications, firmware update process, and certification requirements]

## Related Prompts
- [System Architecture Design](/prompts/technical/system-architecture.md)
- [Test Case Generator](/prompts/creation/test-case-generator.md)
- [Technical Documentation Writer](/prompts/creation/technical-docs.md)

## Research Notes
- Based on IEEE and industry standard practices
- Emphasizes traceability and testability
- Includes multiple stakeholder perspectives
- Balances detail with maintainability
- Provides templates and examples for clarity