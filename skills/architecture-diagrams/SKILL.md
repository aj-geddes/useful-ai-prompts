---
name: architecture-diagrams
description: >
  Create system architecture diagrams using Mermaid, PlantUML, C4 model,
  flowcharts, and sequence diagrams. Use when documenting architecture, system
  design, data flows, or technical workflows.
---

# Architecture Diagrams

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Create clear, maintainable architecture diagrams using code-based diagramming tools like Mermaid and PlantUML for system design, data flows, and technical documentation.

## When to Use

- System architecture documentation
- C4 model diagrams
- Data flow diagrams
- Sequence diagrams
- Component relationships
- Deployment diagrams
- Infrastructure architecture
- Microservices architecture
- Database schemas (visual)
- Integration patterns

## Quick Start

Minimal working example:

```mermaid
graph TB
    subgraph "Client Layer"
        Web[Web App]
        Mobile[Mobile App]
        CLI[CLI Tool]
    end

    subgraph "API Gateway Layer"
        Gateway[API Gateway<br/>Rate Limiting<br/>Authentication]
    end

    subgraph "Service Layer"
        Auth[Auth Service]
        User[User Service]
        Order[Order Service]
        Payment[Payment Service]
        Notification[Notification Service]
    end

    subgraph "Data Layer"
        UserDB[(User DB<br/>PostgreSQL)]
        OrderDB[(Order DB<br/>PostgreSQL)]
        Cache[(Redis Cache)]
        Queue[Message Queue<br/>RabbitMQ]
    end
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [System Architecture Diagram](references/system-architecture-diagram.md) | System Architecture Diagram |
| [Sequence Diagram](references/sequence-diagram.md) | Sequence Diagram |
| [C4 Context Diagram](references/c4-context-diagram.md) | C4 Context Diagram |
| [Component Diagram](references/component-diagram.md) | Component Diagram |
| [Deployment Diagram](references/deployment-diagram.md) | Deployment Diagram |
| [Data Flow Diagram](references/data-flow-diagram.md) | Data Flow Diagram |
| [Class Diagram](references/class-diagram.md) | Class Diagram |
| [Component Diagram](references/component-diagram-2.md) | Component Diagram |
| [Deployment Diagram](references/deployment-diagram-2.md) | Deployment Diagram |

## Best Practices

### ✅ DO

- Use consistent notation and symbols
- Include legends for complex diagrams
- Keep diagrams focused on one aspect
- Use color coding meaningfully
- Include titles and descriptions
- Version control your diagrams
- Use text-based formats (Mermaid, PlantUML)
- Show data flow direction clearly
- Include deployment details
- Document diagram conventions
- Keep diagrams up-to-date with code
- Use subgraphs for logical grouping

### ❌ DON'T

- Overcrowd diagrams with details
- Use inconsistent styling
- Skip diagram legends
- Create binary image files only
- Forget to document relationships
- Mix abstraction levels in one diagram
- Use proprietary formats
