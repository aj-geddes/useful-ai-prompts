# Composition Pattern

## Composition Pattern

```typescript
// Card.tsx
interface CardProps {
  children: React.ReactNode;
  className?: string;
}

const Card: React.FC<CardProps> = ({ children, className = '' }) => (
  <div className={`border rounded p-4 ${className}`}>{children}</div>
);

const CardHeader: React.FC<CardProps> = ({ children }) => (
  <div className="border-b pb-2 mb-3 font-bold">{children}</div>
);

const CardBody: React.FC<CardProps> = ({ children }) => (
  <div className="py-2">{children}</div>
);

const CardFooter: React.FC<CardProps> = ({ children }) => (
  <div className="border-t pt-2 mt-3">{children}</div>
);

// Compound component
export { Card };
Card.Header = CardHeader;
Card.Body = CardBody;
Card.Footer = CardFooter;

// Usage
<Card>
  <Card.Header>Title</Card.Header>
  <Card.Body>Content</Card.Body>
  <Card.Footer>Actions</Card.Footer>
</Card>
```
