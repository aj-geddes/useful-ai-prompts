---
name: test-data-generation
description: Generate realistic, consistent test data using factories, fixtures, and fake data libraries. Use for test data, fixtures, mock data, faker, test builders, and seed data generation.
---

# Test Data Generation

## Overview

Test data generation creates realistic, consistent, and maintainable test data for automated testing. Well-designed test data reduces test brittleness, improves readability, and makes it easier to create diverse test scenarios.

## When to Use

- Creating fixtures for integration tests
- Generating fake data for development databases
- Building test data with complex relationships
- Creating realistic user inputs for testing
- Seeding test databases
- Generating edge cases and boundary values
- Building reusable test data factories

## Instructions

### 1. **Factory Pattern for Test Data**

#### JavaScript/Jest with Factory Functions
```javascript
// tests/factories/userFactory.js
const { faker } = require('@faker-js/faker');

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
        country: 'USA'
      },
      role: 'user',
      isActive: true,
      createdAt: faker.date.past(),
      ...overrides
    };
  }

  static buildMany(count, overrides = {}) {
    return Array.from({ length: count }, () => this.build(overrides));
  }

  static buildAdmin(overrides = {}) {
    return this.build({
      role: 'admin',
      permissions: ['read', 'write', 'delete'],
      ...overrides
    });
  }

  static buildInactive(overrides = {}) {
    return this.build({
      isActive: false,
      deactivatedAt: faker.date.recent(),
      ...overrides
    });
  }
}

// tests/user.test.js
describe('User Service', () => {
  test('should create user with valid data', () => {
    const userData = UserFactory.build();
    const user = userService.create(userData);

    expect(user.email).toBe(userData.email);
    expect(user.isActive).toBe(true);
  });

  test('should handle admin users differently', () => {
    const admin = UserFactory.buildAdmin();
    expect(admin.role).toBe('admin');
    expect(admin.permissions).toContain('delete');
  });

  test('should process multiple users', () => {
    const users = UserFactory.buildMany(5);
    expect(users).toHaveLength(5);
    expect(new Set(users.map(u => u.email)).size).toBe(5); // All unique
  });
});
```

#### Python with Factory Boy
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

### 2. **Builder Pattern for Complex Objects**

```typescript
// tests/builders/OrderBuilder.ts
import { faker } from '@faker-js/faker';

export class OrderBuilder {
  private order: Partial<Order> = {
    id: faker.string.uuid(),
    status: 'pending',
    items: [],
    total: 0,
    createdAt: new Date(),
  };

  withId(id: string): this {
    this.order.id = id;
    return this;
  }

  withStatus(status: OrderStatus): this {
    this.order.status = status;
    return this;
  }

  withUser(user: User): this {
    this.order.userId = user.id;
    this.order.user = user;
    return this;
  }

  withItems(items: OrderItem[]): this {
    this.order.items = items;
    this.order.total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    return this;
  }

  addItem(product: Product, quantity: number = 1): this {
    const item: OrderItem = {
      productId: product.id,
      product,
      quantity,
      price: product.price,
      subtotal: product.price * quantity,
    };

    this.order.items = [...(this.order.items || []), item];
    this.order.total = (this.order.total || 0) + item.subtotal;
    return this;
  }

  withShippingAddress(address: Address): this {
    this.order.shippingAddress = address;
    return this;
  }

  asPaid(): this {
    this.order.status = 'paid';
    this.order.paidAt = new Date();
    return this;
  }

  asShipped(): this {
    this.order.status = 'shipped';
    this.order.shippedAt = new Date();
    return this;
  }

  build(): Order {
    return this.order as Order;
  }
}

// Usage in tests
describe('Order Processing', () => {
  it('should calculate total correctly', () => {
    const product1 = ProductBuilder.aProduct().withPrice(10.00).build();
    const product2 = ProductBuilder.aProduct().withPrice(25.00).build();

    const order = new OrderBuilder()
      .withUser(UserBuilder.aUser().build())
      .addItem(product1, 2)  // $20
      .addItem(product2, 1)  // $25
      .build();

    expect(order.total).toBe(45.00);
    expect(order.items).toHaveLength(2);
  });

  it('should process paid orders', () => {
    const order = new OrderBuilder()
      .withUser(UserBuilder.aUser().build())
      .addItem(ProductBuilder.aProduct().build())
      .asPaid()
      .build();

    expect(order.status).toBe('paid');
    expect(order.paidAt).toBeDefined();
  });
});
```

### 3. **Fixtures for Integration Tests**

#### Jest/TypeScript with Database Fixtures
```typescript
// tests/fixtures/database.ts
import { PrismaClient } from '@prisma/client';
import { UserFactory, ProductFactory, OrderFactory } from './factories';

export class DatabaseFixtures {
  constructor(private prisma: PrismaClient) {}

  async seed() {
    // Create users
    const users = await Promise.all(
      UserFactory.buildMany(10).map(userData =>
        this.prisma.user.create({ data: userData })
      )
    );

    // Create products
    const products = await Promise.all(
      ProductFactory.buildMany(20).map(productData =>
        this.prisma.product.create({ data: productData })
      )
    );

    // Create orders
    const orders = await Promise.all(
      OrderFactory.buildMany(15).map(orderData =>
        this.prisma.order.create({
          data: {
            ...orderData,
            userId: users[Math.floor(Math.random() * users.length)].id,
            items: {
              create: products.slice(0, 3).map(product => ({
                productId: product.id,
                quantity: Math.floor(Math.random() * 3) + 1,
                price: product.price,
              })),
            },
          },
        })
      )
    );

    return { users, products, orders };
  }

  async clear() {
    await this.prisma.orderItem.deleteMany();
    await this.prisma.order.deleteMany();
    await this.prisma.product.deleteMany();
    await this.prisma.user.deleteMany();
  }
}

// tests/setup.ts
import { PrismaClient } from '@prisma/client';
import { DatabaseFixtures } from './fixtures/database';

const prisma = new PrismaClient();
const fixtures = new DatabaseFixtures(prisma);

beforeAll(async () => {
  await fixtures.clear();
  await fixtures.seed();
});

afterAll(async () => {
  await fixtures.clear();
  await prisma.$disconnect();
});
```

#### pytest Fixtures
```python
# tests/conftest.py
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tests.factories import UserFactory, ProductFactory, OrderFactory

@pytest.fixture(scope='session')
def engine():
    """Create database engine."""
    return create_engine('sqlite:///:memory:')

@pytest.fixture(scope='session')
def tables(engine):
    """Create all tables."""
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.fixture
def db_session(engine, tables):
    """Create database session for each test."""
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.rollback()
    session.close()

@pytest.fixture
def sample_users(db_session):
    """Create sample users for testing."""
    users = UserFactory.build_batch(5)
    db_session.add_all(users)
    db_session.commit()
    return users

@pytest.fixture
def sample_products(db_session):
    """Create sample products for testing."""
    products = ProductFactory.build_batch(10)
    db_session.add_all(products)
    db_session.commit()
    return products

@pytest.fixture
def admin_user(db_session):
    """Create an admin user."""
    admin = UserFactory.build(admin=True)
    db_session.add(admin)
    db_session.commit()
    return admin

@pytest.fixture
def order_with_items(db_session, sample_users, sample_products):
    """Create an order with items."""
    order = OrderFactory.build(
        user=sample_users[0],
        products=sample_products[:3]
    )
    db_session.add(order)
    db_session.commit()
    return order

# Usage in tests
def test_user_orders(order_with_items):
    """Test user has correct orders."""
    user = order_with_items.user
    assert len(user.orders) == 1
    assert user.orders[0].id == order_with_items.id
```

### 4. **Realistic Data Generation**

```javascript
// tests/helpers/dataGenerator.js
const { faker } = require('@faker-js/faker');

class DataGenerator {
  static generateCreditCard() {
    return {
      number: faker.finance.creditCardNumber('#### #### #### ####'),
      cvv: faker.finance.creditCardCVV(),
      expiry: faker.date.future().toISOString().slice(0, 7), // YYYY-MM
      type: faker.helpers.arrayElement(['visa', 'mastercard', 'amex']),
    };
  }

  static generateAddress() {
    return {
      street: faker.location.streetAddress(),
      city: faker.location.city(),
      state: faker.location.state(),
      zip: faker.location.zipCode(),
      country: faker.location.country(),
      coordinates: {
        lat: parseFloat(faker.location.latitude()),
        lng: parseFloat(faker.location.longitude()),
      },
    };
  }

  static generateDateRange(days = 30) {
    const endDate = new Date();
    const startDate = new Date();
    startDate.setDate(startDate.getDate() - days);
    return { startDate, endDate };
  }

  static generateTimeSeries(count, interval = 'day') {
    const data = [];
    const now = new Date();

    for (let i = count - 1; i >= 0; i--) {
      const date = new Date(now);
      if (interval === 'day') date.setDate(date.getDate() - i);
      if (interval === 'hour') date.setHours(date.getHours() - i);

      data.push({
        timestamp: date,
        value: faker.number.float({ min: 0, max: 100, precision: 0.01 }),
      });
    }

    return data;
  }

  static generateRealisticEmail(firstName, lastName, domain = 'example.com') {
    const patterns = [
      `${firstName}.${lastName}`,
      `${firstName}${lastName}`,
      `${firstName.charAt(0)}${lastName}`,
      `${firstName}_${lastName}`,
    ];

    const pattern = faker.helpers.arrayElement(patterns);
    return `${pattern.toLowerCase()}@${domain}`;
  }
}

module.exports = { DataGenerator };
```

## Best Practices

### ✅ DO
- Use faker libraries for realistic data
- Create reusable factories for common objects
- Make factories flexible with overrides
- Generate unique values where needed (emails, IDs)
- Use builders for complex object construction
- Create fixtures for integration test setup
- Generate edge cases (empty strings, nulls, boundaries)
- Keep test data deterministic when possible

### ❌ DON'T
- Hardcode test data in multiple places
- Use production data in tests
- Generate truly random data for reproducible tests
- Create overly complex factory hierarchies
- Ignore data relationships and constraints
- Generate massive datasets for simple tests
- Forget to clean up generated data
- Use the same test data for all tests

## Tools & Libraries

- **JavaScript**: @faker-js/faker, fishery, rosie, casual
- **Python**: factory_boy, faker, hypothesis
- **Java**: Instancio, EasyRandom, JavaFaker, Mockito
- **Ruby**: FactoryBot, Faker, Fabrication
- **Database**: SQL fixtures, JSON fixtures, CSV imports

## Example: Complete Test Data Setup

```typescript
// tests/setup/testData.ts
import { faker } from '@faker-js/faker';

// Configure faker for deterministic tests
faker.seed(12345);

export const TestData = {
  users: {
    admin: () => ({
      email: 'admin@test.com',
      role: 'admin',
      permissions: ['read', 'write', 'delete'],
    }),
    regular: () => ({
      email: faker.internet.email(),
      role: 'user',
      isActive: true,
    }),
  },

  products: {
    inStock: (overrides = {}) => ({
      name: faker.commerce.productName(),
      price: parseFloat(faker.commerce.price()),
      stock: faker.number.int({ min: 10, max: 100 }),
      isAvailable: true,
      ...overrides,
    }),
    outOfStock: () => ({
      ...TestData.products.inStock(),
      stock: 0,
      isAvailable: false,
    }),
  },

  orders: {
    pending: (userId: string) => ({
      userId,
      status: 'pending',
      items: [],
      total: 0,
    }),
    completed: (userId: string) => ({
      userId,
      status: 'completed',
      completedAt: faker.date.recent(),
      items: [],
      total: faker.number.float({ min: 10, max: 1000 }),
    }),
  },
};
```

## Examples

See also: integration-testing, mocking-stubbing, continuous-testing skills for using test data effectively.
