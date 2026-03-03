# Repository Pattern

## Repository Pattern

Abstract data access logic.

```python
from abc import ABC, abstractmethod
from typing import List, Optional

class UserRepository(ABC):
    @abstractmethod
    def find_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def find_all(self) -> List[User]:
        pass

    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass

class DatabaseUserRepository(UserRepository):
    def __init__(self, db_connection):
        self.db = db_connection

    def find_by_id(self, user_id: int) -> Optional[User]:
        result = self.db.query('SELECT * FROM users WHERE id = ?', user_id)
        return User.from_dict(result) if result else None

    def find_all(self) -> List[User]:
        results = self.db.query('SELECT * FROM users')
        return [User.from_dict(r) for r in results]

    def save(self, user: User) -> User:
        self.db.execute('INSERT INTO users (...) VALUES (...)', user.to_dict())
        return user

    def delete(self, user_id: int) -> bool:
        return self.db.execute('DELETE FROM users WHERE id = ?', user_id)
```
