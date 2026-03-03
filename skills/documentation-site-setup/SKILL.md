---
name: documentation-site-setup
description: >
  Set up documentation websites using Docusaurus, MkDocs, VitePress, GitBook, or
  static site generators. Use when creating docs sites, setting up documentation
  portals, or building static documentation.
---

# Documentation Site Setup

## Table of Contents

- [Overview](#overview)
- [When to Use](#when-to-use)
- [Quick Start](#quick-start)
- [Reference Guides](#reference-guides)
- [Best Practices](#best-practices)

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

## Quick Start

- Multi-version documentation

```bash
# Create new Docusaurus site
npx create-docusaurus@latest my-docs classic

cd my-docs

# Install dependencies
npm install

# Start development server
npm start
```

## Reference Guides

Detailed implementations in the `references/` directory:

| Guide | Contents |
|---|---|
| [Installation](references/installation.md) | Installation, Project Structure |
| [Configuration](references/configuration.md) | Configuration |
| [Sidebar Configuration](references/sidebar-configuration.md) | Sidebar Configuration |
| [Versioning](references/versioning.md) | Versioning, Deployment |
| [Installation](references/installation-2.md) | Installation, Project Structure |
| [Configuration](references/configuration-2.md) | Configuration |
| [Admonitions](references/admonitions.md) | Admonitions, Deployment |
| [Installation](references/installation-3.md) | Installation |
| [Configuration](references/configuration-3.md) | Configuration |
| [Installation](references/installation-4.md) | Installation, Project Structure, Configuration, Table of Contents |

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
