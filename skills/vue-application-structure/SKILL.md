---
name: vue-application-structure
description: Structure Vue 3 applications using Composition API, component organization, and TypeScript. Use when building scalable Vue applications with proper separation of concerns.
---

# Vue Application Structure

## Overview

Build well-organized Vue 3 applications using Composition API, proper file organization, and TypeScript for type safety and maintainability.

## When to Use

- Large-scale Vue applications
- Component library development
- Reusable composable hooks
- Complex state management
- Performance optimization

## Implementation Examples

### 1. **Vue 3 Composition API Component**

```typescript
// useCounter.ts (Composable)
import { ref, computed } from 'vue';

export function useCounter(initialValue = 0) {
  const count = ref(initialValue);

  const doubled = computed(() => count.value * 2);
  const increment = () => count.value++;
  const decrement = () => count.value--;
  const reset = () => count.value = initialValue;

  return {
    count,
    doubled,
    increment,
    decrement,
    reset
  };
}

// Counter.vue
<template>
  <div class="counter">
    <p>Count: {{ count }}</p>
    <p>Doubled: {{ doubled }}</p>
    <button @click="increment">+</button>
    <button @click="decrement">-</button>
    <button @click="reset">Reset</button>
  </div>
</template>

<script setup lang="ts">
import { useCounter } from './useCounter';

const { count, doubled, increment, decrement, reset } = useCounter(0);
</script>

<style scoped>
.counter {
  padding: 20px;
  border: 1px solid #ccc;
}
</style>
```

### 2. **Async Data Fetching Composable**

```typescript
// useFetch.ts
import { ref, computed, onMounted } from 'vue';

interface UseFetchOptions {
  immediate?: boolean;
}

export function useFetch<T>(
  url: string,
  options: UseFetchOptions = {}
) {
  const data = ref<T | null>(null);
  const loading = ref(false);
  const error = ref<Error | null>(null);

  const isLoading = computed(() => loading.value);
  const hasError = computed(() => error.value !== null);

  const fetch = async () => {
    loading.value = true;
    error.value = null;

    try {
      const response = await globalThis.fetch(url);
      if (!response.ok) throw new Error(`HTTP ${response.status}`);
      data.value = await response.json();
    } catch (e) {
      error.value = e instanceof Error ? e : new Error(String(e));
    } finally {
      loading.value = false;
    }
  };

  const refetch = () => fetch();

  if (options.immediate !== false) {
    onMounted(fetch);
  }

  return {
    data,
    loading: isLoading,
    error: hasError,
    fetch,
    refetch
  };
}

// UserList.vue
<template>
  <div>
    <button @click="refetch">Refresh</button>
    <p v-if="loading">Loading...</p>
    <p v-if="error" class="text-red-500">Error loading users</p>
    <ul v-else>
      <li v-for="user in data" :key="user.id">{{ user.name }}</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { useFetch } from './useFetch';

interface User {
  id: number;
  name: string;
}

const { data, loading, error, refetch } = useFetch<User[]>('/api/users');
</script>
```

### 3. **Component Organization Structure**

```
src/
├── components/
│   ├── common/
│   │   ├── Button.vue
│   │   ├── Card.vue
│   │   └── Modal.vue
│   ├── forms/
│   │   ├── FormInput.vue
│   │   └── FormSelect.vue
│   └── layouts/
│       ├── Header.vue
│       └── Sidebar.vue
├── composables/
│   ├── useCounter.ts
│   ├── useFetch.ts
│   └── useForm.ts
├── services/
│   ├── api.ts
│   └── auth.ts
├── stores/
│   ├── user.ts
│   └── auth.ts
├── types/
│   ├── models.ts
│   └── api.ts
├── App.vue
└── main.ts
```

### 4. **Form Handling Composable**

```typescript
// useForm.ts
import { ref, reactive } from 'vue';

interface UseFormOptions<T> {
  onSubmit: (data: T) => Promise<void>;
  initialValues: T;
}

export function useForm<T extends Record<string, any>>(
  options: UseFormOptions<T>
) {
  const formData = reactive<T>(options.initialValues);
  const errors = reactive<Record<string, string>>({});
  const isSubmitting = ref(false);

  const handleSubmit = async (e?: Event) => {
    e?.preventDefault();
    isSubmitting.value = true;

    try {
      await options.onSubmit(formData);
    } catch (error) {
      const err = error as any;
      if (err.fieldErrors) {
        Object.assign(errors, err.fieldErrors);
      }
    } finally {
      isSubmitting.value = false;
    }
  };

  const reset = () => {
    Object.assign(formData, options.initialValues);
    Object.keys(errors).forEach(key => delete errors[key]);
  };

  return {
    formData,
    errors,
    isSubmitting,
    handleSubmit,
    reset
  };
}

// LoginForm.vue
<template>
  <form @submit="handleSubmit">
    <input v-model="formData.email" type="email" />
    <span v-if="errors.email" class="error">{{ errors.email }}</span>

    <input v-model="formData.password" type="password" />
    <span v-if="errors.password" class="error">{{ errors.password }}</span>

    <button type="submit" :disabled="isSubmitting">Login</button>
  </form>
</template>

<script setup lang="ts">
import { useForm } from './useForm';

const { formData, errors, isSubmitting, handleSubmit } = useForm({
  initialValues: { email: '', password: '' },
  onSubmit: async (data) => {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify(data)
    });
    if (!response.ok) throw new Error('Login failed');
  }
});
</script>
```

### 5. **Pinia Store (State Management)**

```typescript
// stores/user.ts
import { defineStore } from 'pinia';
import { ref, computed } from 'vue';

interface User {
  id: number;
  name: string;
  email: string;
}

export const useUserStore = defineStore('user', () => {
  const user = ref<User | null>(null);
  const isLoading = ref(false);

  const isLoggedIn = computed(() => user.value !== null);

  const fetchUser = async (id: number) => {
    isLoading.value = true;
    try {
      const response = await fetch(`/api/users/${id}`);
      user.value = await response.json();
    } finally {
      isLoading.value = false;
    }
  };

  const logout = () => {
    user.value = null;
  };

  return {
    user,
    isLoading,
    isLoggedIn,
    fetchUser,
    logout
  };
});

// Usage in component
import { useUserStore } from '@/stores/user';

export default {
  setup() {
    const userStore = useUserStore();
    userStore.fetchUser(1);
    return { userStore };
  }
};
```

## Best Practices

- Organize by features or domains
- Use Composition API for logic reuse
- Extract composables for shared logic
- Use TypeScript for type safety
- Implement proper error handling
- Keep components focused and testable
- Use Pinia for state management

## Resources

- [Vue 3 Documentation](https://vuejs.org)
- [Vue Composition API](https://vuejs.org/guide/extras/composition-api-faq.html)
- [Pinia State Management](https://pinia.vuejs.org)
