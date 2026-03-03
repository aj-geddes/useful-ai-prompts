# React Native Offline Storage

## React Native Offline Storage

```javascript
import AsyncStorage from '@react-native-async-storage/async-storage';
import NetInfo from '@react-native-community/netinfo';

class StorageManager {
  static async saveItems(items) {
    try {
      await AsyncStorage.setItem(
        'items_cache',
        JSON.stringify({ data: items, timestamp: Date.now() })
      );
    } catch (error) {
      console.error('Failed to save items:', error);
    }
  }

  static async getItems() {
    try {
      const data = await AsyncStorage.getItem('items_cache');
      return data ? JSON.parse(data) : null;
    } catch (error) {
      console.error('Failed to retrieve items:', error);
      return null;
    }
  }

  static async queueAction(action) {
    try {
      const queue = await AsyncStorage.getItem('action_queue');
      const actions = queue ? JSON.parse(queue) : [];
      actions.push({ ...action, id: Date.now(), attempts: 0 });
      await AsyncStorage.setItem('action_queue', JSON.stringify(actions));
    } catch (error) {
      console.error('Failed to queue action:', error);
    }
  }

  static async getActionQueue() {
    try {
      const queue = await AsyncStorage.getItem('action_queue');
      return queue ? JSON.parse(queue) : [];
    } catch (error) {
      return [];
    }
  }

  static async removeFromQueue(actionId) {
    try {
      const queue = await AsyncStorage.getItem('action_queue');
      const actions = queue ? JSON.parse(queue) : [];
      const filtered = actions.filter(a => a.id !== actionId);
      await AsyncStorage.setItem('action_queue', JSON.stringify(filtered));
    } catch (error) {
      console.error('Failed to remove from queue:', error);
    }
  }
}

class OfflineAPIService {
  async fetchItems() {
    const isOnline = await this.checkConnectivity();

    if (isOnline) {
      try {
        const response = await fetch('https://api.example.com/items');
        const items = await response.json();
        await StorageManager.saveItems(items);
        return items;
      } catch (error) {
        const cached = await StorageManager.getItems();
        return cached?.data || [];
      }
    } else {
      const cached = await StorageManager.getItems();
      return cached?.data || [];
    }
  }

  async createItem(item) {
    const isOnline = await this.checkConnectivity();

    if (isOnline) {
      try {
        const response = await fetch('https://api.example.com/items', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(item)
        });
        const created = await response.json();
        return { success: true, data: created };
      } catch (error) {
        await StorageManager.queueAction({
          type: 'CREATE_ITEM',
          payload: item
        });
        return { success: false, queued: true };
      }
    } else {
      await StorageManager.queueAction({
        type: 'CREATE_ITEM',
        payload: item
      });
      return { success: false, queued: true };
    }
  }

  async syncQueue() {
    const queue = await StorageManager.getActionQueue();

    for (const action of queue) {
      try {
        await this.executeAction(action);
        await StorageManager.removeFromQueue(action.id);
      } catch (error) {
        action.attempts = (action.attempts || 0) + 1;
        if (action.attempts > 3) {
          await StorageManager.removeFromQueue(action.id);
        }
      }
    }
  }

  private async executeAction(action) {
    switch (action.type) {
      case 'CREATE_ITEM':
        return fetch('https://api.example.com/items', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(action.payload)
        });
      default:
        return Promise.reject(new Error('Unknown action type'));
    }
  }

  async checkConnectivity() {
    const state = await NetInfo.fetch();
    return state.isConnected ?? false;
  }
}

export function OfflineListScreen() {
  const [items, setItems] = useState([]);
  const [isOnline, setIsOnline] = useState(true);
  const [syncing, setSyncing] = useState(false);
  const apiService = new OfflineAPIService();

  useFocusEffect(
    useCallback(() => {
      loadItems();
      const unsubscribe = NetInfo.addEventListener(state => {
        setIsOnline(state.isConnected ?? false);
        if (state.isConnected) {
          syncQueue();
        }
      });

      return unsubscribe;
    }, [])
  );

  const loadItems = async () => {
    const items = await apiService.fetchItems();
    setItems(items);
  };

  const syncQueue = async () => {
    setSyncing(true);
    await apiService.syncQueue();
    await loadItems();
    setSyncing(false);
  };

  return (
    <View style={styles.container}>
      {!isOnline && <Text style={styles.offline}>Offline Mode</Text>}
      {syncing && <ActivityIndicator size="large" />}
      <FlatList
        data={items}
        renderItem={({ item }) => <ItemCard item={item} />}
        keyExtractor={item => item.id}
      />
    </View>
  );
}
```
