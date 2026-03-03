# Pinia Store (State Management)

## Pinia Store (State Management)

```typescript
// stores/user.ts
import { defineStore } from "pinia";
import { ref, computed } from "vue";

interface User {
  id: number;
  name: string;
  email: string;
}

export const useUserStore = defineStore("user", () => {
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
    logout,
  };
});

// Usage in component
import { useUserStore } from "@/stores/user";

export default {
  setup() {
    const userStore = useUserStore();
    userStore.fetchUser(1);
    return { userStore };
  },
};
```
