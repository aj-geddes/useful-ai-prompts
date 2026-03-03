# Database Migrations

## Database Migrations

```ruby
# db/migrate/20240101120000_create_users.rb
class CreateUsers < ActiveRecord::Migration[7.0]
  def change
    create_table :users do |t|
      t.string :email, null: false
      t.string :password_digest, null: false
      t.string :first_name, null: false
      t.string :last_name, null: false
      t.integer :role, default: 0
      t.boolean :is_active, default: true
      t.timestamps
    end

    add_index :users, :email, unique: true
    add_index :users, :role
  end
end

# db/migrate/20240101120001_create_posts.rb
class CreatePosts < ActiveRecord::Migration[7.0]
  def change
    create_table :posts do |t|
      t.string :title, null: false
      t.text :content, null: false
      t.integer :status, default: 0
      t.references :user, null: false, foreign_key: true
      t.timestamps
    end

    add_index :posts, :status
    add_index :posts, [:user_id, :status]
  end
end

# db/migrate/20240101120002_create_comments.rb
class CreateComments < ActiveRecord::Migration[7.0]
  def change
    create_table :comments do |t|
      t.text :content, null: false
      t.references :user, null: false, foreign_key: true
      t.references :post, null: false, foreign_key: true
      t.timestamps
    end

    add_index :comments, [:post_id, :created_at]
    add_index :comments, [:user_id, :created_at]
  end
end
```
