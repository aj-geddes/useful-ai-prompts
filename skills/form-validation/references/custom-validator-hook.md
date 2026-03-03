# Custom Validator Hook

## Custom Validator Hook

```typescript
// hooks/useFieldValidator.ts
import { useState, useCallback } from "react";

export interface ValidationRule {
  validate: (value: any) => boolean | string;
  message: string;
}

export interface FieldError {
  isValid: boolean;
  message: string | null;
}

export const useFieldValidator = (rules: ValidationRule[] = []) => {
  const [error, setError] = useState<FieldError>({
    isValid: true,
    message: null,
  });

  const validate = useCallback(
    (value: any) => {
      for (const rule of rules) {
        const result = rule.validate(value);
        if (result !== true) {
          setError({
            isValid: false,
            message: typeof result === "string" ? result : rule.message,
          });
          return false;
        }
      }

      setError({
        isValid: true,
        message: null,
      });
      return true;
    },
    [rules],
  );

  const clearError = useCallback(() => {
    setError({
      isValid: true,
      message: null,
    });
  }, []);

  return { error, validate, clearError };
};

// Usage
const { error: emailError, validate: validateEmail } = useFieldValidator([
  {
    validate: (v) => v.length > 0,
    message: "Email is required",
  },
  {
    validate: (v) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v),
    message: "Invalid email format",
  },
]);
```
