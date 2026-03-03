# API Integration Testing

## API Integration Testing

### Express/Node.js with Jest and Supertest

```javascript
// test/api/users.integration.test.js
const request = require("supertest");
const app = require("../../src/app");
const { setupTestDB, teardownTestDB } = require("../helpers/db");

describe("User API Integration Tests", () => {
  beforeAll(async () => {
    await setupTestDB();
  });

  afterAll(async () => {
    await teardownTestDB();
  });

  beforeEach(async () => {
    await clearUsers();
  });

  describe("POST /api/users", () => {
    it("should create a new user with valid data", async () => {
      const userData = {
        email: "test@example.com",
        name: "Test User",
        password: "SecurePass123!",
      };

      const response = await request(app)
        .post("/api/users")
        .send(userData)
        .expect(201);

      expect(response.body).toMatchObject({
        id: expect.any(String),
        email: userData.email,
        name: userData.name,
      });
      expect(response.body.password).toBeUndefined();

      // Verify in database
      const user = await User.findById(response.body.id);
      expect(user).toBeTruthy();
      expect(user.email).toBe(userData.email);
    });

    it("should reject duplicate email addresses", async () => {
      const userData = {
        email: "test@example.com",
        name: "Test",
        password: "pass",
      };

      await request(app).post("/api/users").send(userData).expect(201);

      const response = await request(app)
        .post("/api/users")
        .send(userData)
        .expect(409);

      expect(response.body.error).toMatch(/email.*exists/i);
    });
  });

  describe("GET /api/users/:id", () => {
    it("should retrieve user with associated orders", async () => {
      const user = await createTestUser();
      await createTestOrder({ userId: user.id, total: 99.99 });

      const response = await request(app)
        .get(`/api/users/${user.id}`)
        .set("Authorization", `Bearer ${user.token}`)
        .expect(200);

      expect(response.body).toMatchObject({
        id: user.id,
        orders: expect.arrayContaining([
          expect.objectContaining({ total: 99.99 }),
        ]),
      });
    });
  });
});
```

### FastAPI/Python with pytest

```python
# tests/integration/test_user_api.py
import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession

from app.main import app
from app.models import User
from tests.conftest import test_db

@pytest.mark.asyncio
class TestUserAPI:
    async def test_create_user_integration(
        self,
        client: AsyncClient,
        db: AsyncSession
    ):
        """Test user creation with database persistence."""
        user_data = {
            "email": "test@example.com",
            "name": "Test User",
            "password": "SecurePass123!"
        }

        response = await client.post("/api/users", json=user_data)

        assert response.status_code == 201
        data = response.json()
        assert data["email"] == user_data["email"]
        assert "password" not in data

        # Verify in database
        result = await db.execute(
            select(User).where(User.email == user_data["email"])
        )
        user = result.scalar_one()
        assert user is not None
        assert user.name == user_data["name"]

    async def test_user_with_relationships(
        self,
        client: AsyncClient,
        db: AsyncSession
    ):
        """Test retrieving user with related data."""
        # Setup: Create user with orders
        user = await create_test_user(db)
        await create_test_order(db, user_id=user.id, total=99.99)

        # Test: Fetch user with orders
        response = await client.get(
            f"/api/users/{user.id}",
            headers={"Authorization": f"Bearer {user.token}"}
        )

        assert response.status_code == 200
        data = response.json()
        assert data["id"] == user.id
        assert len(data["orders"]) == 1
        assert data["orders"][0]["total"] == 99.99
```
