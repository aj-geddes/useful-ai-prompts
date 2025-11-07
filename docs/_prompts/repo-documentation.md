---
category: management-leadership
compatible_models:
- claude-3.5-sonnet
- gpt-4
- gemini-pro
date: '2025-08-16'
description: Generate comprehensive, evidence-based repository documentation with professional Mermaid diagrams and architecture visualization
layout: prompt
slug: repo-documentation
tags:
- project management
- documentation
- architecture
- visualization
title: Repository Documentation Generator
use_cases:
- project-management optimization
- professional workflow enhancement
- documentation automation
version: 3.0.0
prompt: |
  I'll help you create comprehensive, evidence-based documentation for your repository. Let me understand your project:

  ## Understanding Your Documentation Needs

  **Repository Information:**
  - What repository should I document? (path or URL)
  - What is the primary purpose of this project?
  - Who is the target audience? (developers, users, contributors, stakeholders)
  - What programming languages and frameworks are used?

  **Documentation Scope:**
  - What level of detail do you need? (high-level overview, detailed technical docs, both)
  - Should I include architecture diagrams?
  - Do you need API or component documentation?
  - Are there specific sections you want? (setup, usage, contribution, deployment)

  **Architecture Visualization:**
  - What diagrams would be most valuable? (system architecture, class structure, process flows, data models)
  - Do you prefer flowcharts, sequence diagrams, or entity-relationship diagrams?
  - Should diagrams show deployment infrastructure?
  - Do you need directory structure visualization?

  **Style Preferences:**
  - What documentation style do you prefer? (technical, user-friendly, academic)
  - Are there organizational documentation standards?
  - Do you want dark or light themed diagrams?
  - Should code examples be included?

  **Content Requirements:**
  - What must be documented? (installation, configuration, usage, API, architecture)
  - Are there compliance or audit requirements?
  - Do you need version history or changelog?
  - Should troubleshooting guides be included?

  ---

  Based on your answers, I'll provide:

  ## 1. Professional README.md

  Comprehensive project overview with:
  - **Header Section**: Project name from manifest files, status badges for CI/CD
  - **Project Description**: Extracted from package.json, setup.py, or module docstrings
  - **Features List**: ONLY features with implemented code evidence
  - **Installation Instructions**: Based on actual setup scripts and dependencies
  - **Configuration Guide**: Environment variables and options referenced in code
  - **Usage Examples**: Practical demonstrations with code snippets
  - **Contributing Guidelines**: Development setup and contribution process

  ## 2. System Architecture Documentation

  High-level architecture with Mermaid diagrams:
  - **Component Diagram**: System structure and interactions
  - **Dark Handdrawn Theme**: Professional, consistent styling
  - **Layer Architecture**: Frontend, backend, database, external services
  - **Communication Flow**: Data flow and API interactions
  - **Integration Points**: Third-party services and dependencies
  - Evidence-based structure from actual codebase

  ## 3. Class and Code Structure

  Detailed class structure visualization:
  - **Class Diagrams**: Inheritance and composition relationships
  - **Method Documentation**: Public methods and their signatures
  - **Attribute Mapping**: Class properties and types
  - **Relationship Notation**: Accurate inheritance, composition, aggregation
  - **Design Patterns**: Documented patterns in use
  - Based ONLY on actual code analysis

  ## 4. Process and Workflow Documentation

  Operational flow diagrams:
  - **Sequence Diagrams**: Key process flows with method calls
  - **State Diagrams**: Component state transitions
  - **Timing Diagrams**: Interaction timing and sequence
  - **Activity Flows**: User workflows and system processes
  - Derived from actual method implementations

  ## 5. Data Model Documentation

  Database and data structure diagrams:
  - **Entity-Relationship Diagrams**: Data models and relationships
  - **Schema Documentation**: Table structures and constraints
  - **Cardinality Notation**: One-to-many, many-to-many relationships
  - **Data Types**: Field types and constraints
  - Based on actual database models in code

  ## 6. Infrastructure Documentation

  Deployment and infrastructure visualization:
  - **Deployment Diagrams**: Production infrastructure components
  - **Cloud Architecture**: Services and networking
  - **Scaling Patterns**: Load balancing and distribution
  - **Service Dependencies**: External service integrations
  - From actual infrastructure as code and deployment configs

  ## 7. Repository Structure Documentation

  Directory organization visualization:
  - **Directory Tree Diagrams**: Hierarchical structure
  - **Module Organization**: Logical grouping of components
  - **File Purpose**: Key file descriptions
  - **Configuration Files**: Important config locations
  - Accurate representation of actual repository

  ## 8. Build and CI/CD Process

  Development workflow documentation:
  - **Build Process Flow**: Compilation and packaging steps
  - **CI/CD Pipeline**: Automated testing and deployment
  - **Quality Gates**: Checks and validations
  - **Deployment Stages**: Dev, staging, production flow
  - Based on actual CI/CD configurations

  ## 9. Mermaid Diagram Standards

  All diagrams follow consistent styling:
  - **Dark Handdrawn Theme**: Professional, modern appearance
  - **GitHub Compatibility**: Proper node text quoting
  - **Readable Complexity**: 5-15 elements per diagram
  - **Accurate Relationships**: Correct notation and arrows
  - **Evidence-Based**: Only documented actual code structures
  - **File Path References**: Supporting documentation for each element

  ## 10. Documentation Quality Standards

  Ensuring accuracy and completeness:
  - **Zero Speculation**: Only document what exists in code
  - **Deterministic Output**: Reproducible documentation
  - **Source References**: File paths supporting all statements
  - **Focused Diagrams**: Complex systems broken into multiple views
  - **Maintainability**: Easy to update as code evolves

  ## 11. Comprehensive Coverage

  Complete documentation package:
  - **API Documentation**: Endpoints, parameters, responses
  - **Configuration Guide**: All configuration options explained
  - **Security Practices**: Authentication, authorization, data protection
  - **Performance Considerations**: Optimization tips and bottlenecks
  - **Troubleshooting**: Common issues and solutions
  - **Version History**: Changes and migration guides

  ## 12. Special Section Documentation

  Targeted documentation for specific needs:
  - **Developer Guide**: Setup, testing, debugging
  - **User Guide**: Installation, usage, examples
  - **API Reference**: Complete endpoint documentation
  - **Architecture Decision Records**: Why certain patterns were chosen
  - **Security Documentation**: Threat model and mitigations
  - **Deployment Guide**: Production deployment procedures

  ## 13. Code Example Integration

  Practical demonstrations:
  - **Basic Usage**: Simple getting-started examples
  - **Advanced Patterns**: Complex use case demonstrations
  - **Integration Examples**: Third-party service integration
  - **Testing Examples**: Unit and integration test patterns
  - All examples with working, tested code

  ## 14. Validation and Quality Checks

  Pre-generation analysis:
  - Codebase structure analysis
  - Actual relationship mapping
  - Diagram type selection based on code patterns
  - Important structure highlighting
  - Evidence verification for all statements

  ## 15. Output Format

  Professional Markdown structure:
  - Clean, hierarchical organization
  - Proper headings and navigation
  - Code blocks with syntax highlighting
  - Mermaid diagrams with consistent theming
  - Tables for structured information
  - Links and cross-references

  Tell me about your repository and I'll create comprehensive, evidence-based documentation with professional architecture diagrams that accurately represent your codebase!
---
