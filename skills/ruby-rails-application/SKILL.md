---
name: ruby-rails-application
description: Develop Ruby on Rails applications with models, controllers, views, Active Record ORM, authentication, and RESTful routes. Use when building Rails applications, managing database relationships, and implementing MVC architecture.
---

# Ruby Rails Application

## Overview

Build comprehensive Ruby on Rails applications with proper model associations, RESTful controllers, Active Record queries, authentication systems, middleware chains, and view rendering following Rails conventions.

## When to Use

- Building Rails web applications
- Implementing Active Record models with associations
- Creating RESTful controllers and actions
- Integrating authentication and authorization
- Building complex database relationships
- Implementing Rails middleware and filters

## Instructions

### 1. **Rails Project Setup**

```bash
rails new myapp --api --database=postgresql
cd myapp
rails db:create
```

### 2. **Models with Active Record**

```ruby
# app/models/user.rb
class User < ApplicationRecord
  has_many :posts, dependent: :destroy
  has_many :comments, dependent: :destroy

  enum role: { user: 0, admin: 1 }

  validates :email, presence: true, uniqueness: true, format: { with: URI::MailTo::EMAIL_REGEXP }
  validates :password, presence: true, length: { minimum: 8 }, if: :new_record?
  validates :first_name, :last_name, presence: true

  has_secure_password

  before_save :downcase_email

  def full_name
    "#{first_name} #{last_name}"
  end

  def active?
    is_active
  end

  private

  def downcase_email
    self.email = email.downcase
  end
end

# app/models/post.rb
class Post < ApplicationRecord
  belongs_to :user
  has_many :comments, dependent: :destroy

  enum status: { draft: 0, published: 1, archived: 2 }

  validates :title, presence: true, length: { minimum: 1, maximum: 255 }
  validates :content, presence: true, length: { minimum: 1 }
  validates :user_id, presence: true

  scope :published, -> { where(status: :published) }
  scope :recent, -> { order(created_at: :desc) }
  scope :by_author, ->(user_id) { where(user_id: user_id) }

  def publish!
    update(status: :published)
  end

  def unpublish!
    update(status: :draft)
  end
end

# app/models/comment.rb
class Comment < ApplicationRecord
  belongs_to :user
  belongs_to :post

  validates :content, presence: true, length: { minimum: 1 }
  validates :user_id, :post_id, presence: true

  scope :recent, -> { order(created_at: :desc) }
  scope :by_author, ->(user_id) { where(user_id: user_id) }
end
```

### 3. **Database Migrations**

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

### 4. **Controllers with RESTful Actions**

```ruby
# app/controllers/api/v1/users_controller.rb
module Api
  module V1
    class UsersController < ApplicationController
      before_action :authenticate_request, except: [:create]
      before_action :set_user, only: [:show, :update, :destroy]
      before_action :authorize_user!, only: [:update, :destroy]

      def index
        users = User.all
        users = users.where("email ILIKE ?", "%#{params[:q]}%") if params[:q].present?
        users = users.page(params[:page]).per(params[:limit] || 20)

        render json: {
          data: users,
          pagination: pagination_data(users)
        }
      end

      def show
        render json: @user
      end

      def create
        user = User.new(user_params)

        if user.save
          token = encode_token(user.id)
          render json: {
            user: user,
            token: token
          }, status: :created
        else
          render json: { errors: user.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def update
        if @user.update(user_params)
          render json: @user
        else
          render json: { errors: @user.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def destroy
        @user.destroy
        head :no_content
      end

      private

      def set_user
        @user = User.find(params[:id])
      rescue ActiveRecord::RecordNotFound
        render json: { error: 'User not found' }, status: :not_found
      end

      def authorize_user!
        unless current_user.id == @user.id || current_user.admin?
          render json: { error: 'Unauthorized' }, status: :forbidden
        end
      end

      def user_params
        params.require(:user).permit(:email, :password, :first_name, :last_name)
      end

      def pagination_data(collection)
        {
          page: collection.current_page,
          per_page: collection.limit_value,
          total: collection.total_count,
          total_pages: collection.total_pages
        }
      end
    end
  end
end

# app/controllers/api/v1/posts_controller.rb
module Api
  module V1
    class PostsController < ApplicationController
      before_action :authenticate_request, except: [:index, :show]
      before_action :set_post, only: [:show, :update, :destroy, :publish]
      before_action :authorize_post_owner!, only: [:update, :destroy, :publish]

      def index
        posts = Post.published.recent
        posts = posts.by_author(params[:author_id]) if params[:author_id].present?
        posts = posts.where("title ILIKE ?", "%#{params[:q]}%") if params[:q].present?
        posts = posts.page(params[:page]).per(params[:limit] || 20)

        render json: {
          data: posts,
          pagination: pagination_data(posts)
        }
      end

      def show
        if @post.published? || current_user&.id == @post.user_id
          render json: @post
        else
          render json: { error: 'Post not found' }, status: :not_found
        end
      end

      def create
        @post = current_user.posts.build(post_params)

        if @post.save
          render json: @post, status: :created
        else
          render json: { errors: @post.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def update
        if @post.update(post_params)
          render json: @post
        else
          render json: { errors: @post.errors.full_messages }, status: :unprocessable_entity
        end
      end

      def destroy
        @post.destroy
        head :no_content
      end

      def publish
        @post.publish!
        render json: @post
      end

      private

      def set_post
        @post = Post.find(params[:id])
      rescue ActiveRecord::RecordNotFound
        render json: { error: 'Post not found' }, status: :not_found
      end

      def authorize_post_owner!
        unless current_user.id == @post.user_id || current_user.admin?
          render json: { error: 'Unauthorized' }, status: :forbidden
        end
      end

      def post_params
        params.require(:post).permit(:title, :content, :status)
      end

      def pagination_data(collection)
        {
          page: collection.current_page,
          per_page: collection.limit_value,
          total: collection.total_count
        }
      end
    end
  end
end
```

### 5. **Authentication with JWT**

```ruby
# app/controllers/application_controller.rb
class ApplicationController < ActionController::API
  include ActionController::Cookies

  SECRET_KEY = Rails.application.secrets.secret_key_base

  def encode_token(user_id)
    payload = { user_id: user_id, exp: 24.hours.from_now.to_i }
    JWT.encode(payload, SECRET_KEY, 'HS256')
  end

  def decode_token(token)
    begin
      JWT.decode(token, SECRET_KEY, true, { algorithm: 'HS256' })
    rescue JWT::ExpiredSignature, JWT::DecodeError
      nil
    end
  end

  def authenticate_request
    header = request.headers['Authorization']
    token = header.split(' ').last if header.present?

    decoded = decode_token(token)
    if decoded
      @current_user_id = decoded[0]['user_id']
      @current_user = User.find(@current_user_id)
    else
      render json: { error: 'Unauthorized' }, status: :unauthorized
    end
  end

  def current_user
    @current_user
  end

  def logged_in?
    current_user.present?
  end
end

# config/routes.rb
Rails.application.routes.draw do
  namespace :api do
    namespace :v1 do
      post 'auth/login', to: 'auth#login'
      post 'auth/register', to: 'auth#register'

      resources :users
      resources :posts do
        member do
          patch :publish
        end
        resources :comments, only: [:index, :create, :destroy]
      end
    end
  end
end
```

### 6. **Active Record Queries**

```ruby
# app/services/post_service.rb
class PostService
  def self.get_user_posts(user_id, status: nil)
    posts = Post.by_author(user_id)
    posts = posts.where(status: status) if status.present?
    posts.recent
  end

  def self.trending_posts(limit: 10)
    Post.published
        .joins(:comments)
        .group('posts.id')
        .order('COUNT(comments.id) DESC')
        .limit(limit)
  end

  def self.search_posts(query)
    Post.published
        .where("title ILIKE ? OR content ILIKE ?", "%#{query}%", "%#{query}%")
        .recent
  end

  def self.archive_old_drafts(days: 30)
    Post.where(status: :draft)
        .where('created_at < ?', days.days.ago)
        .update_all(status: :archived)
  end
end

# Usage
posts = Post.includes(:user).recent.limit(10)
recent_comments = Comment.where(post_id: post.id).order(created_at: :desc).limit(5)
```

### 7. **Serializers**

```ruby
# app/serializers/user_serializer.rb
class UserSerializer
  def initialize(user)
    @user = user
  end

  def to_json
    {
      id: @user.id,
      email: @user.email,
      first_name: @user.first_name,
      last_name: @user.last_name,
      full_name: @user.full_name,
      role: @user.role,
      is_active: @user.is_active,
      created_at: @user.created_at.iso8601,
      updated_at: @user.updated_at.iso8601
    }
  end
end

# In controller
def show
  render json: UserSerializer.new(@user).to_json
end
```

## Best Practices

### ✅ DO
- Use conventions over configuration
- Leverage Active Record associations
- Implement proper scopes for queries
- Use strong parameters for security
- Implement authentication in ApplicationController
- Use services for complex business logic
- Implement proper error handling
- Use database migrations for schema changes
- Validate all inputs at model level
- Use before_action filters appropriately

### ❌ DON'T
- Use raw SQL without parameterization
- Implement business logic in controllers
- Trust user input without validation
- Store secrets in code
- Use select * without specifying columns
- Forget N+1 query problems (use includes/joins)
- Implement authentication in each controller
- Use global variables
- Ignore database constraints

## Complete Example

```ruby
# Gemfile
source 'https://rubygems.org'
gem 'rails', '~> 7.0.0'
gem 'pg', '~> 1.1'
gem 'bcrypt', '~> 3.1.7'
gem 'jwt'
gem 'kaminari'

# models.rb + controllers.rb (see sections above)
# routes.rb and migrations (see sections above)
```
