---
name: android-kotlin-development
description: >
  Develop native Android apps with Kotlin. Covers MVVM with Jetpack, Compose for
  modern UI, Retrofit for API calls, Room for local storage, and navigation
  architecture.
---

# Android Kotlin Development

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build robust native Android applications using Kotlin with modern architecture patterns, Jetpack libraries, and Compose for declarative UI.

## When to Use

- Creating native Android applications with best practices
- Using Kotlin for type-safe development
- Implementing MVVM architecture with Jetpack
- Building modern UIs with Jetpack Compose
- Integrating with Android platform APIs

## Quick Start

Minimal working example:

```kotlin
// Models
data class User(
  val id: String,
  val name: String,
  val email: String,
  val avatarUrl: String? = null
)

data class Item(
  val id: String,
  val title: String,
  val description: String,
  val imageUrl: String? = null,
  val price: Double
)

// API Service with Retrofit
interface ApiService {
  @GET("/users/{id}")
  suspend fun getUser(@Path("id") userId: String): User

  @PUT("/users/{id}")
  suspend fun updateUser(
    @Path("id") userId: String,
    @Body user: User
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Models & API Service](references/models-api-service.md) | Models & API Service |
| [MVVM ViewModels with Jetpack](references/mvvm-viewmodels-with-jetpack.md) | MVVM ViewModels with Jetpack |
| [Jetpack Compose UI](references/jetpack-compose-ui.md) | Jetpack Compose UI |

## Best Practices

### ✅ DO

- Use Kotlin for all new Android code
- Implement MVVM with Jetpack libraries
- Use Jetpack Compose for UI development
- Leverage coroutines for async operations
- Use Room for local data persistence
- Implement proper error handling
- Use Hilt for dependency injection
- Use StateFlow for reactive state
- Test on multiple device types
- Follow Android design guidelines

### ❌ DON'T

- Store tokens in SharedPreferences
- Make network calls on main thread
- Ignore lifecycle management
- Skip null safety checks
- Hardcode strings and resources
- Ignore configuration changes
- Store passwords in code
- Deploy without device testing
- Use deprecated APIs
- Accumulate memory leaks
