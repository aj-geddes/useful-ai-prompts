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

- Validate on both client and server — client-side validation is a UX convenience, not a security boundary
- Show inline error messages next to the field that failed, not just a summary at the top
- Use schema-based validation (Zod, Yup) to share validation rules between frontend and backend
- Debounce async validators (e.g., username availability checks) to avoid excessive API calls
- Associate error messages with fields via aria-describedby for screen reader accessibility
- Preserve user input on validation failure — never clear the form on error

### ❌ DON'T

- Validate on blur alone — combine with on-submit validation so users see all errors before submitting
- Write custom regex for emails — use the validation library's built-in email validator or type="email"
- Block form submission silently — always surface a visible, specific error message
- Rely on HTML5 required/pattern attributes as the sole validation — they vary across browsers
