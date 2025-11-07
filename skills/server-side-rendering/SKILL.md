---
name: server-side-rendering
description: Implement server-side rendering with template engines, view layers, and dynamic content generation. Use when building server-rendered applications, implementing MVC architectures, and generating HTML on the server.
---

# Server-Side Rendering

## Overview

Build server-side rendered applications using modern template engines, view layers, and data-driven HTML generation with caching, streaming, and performance optimization across Python, Node.js, and Ruby frameworks.

## When to Use

- Building traditional web applications
- Rendering HTML on the server
- Implementing SEO-friendly applications
- Creating real-time updating pages
- Building admin dashboards
- Implementing email templates

## Instructions

### 1. **Flask with Jinja2 Templates**

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

### 2. **Jinja2 Template Examples**

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{{ app_name }}{% endblock %}</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
    {% block extra_head %}{% endblock %}
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <h1>{{ app_name }}</h1>
            <ul>
                <li><a href="{{ url_for('index') }}">Home</a></li>
                {% if current_user.is_authenticated %}
                    <li><a href="{{ url_for('dashboard') }}">Dashboard</a></li>
                    <li><a href="{{ url_for('logout') }}">Logout</a></li>
                {% else %}
                    <li><a href="{{ url_for('login') }}">Login</a></li>
                    <li><a href="{{ url_for('register') }}">Register</a></li>
                {% endif %}
            </ul>
        </div>
    </nav>

    <main class="container">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}

        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; {{ current_year }} {{ app_name }}. All rights reserved.</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block extra_scripts %}{% endblock %}
</body>
</html>

<!-- dashboard.html -->
{% extends "base.html" %}

{% block title %}Dashboard - {{ app_name }}{% endblock %}

{% block content %}
<div class="dashboard">
    <h1>Welcome, {{ current_user.first_name }}!</h1>

    <div class="stats-grid">
        <div class="stat-card">
            <h3>Total Posts</h3>
            <p class="stat-value">{{ stats.total_posts }}</p>
        </div>
        <div class="stat-card">
            <h3>Total Views</h3>
            <p class="stat-value">{{ stats.total_views | default(0) }}</p>
        </div>
        <div class="stat-card">
            <h3>Followers</h3>
            <p class="stat-value">{{ stats.total_followers }}</p>
        </div>
    </div>

    <section class="recent-activity">
        <h2>Recent Activity</h2>
        {% if activity %}
            <ul class="activity-list">
                {% for item in activity %}
                    <li>
                        <span class="activity-date">{{ item.created_at | date_format }}</span>
                        <span class="activity-text">{{ item.description }}</span>
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No recent activity.</p>
        {% endif %}
    </section>
</div>
{% endblock %}

<!-- post.html -->
{% extends "base.html" %}

{% block title %}{{ post.title }} - {{ app_name }}{% endblock %}

{% block content %}
<article class="post">
    <header class="post-header">
        <h1>{{ post.title }}</h1>
        <div class="post-meta">
            <span class="author">By {{ post.author.full_name }}</span>
            <span class="date">{{ post.created_at | date_format }}</span>
            <span class="category">
                <a href="{{ url_for('view_category', slug=post.category.slug) }}">
                    {{ post.category.name }}
                </a>
            </span>
        </div>
    </header>

    <div class="post-content">
        {{ post.content | safe }}
    </div>

    {% if related_posts %}
        <section class="related-posts">
            <h3>Related Posts</h3>
            <div class="posts-grid">
                {% for related in related_posts %}
                    <div class="post-card">
                        <h4><a href="{{ url_for('view_post', slug=related.slug) }}">{{ related.title }}</a></h4>
                        <p>{{ related.excerpt or related.content[:100] }}...</p>
                        <a href="{{ url_for('view_post', slug=related.slug) }}" class="read-more">Read More</a>
                    </div>
                {% endfor %}
            </div>
        </section>
    {% endif %}

    <section class="comments">
        <h3>Comments ({{ comments | length }})</h3>
        {% if comments %}
            <ul class="comment-list">
                {% for comment in comments %}
                    <li class="comment">
                        <strong>{{ comment.author.full_name }}</strong>
                        <time>{{ comment.created_at | date_format }}</time>
                        <p>{{ comment.content }}</p>
                    </li>
                {% endfor %}
            </ul>
        {% else %}
            <p>No comments yet.</p>
        {% endif %}

        {% if current_user.is_authenticated %}
            <form method="POST" action="{{ url_for('add_comment', post_id=post.id) }}" class="comment-form">
                <textarea name="content" placeholder="Add a comment..." required></textarea>
                <button type="submit">Post Comment</button>
            </form>
        {% endif %}
    </section>
</article>
{% endblock %}
```

### 3. **Node.js/Express with EJS Templates**

```javascript
// app.js
const express = require('express');
const path = require('path');

const app = express();

// Set template engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, 'public')));

// Local variables middleware
app.use((req, res, next) => {
    res.locals.currentUser = req.user || null;
    res.locals.appName = 'My App';
    res.locals.currentYear = new Date().getFullYear();
    next();
});

// Routes
app.get('/', (req, res) => {
    const posts = [
        { id: 1, title: 'Post 1', excerpt: 'First post', slug: 'post-1' },
        { id: 2, title: 'Post 2', excerpt: 'Second post', slug: 'post-2' }
    ];

    res.render('index', { posts });
});

app.get('/posts/:slug', async (req, res) => {
    const { slug } = req.params;
    const post = await Post.findOne({ where: { slug } });

    if (!post) {
        return res.status(404).render('404');
    }

    const comments = await post.getComments();
    const relatedPosts = await Post.findAll({
        where: { categoryId: post.categoryId },
        limit: 5
    });

    res.render('post', {
        post,
        comments,
        relatedPosts
    });
});

app.get('/dashboard', requireAuth, (req, res) => {
    const stats = {
        totalPosts: req.user.posts.length,
        totalViews: req.user.posts.reduce((sum, p) => sum + p.views, 0)
    };

    res.render('dashboard', { stats });
});

app.listen(3000);
```

### 4. **EJS Template Examples**

```html
<!-- views/layout.ejs -->
<!DOCTYPE html>
<html>
<head>
    <title><%= typeof title != 'undefined' ? title + ' - ' : '' %><%= appName %></title>
    <link rel="stylesheet" href="/css/style.css">
</head>
<body>
    <%- include('partials/navbar') %>

    <main class="container">
        <%- body %>
    </main>

    <%- include('partials/footer') %>

    <script src="/js/main.js"></script>
</body>
</html>

<!-- views/post.ejs -->
<article class="post">
    <h1><%= post.title %></h1>
    <div class="post-meta">
        <span>By <%= post.author.name %></span>
        <span><%= new Date(post.createdAt).toLocaleDateString() %></span>
    </div>

    <div class="post-content">
        <%- post.content %>
    </div>

    <% if (relatedPosts && relatedPosts.length > 0) { %>
        <section class="related-posts">
            <h3>Related Posts</h3>
            <% relatedPosts.forEach(related => { %>
                <div class="post-card">
                    <h4><a href="/posts/<%= related.slug %>"><%= related.title %></a></h4>
                    <p><%= related.excerpt %></p>
                </div>
            <% }); %>
        </section>
    <% } %>

    <section class="comments">
        <h3>Comments (<%= comments.length %>)</h3>

        <% comments.forEach(comment => { %>
            <div class="comment">
                <strong><%= comment.author.name %></strong>
                <time><%= new Date(comment.createdAt).toLocaleDateString() %></time>
                <p><%= comment.content %></p>
            </div>
        <% }); %>

        <% if (currentUser) { %>
            <form method="POST" action="/posts/<%= post.id %>/comments" class="comment-form">
                <textarea name="content" placeholder="Add comment..." required></textarea>
                <button type="submit">Post</button>
            </form>
        <% } %>
    </section>
</article>
```

### 5. **Caching and Performance**

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

### 6. **Django Template Examples**

```python
# views.py
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db.models import Q
from .models import Post, Comment

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        return Post.objects.filter(published=True).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['featured_posts'] = Post.objects.filter(featured=True)[:5]
        return context

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'
    slug_field = 'slug'

    def get_queryset(self):
        return Post.objects.filter(published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['related_posts'] = Post.objects.filter(
            category=self.object.category
        ).exclude(id=self.object.id)[:5]
        return context
```

### 7. **Django Templates**

```html
<!-- blog/post_list.html -->
{% extends "base.html" %}
{% load custom_filters %}

{% block title %}Blog - {{ app_name }}{% endblock %}

{% block content %}
<div class="blog-section">
    <h1>Blog Posts</h1>

    {% if featured_posts %}
        <section class="featured">
            <h2>Featured Posts</h2>
            <div class="posts-grid">
                {% for post in featured_posts %}
                    <article class="post-card">
                        <h3><a href="{% url 'post-detail' post.slug %}">{{ post.title }}</a></h3>
                        <p>{{ post.excerpt }}</p>
                        <a href="{% url 'post-detail' post.slug %}" class="read-more">Read More</a>
                    </article>
                {% endfor %}
            </div>
        </section>
    {% endif %}

    <section class="posts">
        <h2>All Posts</h2>
        {% for post in posts %}
            <article class="post-item">
                <h3><a href="{% url 'post-detail' post.slug %}">{{ post.title }}</a></h3>
                <div class="meta">
                    <span>By {{ post.author.get_full_name }}</span>
                    <span>{{ post.created_at|date:"M d, Y" }}</span>
                </div>
                <p>{{ post.content|truncatewords:50 }}</p>
            </article>
        {% empty %}
            <p>No posts yet.</p>
        {% endfor %}
    </section>

    {% if is_paginated %}
        <nav class="pagination">
            {% if page_obj.has_previous %}
                <a href="?page=1">First</a>
                <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
            {% endif %}

            <span>Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span>

            {% if page_obj.has_next %}
                <a href="?page={{ page_obj.next_page_number }}">Next</a>
                <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
            {% endif %}
        </nav>
    {% endif %}
</div>
{% endblock %}
```

## Best Practices

### ✅ DO
- Use template inheritance for DRY code
- Implement caching for frequently rendered pages
- Use template filters for formatting
- Separate concerns between views and templates
- Validate and sanitize all user input
- Use context processors for global variables
- Implement proper pagination
- Use conditional rendering appropriately
- Cache expensive queries
- Optimize template rendering

### ❌ DON'T
- Put business logic in templates
- Use unbounded loops in templates
- Execute database queries in templates
- Trust user input without sanitization
- Over-nest template inheritance
- Use very long template files
- Render sensitive data in templates
- Ignore template caching opportunities
- Use global variables excessively
- Mix multiple concerns in one template

## Complete Example

```python
@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', name=name)

# hello.html
<h1>Hello, {{ name | capitalize }}!</h1>
```
