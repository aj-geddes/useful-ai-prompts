# Database Query Performance

## Database Query Performance

```python
# test_database_performance.py
import pytest
import time
from sqlalchemy import create_engine
from app.models import User, Order

class TestDatabasePerformance:
    @pytest.fixture
    def db_session(self):
        """Create test database session."""
        engine = create_engine('postgresql://localhost/testdb')
        Session = sessionmaker(bind=engine)
        return Session()

    def test_query_without_index(self, db_session, benchmark):
        """Measure query performance without index."""
        def query():
            return db_session.query(User).filter(
                User.email == 'test@example.com'
            ).first()

        result = benchmark(query)

    def test_query_with_index(self, db_session, benchmark):
        """Measure query performance with index."""
        # Assume email column is indexed
        def query():
            return db_session.query(User).filter(
                User.email == 'test@example.com'
            ).first()

        result = benchmark(query)

    def test_n_plus_one_query(self, db_session):
        """Identify N+1 query problem."""
        start = time.time()

        # ❌ N+1 queries
        users = db_session.query(User).all()
        for user in users:
            orders = user.orders  # Triggers separate query for each user

        n_plus_one_time = time.time() - start

        # ✅ Eager loading
        start = time.time()
        users = db_session.query(User).options(
            joinedload(User.orders)
        ).all()

        eager_time = time.time() - start

        assert eager_time < n_plus_one_time, "Eager loading should be faster"
        print(f"N+1: {n_plus_one_time:.3f}s, Eager: {eager_time:.3f}s")

    def test_pagination_performance(self, db_session, benchmark):
        """Test pagination efficiency."""
        def paginate():
            return db_session.query(Product)\
                .order_by(Product.id)\
                .limit(50)\
                .offset(1000)\
                .all()

        results = benchmark(paginate)
        assert len(results) == 50
```
