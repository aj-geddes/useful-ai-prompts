# SwiftUI Views

## SwiftUI Views

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
