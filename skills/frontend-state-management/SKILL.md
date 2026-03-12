---
name: frontend-state-management
description: >
  Manage application state using Redux, MobX, Zustand, and Context API. Use when
  centralizing state for complex applications with multiple components.
---

# Frontend State Management

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement scalable state management solutions using modern patterns and libraries to handle application state, side effects, and data flow across components.

## When to Use

- Complex application state
- Multiple components sharing state
- Predictable state mutations
- Time-travel debugging needs
- Server state synchronization

## Quick Start

Minimal working example:

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
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Redux with Redux Toolkit (React)](references/redux-with-redux-toolkit-react.md) | Redux with Redux Toolkit (React) |
| [Zustand (Lightweight State Management)](references/zustand-lightweight-state-management.md) | Zustand (Lightweight State Management) |
| [Context API + useReducer](references/context-api-usereducer.md) | Context API + useReducer |
| [MobX (Observable State)](references/mobx-observable-state.md) | MobX (Observable State) |

## Best Practices

### ✅ DO

- Co-locate state as close to the consuming component as possible — lift only when shared
- Separate server-cache state (React Query, SWR) from client UI state (Zustand, Redux)
- Use selectors to derive computed values rather than storing redundant data in the store
- Keep reducers and actions pure — side effects belong in middleware or effect hooks
- Normalize nested data structures to avoid deep cloning and stale reference bugs
- Use TypeScript to type your store slices, actions, and selectors for compile-time safety

### ❌ DON'T

- Put every piece of state in a global store — form input, hover state, and animation state should stay local
- Mutate state directly — always produce a new reference (Redux Toolkit's Immer handles this, raw Redux does not)
- Use Context API for frequently-updating values — it re-renders all consumers on every change
- Create actions that do too much — keep them granular so time-travel debugging stays useful
