---
name: ios-swift-development
description: Develop native iOS apps with Swift. Covers MVVM architecture, SwiftUI, URLSession for networking, Combine for reactive programming, and Core Data persistence.
---

# iOS Swift Development

## Overview

Build high-performance native iOS applications using Swift with modern frameworks including SwiftUI, Combine, and async/await patterns.

## When to Use

- Creating native iOS applications with optimal performance
- Leveraging iOS-specific features and APIs
- Building apps that require tight hardware integration
- Using SwiftUI for declarative UI development
- Implementing complex animations and transitions

## Instructions

### 1. **MVVM Architecture Setup**

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

    do {
      user = try await networkService.fetch(User.self, from: "/users/\(id)")
    } catch {
      errorMessage = error.localizedDescription
    }

    isLoading = false
  }

  @MainActor
  func updateUser(_ userData: User) async {
    guard let user = user else { return }

    do {
      self.user = try await networkService.put(
        User.self,
        to: "/users/\(user.id)",
        body: userData
      )
    } catch {
      errorMessage = "Failed to update user"
    }
  }

  func logout() {
    user = nil
    errorMessage = nil
  }
}
```

### 2. **Network Service with URLSession**

```swift
class NetworkService {
  static let shared = NetworkService()

  private let session: URLSession
  private let baseURL: URL

  init(
    session: URLSession = .shared,
    baseURL: URL = URL(string: "https://api.example.com")!
  ) {
    self.session = session
    self.baseURL = baseURL
  }

  func fetch<T: Decodable>(
    _: T.Type,
    from endpoint: String
  ) async throws -> T {
    let url = baseURL.appendingPathComponent(endpoint)
    var request = URLRequest(url: url)
    request.addAuthHeader()

    let (data, response) = try await session.data(for: request)
    try validateResponse(response)

    let decoder = JSONDecoder()
    decoder.dateDecodingStrategy = .iso8601
    return try decoder.decode(T.self, from: data)
  }

  func put<T: Decodable, Body: Encodable>(
    _: T.Type,
    to endpoint: String,
    body: Body
  ) async throws -> T {
    let url = baseURL.appendingPathComponent(endpoint)
    var request = URLRequest(url: url)
    request.httpMethod = "PUT"
    request.addAuthHeader()
    request.setValue("application/json", forHTTPHeaderField: "Content-Type")

    let encoder = JSONEncoder()
    encoder.dateEncodingStrategy = .iso8601
    request.httpBody = try encoder.encode(body)

    let (data, response) = try await session.data(for: request)
    try validateResponse(response)

    let decoder = JSONDecoder()
    return try decoder.decode(T.self, from: data)
  }

  private func validateResponse(_ response: URLResponse) throws {
    guard let httpResponse = response as? HTTPURLResponse else {
      throw NetworkError.invalidResponse
    }

    switch httpResponse.statusCode {
    case 200...299:
      return
    case 401:
      throw NetworkError.unauthorized
    case 500...599:
      throw NetworkError.serverError
    default:
      throw NetworkError.unknown
    }
  }
}

enum NetworkError: LocalizedError {
  case invalidResponse
  case unauthorized
  case serverError
  case unknown

  var errorDescription: String? {
    switch self {
    case .invalidResponse: return "Invalid response"
    case .unauthorized: return "Unauthorized"
    case .serverError: return "Server error"
    case .unknown: return "Unknown error"
    }
  }
}

extension URLRequest {
  mutating func addAuthHeader() {
    if let token = KeychainManager.shared.getToken() {
      setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")
    }
  }
}
```

### 3. **SwiftUI Views**

```swift
struct ContentView: View {
  @StateObject var userViewModel = UserViewModel()

  var body: some View {
    TabView {
      HomeView()
        .tabItem { Label("Home", systemImage: "house") }

      ProfileView(viewModel: userViewModel)
        .tabItem { Label("Profile", systemImage: "person") }
    }
  }
}

struct HomeView: View {
  @State var items: [Item] = []
  @State var loading = true

  var body: some View {
    NavigationView {
      ZStack {
        if loading {
          ProgressView()
        } else {
          List(items) { item in
            NavigationLink(destination: ItemDetailView(item: item)) {
              VStack(alignment: .leading) {
                Text(item.title).font(.headline)
                Text(item.description).font(.subheadline).foregroundColor(.gray)
              }
            }
          }
        }
      }
      .navigationTitle("Items")
      .task {
        await loadItems()
      }
    }
  }

  private func loadItems() async {
    do {
      items = try await NetworkService.shared.fetch([Item].self, from: "/items")
    } catch {
      print("Error: \(error)")
    }
    loading = false
  }
}

struct ItemDetailView: View {
  let item: Item
  @Environment(\.dismiss) var dismiss

  var body: some View {
    ScrollView {
      VStack(alignment: .leading, spacing: 16) {
        Text(item.title).font(.title2).fontWeight(.bold)
        Text(item.description).font(.body)
        Text("Price: $\(String(format: "%.2f", item.price))")
          .font(.headline).foregroundColor(.blue)
        Spacer()
      }
      .padding()
    }
    .navigationBarTitleDisplayMode(.inline)
  }
}

struct ProfileView: View {
  @ObservedObject var viewModel: UserViewModel
  @State var isLoading = true

  var body: some View {
    NavigationView {
      ZStack {
        if viewModel.isLoading {
          ProgressView()
        } else if let user = viewModel.user {
          VStack(spacing: 20) {
            Text(user.name).font(.title).fontWeight(.bold)
            Text(user.email).font(.subheadline)
            Button("Logout") { viewModel.logout() }
              .foregroundColor(.red)
            Spacer()
          }
          .padding()
        } else {
          Text("No profile data")
        }
      }
      .navigationTitle("Profile")
      .task {
        await viewModel.fetchUser(id: UUID())
      }
    }
  }
}

struct Item: Codable, Identifiable {
  let id: String
  let title: String
  let description: String
  let price: Double
}
```

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
