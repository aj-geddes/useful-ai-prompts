# Service Layer for Business Logic

## Service Layer for Business Logic

```python
# services.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from database import User, Post
from models import UserCreate, UserUpdate, PostCreate
from security import hash_password, verify_password
from typing import Optional

class UserService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_user(self, user_data: UserCreate) -> User:
        db_user = User(
            email=user_data.email,
            password_hash=hash_password(user_data.password),
            first_name=user_data.first_name,
            last_name=user_data.last_name
        )
        self.db.add(db_user)
        await self.db.commit()
        await self.db.refresh(db_user)
        return db_user

    async def get_user_by_email(self, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email.lower())
        result = await self.db.execute(stmt)
        return result.scalar_one_or_none()

    async def get_user_by_id(self, user_id: str) -> Optional[User]:
        return await self.db.get(User, user_id)

    async def authenticate_user(self, email: str, password: str) -> Optional[User]:
        user = await self.get_user_by_email(email)
        if user and verify_password(password, user.password_hash):
            return user
        return None

    async def update_user(self, user_id: str, user_data: UserUpdate) -> Optional[User]:
        user = await self.get_user_by_id(user_id)
        if not user:
            return None

        update_data = user_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(user, field, value)

        await self.db.commit()
        await self.db.refresh(user)
        return user

    async def list_users(self, skip: int = 0, limit: int = 20) -> tuple:
        stmt = select(User).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        users = result.scalars().all()

        count_stmt = select(User)
        count_result = await self.db.execute(count_stmt)
        total = len(count_result.scalars().all())

        return users, total

class PostService:
    def __init__(self, db: AsyncSession):
        self.db = db

    async def create_post(self, author_id: str, post_data: PostCreate) -> Post:
        db_post = Post(
            title=post_data.title,
            content=post_data.content,
            author_id=author_id,
            published=post_data.published
        )
        self.db.add(db_post)
        await self.db.commit()
        await self.db.refresh(db_post)
        return db_post

    async def get_published_posts(self, skip: int = 0, limit: int = 20) -> tuple:
        stmt = select(Post).where(Post.published == True).offset(skip).limit(limit)
        result = await self.db.execute(stmt)
        posts = result.scalars().all()
        return posts, len(posts)
```
