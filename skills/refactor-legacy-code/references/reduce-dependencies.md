# Reduce Dependencies

## Reduce Dependencies

Break tight coupling:

```python
# BEFORE: Tight coupling to specific implementation
class OrderProcessor:
    def __init__(self):
        self.db = MySQLDatabase()  # Tightly coupled
        self.email = SendGridEmail()  # Tightly coupled

    def process_order(self, order):
        self.db.save(order)
        self.email.send(order.customer_email, "Order confirmed")

# AFTER: Dependency injection
class OrderProcessor:
    def __init__(self, database, email_service):
        self.db = database  # Any database implementation
        self.email = email_service  # Any email service

    def process_order(self, order):
        self.db.save(order)
        self.email.send(order.customer_email, "Order confirmed")

# Easy to test with mocks
processor = OrderProcessor(MockDatabase(), MockEmailService())
```


## Documentation

Document refactoring decisions:

```markdown
