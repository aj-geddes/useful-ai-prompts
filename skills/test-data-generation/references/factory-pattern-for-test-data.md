# Factory Pattern for Test Data

## Factory Pattern for Test Data

### JavaScript/Jest with Factory Functions

```javascript
// tests/factories/userFactory.js
const { faker } = require("@faker-js/faker");

class UserFactory {
  static build(overrides = {}) {
    return {
      id: faker.string.uuid(),
      email: faker.internet.email(),
      firstName: faker.person.firstName(),
      lastName: faker.person.lastName(),
      age: faker.number.int({ min: 18, max: 80 }),
      phone: faker.phone.number(),
      address: {
        street: faker.location.streetAddress(),
        city: faker.location.city(),
        state: faker.location.state(),
        zip: faker.location.zipCode(),
        country: "USA",
      },
      role: "user",
      isActive: true,
      createdAt: faker.date.past(),
      ...overrides,
    };
  }

  static buildMany(count, overrides = {}) {
    return Array.from({ length: count }, () => this.build(overrides));
  }

  static buildAdmin(overrides = {}) {
    return this.build({
      role: "admin",
      permissions: ["read", "write", "delete"],
      ...overrides,
    });
  }

  static buildInactive(overrides = {}) {
    return this.build({
      isActive: false,
      deactivatedAt: faker.date.recent(),
      ...overrides,
    });
  }
}

// tests/user.test.js
describe("User Service", () => {
  test("should create user with valid data", () => {
    const userData = UserFactory.build();
    const user = userService.create(userData);

    expect(user.email).toBe(userData.email);
    expect(user.isActive).toBe(true);
  });

  test("should handle admin users differently", () => {
    const admin = UserFactory.buildAdmin();
    expect(admin.role).toBe("admin");
    expect(admin.permissions).toContain("delete");
  });

  test("should process multiple users", () => {
    const users = UserFactory.buildMany(5);
    expect(users).toHaveLength(5);
    expect(new Set(users.map((u) => u.email)).size).toBe(5); // All unique
  });
});
```

### Python with Factory Boy

```python
# tests/factories.py
import factory
from factory.faker import Faker
from datetime import datetime, timedelta
from app.models import User, Order, Product

class UserFactory(factory.Factory):
    class Meta:
        model = User

    id = factory.Sequence(lambda n: n)
    email = Faker('email')
    first_name = Faker('first_name')
    last_name = Faker('last_name')
    username = factory.LazyAttribute(
        lambda obj: f"{obj.first_name.lower()}.{obj.last_name.lower()}"
    )
    age = Faker('random_int', min=18, max=80)
    phone = Faker('phone_number')
    is_active = True
    role = 'user'
    created_at = Faker('date_time_this_year')

    class Params:
        # Traits for different user types
        admin = factory.Trait(
            role='admin',
            permissions=['read', 'write', 'delete']
        )
        inactive = factory.Trait(
            is_active=False,
            deactivated_at=factory.LazyFunction(datetime.now)
        )
        premium = factory.Trait(
            subscription='premium',
            subscription_end=factory.LazyFunction(
                lambda: datetime.now() + timedelta(days=365)
            )
        )

class ProductFactory(factory.Factory):
    class Meta:
        model = Product

    id = factory.Sequence(lambda n: n)
    name = Faker('commerce_product_name')
    description = Faker('text', max_nb_chars=200)
    price = Faker('pydecimal', left_digits=3, right_digits=2, positive=True)
    sku = factory.LazyAttribute(
        lambda obj: f"SKU-{obj.id:06d}"
    )
    stock = Faker('random_int', min=0, max=100)
    category = Faker('random_element', elements=['electronics', 'clothing', 'books'])
    is_available = factory.LazyAttribute(lambda obj: obj.stock > 0)

class OrderFactory(factory.Factory):
    class Meta:
        model = Order

    id = factory.Sequence(lambda n: n)
    user = factory.SubFactory(UserFactory)
    status = 'pending'
    total = Faker('pydecimal', left_digits=4, right_digits=2, positive=True)
    created_at = Faker('date_time_this_month')

    @factory.post_generation
    def products(self, create, extracted, **kwargs):
        """Add products to order after creation."""
        if not create:
            return

        if extracted:
            for product in extracted:
                self.products.add(product)
        else:
            # Add 1-3 random products by default
            count = kwargs.get('count', 3)
            self.products.add(*ProductFactory.build_batch(count))

# tests/test_orders.py
import pytest
from tests.factories import UserFactory, OrderFactory, ProductFactory

def test_create_order_with_products():
    """Test order creation with specific products."""
    products = ProductFactory.build_batch(3)
    order = OrderFactory.build(products=products)

    assert order.user is not None
    assert len(order.products) == 3
    assert order.status == 'pending'

def test_admin_user_permissions():
    """Test admin user has correct permissions."""
    admin = UserFactory.build(admin=True)

    assert admin.role == 'admin'
    assert 'delete' in admin.permissions

def test_inactive_user():
    """Test inactive user properties."""
    user = UserFactory.build(inactive=True)

    assert not user.is_active
    assert user.deactivated_at is not None

def test_bulk_user_creation():
    """Test creating multiple users at once."""
    users = UserFactory.build_batch(10, role='user')

    assert len(users) == 10
    assert all(u.role == 'user' for u in users)
    # All emails should be unique
    assert len(set(u.email for u in users)) == 10
```
