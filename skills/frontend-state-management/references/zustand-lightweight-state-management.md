# Zustand (Lightweight State Management)

## Zustand (Lightweight State Management)

```typescript
// store/useUserStore.ts
import create from 'zustand';

interface User {
  id: number;
  name: string;
  email: string;
}

interface UserStore {
  users: User[];
  loading: boolean;
  error: string | null;
  fetchUsers: () => Promise<void>;
  addUser: (user: User) => void;
  removeUser: (id: number) => void;
  clearError: () => void;
}

export const useUserStore = create<UserStore>((set) => ({
  users: [],
  loading: false,
  error: null,

  fetchUsers: async () => {
    set({ loading: true, error: null });
    try {
      const response = await fetch('/api/users');
      if (!response.ok) throw new Error('Failed to fetch');
      const users = await response.json();
      set({ users, loading: false });
    } catch (error) {
      set({ error: (error as Error).message, loading: false });
    }
  },

  addUser: (user) => set((state) => ({
    users: [...state.users, user]
  })),

  removeUser: (id) => set((state) => ({
    users: state.users.filter(u => u.id !== id)
  })),

  clearError: () => set({ error: null })
}));

// Usage in component
const UsersList: React.FC = () => {
  const { users, loading, error, fetchUsers } = useUserStore();

  React.useEffect(() => {
    fetchUsers();
  }, [fetchUsers]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {users.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
```
