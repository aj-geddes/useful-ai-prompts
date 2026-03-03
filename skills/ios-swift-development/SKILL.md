---
name: ios-swift-development
description: >
  Develop native iOS apps with Swift. Covers MVVM architecture, SwiftUI,
  URLSession for networking, Combine for reactive programming, and Core Data
  persistence.
---

# iOS Swift Development

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Build high-performance native iOS applications using Swift with modern frameworks including SwiftUI, Combine, and async/await patterns.

## When to Use

- Creating native iOS applications with optimal performance
- Leveraging iOS-specific features and APIs
- Building apps that require tight hardware integration
- Using SwiftUI for declarative UI development
- Implementing complex animations and transitions

## Quick Start

Minimal working example:

```swift
import Foundation
import Combine

struct User: Codable, Identifiable {
  let id: UUID
  var name: String
  var email: String
}

class UserViewModel: ObservableObject {
  @Published var user: User?
  @Published var isLoading = false
  @Published var errorMessage: String?

  private let networkService: NetworkService

  init(networkService: NetworkService = .shared) {
    self.networkService = networkService
  }

  @MainActor
  func fetchUser(id: UUID) async {
    isLoading = true
    errorMessage = nil

// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [MVVM Architecture Setup](references/mvvm-architecture-setup.md) | MVVM Architecture Setup |
| [Network Service with URLSession](references/network-service-with-urlsession.md) | Network Service with URLSession |
| [SwiftUI Views](references/swiftui-views.md) | SwiftUI Views |

## Best Practices

### ✅ DO

- Use SwiftUI for modern UI development
- Implement MVVM architecture
- Use async/await patterns
- Store sensitive data in Keychain
- Handle errors gracefully
- Use @StateObject for ViewModels
- Validate API responses properly
- Implement Core Data for persistence
- Test on multiple iOS versions
- Use dependency injection
- Follow Swift style guidelines

### ❌ DON'T

- Store tokens in UserDefaults
- Make network calls on main thread
- Use deprecated UIKit patterns
- Ignore memory leaks
- Skip error handling
- Use force unwrapping (!)
- Store passwords in code
- Ignore accessibility
- Deploy untested code
- Use hardcoded API URLs
