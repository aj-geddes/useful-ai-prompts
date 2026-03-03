# Django Templates

## Django Templates

```html
<!-- blog/post_list.html -->
{% extends "base.html" %} {% load custom_filters %} {% block title %}Blog - {{
app_name }}{% endblock %} {% block content %}
<div class="blog-section">
  <h1>Blog Posts</h1>

  {% if featured_posts %}
  <section class="featured">
    <h2>Featured Posts</h2>
    <div class="posts-grid">
      {% for post in featured_posts %}
      <article class="post-card">
        <h3>
          <a href="{% url 'post-detail' post.slug %}">{{ post.title }}</a>
        </h3>
        <p>{{ post.excerpt }}</p>
        <a href="{% url 'post-detail' post.slug %}" class="read-more"
          >Read More</a
        >
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

    <span
      >Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}</span
    >

    {% if page_obj.has_next %}
    <a href="?page={{ page_obj.next_page_number }}">Next</a>
    <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
    {% endif %}
  </nav>
  {% endif %}
</div>
{% endblock %}
```
