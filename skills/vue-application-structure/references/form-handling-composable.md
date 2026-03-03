# Form Handling Composable

## Form Handling Composable

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
