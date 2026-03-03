# Android Testing with Espresso

## Android Testing with Espresso

```kotlin
@RunWith(AndroidJUnit4::class)
class UserViewModelTest {
  private lateinit var viewModel: UserViewModel
  private val mockApiService = mock<ApiService>()

  @Before
  fun setUp() {
    viewModel = UserViewModel(mockApiService)
  }

  @Test
  fun fetchUserSuccess() = runTest {
    val expectedUser = User("1", "John", "john@example.com")
    `when`(mockApiService.getUser("1")).thenReturn(expectedUser)

    viewModel.fetchUser("1")

    assertEquals(expectedUser.name, viewModel.user.value?.name)
    assertEquals(null, viewModel.errorMessage.value)
  }

  @Test
  fun fetchUserFailure() = runTest {
    `when`(mockApiService.getUser("1"))
      .thenThrow(IOException("Network error"))

    viewModel.fetchUser("1")

    assertEquals(null, viewModel.user.value)
    assertNotNull(viewModel.errorMessage.value)
  }
}

// UI Test with Espresso
@RunWith(AndroidJUnit4::class)
class LoginActivityTest {
  @get:Rule
  val activityRule = ActivityScenarioRule(LoginActivity::class.java)

  @Test
  fun testLoginWithValidCredentials() {
    onView(withId(R.id.emailInput))
      .perform(typeText("user@example.com"))

    onView(withId(R.id.passwordInput))
      .perform(typeText("password123"))

    onView(withId(R.id.loginButton))
      .perform(click())

    onView(withText("Home"))
      .check(matches(isDisplayed()))
  }

  @Test
  fun testLoginWithInvalidCredentials() {
    onView(withId(R.id.emailInput))
      .perform(typeText("invalid@example.com"))

    onView(withId(R.id.passwordInput))
      .perform(typeText("wrongpassword"))

    onView(withId(R.id.loginButton))
      .perform(click())

    onView(withText(containsString("Invalid credentials")))
      .check(matches(isDisplayed()))
  }

  @Test
  fun testNavigationBetweenTabs() {
    onView(withId(R.id.profileTab)).perform(click())
    onView(withText("Profile")).check(matches(isDisplayed()))

    onView(withId(R.id.homeTab)).perform(click())
    onView(withText("Home")).check(matches(isDisplayed()))
  }
}
```
