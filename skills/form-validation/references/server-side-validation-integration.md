# Server-Side Validation Integration

## Server-Side Validation Integration

```typescript
// Async server validation
const useAsyncValidation = () => {
  const validateEmail = async (email: string) => {
    const response = await fetch(`/api/validate/email?email=${email}`);
    const { available } = await response.json();
    return available ? true : "Email already registered";
  };

  const validateUsername = async (username: string) => {
    const response = await fetch(`/api/validate/username?username=${username}`);
    const { available } = await response.json();
    return available ? true : "Username taken";
  };

  return { validateEmail, validateUsername };
};

// React Hook Form with async validation
const { validateEmail } = useAsyncValidation();

register("email", {
  required: "Email required",
  validate: async (value) => {
    return await validateEmail(value);
  },
});
```
