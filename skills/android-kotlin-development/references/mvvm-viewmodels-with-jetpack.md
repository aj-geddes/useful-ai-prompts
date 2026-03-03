# MVVM ViewModels with Jetpack

## MVVM ViewModels with Jetpack

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
