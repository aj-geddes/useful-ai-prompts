# Active Record Queries

## Active Record Queries

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
