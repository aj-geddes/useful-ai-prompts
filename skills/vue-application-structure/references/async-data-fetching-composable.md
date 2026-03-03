# Async Data Fetching Composable

## Async Data Fetching Composable

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
