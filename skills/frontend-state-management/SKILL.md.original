---
name: frontend-state-management
description: Manage application state using Redux, MobX, Zustand, and Context API. Use when centralizing state for complex applications with multiple components.
---

# Frontend State Management

## Overview

Implement scalable state management solutions using modern patterns and libraries to handle application state, side effects, and data flow across components.

## When to Use

- Complex application state
- Multiple components sharing state
- Predictable state mutations
- Time-travel debugging needs
- Server state synchronization

## Implementation Examples

### 1. **Redux with Redux Toolkit (React)**

```typescript
// store/userSlice.ts
import { createSlice, createAsyncThunk, PayloadAction } from '@reduxjs/toolkit';

interface User {
  id: number;
  name: string;
  email: string;
}

interface UserState {
  items: User[];
  loading: boolean;
  error: string | null;
}

const initialState: UserState = {
  items: [],
  loading: false,
  error: null
};

export const fetchUsers = createAsyncThunk(
  'users/fetchUsers',
  async (_, { rejectWithValue }) => {
    try {
      const response = await fetch('/api/users');
      if (!response.ok) throw new Error('Failed to fetch');
      return await response.json();
    } catch (error) {
      return rejectWithValue((error as Error).message);
    }
  }
);

const userSlice = createSlice({
  name: 'users',
  initialState,
  reducers: {
    userAdded(state, action: PayloadAction<User>) {
      state.items.push(action.payload);
    },
    userRemoved(state, action: PayloadAction<number>) {
      state.items = state.items.filter(u => u.id !== action.payload);
    }
  },
  extraReducers: (builder) => {
    builder
      .addCase(fetchUsers.pending, (state) => {
        state.loading = true;
        state.error = null;
      })
      .addCase(fetchUsers.fulfilled, (state, action) => {
        state.loading = false;
        state.items = action.payload;
      })
      .addCase(fetchUsers.rejected, (state, action) => {
        state.loading = false;
        state.error = action.payload as string;
      });
  }
});

export const { userAdded, userRemoved } = userSlice.actions;
export default userSlice.reducer;

// store/index.ts
import { configureStore } from '@reduxjs/toolkit';
import userReducer from './userSlice';

export const store = configureStore({
  reducer: {
    users: userReducer
  }
});

export type RootState = ReturnType<typeof store.getState>;
export type AppDispatch = typeof store.dispatch;

// Usage in component
import { useDispatch, useSelector } from 'react-redux';

const UsersList: React.FC = () => {
  const dispatch = useDispatch<AppDispatch>();
  const { items, loading, error } = useSelector(
    (state: RootState) => state.users
  );

  React.useEffect(() => {
    dispatch(fetchUsers());
  }, [dispatch]);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <ul>
      {items.map(user => (
        <li key={user.id}>{user.name}</li>
      ))}
    </ul>
  );
};
```

### 2. **Zustand (Lightweight State Management)**

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

### 3. **Context API + useReducer**

```typescript
// context/AuthContext.tsx
import React, { createContext, useReducer, useCallback } from 'react';

interface User {
  id: number;
  name: string;
  email: string;
}

interface AuthState {
  user: User | null;
  loading: boolean;
  error: string | null;
  isAuthenticated: boolean;
}

type AuthAction =
  | { type: 'LOGIN_START' }
  | { type: 'LOGIN_SUCCESS'; payload: User }
  | { type: 'LOGIN_ERROR'; payload: string }
  | { type: 'LOGOUT' };

const initialState: AuthState = {
  user: null,
  loading: false,
  error: null,
  isAuthenticated: false
};

function authReducer(state: AuthState, action: AuthAction): AuthState {
  switch (action.type) {
    case 'LOGIN_START':
      return { ...state, loading: true, error: null };
    case 'LOGIN_SUCCESS':
      return {
        ...state,
        user: action.payload,
        loading: false,
        isAuthenticated: true
      };
    case 'LOGIN_ERROR':
      return { ...state, error: action.payload, loading: false };
    case 'LOGOUT':
      return { ...state, user: null, isAuthenticated: false };
    default:
      return state;
  }
}

interface AuthContextType {
  state: AuthState;
  login: (email: string, password: string) => Promise<void>;
  logout: () => void;
}

export const AuthContext = createContext<AuthContextType | undefined>(undefined);

export const AuthProvider: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const [state, dispatch] = useReducer(authReducer, initialState);

  const login = useCallback(async (email: string, password: string) => {
    dispatch({ type: 'LOGIN_START' });
    try {
      const response = await fetch('/api/login', {
        method: 'POST',
        body: JSON.stringify({ email, password })
      });
      if (!response.ok) throw new Error('Login failed');
      const user = await response.json();
      dispatch({ type: 'LOGIN_SUCCESS', payload: user });
    } catch (error) {
      dispatch({
        type: 'LOGIN_ERROR',
        payload: (error as Error).message
      });
    }
  }, []);

  const logout = useCallback(() => {
    dispatch({ type: 'LOGOUT' });
  }, []);

  return (
    <AuthContext.Provider value={{ state, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = React.useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
};
```

### 4. **MobX (Observable State)**

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

## Best Practices

- Choose state management based on app complexity
- Keep state normalized and flat
- Separate application and UI state
- Implement proper error handling
- Use selectors to derive data
- Implement middleware for side effects
- Monitor performance and bundle size
- Document state shape and actions

## Resources

- [Redux Documentation](https://redux.js.org/)
- [Zustand](https://github.com/pmndrs/zustand)
- [MobX](https://mobx.js.org/)
- [Context API](https://react.dev/reference/react/useContext)
- [Pinia (Vue)](https://pinia.vuejs.org/)
