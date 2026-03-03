# Caching and Performance

## Caching and Performance

```python
# Flask caching
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'redis'})

@app.route('/posts/<slug>')
@cache.cached(timeout=3600)  # Cache for 1 hour
def view_post(slug):
    """Cached post view"""
    post = Post.query.filter_by(slug=slug).first_or_404()
    comments = post.comments.all()
    return render_template('post.html', post=post, comments=comments)

@app.route('/api/posts')
@cache.cached(timeout=300)  # Cache for 5 minutes
def get_posts():
    """Cached API endpoint"""
    posts = Post.query.filter_by(published=True).all()
    return jsonify([p.to_dict() for p in posts])

# Invalidate cache
@app.route('/admin/posts/<id>/edit', methods=['POST'])
@admin_required
def edit_post(id):
    post = Post.query.get(id)
    # Update post
    db.session.commit()

    # Clear cache
    cache.delete_memoized(view_post, post.slug)
    cache.delete_memoized(get_posts)

    return redirect(url_for('view_post', slug=post.slug))
```
