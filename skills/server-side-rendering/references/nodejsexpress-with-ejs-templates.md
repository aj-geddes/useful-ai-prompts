# Node.js/Express with EJS Templates

## Node.js/Express with EJS Templates

```javascript
// app.js
const express = require("express");
const path = require("path");

const app = express();

// Set template engine
app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));

// Middleware
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, "public")));

// Local variables middleware
app.use((req, res, next) => {
  res.locals.currentUser = req.user || null;
  res.locals.appName = "My App";
  res.locals.currentYear = new Date().getFullYear();
  next();
});

// Routes
app.get("/", (req, res) => {
  const posts = [
    { id: 1, title: "Post 1", excerpt: "First post", slug: "post-1" },
    { id: 2, title: "Post 2", excerpt: "Second post", slug: "post-2" },
  ];

  res.render("index", { posts });
});

app.get("/posts/:slug", async (req, res) => {
  const { slug } = req.params;
  const post = await Post.findOne({ where: { slug } });

  if (!post) {
    return res.status(404).render("404");
  }

  const comments = await post.getComments();
  const relatedPosts = await Post.findAll({
    where: { categoryId: post.categoryId },
    limit: 5,
  });

  res.render("post", {
    post,
    comments,
    relatedPosts,
  });
});

app.get("/dashboard", requireAuth, (req, res) => {
  const stats = {
    totalPosts: req.user.posts.length,
    totalViews: req.user.posts.reduce((sum, p) => sum + p.views, 0),
  };

  res.render("dashboard", { stats });
});

app.listen(3000);
```
