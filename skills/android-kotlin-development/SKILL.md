---
name: android-kotlin-development
description: Develop native Android apps with Kotlin. Covers MVVM with Jetpack, Compose for modern UI, Retrofit for API calls, Room for local storage, and navigation architecture.
---

# Android Kotlin Development

## Overview

Build robust native Android applications using Kotlin with modern architecture patterns, Jetpack libraries, and Compose for declarative UI.

## When to Use

- Creating native Android applications with best practices
- Using Kotlin for type-safe development
- Implementing MVVM architecture with Jetpack
- Building modern UIs with Jetpack Compose
- Integrating with Android platform APIs

## Instructions

### 1. **Models & API Service**

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
  ): User

  @GET("/items")
  suspend fun getItems(@Query("filter") filter: String = "all"): List<Item>

  @POST("/items")
  suspend fun createItem(@Body item: Item): Item
}

// Network client setup
@Module
@InstallIn(SingletonComponent::class)
object NetworkModule {
  @Provides
  @Singleton
  fun provideRetrofit(): Retrofit {
    val httpClient = OkHttpClient.Builder()
      .addInterceptor { chain ->
        val original = chain.request()
        val requestBuilder = original.newBuilder()

        val token = PreferencesManager.getToken()
        if (token.isNotEmpty()) {
          requestBuilder.addHeader("Authorization", "Bearer $token")
        }

        requestBuilder.addHeader("Content-Type", "application/json")
        chain.proceed(requestBuilder.build())
      }
      .connectTimeout(30, TimeUnit.SECONDS)
      .readTimeout(30, TimeUnit.SECONDS)
      .build()

    return Retrofit.Builder()
      .baseUrl("https://api.example.com")
      .client(httpClient)
      .addConverterFactory(GsonConverterFactory.create())
      .build()
  }

  @Provides
  @Singleton
  fun provideApiService(retrofit: Retrofit): ApiService {
    return retrofit.create(ApiService::class.java)
  }
}
```

### 2. **MVVM ViewModels with Jetpack**

```kotlin
@HiltViewModel
class UserViewModel @Inject constructor(
  private val apiService: ApiService
) : ViewModel() {
  private val _user = MutableStateFlow<User?>(null)
  val user: StateFlow<User?> = _user.asStateFlow()

  private val _isLoading = MutableStateFlow(false)
  val isLoading: StateFlow<Boolean> = _isLoading.asStateFlow()

  private val _errorMessage = MutableStateFlow<String?>(null)
  val errorMessage: StateFlow<String?> = _errorMessage.asStateFlow()

  fun fetchUser(userId: String) {
    viewModelScope.launch {
      _isLoading.value = true
      _errorMessage.value = null

      try {
        val user = apiService.getUser(userId)
        _user.value = user
      } catch (e: Exception) {
        _errorMessage.value = e.message ?: "Unknown error"
      } finally {
        _isLoading.value = false
      }
    }
  }

  fun logout() {
    _user.value = null
  }
}

@HiltViewModel
class ItemsViewModel @Inject constructor(
  private val apiService: ApiService
) : ViewModel() {
  private val _items = MutableStateFlow<List<Item>>(emptyList())
  val items: StateFlow<List<Item>> = _items.asStateFlow()

  private val _isLoading = MutableStateFlow(false)
  val isLoading: StateFlow<Boolean> = _isLoading.asStateFlow()

  fun fetchItems(filter: String = "all") {
    viewModelScope.launch {
      _isLoading.value = true
      try {
        val items = apiService.getItems(filter)
        _items.value = items
      } catch (e: Exception) {
        println("Error fetching items: ${e.message}")
      } finally {
        _isLoading.value = false
      }
    }
  }

  fun addItem(item: Item) {
    viewModelScope.launch {
      try {
        val created = apiService.createItem(item)
        _items.value = _items.value + created
      } catch (e: Exception) {
        println("Error creating item: ${e.message}")
      }
    }
  }
}
```

### 3. **Jetpack Compose UI**

```kotlin
@Composable
fun MainScreen() {
  val navController = rememberNavController()

  NavHost(navController = navController, startDestination = "home") {
    composable("home") { HomeScreen(navController) }
    composable("profile") { ProfileScreen(navController) }
    composable("details/{itemId}") { backStackEntry ->
      val itemId = backStackEntry.arguments?.getString("itemId") ?: return@composable
      DetailsScreen(itemId = itemId, navController = navController)
    }
  }
}

@Composable
fun HomeScreen(navController: NavController) {
  val viewModel: ItemsViewModel = hiltViewModel()
  val items by viewModel.items.collectAsState()
  val isLoading by viewModel.isLoading.collectAsState()

  LaunchedEffect(Unit) {
    viewModel.fetchItems()
  }

  Scaffold(
    topBar = { TopAppBar(title = { Text("Items") }) }
  ) { paddingValues ->
    if (isLoading) {
      Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        CircularProgressIndicator()
      }
    } else {
      LazyColumn(
        modifier = Modifier
          .padding(paddingValues)
          .fillMaxSize(),
        contentPadding = PaddingValues(8.dp)
      ) {
        items(items) { item ->
          ItemCard(
            item = item,
            onClick = { navController.navigate("details/${item.id}") }
          )
        }
      }
    }
  }
}

@Composable
fun ItemCard(item: Item, onClick: () -> Unit) {
  Card(
    modifier = Modifier
      .fillMaxWidth()
      .padding(8.dp)
      .clickable { onClick() }
  ) {
    Row(modifier = Modifier.padding(16.dp)) {
      Column(modifier = Modifier.weight(1f)) {
        Text(text = item.title, style = MaterialTheme.typography.headlineSmall)
        Text(text = item.description, style = MaterialTheme.typography.bodyMedium)
        Text(text = "$${item.price}", style = MaterialTheme.typography.bodySmall)
      }
      Icon(imageVector = Icons.Default.ArrowForward, contentDescription = null)
    }
  }
}

@Composable
fun ProfileScreen(navController: NavController) {
  val viewModel: UserViewModel = hiltViewModel()
  val user by viewModel.user.collectAsState()
  val isLoading by viewModel.isLoading.collectAsState()

  LaunchedEffect(Unit) {
    viewModel.fetchUser("current-user")
  }

  Scaffold(
    topBar = { TopAppBar(title = { Text("Profile") }) }
  ) { paddingValues ->
    if (isLoading) {
      Box(modifier = Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        CircularProgressIndicator()
      }
    } else if (user != null) {
      Column(
        modifier = Modifier
          .padding(paddingValues)
          .fillMaxSize()
          .padding(16.dp)
      ) {
        Text(text = user!!.name, style = MaterialTheme.typography.headlineMedium)
        Text(text = user!!.email, style = MaterialTheme.typography.bodyMedium)

        Spacer(modifier = Modifier.height(24.dp))

        Button(
          onClick = { viewModel.logout() },
          modifier = Modifier.fillMaxWidth()
        ) {
          Text("Logout")
        }
      }
    }
  }
}

@Composable
fun DetailsScreen(itemId: String, navController: NavController) {
  Scaffold(
    topBar = {
      TopAppBar(
        title = { Text("Details") },
        navigationIcon = {
          IconButton(onClick = { navController.popBackStack() }) {
            Icon(Icons.Default.ArrowBack, contentDescription = "Back")
          }
        }
      )
    }
  ) { paddingValues ->
    Column(
      modifier = Modifier
        .padding(paddingValues)
        .fillMaxSize()
        .padding(16.dp),
      horizontalAlignment = Alignment.CenterHorizontally,
      verticalArrangement = Arrangement.Center
    ) {
      Text("Item ID: $itemId", style = MaterialTheme.typography.headlineSmall)
    }
  }
}
```

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
