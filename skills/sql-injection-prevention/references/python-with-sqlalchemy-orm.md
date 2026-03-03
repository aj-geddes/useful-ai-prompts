# Python with SQLAlchemy ORM

## Python with SQLAlchemy ORM

```python
# secure_queries.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import re

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(100))
    password_hash = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

class SecureDatabase:
    def __init__(self, connection_string):
        self.engine = create_engine(connection_string, pool_pre_ping=True)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def get_user_by_id(self, user_id: int):
        """✅ SECURE: ORM query"""
        return self.session.query(User).filter(User.id == user_id).first()

    def search_users(self, email: str):
        """✅ SECURE: Parameterized LIKE query"""
        return self.session.query(User).filter(
            User.email.like(f'%{email}%')
        ).limit(100).all()

    def get_users_sorted(self, sort_by: str = 'created_at', order: str = 'desc'):
        """✅ SECURE: Whitelisted column sorting"""
        allowed_columns = {
            'id': User.id,
            'email': User.email,
            'name': User.name,
            'created_at': User.created_at
        }

        if sort_by not in allowed_columns:
            sort_by = 'created_at'

        column = allowed_columns[sort_by]

        if order.lower() == 'asc':
            column = column.asc()
        else:
            column = column.desc()

        return self.session.query(User).order_by(column).limit(100).all()

    def raw_query_secure(self, user_id: int):
        """✅ SECURE: Raw SQL with parameters"""
        from sqlalchemy import text

        query = text("SELECT * FROM users WHERE id = :id")
        result = self.session.execute(query, {'id': user_id})

        return result.fetchall()

    def validate_and_sanitize(self, input_str: str) -> str:
        """Validate and sanitize user input"""
        # Remove potentially dangerous characters
        # Only allow alphanumeric, spaces, and common punctuation
        sanitized = re.sub(r'[^\w\s@.,\-]', '', input_str)

        # Limit length
        sanitized = sanitized[:255]

        return sanitized

    def vulnerable_query(self, user_input: str):
        """❌ VULNERABLE: String formatting (DON'T USE)"""
        from sqlalchemy import text

        # VULNERABLE TO SQL INJECTION!
        query = text(f"SELECT * FROM users WHERE email = '{user_input}'")
        # Attack: user_input = "' OR '1'='1"

        result = self.session.execute(query)
        return result.fetchall()

# Usage
if __name__ == '__main__':
    db = SecureDatabase('postgresql://user:pass@localhost/mydb')

    # Secure queries
    user = db.get_user_by_id(123)
    users = db.search_users('example.com')
    sorted_users = db.get_users_sorted('email', 'asc')
```
