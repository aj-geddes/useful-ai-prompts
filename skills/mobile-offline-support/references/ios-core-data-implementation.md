# iOS Core Data Implementation

## iOS Core Data Implementation

```swift
import CoreData

class PersistenceController {
  static let shared = PersistenceController()

  let container: NSPersistentContainer

  init(inMemory: Bool = false) {
    container = NSPersistentContainer(name: "MyApp")

    if inMemory {
      container.persistentStoreDescriptions.first?.url = URL(fileURLWithPath: "/dev/null")
    }

    container.loadPersistentStores { _, error in
      if let error = error as NSError? {
        print("Core Data load error: \(error)")
      }
    }

    container.viewContext.automaticallyMergesChangesFromParent = true
  }

  func save(_ context: NSManagedObjectContext = PersistenceController.shared.container.viewContext) {
    if context.hasChanges {
      do {
        try context.save()
      } catch {
        print("Save error: \(error)")
      }
    }
  }
}

// Core Data Models
@NSManaged class ItemEntity: NSManagedObject {
  @NSManaged var id: String
  @NSManaged var title: String
  @NSManaged var description: String?
  @NSManaged var isSynced: Bool
}

@NSManaged class ActionQueueEntity: NSManagedObject {
  @NSManaged var id: UUID
  @NSManaged var type: String
  @NSManaged var payload: Data?
  @NSManaged var createdAt: Date
}

class OfflineSyncManager: NSObject, ObservableObject {
  @Published var isOnline = true
  @Published var isSyncing = false

  private let networkMonitor = NWPathMonitor()
  private let persistenceController = PersistenceController.shared

  override init() {
    super.init()
    setupNetworkMonitoring()
  }

  private func setupNetworkMonitoring() {
    networkMonitor.pathUpdateHandler = { [weak self] path in
      DispatchQueue.main.async {
        self?.isOnline = path.status == .satisfied
        if path.status == .satisfied {
          self?.syncWithServer()
        }
      }
    }

    let queue = DispatchQueue(label: "NetworkMonitor")
    networkMonitor.start(queue: queue)
  }

  func saveItem(_ item: Item) {
    let context = persistenceController.container.viewContext
    let entity = ItemEntity(context: context)
    entity.id = item.id
    entity.title = item.title
    entity.isSynced = false

    persistenceController.save(context)

    if isOnline {
      syncItem(item)
    }
  }

  func syncWithServer() {
    isSyncing = true
    let context = persistenceController.container.viewContext
    let request: NSFetchRequest<ActionQueueEntity> = ActionQueueEntity.fetchRequest()

    do {
      let pendingActions = try context.fetch(request)
      for action in pendingActions {
        context.delete(action)
      }
      persistenceController.save(context)
    } catch {
      print("Sync error: \(error)")
    }

    isSyncing = false
  }
}
```
