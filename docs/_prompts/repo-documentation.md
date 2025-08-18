---
category: project-management
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Professional prompt for project-management optimization and expert consultation
layout: prompt
slug: repo-documentation
tags:
- project management
title: Repo Documentation
use_cases:
- project-management optimization
- professional workflow enhancement
version: 3.0.0
---

Temperature: 0

Review the entire codebase in this repository and generate factual, evidence-based documentation with professional Mermaid diagrams using a consistent dark handdrawn style. Generate ONLY documentation and diagrams that can be directly supported by evidence in the code.

1. README.md - Based EXCLUSIVELY on actual repository contents:

   ## Header Section
   - Project name (extract directly from package.json, setup.py, pom.xml, or similar manifest files)
   - Status badges - Include ONLY for CI/CD systems with configuration files present

   ## Core Content
   - Project description: Use EXACT description from manifest files or main module docstrings
   - High-level Mermaid architecture diagram showing the system architecture:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     flowchart TD
       A["Module A"] -.-> B{"Component B"}
       B -.->|"Option 1"| C["Component C"]
       B -.->|"Option 2"| D["Component D"]
       C -.-> E["Output"]
       D -.-> E
     ```
   - Features list: ONLY features with corresponding implemented code
   - Installation instructions: Based SOLELY on actual setup scripts and declared dependencies
   - Configuration: Document ONLY environment variables and options actually referenced in code

2. Architecture Documentation:
   - Component diagram showing actual system structure:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     flowchart TD
       subgraph FE["Frontend"]
         UI["User Interface"]
         Logic["Client Logic"]
       end
       subgraph BE["Backend"]
         API["API Layer"]
         Service["Service Layer"]
         DB[("Database")]
       end
       UI -.-> Logic
       Logic -.-> API
       API -.-> Service
       Service -.-> DB
     ```

3. Class Structure Documentation:
   - Class diagram showing actual inheritance and composition relationships:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     classDiagram
       class BaseClass {
         +string property
         +method()
       }
       class ChildClass {
         +childMethod()
       }
       BaseClass <|-- ChildClass : extends
       ChildClass *-- ComposedClass : contains
     ```

4. Process Documentation:
   - Sequence diagram for key processes based on actual method calls:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD',
         'activationBorderColor': '#6BB4DD'
       }
     }}%%
     sequenceDiagram
       participant Client
       participant Server
       Client->>Server: request()
       activate Server
       Note over Server: Process request
       Server-->>Client: response
       deactivate Server
     ```
   - State diagram for components with state transitions:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     stateDiagram-v2
       [*] --> Idle
       Idle --> Processing: start
       Processing --> Complete: finish
       Processing --> Error: exception
       Complete --> [*]
       Error --> Idle: retry
     ```

5. Data Model Documentation:
   - Entity-relationship diagram for actual data models:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     erDiagram
       USER ||--o{ ORDER : places
       ORDER ||--|{ LINE-ITEM : contains
       USER {
         string id
         string name
         string email
       }
       ORDER {
         string id
         date created_at
         string status
       }
     ```

6. Infrastructure Documentation (if applicable):
   - Deployment diagram showing actual infrastructure components:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     flowchart TD
       subgraph Cloud["Cloud Environment"]
         LB["Load Balancer"]
         subgraph AppServers["Application Servers"]
           App1["Server 1"]
           App2["Server 2"]
         end
         subgraph DB["Database Cluster"]
           Primary[("Primary DB")]
           Secondary[("Secondary DB")]
         end
       end
       User["User"] -.-> LB
       LB -.-> AppServers
       AppServers -.-> DB
     ```

7. Repository Structure Documentation:
   - Directory structure diagram:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     flowchart TD
       Root["Root Directory"] -.-> Src["src/"]
       Root -.-> Docs["docs/"]
       Root -.-> Tests["tests/"]
       Src -.-> Components["components/"]
       Src -.-> Utils["utils/"]
       Components -.-> UI["ui/"]
       Components -.-> Logic["logic/"]
     ```

8. Build/CI Process Documentation (if applicable):
   - Workflow diagram showing actual build process:
     ```mermaid
     %%{init: {
       'theme': 'dark',
       'themeVariables': {
         'fontFamily': 'monospace',
         'primaryBorderColor': '#6BB4DD',
         'primaryColor': '#2D3A4D',
         'primaryTextColor': '#fff',
         'lineColor': '#6BB4DD'
       }
     }}%%
     flowchart TD
       Start["Start"] -.-> Build["Build"]
       Build -.-> Test["Test"]
       Test -.-> Deploy["Deploy"]
       Test -.-> Fail["Fail"]
       Deploy -.-> Release["Release"]
     ```

For all diagrams:

- Generate based ONLY on concrete evidence in the code
- Use the consistent dark handdrawn theme shown in the examples
- Keep diagrams focused and readable (5-15 elements per diagram)
- Include all relevant attributes and methods found in the code
- Use accurate relationship notations (inheritance, composition, etc.)
- Maintain the professional appearance while using the handdrawn style
- Apply appropriate level of detail based on the complexity of the code
- Use quotation marks for node text to ensure GitHub compatibility
- Avoid using special node shapes that might not be supported in GitHub

For all documentation:

- Reference specific file paths that support diagram elements
- Focus on actual implemented code, not aspirational features
- Maintain factual accuracy with zero speculation
- Break complex systems into multiple focused diagrams
- Ensure all documentation is deterministic and based only on evidence in the code

Before generating:

1. Analyze the codebase structure to identify components
2. Map actual relationships between components
3. Determine which diagram types best represent the specific code patterns
4. Plan diagrams to highlight the most important structures

Format the README.md and all documentation using clean, professional Markdown structure with appropriate headings, lists, and code blocks.
