# MVVM Architecture Setup

## MVVM Architecture Setup

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
