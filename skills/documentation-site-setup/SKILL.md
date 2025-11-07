---
name: documentation-site-setup
description: Set up documentation websites using Docusaurus, MkDocs, VitePress, GitBook, or static site generators. Use when creating docs sites, setting up documentation portals, or building static documentation.
---

# Documentation Site Setup

## Overview

Set up professional documentation websites using popular static site generators like Docusaurus, MkDocs, VitePress, and GitBook.

## When to Use

- Documentation website setup
- API documentation portals
- Product documentation sites
- Technical documentation hubs
- Static site generation
- GitHub Pages deployment
- Multi-version documentation

## Docusaurus Setup

### Installation

```bash
# Create new Docusaurus site
npx create-docusaurus@latest my-docs classic

cd my-docs

# Install dependencies
npm install

# Start development server
npm start
```

### Project Structure

```
my-docs/
├── docs/                    # Documentation pages
│   ├── intro.md
│   ├── tutorial/
│   │   ├── basics.md
│   │   └── advanced.md
│   └── api/
│       └── reference.md
├── blog/                    # Blog posts (optional)
│   ├── 2025-01-15-post.md
│   └── authors.yml
├── src/
│   ├── components/          # React components
│   ├── css/                 # Custom CSS
│   └── pages/               # Custom pages
│       ├── index.js         # Homepage
│       └── about.md
├── static/                  # Static assets
│   └── img/
├── docusaurus.config.js     # Site configuration
├── sidebars.js              # Sidebar configuration
└── package.json
```

### Configuration

```javascript
// docusaurus.config.js
module.exports = {
  title: 'My Documentation',
  tagline: 'Comprehensive documentation for developers',
  url: 'https://docs.example.com',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'myorg',
  projectName: 'my-docs',

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: 'https://github.com/myorg/my-docs/tree/main/',
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
        },
        blog: {
          showReadingTime: true,
          editUrl: 'https://github.com/myorg/my-docs/tree/main/',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: 'My Docs',
      logo: {
        alt: 'Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'intro',
          position: 'left',
          label: 'Docs',
        },
        {
          to: '/blog',
          label: 'Blog',
          position: 'left'
        },
        {
          href: 'https://github.com/myorg/repo',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Getting Started',
              to: '/docs/intro',
            },
            {
              label: 'API Reference',
              to: '/docs/api/reference',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Discord',
              href: 'https://discord.gg/example',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/example',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Company.`,
    },
    prism: {
      theme: require('prism-react-renderer/themes/github'),
      darkTheme: require('prism-react-renderer/themes/dracula'),
      additionalLanguages: ['bash', 'diff', 'json'],
    },
    algolia: {
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
    },
  },
};
```

### Sidebar Configuration

```javascript
// sidebars.js
module.exports = {
  docs: [
    'intro',
    {
      type: 'category',
      label: 'Getting Started',
      items: [
        'getting-started/installation',
        'getting-started/quick-start',
        'getting-started/configuration',
      ],
    },
    {
      type: 'category',
      label: 'Guides',
      items: [
        'guides/authentication',
        'guides/database',
        'guides/deployment',
      ],
    },
    {
      type: 'category',
      label: 'API Reference',
      items: [
        'api/overview',
        'api/endpoints',
        'api/errors',
      ],
    },
  ],
};
```

### Versioning

```bash
# Create version 1.0
npm run docusaurus docs:version 1.0

# Files created:
# - versioned_docs/version-1.0/
# - versioned_sidebars/version-1.0-sidebars.json
# - versions.json
```

### Deployment

```bash
# Build for production
npm run build

# Deploy to GitHub Pages
GIT_USER=<username> npm run deploy
```

---

## MkDocs Setup

### Installation

```bash
# Install MkDocs
pip install mkdocs

# Install Material theme
pip install mkdocs-material

# Create new project
mkdocs new my-docs
cd my-docs

# Start development server
mkdocs serve
```

### Project Structure

```
my-docs/
├── docs/
│   ├── index.md
│   ├── getting-started.md
│   ├── api/
│   │   └── reference.md
│   └── guides/
│       └── tutorial.md
├── mkdocs.yml
└── requirements.txt
```

### Configuration

```yaml
# mkdocs.yml
site_name: My Documentation
site_url: https://docs.example.com
site_description: Comprehensive documentation
site_author: Your Name

repo_name: myorg/repo
repo_url: https://github.com/myorg/repo
edit_uri: edit/main/docs/

theme:
  name: material
  palette:
    # Light mode
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    # Dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.instant
    - navigation.tracking
    - navigation.tabs
    - navigation.sections
    - navigation.expand
    - navigation.top
    - search.suggest
    - search.highlight
    - content.code.annotate
    - content.tabs.link

plugins:
  - search
  - minify:
      minify_html: true

markdown_extensions:
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - pymdownx.superfences:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:pymdownx.superfences.fence_code_format
  - pymdownx.tabbed:
      alternate_style: true
  - admonition
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:materialx.emoji.twemoji
      emoji_generator: !!python/name:materialx.emoji.to_svg
  - attr_list
  - md_in_html

nav:
  - Home: index.md
  - Getting Started:
    - Installation: getting-started/installation.md
    - Quick Start: getting-started/quick-start.md
  - Guides:
    - Tutorial: guides/tutorial.md
    - Best Practices: guides/best-practices.md
  - API Reference:
    - Overview: api/overview.md
    - Endpoints: api/reference.md

extra:
  social:
    - icon: fontawesome/brands/github
      link: https://github.com/myorg
    - icon: fontawesome/brands/twitter
      link: https://twitter.com/myorg
  version:
    provider: mike
```

### Admonitions

```markdown
!!! note
    This is a note

!!! tip
    This is a tip

!!! warning
    This is a warning

!!! danger
    This is dangerous

!!! info "Custom Title"
    Custom admonition with title
```

### Deployment

```bash
# Build site
mkdocs build

# Deploy to GitHub Pages
mkdocs gh-deploy
```

---

## VitePress Setup

### Installation

```bash
# Create project
mkdir my-docs
cd my-docs

# Initialize
npm init -y
npm install -D vitepress

# Create docs
mkdir docs
echo '# Hello VitePress' > docs/index.md

# Add scripts to package.json
```

```json
{
  "scripts": {
    "docs:dev": "vitepress dev docs",
    "docs:build": "vitepress build docs",
    "docs:preview": "vitepress preview docs"
  }
}
```

### Configuration

```javascript
// docs/.vitepress/config.js
export default {
  title: 'My Documentation',
  description: 'Comprehensive documentation',
  themeConfig: {
    nav: [
      { text: 'Guide', link: '/guide/' },
      { text: 'API', link: '/api/' },
      { text: 'GitHub', link: 'https://github.com/myorg/repo' }
    ],
    sidebar: {
      '/guide/': [
        {
          text: 'Getting Started',
          items: [
            { text: 'Introduction', link: '/guide/' },
            { text: 'Installation', link: '/guide/installation' },
            { text: 'Quick Start', link: '/guide/quick-start' }
          ]
        },
        {
          text: 'Advanced',
          items: [
            { text: 'Configuration', link: '/guide/configuration' },
            { text: 'Deployment', link: '/guide/deployment' }
          ]
        }
      ],
      '/api/': [
        {
          text: 'API Reference',
          items: [
            { text: 'Overview', link: '/api/' },
            { text: 'Endpoints', link: '/api/endpoints' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/myorg/repo' }
    ],
    editLink: {
      pattern: 'https://github.com/myorg/repo/edit/main/docs/:path',
      text: 'Edit this page on GitHub'
    },
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2025-present My Company'
    },
    search: {
      provider: 'local'
    }
  }
}
```

---

## GitBook Setup

### Installation

```bash
# Install GitBook CLI
npm install -g gitbook-cli

# Initialize book
gitbook init

# Start development server
gitbook serve
```

### Project Structure

```
my-docs/
├── README.md        # Introduction
├── SUMMARY.md       # Table of contents
├── book.json        # Configuration
└── chapters/
    ├── chapter1.md
    └── chapter2.md
```

### Configuration

```json
{
  "title": "My Documentation",
  "description": "Comprehensive documentation",
  "author": "Your Name",
  "language": "en",
  "gitbook": "3.2.3",
  "plugins": [
    "search",
    "prism",
    "-highlight",
    "github",
    "edit-link",
    "versions"
  ],
  "pluginsConfig": {
    "github": {
      "url": "https://github.com/myorg/repo"
    },
    "edit-link": {
      "base": "https://github.com/myorg/repo/edit/main",
      "label": "Edit This Page"
    }
  }
}
```

### Table of Contents

```markdown
# Summary

* [Introduction](README.md)

## Getting Started
* [Installation](chapters/installation.md)
* [Quick Start](chapters/quick-start.md)

## Guides
* [Tutorial](chapters/tutorial.md)
* [Best Practices](chapters/best-practices.md)

## API Reference
* [Overview](chapters/api-overview.md)
* [Endpoints](chapters/api-endpoints.md)
```

---

## GitHub Pages Deployment

### Workflow

```yaml
# .github/workflows/deploy-docs.yml
name: Deploy Documentation

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: 18

      - name: Install dependencies
        run: npm ci

      - name: Build documentation
        run: npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./build
```

---

## Custom Domain Setup

### DNS Configuration

```
# Add CNAME record
docs.example.com -> username.github.io
```

### GitHub Pages Settings

1. Go to repository Settings > Pages
2. Set source to `gh-pages` branch
3. Add custom domain: `docs.example.com`
4. Enable "Enforce HTTPS"

---

## Search Integration

### Algolia DocSearch

```javascript
// docusaurus.config.js
module.exports = {
  themeConfig: {
    algolia: {
      appId: 'YOUR_APP_ID',
      apiKey: 'YOUR_SEARCH_API_KEY',
      indexName: 'YOUR_INDEX_NAME',
      contextualSearch: true,
      searchParameters: {},
      searchPagePath: 'search',
    },
  },
};
```

### Local Search

```bash
# MkDocs
pip install mkdocs-material[search]

# VitePress (built-in)
# No additional setup needed
```

---

## Best Practices

### ✅ DO
- Use consistent navigation structure
- Enable search functionality
- Add edit links to pages
- Include version selector for versioned docs
- Use syntax highlighting for code blocks
- Add dark mode support
- Optimize images and assets
- Enable analytics
- Add social media links
- Use responsive design
- Include breadcrumbs
- Add table of contents
- Test on mobile devices

### ❌ DON'T
- Use outdated frameworks
- Skip search functionality
- Forget mobile responsiveness
- Use slow-loading assets
- Skip accessibility features
- Ignore SEO optimization

## Resources

- [Docusaurus](https://docusaurus.io/)
- [MkDocs](https://www.mkdocs.org/)
- [MkDocs Material](https://squidfunk.github.io/mkdocs-material/)
- [VitePress](https://vitepress.dev/)
- [GitBook](https://www.gitbook.com/)
- [GitHub Pages](https://pages.github.com/)
- [Algolia DocSearch](https://docsearch.algolia.com/)
