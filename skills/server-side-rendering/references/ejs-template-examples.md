# EJS Template Examples

## EJS Template Examples

```html
<!-- views/layout.ejs -->
<!DOCTYPE html>
<html>
  <head>
    <title>
      <%= typeof title != 'undefined' ? title + ' - ' : '' %><%= appName %>
    </title>
    <link rel="stylesheet" href="/css/style.css" />
  </head>
  <body>
    <%- include('partials/navbar') %>

    <main class="container"><%- body %></main>

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

  <div class="post-content"><%- post.content %></div>

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
    <% }); %> <% if (currentUser) { %>
    <form
      method="POST"
      action="/posts/<%= post.id %>/comments"
      class="comment-form"
    >
      <textarea name="content" placeholder="Add comment..." required></textarea>
      <button type="submit">Post</button>
    </form>
    <% } %>
  </section>
</article>
```
