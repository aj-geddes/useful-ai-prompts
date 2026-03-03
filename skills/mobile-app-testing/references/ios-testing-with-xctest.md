# iOS Testing with XCTest

## iOS Testing with XCTest

```swift
import XCTest
@testable import MyApp

class UserViewModelTests: XCTestCase {
  var viewModel: UserViewModel!
  var mockNetworkService: MockNetworkService!

  override func setUp() {
    super.setUp()
    mockNetworkService = MockNetworkService()
    viewModel = UserViewModel(networkService: mockNetworkService)
  }

  func testFetchUserSuccess() async {
    let expectedUser = User(id: UUID(), name: "John", email: "john@example.com")
    mockNetworkService.mockUser = expectedUser

    await viewModel.fetchUser(id: expectedUser.id)

    XCTAssertEqual(viewModel.user?.name, "John")
    XCTAssertNil(viewModel.errorMessage)
    XCTAssertFalse(viewModel.isLoading)
  }

  func testFetchUserFailure() async {
    mockNetworkService.shouldFail = true

    await viewModel.fetchUser(id: UUID())

    XCTAssertNil(viewModel.user)
    XCTAssertNotNil(viewModel.errorMessage)
    XCTAssertFalse(viewModel.isLoading)
  }
}

class MockNetworkService: NetworkService {
  var mockUser: User?
  var shouldFail = false

  override func fetch<T: Decodable>(
    _: T.Type,
    from endpoint: String
  ) async throws -> T {
    if shouldFail {
      throw NetworkError.unknown
    }
    return mockUser as! T
  }
}

// UI Test
class LoginUITests: XCTestCase {
  override func setUp() {
    super.setUp()
    continueAfterFailure = false
    XCUIApplication().launch()
  }

  func testLoginFlow() {
    let app = XCUIApplication()

    let emailTextField = app.textFields["emailInput"]
    let passwordTextField = app.secureTextFields["passwordInput"]
    let loginButton = app.buttons["loginButton"]

    emailTextField.tap()
    emailTextField.typeText("user@example.com")

    passwordTextField.tap()
    passwordTextField.typeText("password123")

    loginButton.tap()

    let homeText = app.staticTexts["Home Feed"]
    XCTAssertTrue(homeText.waitForExistence(timeout: 5))
  }

  func testNavigationBetweenTabs() {
    let app = XCUIApplication()
    let profileTab = app.tabBars.buttons["Profile"]
    let homeTab = app.tabBars.buttons["Home"]

    profileTab.tap()
    XCTAssertTrue(app.staticTexts["Profile"].exists)

    homeTab.tap()
    XCTAssertTrue(app.staticTexts["Home"].exists)
  }
}
```
