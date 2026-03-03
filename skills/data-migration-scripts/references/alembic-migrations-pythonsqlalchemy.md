# Alembic Migrations (Python/SQLAlchemy)

## Alembic Migrations (Python/SQLAlchemy)

```python
"""Add user roles and permissions

Revision ID: a1b2c3d4e5f6
Revises: previous_revision
Create Date: 2024-01-01 00:00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers
revision = 'a1b2c3d4e5f6'
down_revision = 'previous_revision'
branch_labels = None
depends_on = None


def upgrade():
    # Create roles table
    op.create_table(
        'roles',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('name', sa.String(50), unique=True, nullable=False),
        sa.Column('description', sa.Text()),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )

    # Create user_roles junction table
    op.create_table(
        'user_roles',
        sa.Column('user_id', sa.Integer(), sa.ForeignKey('users.id', ondelete='CASCADE')),
        sa.Column('role_id', sa.Integer(), sa.ForeignKey('roles.id', ondelete='CASCADE')),
        sa.Column('assigned_at', sa.DateTime(), server_default=sa.func.now()),
        sa.PrimaryKeyConstraint('user_id', 'role_id')
    )

    # Create indexes
    op.create_index('idx_user_roles_user_id', 'user_roles', ['user_id'])
    op.create_index('idx_user_roles_role_id', 'user_roles', ['role_id'])

    # Insert default roles
    op.execute("""
        INSERT INTO roles (name, description) VALUES
        ('admin', 'Administrator with full access'),
        ('user', 'Standard user'),
        ('guest', 'Guest with limited access')
    """)

    # Migrate existing users to default role
    op.execute("""
        INSERT INTO user_roles (user_id, role_id)
        SELECT u.id, r.id
        FROM users u
        CROSS JOIN roles r
        WHERE r.name = 'user'
    """)


def downgrade():
    # Drop tables in reverse order
    op.drop_index('idx_user_roles_role_id', 'user_roles')
    op.drop_index('idx_user_roles_user_id', 'user_roles')
    op.drop_table('user_roles')
    op.drop_table('roles')
```
