# Jinja2 Template Examples

## Jinja2 Template Examples

```html
<!-- base.html -->
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>{% block title %}{{ app_name }}{% endblock %}</title>
    <link
      rel="stylesheet"
      href="{{ url_for('static', filename='css/style.css') }}"
    />
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
      {% with messages = get_flashed_messages(with_categories=true) %} {% if
      messages %} {% for category, message in messages %}
      <div class="alert alert-{{ category }}">{{ message }}</div>
      {% endfor %} {% endif %} {% endwith %} {% block content %}{% endblock %}
    </main>

    <footer>
      <p>&copy; {{ current_year }} {{ app_name }}. All rights reserved.</p>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block extra_scripts %}{% endblock %}
  </body>
</html>

<!-- dashboard.html -->
{% extends "base.html" %} {% block title %}Dashboard - {{ app_name }}{% endblock
%} {% block content %}
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
{% extends "base.html" %} {% block title %}{{ post.title }} - {{ app_name }}{%
endblock %} {% block content %}
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

  <div class="post-content">{{ post.content | safe }}</div>

  {% if related_posts %}
  <section class="related-posts">
    <h3>Related Posts</h3>
    <div class="posts-grid">
      {% for related in related_posts %}
      <div class="post-card">
        <h4>
          <a href="{{ url_for('view_post', slug=related.slug) }}"
            >{{ related.title }}</a
          >
        </h4>
        <p>{{ related.excerpt or related.content[:100] }}...</p>
        <a
          href="{{ url_for('view_post', slug=related.slug) }}"
          class="read-more"
          >Read More</a
        >
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
    {% endif %} {% if current_user.is_authenticated %}
    <form
      method="POST"
      action="{{ url_for('add_comment', post_id=post.id) }}"
      class="comment-form"
    >
      <textarea
        name="content"
        placeholder="Add a comment..."
        required
      ></textarea>
      <button type="submit">Post Comment</button>
    </form>
    {% endif %}
  </section>
</article>
{% endblock %}
```
