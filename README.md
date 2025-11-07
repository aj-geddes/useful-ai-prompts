# AI Assistant Prompt & Skills Library

## 486+ Expert Prompts & 200 Claude Code Skills

This repository contains:
- **486 specialized prompts** across **22 categories** designed for AI assistants to adopt expert personas
- **200 focused skills** across **20 categories** for Claude Code to handle specific technical tasks

Each prompt combines multiple expert perspectives with professional frameworks. Each skill provides step-by-step guidance with code examples and best practices.

### 🚀 **Massive 2025 Expansion**

The library has grown from 259 to **486+ prompts**, adding comprehensive coverage for high-growth sectors:

- **Biotechnology** (15 prompts): Drug discovery, bioinformatics, gene editing, clinical trials
- **Blockchain** (5 prompts): DeFi, smart contracts, tokenization, Web3 development
- **Government Digital** (8 prompts): Digital transformation, smart cities, citizen services, policy
- **Healthcare Digital** (20 prompts): Telehealth, AI clinical decision support, patient engagement, EHR
- **Quantum Computing** (14 prompts): Algorithm development, quantum circuits, quantum ML, optimization
- **Renewable Energy** (19 prompts): Solar development, energy storage, grid integration, sustainability
- **Space Economy** (24 prompts): Commercial spaceflight, satellite operations, space tech, mission planning
- **Supply Chain** (6 prompts): Resilience planning, digital transformation, logistics optimization

### Quick Selection Guide

When assigned a task, select the appropriate prompt based on:

1. **Task Type** → Find matching workflow category
2. **Domain** → Select relevant expertise area
3. **Complexity** → Choose appropriate depth level

### Prompt Selection Matrix

| Task Category                | Primary Location                           | Key Prompts                                                                                       |
| ---------------------------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------- |
| **Financial Analysis**       | `/prompts/finance/`                        | `financial-analysis-expert.md` - Investment analysis, valuation, portfolio management             |
| **Software Development**     | `/prompts/technical/software-engineering/` | `fullstack-developer-architect.md` - Full-stack development with system architecture              |
| **Security Operations**      | `/prompts/technical/security/`             | `cybersecurity-defense-architect.md` - Threat detection, incident response, security architecture |
| **Business Analysis**        | `/prompts/business/business-analysis/`     | `business-analyst-strategic-excellence.md` - Requirements engineering, process improvement        |
| **Project Management**       | `/prompts/business/project-management/`    | `comprehensive-risk-assessment.md` - Risk analysis and mitigation planning                        |
| **Marketing Strategy**       | `/prompts/business/marketing/`             | `marketing-manager-strategist.md` - Team leadership, campaign management                          |
| **HR Management**            | `/prompts/human-resources/`                | `hr-excellence-leader.md` - Talent strategy, organizational development                           |
| **Customer Service**         | `/prompts/customer-service/`               | `customer-experience-excellence-leader.md` - Service operations, team leadership                  |
| **Data Science**             | `/prompts/technical/data-science/`         | `model-evaluation-framework.md` - ML model validation and deployment                              |
| **Research**                 | `/prompts/academic/research/`              | `research-excellence-scientist.md` - Scientific research and grant writing                        |
| **Executive Support**        | `/prompts/administrative/`                 | `executive-excellence-partner.md` - Strategic administrative support                              |
| **Supply Chain**             | `/prompts/operations/`                     | `supply-chain-excellence-director.md` - Logistics and network optimization                        |
| **Construction**             | `/prompts/engineering/`                    | `construction-excellence-director.md` - Project delivery and safety management                    |
| **Pharmaceutical R&D**       | `/prompts/healthcare/`                     | `pharmaceutical-research-excellence.md` - Drug development and clinical trials                    |
| **Graphic Design**           | `/prompts/creative/design/`                | `graphic-design-expert.md` - Visual design and brand strategy                                     |
| **Compliance**               | `/prompts/business/legal/`                 | `compliance-officer-expert.md` - Regulatory compliance and risk management                        |
| **Operations**               | `/prompts/business/operations/`            | `operations-manager-excellence.md` - Operational excellence and team development                  |
| **🧬 Biotechnology**          | `/prompts/biotechnology/`                  | `ai-powered-drug-screening-optimization.md` - Drug discovery and bioinformatics analysis         |
| **🔗 Blockchain & Web3**      | `/prompts/blockchain/`                     | `decentralized-finance-protocol-development.md` - DeFi protocols and smart contracts             |
| **🏛️ Government Digital**     | `/prompts/government/`                     | `digital-government-transformation-strategy.md` - Public sector digital transformation           |
| **🏥 Healthcare Digital**     | `/prompts/healthcare-digital/`             | `healthcare-digital-transformation-strategist.md` - Healthcare technology and telehealth         |
| **⚛️ Quantum Computing**      | `/prompts/quantum-computing/`              | `quantum-circuit-optimization-design.md` - Quantum algorithms and circuit development            |
| **☀️ Renewable Energy**       | `/prompts/renewable-energy/`               | `utility-scale-solar-farm-development.md` - Solar development and clean energy projects          |
| **🚀 Space Economy**          | `/prompts/space-economy/`                  | `commercial-space-mission-architecture.md` - Commercial spaceflight and satellite operations     |
| **📦 Supply Chain Digital**   | `/prompts/supply-chain/`                   | `supply-chain-resilience-strategy-architect.md` - Digital supply chain transformation            |

### How to Use Prompts

1. **Load the appropriate prompt file**
2. **Replace all `{{variables}}` with context-specific information**
3. **Execute the four-phase framework**:
   - Phase 1: Assessment/Analysis
   - Phase 2: Strategic Design
   - Phase 3: Implementation/Execution
   - Phase 4: Optimization/Control

### Prompt Structure

Each prompt contains:

```yaml
Metadata:
  - Category: Domain classification
  - Tags: Searchable keywords
  - Personas: Expert roles to adopt
  - Use Cases: Applicable scenarios

Architecture:
  - Dual-Persona: Primary expert + complementary specialist
  - Frameworks: 3-5 professional methodologies
  - Processing: 4-phase systematic approach
  - Output: Structured deliverables (600+ lines average)
```

### Task Matching Examples

**User Request**: "Help me analyze our company's financial performance and create projections"
→ **Select**: `/prompts/finance/financial-analysis-expert.md`

**User Request**: "Design a secure architecture for our cloud migration"
→ **Select**: `/prompts/technical/security/cybersecurity-defense-architect.md`

**User Request**: "Create a comprehensive hiring process for engineering roles"
→ **Select**: `/prompts/human-resources/hr-excellence-leader.md`

**User Request**: "Optimize our software deployment pipeline"
→ **Select**: `/prompts/technical/devops/cicd-pipeline-optimizer.md`

### Integration Guidelines

For AI agents and assistants:

1. **Parse task requirements** to identify:
   - Primary domain (technical, business, creative, etc.)
   - Specific workflow (analysis, creation, optimization, etc.)
   - Output requirements (reports, code, strategies, etc.)

2. **Match to prompt taxonomy**:

   ```mermaid
   flowchart LR
       A[Task] --> B{Domain?}
       B -->|Technical| C[prompts/technical/]
       B -->|Business| D[prompts/business/]
       B -->|Creative| E[prompts/creative/]
       B -->|Specialized| F[prompts/specialized/]

       C --> C1[subcategory/]
       D --> D1[subcategory/]
       E --> E1[subcategory/]
       F --> F1[subcategory/]

       C1 --> G[specific-prompt.md]
       D1 --> G
       E1 --> G
       F1 --> G

       style A fill:#0066cc,color:#fff
       style G fill:#00aa66,color:#fff
   ```

3. **Load and customize** the selected prompt:
   - Inject task-specific context
   - Set appropriate variables
   - Adjust output format if needed

4. **Execute systematically**:
   - Follow the 4-phase framework
   - Maintain persona consistency
   - Deliver structured outputs

### Metadata Index

Quick reference for programmatic selection:

```mermaid
graph TB
    A[Prompt Library] --> B[Technical]
    A --> C[Business]
    A --> D[Creative]
    A --> E[Specialized]

    B --> B1[software-engineering]
    B --> B2[devops]
    B --> B3[data-science]
    B --> B4[security]
    B --> B5[architecture]

    C --> C1[finance]
    C --> C2[marketing]
    C --> C3[operations]
    C --> C4[management]
    C --> C5[legal]

    D --> D1[design]
    D --> D2[content-strategy]
    D --> D3[ux-design]

    E --> E1[healthcare]
    E --> E2[engineering]
    E --> E3[education]
    E --> E4[research]

    style A fill:#0066cc,color:#fff
    style B fill:#00aa66,color:#fff
    style C fill:#00aa66,color:#fff
    style D fill:#00aa66,color:#fff
    style E fill:#00aa66,color:#fff
```

**JSON Format** (for programmatic access):
```json
{
  "prompts": {
    "technical": [
      "software-engineering",
      "devops",
      "data-science",
      "security",
      "architecture"
    ],
    "business": ["finance", "marketing", "operations", "management", "legal"],
    "creative": ["design", "content-strategy", "ux-design"],
    "specialized": ["healthcare", "engineering", "education", "research"]
  }
}
```

---

## Claude Code Skills Library

In addition to comprehensive prompts, this repository includes **200 specialized skills** designed specifically for [Claude Code](https://code.claude.com/). Skills provide focused, actionable guidance for specific technical tasks.

### What are Skills?

Skills are specialized capabilities that Claude Code can invoke automatically based on your requests. Unlike broad prompts, skills:

- **Focus on one specific capability** (e.g., "refactor legacy code", "design REST APIs")
- **Activate automatically** when Claude detects relevant keywords in your request
- **Provide step-by-step instructions** with code examples and best practices
- **Easy to integrate** - copy to `.claude/skills/` in your project for team sharing

### Skills Overview

```mermaid
graph LR
    A[200 Skills] --> B[Software Dev<br/>35 skills]
    A --> C[DevOps<br/>20 skills]
    A --> D[Testing & QA<br/>15 skills]
    A --> E[Database<br/>12 skills]
    A --> F[API & Integration<br/>12 skills]
    A --> G[Security<br/>15 skills]
    A --> H[12 More<br/>Categories<br/>91 skills]

    style A fill:#0066cc,color:#fff
    style B fill:#00aa66,color:#fff
    style C fill:#00aa66,color:#fff
    style D fill:#00aa66,color:#fff
    style E fill:#00aa66,color:#fff
    style F fill:#00aa66,color:#fff
    style G fill:#00aa66,color:#fff
    style H fill:#00aa66,color:#fff
```

### Skills Categories (200 Total)

| Category | Count | Examples |
|----------|-------|----------|
| **Software Development & Engineering** | 35 | refactor-legacy-code, code-review-analysis, design-patterns |
| **DevOps & Infrastructure** | 20 | docker-containerization, kubernetes-deployment, terraform-iac |
| **Testing & QA** | 15 | unit-testing-framework, e2e-testing, test-automation |
| **Security & Compliance** | 15 | vulnerability-scanning, oauth-implementation, data-encryption |
| **Documentation & Writing** | 15 | api-documentation, architecture-diagrams, runbook-creation |
| **Data Science & Analytics** | 20 | exploratory-data-analysis, feature-engineering, ab-testing |
| **Database & Storage** | 12 | sql-query-optimization, database-indexing, schema-design |
| **API & Integration** | 12 | rest-api-design, graphql-implementation, webhook-development |
| **Cloud Platforms** | 15 | aws-lambda, serverless-architecture, cloud-cost-optimization |
| **Frontend Development** | 12 | react-components, responsive-design, css-architecture |
| **Backend Development** | 12 | nodejs-express, django-application, background-jobs |
| **Mobile Development** | 8 | react-native, flutter-development, push-notifications |
| **Machine Learning & AI** | 10 | ml-model-training, model-deployment, hyperparameter-tuning |
| **Monitoring & Observability** | 8 | prometheus-monitoring, grafana-dashboards, distributed-tracing |
| **Version Control & CI/CD** | 10 | git-workflow-strategy, github-actions, semantic-versioning |
| **Project Management** | 10 | agile-sprint-planning, risk-assessment, release-planning |
| **Business Analysis** | 8 | requirements-gathering, user-story-writing, process-mapping |
| **Design & UX** | 8 | wireframe-prototyping, design-systems, user-research |
| **Performance & Optimization** | 8 | web-performance-audit, bundle-optimization, database-tuning |
| **Troubleshooting & Debugging** | 12 | production-debugging, memory-leak-detection, root-cause-analysis |

### How to Use Skills

1. **Copy skills to your project:**
   ```bash
   cp -r skills/ /path/to/your/project/.claude/skills/
   ```

2. **Use naturally in conversations:**
   ```
   You: "Help me refactor this legacy code"
   Claude: (Automatically invokes refactor-legacy-code skill)
   ```

3. **Skills activate automatically** based on keywords in your requests

### Skills Resources

- **[Complete Skills Matrix](SKILLS-MATRIX.md)**: All 200 skills with descriptions and trigger keywords
- **[Skills Website](https://aj-geddes.github.io/useful-ai-prompts/skills)**: Browse skills by category on GitHub Pages
- **[Claude Code Skills Docs](https://code.claude.com/docs/en/skills)**: Official documentation for creating and using skills

### Example Skills

#### `refactor-legacy-code`
Modernize legacy codebases with:
- Incremental refactoring strategies
- Modern pattern implementations
- Safety net testing approaches
- Complete before/after examples

#### `docker-containerization`
Create production-ready containers with:
- Multi-stage build optimization
- Security best practices
- Docker Compose multi-container setups
- Language-specific examples

#### `rest-api-design`
Design RESTful APIs following best practices:
- Resource naming conventions
- HTTP method usage
- Response format standards
- OpenAPI documentation

#### `unit-testing-framework`
Write comprehensive tests with:
- AAA pattern structure
- Language-specific examples (Jest, pytest, JUnit)
- Mocking strategies
- Coverage guidelines

See [`skills/`](skills/) for complete implementations.

---

### Performance Notes

- Each prompt is designed for 600+ line outputs
- Combines multiple expert perspectives
- Includes industry-standard frameworks
- Optimized for accuracy and completeness

### Repository Structure

```mermaid
graph TD
    A[useful-ai-prompts] --> B[prompts/]
    A --> C[skills/]
    A --> D[metadata/]
    A --> E[docs/]
    A --> F[PROMPT-INDEX.json]
    A --> G[SKILLS-MATRIX.md]

    B --> B1[486 expert prompts<br/>organized by domain]
    C --> C1[200 Claude Code skills<br/>organized by category]
    D --> D1[Framework definitions<br/>and guidelines]
    E --> E1[Jekyll website<br/>for browsing & search]
    F --> F1[Machine-readable<br/>prompt catalog]
    G --> G1[Complete skills reference<br/>with trigger keywords]

    style A fill:#0066cc,color:#fff
    style B fill:#00aa66,color:#fff
    style C fill:#ff6b6b,color:#fff
    style D fill:#00aa66,color:#fff
    style E fill:#00aa66,color:#fff
    style F fill:#00aa66,color:#fff
    style G fill:#ff6b6b,color:#fff
```

---

**For human users**: See [README-HUMANS.md](README-HUMANS.md) for user-friendly documentation and examples.

**For developers**: See [AI-AGENT-GUIDE.md](AI-AGENT-GUIDE.md) for integration specifications.
