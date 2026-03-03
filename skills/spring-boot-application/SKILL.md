---
name: spring-boot-application
description: >
  Build enterprise Spring Boot applications with annotations, dependency
  injection, data persistence, REST controllers, and security. Use when
  developing Spring applications, managing beans, implementing services, and
  configuring Spring Boot projects.
---

# Spring Boot Application

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Develop production-ready Spring Boot applications with proper annotation-based configuration, dependency injection, REST controllers, JPA data persistence, service layers, and security implementation following Spring conventions.

## When to Use

- Building Spring Boot REST APIs
- Implementing service-oriented architectures
- Configuring data persistence with JPA
- Managing dependency injection
- Implementing Spring Security
- Building microservices with Spring Boot

## Quick Start

Minimal working example:

```xml
<!-- pom.xml -->
<project>
    <modelVersion>4.0.0</modelVersion>
    <groupId>com.example</groupId>
    <artifactId>api-service</artifactId>
    <version>1.0.0</version>

    <parent>
        <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-starter-parent</artifactId>
        <version>3.1.0</version>
    </parent>

    <dependencies>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-security</artifactId>
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Spring Boot Project Setup](references/spring-boot-project-setup.md) | Spring Boot Project Setup |
| [Entity Models with JPA Annotations](references/entity-models-with-jpa-annotations.md) | Entity Models with JPA Annotations |
| [Repository Layer with Spring Data JPA](references/repository-layer-with-spring-data-jpa.md) | Repository Layer with Spring Data JPA |
| [Service Layer with Business Logic](references/service-layer-with-business-logic.md) | Service Layer with Business Logic |
| [REST Controllers with Request/Response Handling](references/rest-controllers-with-requestresponse-handling.md) | REST Controllers with Request/Response Handling |
| [Spring Security Configuration](references/spring-security-configuration.md) | Spring Security Configuration |
| [Application Configuration](references/application-configuration.md) | Application Configuration |

## Best Practices

### ✅ DO

- Use dependency injection for loose coupling
- Implement service layer for business logic
- Use repositories for data access
- Leverage Spring Security for authentication
- Use @Transactional for transaction management
- Validate input in controllers
- Return appropriate HTTP status codes
- Use DTOs for request/response mapping
- Implement proper exception handling
- Use Spring's @Async for async operations

### ❌ DON'T

- Put business logic in controllers
- Access database directly in controllers
- Store secrets in configuration files
- Use eager loading for large relationships
- Ignore transaction boundaries
- Return database entities in API responses
- Implement authentication in controllers
- Use raw SQL without parameterized queries
- Forget to validate user input
