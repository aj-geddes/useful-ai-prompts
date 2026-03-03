# Custom Hooks Pattern

## Custom Hooks Pattern

```typescript
// useFormInput.ts
import { useState, useCallback } from 'react';

interface UseFormInputOptions {
  initialValue?: string;
  validator?: (value: string) => string | null;
}

export const useFormInput = (options: UseFormInputOptions = {}) => {
  const [value, setValue] = useState(options.initialValue || '');
  const [error, setError] = useState<string | null>(null);

  const validate = useCallback(() => {
    if (options.validator) {
      const validationError = options.validator(value);
      setError(validationError);
      return !validationError;
    }
    return true;
  }, [value, options.validator]);

  const reset = useCallback(() => {
    setValue(options.initialValue || '');
    setError(null);
  }, [options.initialValue]);

  return {
    value,
    setValue,
    error,
    validate,
    reset,
    bind: {
      value,
      onChange: (e: React.ChangeEvent<HTMLInputElement>) => setValue(e.target.value)
    }
  };
};

// Usage
const MyForm: React.FC = () => {
  const email = useFormInput({
    validator: (v) => !v.includes('@') ? 'Invalid email' : null
  });

  return (
    <div>
      <input {...email.bind} />
      {email.error && <span className="text-red-500">{email.error}</span>}
    </div>
  );
};
```
