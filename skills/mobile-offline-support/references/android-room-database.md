# Android Room Database

## Android Room Database

```kotlin
@Entity(tableName = "items")
data class ItemEntity(
  @PrimaryKey val id: String,
  val title: String,
  val description: String?,
  val isSynced: Boolean = false
)

@Entity(tableName = "action_queue")
data class ActionQueueEntity(
  @PrimaryKey val id: Long = System.currentTimeMillis(),
  val type: String,
  val payload: String,
  val createdAt: Long = System.currentTimeMillis()
)

@Dao
interface ItemDao {
  @Insert(onConflict = OnConflictStrategy.REPLACE)
  suspend fun insertItem(item: ItemEntity)

  @Query("SELECT * FROM items")
  fun getAllItems(): Flow<List<ItemEntity>>

  @Update
  suspend fun updateItem(item: ItemEntity)
}

@Dao
interface ActionQueueDao {
  @Insert
  suspend fun insertAction(action: ActionQueueEntity)

  @Query("SELECT * FROM action_queue ORDER BY createdAt ASC")
  suspend fun getAllActions(): List<ActionQueueEntity>

  @Delete
  suspend fun deleteAction(action: ActionQueueEntity)
}

@Database(entities = [ItemEntity::class, ActionQueueEntity::class], version = 1)
abstract class AppDatabase : RoomDatabase() {
  abstract fun itemDao(): ItemDao
  abstract fun actionQueueDao(): ActionQueueDao
}

@HiltViewModel
class OfflineItemsViewModel @Inject constructor(
  private val itemDao: ItemDao,
  private val actionQueueDao: ActionQueueDao,
  private val connectivityManager: ConnectivityManager
) : ViewModel() {
  private val _items = MutableStateFlow<List<Item>>(emptyList())
  val items: StateFlow<List<Item>> = _items.asStateFlow()

  init {
    viewModelScope.launch {
      itemDao.getAllItems().collect { entities ->
        _items.value = entities.map { it.toItem() }
      }
    }
    observeNetworkConnectivity()
  }

  fun saveItem(item: Item) {
    viewModelScope.launch {
      val entity = item.toEntity()
      itemDao.insertItem(entity)

      if (isNetworkAvailable()) {
        syncItem(item)
      } else {
        actionQueueDao.insertAction(
          ActionQueueEntity(
            type = "CREATE_ITEM",
            payload = Json.encodeToString(item)
          )
        )
      }
    }
  }

  private fun observeNetworkConnectivity() {
    val networkRequest = NetworkRequest.Builder()
      .addCapability(NET_CAPABILITY_INTERNET)
      .build()

    connectivityManager.registerNetworkCallback(
      networkRequest,
      object : ConnectivityManager.NetworkCallback() {
        override fun onAvailable(network: Network) {
          viewModelScope.launch { syncQueue() }
        }
      }
    )
  }

  private suspend fun syncQueue() {
    val queue = actionQueueDao.getAllActions()
    for (action in queue) {
      try {
        actionQueueDao.deleteAction(action)
      } catch (e: Exception) {
        println("Sync error: ${e.message}")
      }
    }
  }

  private fun isNetworkAvailable(): Boolean {
    val activeNetwork = connectivityManager.activeNetwork ?: return false
    val capabilities = connectivityManager.getNetworkCapabilities(activeNetwork) ?: return false
    return capabilities.hasCapability(NET_CAPABILITY_INTERNET)
  }
}
```
