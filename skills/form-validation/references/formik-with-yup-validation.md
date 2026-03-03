# Formik with Yup Validation

## Formik with Yup Validation

```typescript
// validationSchema.ts
import * as Yup from 'yup';

export const registerValidationSchema = Yup.object().shape({
  email: Yup.string()
    .email('Invalid email')
    .required('Email is required'),
  password: Yup.string()
    .min(8, 'Password must be at least 8 characters')
    .matches(/[A-Z]/, 'Must contain uppercase letter')
    .matches(/[0-9]/, 'Must contain number')
    .required('Password is required'),
  confirmPassword: Yup.string()
    .oneOf([Yup.ref('password')], 'Passwords must match')
    .required('Confirm password is required'),
  name: Yup.string()
    .min(2, 'Name too short')
    .required('Name is required'),
  terms: Yup.boolean()
    .oneOf([true], 'You must accept terms')
    .required()
});

// components/RegisterForm.tsx
import { Formik, Form, Field, ErrorMessage } from 'formik';
import { registerValidationSchema } from '../validationSchema';
import { RegisterFormData } from '../types/form';

export const RegisterForm: React.FC = () => {
  const initialValues: RegisterFormData = {
    email: '',
    password: '',
    confirmPassword: '',
    name: '',
    terms: false
  };

  const handleSubmit = async (
    values: RegisterFormData,
    { setSubmitting, setFieldError }: any
  ) => {
    try {
      const response = await fetch('/api/register', {
        method: 'POST',
        body: JSON.stringify(values)
      });

      if (!response.ok) {
        const error = await response.json();
        if (error.emailExists) {
          setFieldError('email', 'Email already registered');
        }
        throw new Error(error.message);
      }
    } catch (error) {
      console.error(error);
    } finally {
      setSubmitting(false);
    }
  };

  return (
    <Formik
      initialValues={initialValues}
      validationSchema={registerValidationSchema}
      onSubmit={handleSubmit}
    >
      {({ isSubmitting, isValid }) => (
        <Form>
          <div>
            <label htmlFor="name">Name</label>
            <Field name="name" type="text" />
            <ErrorMessage name="name" component="span" className="error" />
          </div>

          <div>
            <label htmlFor="email">Email</label>
            <Field name="email" type="email" />
            <ErrorMessage name="email" component="span" className="error" />
          </div>

          <div>
            <label htmlFor="password">Password</label>
            <Field name="password" type="password" />
            <ErrorMessage name="password" component="span" className="error" />
          </div>

          <div>
            <label htmlFor="confirmPassword">Confirm Password</label>
            <Field name="confirmPassword" type="password" />
            <ErrorMessage name="confirmPassword" component="span" className="error" />
          </div>

          <div>
            <label>
              <Field name="terms" type="checkbox" />
              I agree to terms
            </label>
            <ErrorMessage name="terms" component="span" className="error" />
          </div>

          <button type="submit" disabled={isSubmitting || !isValid}>
            {isSubmitting ? 'Registering...' : 'Register'}
          </button>
        </Form>
      )}
    </Formik>
  );
};
```
