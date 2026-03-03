# MobX (Observable State)

## MobX (Observable State)

```typescript
// store/UserStore.ts
import { makeObservable, observable, action, runInAction } from 'mobx';

interface User {
  id: number;
  name: string;
  email: string;
}

class UserStore {
  users: User[] = [];
  loading = false;
  error: string | null = null;

  constructor() {
    makeObservable(this, {
      users: observable,
      loading: observable,
      error: observable,
      fetchUsers: action,
      addUser: action,
      removeUser: action,
      clearError: action
    });
  }

  async fetchUsers() {
    this.loading = true;
    this.error = null;

    try {
      const response = await fetch('/api/users');
      if (!response.ok) throw new Error('Failed to fetch');
      const data = await response.json();

      runInAction(() => {
        this.users = data;
        this.loading = false;
      });
    } catch (error) {
      runInAction(() => {
        this.error = (error as Error).message;
        this.loading = false;
      });
    }
  }

  addUser(user: User) {
    this.users.push(user);
  }

  removeUser(id: number) {
    this.users = this.users.filter(u => u.id !== id);
  }

  clearError() {
    this.error = null;
  }
}

export const userStore = new UserStore();

// Usage with React
import { observer } from 'mobx-react-lite';

const UsersList = observer(() => {
  const { users, loading, error, fetchUsers } = userStore;

  React.useEffect(() => {
    fetchUsers();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
});
```
