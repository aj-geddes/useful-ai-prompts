# Vue 3 Composition API Component

## Vue 3 Composition API Component

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
