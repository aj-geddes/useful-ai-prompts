# Jetpack Compose UI

## Jetpack Compose UI

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
