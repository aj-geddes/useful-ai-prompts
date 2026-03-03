# Flask with Jinja2 Templates

## Flask with Jinja2 Templates

```python
# app.py
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Custom Jinja2 filters
@app.template_filter('currency')
def format_currency(value):
    return f"${value:.2f}"

@app.template_filter('date_format')
def format_date(date_obj):
    return date_obj.strftime('%Y-%m-%d %H:%M:%S')

@app.context_processor
def inject_globals():
    """Inject global variables into templates"""
    return {
        'app_name': 'My App',
        'current_year': datetime.now().year,
        'support_email': 'support@example.com'
    }

# routes.py
@app.route('/')
def index():
    """Home page"""
    featured_posts = Post.query.filter_by(featured=True).limit(5).all()
    return render_template('index.html', featured_posts=featured_posts)

@app.route('/dashboard')
@login_required
def dashboard():
    """User dashboard"""
    user_stats = {
        'total_posts': current_user.posts.count(),
        'total_views': sum(p.view_count for p in current_user.posts),
        'total_followers': current_user.followers.count()
    }

    recent_activity = current_user.get_activity(limit=10)

    return render_template(
        'dashboard.html',
        stats=user_stats,
        activity=recent_activity
    )

@app.route('/posts/<slug>')
def view_post(slug):
    """View single post"""
    post = Post.query.filter_by(slug=slug).first_or_404()

    # Increment view count
    post.view_count += 1
    db.session.commit()

    # Get related posts
    related = Post.query.filter(
        Post.category_id == post.category_id,
        Post.id != post.id
    ).limit(5).all()

    return render_template(
        'post.html',
        post=post,
        related_posts=related,
        comments=post.comments.order_by(Comment.created_at.desc()).all()
    )

@app.route('/search')
def search():
    """Search posts"""
    query = request.args.get('q', '')
    page = request.args.get('page', 1, type=int)

    if not query:
        return render_template('search.html', posts=[], query='')

    posts = Post.query.filter(
        Post.title.ilike(f'%{query}%') |
        Post.content.ilike(f'%{query}%')
    ).paginate(page=page, per_page=20)

    return render_template(
        'search.html',
        posts=posts.items,
        total=posts.total,
        query=query,
        page=page
    )

@app.route('/admin/posts/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_post():
    """Create new post"""
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        category_id = request.form['category_id']

        post = Post(
            title=title,
            slug=generate_slug(title),
            content=content,
            category_id=category_id,
            author_id=current_user.id
        )
        db.session.add(post)
        db.session.commit()

        return redirect(url_for('view_post', slug=post.slug))

    categories = Category.query.all()
    return render_template('admin/create_post.html', categories=categories)
```
