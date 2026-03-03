# Vue Vee-Validate

## Vue Vee-Validate

```typescript
// validationRules.ts
import { defineRule } from 'vee-validate';
import { email, required, min, confirmed } from '@vee-validate/rules';

defineRule('required', required);
defineRule('email', email);
defineRule('min', min);
defineRule('confirmed', confirmed);
defineRule('password-strength', (value: string) => {
  if (value.length < 8) return 'Password must be at least 8 characters';
  if (!/[A-Z]/.test(value)) return 'Must contain uppercase letter';
  if (!/[0-9]/.test(value)) return 'Must contain number';
  return true;
});

// components/LoginForm.vue
<template>
  <Form @submit="onSubmit" :validation-schema="validationSchema">
    <div class="form-group">
      <label for="email">Email</label>
      <Field name="email" type="email" as="input" class="form-control" />
      <ErrorMessage name="email" class="error" />
    </div>

    <div class="form-group">
      <label for="password">Password</label>
      <Field name="password" type="password" as="input" class="form-control" />
      <ErrorMessage name="password" class="error" />
    </div>

    <button type="submit" :disabled="isSubmitting">
      {{ isSubmitting ? 'Logging in...' : 'Login' }}
    </button>
  </Form>
</template>

<script setup lang="ts">
import { Form, Field, ErrorMessage } from 'vee-validate';
import { object, string } from 'yup';
import { ref } from 'vue';

const isSubmitting = ref(false);

const validationSchema = object({
  email: string().email('Invalid email').required('Email is required'),
  password: string().required('Password is required')
});

const onSubmit = async (values: any) => {
  isSubmitting.value = true;
  try {
    const response = await fetch('/api/login', {
      method: 'POST',
      body: JSON.stringify(values)
    });
    if (!response.ok) throw new Error('Login failed');
  } catch (error) {
    console.error(error);
  } finally {
    isSubmitting.value = false;
  }
};
</script>
```
