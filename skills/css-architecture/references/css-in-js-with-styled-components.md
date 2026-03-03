# CSS-in-JS with Styled Components

## CSS-in-JS with Styled Components

```typescript
// styled-components example
import styled from 'styled-components';

interface ButtonProps {
  variant?: 'primary' | 'secondary';
  size?: 'sm' | 'md' | 'lg';
  disabled?: boolean;
}

const StyledButton = styled.button<ButtonProps>`
  display: inline-block;
  border: none;
  border-radius: 4px;
  cursor: ${props => props.disabled ? 'not-allowed' : 'pointer'};
  font-size: ${props => {
    switch (props.size) {
      case 'sm': return '12px';
      case 'lg': return '18px';
      default: return '16px';
    }
  }};
  padding: ${props => {
    switch (props.size) {
      case 'sm': return '5px 10px';
      case 'lg': return '15px 30px';
      default: return '10px 20px';
    }
  }};
  background-color: ${props => {
    if (props.disabled) return '#ccc';
    return props.variant === 'secondary' ? '#6c757d' : '#007bff';
  }};
  color: white;
  opacity: ${props => props.disabled ? 0.6 : 1};
  transition: all 0.3s ease;

  &:hover:not(:disabled) {
    background-color: ${props =>
      props.variant === 'secondary' ? '#5a6268' : '#0056b3'
    };
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
  }

  &:active:not(:disabled) {
    transform: translateY(0);
  }
`;

export const Button = (props: ButtonProps) => <StyledButton {...props} />;
```
