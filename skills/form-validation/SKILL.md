---
name: form-validation
description: >
  Implement form validation using React Hook Form, Formik, Vee-Validate, and
  custom validators. Use when building robust form handling with real-time
  validation.
---

# Form Validation

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

## Overview

Implement comprehensive form validation including client-side validation, server-side synchronization, and real-time error feedback with TypeScript type safety.

## When to Use

- User input validation
- Form submission handling
- Real-time error feedback
- Complex validation rules
- Multi-step forms

## Quick Start

Minimal working example:

```typescript
// types/form.ts
export interface LoginFormData {
  email: string;
  password: string;
  rememberMe: boolean;
}

export interface RegisterFormData {
  email: string;
  password: string;
  confirmPassword: string;
  name: string;
  terms: boolean;
}

// components/LoginForm.tsx
import { useForm, SubmitHandler } from 'react-hook-form';
import { LoginFormData } from '../types/form';

const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export const LoginForm: React.FC = () => {
  const {
    register,
    handleSubmit,
// ... (see reference guides for full implementation)
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [React Hook Form with TypeScript](references/react-hook-form-with-typescript.md) | React Hook Form with TypeScript |
| [Formik with Yup Validation](references/formik-with-yup-validation.md) | Formik with Yup Validation |
| [Vue Vee-Validate](references/vue-vee-validate.md) | Vue Vee-Validate |
| [Custom Validator Hook](references/custom-validator-hook.md) | Custom Validator Hook |
| [Server-Side Validation Integration](references/server-side-validation-integration.md) | Server-Side Validation Integration |

## Best Practices

### ✅ DO

- Follow established patterns and conventions
- Write clean, maintainable code
- Add appropriate documentation
- Test thoroughly before deploying

### ❌ DON'T

- Skip testing or validation
- Ignore error handling
- Hard-code configuration values
