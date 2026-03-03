# Models & API Service

## Models & API Service

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
