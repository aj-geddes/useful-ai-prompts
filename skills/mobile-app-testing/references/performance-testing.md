# Performance Testing

## Performance Testing

```swift
import XCTest

class PerformanceTests: XCTestCase {
  func testListRenderingPerformance() {
    let viewModel = ItemsViewModel()
    viewModel.items = (0..<1000).map { i in
      Item(id: UUID(), title: "Item \(i)", price: Double(i))
    }

    measure {
      _ = viewModel.items.filter { $0.price > 50 }
    }
  }

  func testNetworkResponseTime() {
    let networkService = NetworkService()

    measure {
      let expectation = XCTestExpectation(description: "Fetch user")

      Task {
        do {
          _ = try await networkService.fetch(User.self, from: "/users/test")
          expectation.fulfill()
        } catch {
          XCTFail("Network request failed")
        }
      }

      wait(for: [expectation], timeout: 10)
    }
  }
}
```
