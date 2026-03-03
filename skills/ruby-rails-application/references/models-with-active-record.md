# Models with Active Record

## Models with Active Record

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
