# Fixtures for Integration Tests

## Fixtures for Integration Tests

### Jest/TypeScript with Database Fixtures

```typescript
// tests/fixtures/database.ts
import { PrismaClient } from "@prisma/client";
import { UserFactory, ProductFactory, OrderFactory } from "./factories";

export class DatabaseFixtures {
  constructor(private prisma: PrismaClient) {}

  async seed() {
    // Create users
    const users = await Promise.all(
      UserFactory.buildMany(10).map((userData) =>
        this.prisma.user.create({ data: userData }),
      ),
    );

    // Create products
    const products = await Promise.all(
      ProductFactory.buildMany(20).map((productData) =>
        this.prisma.product.create({ data: productData }),
      ),
    );

    // Create orders
    const orders = await Promise.all(
      OrderFactory.buildMany(15).map((orderData) =>
        this.prisma.order.create({
          data: {
            ...orderData,
            userId: users[Math.floor(Math.random() * users.length)].id,
            items: {
              create: products.slice(0, 3).map((product) => ({
                productId: product.id,
                quantity: Math.floor(Math.random() * 3) + 1,
                price: product.price,
              })),
            },
          },
        }),
      ),
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
import { PrismaClient } from "@prisma/client";
import { DatabaseFixtures } from "./fixtures/database";

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

### pytest Fixtures

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
