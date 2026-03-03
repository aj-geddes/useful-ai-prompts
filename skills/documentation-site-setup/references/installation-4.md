# Installation

## Installation

```bash
# Create new Docusaurus site
npx create-docusaurus@latest my-docs classic

cd my-docs

# Install dependencies
npm install

# Start development server
npm start
```


## Project Structure

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


## Configuration

```javascript
// docusaurus.config.js
module.exports = {
  title: "My Documentation",
  tagline: "Comprehensive documentation for developers",
  url: "https://docs.example.com",
  baseUrl: "/",
  onBrokenLinks: "throw",
  onBrokenMarkdownLinks: "warn",
  favicon: "img/favicon.ico",
  organizationName: "myorg",
  projectName: "my-docs",

  presets: [
    [
      "classic",
      {
        docs: {
          sidebarPath: require.resolve("./sidebars.js"),
          editUrl: "https://github.com/myorg/my-docs/tree/main/",
          showLastUpdateTime: true,
          showLastUpdateAuthor: true,
        },
        blog: {
          showReadingTime: true,
          editUrl: "https://github.com/myorg/my-docs/tree/main/",
        },
        theme: {
          customCss: require.resolve("./src/css/custom.css"),
        },
      },
    ],
  ],

  themeConfig: {
    navbar: {
      title: "My Docs",
      logo: {
        alt: "Logo",
        src: "img/logo.svg",
      },
      items: [
        {
          type: "doc",
          docId: "intro",
          position: "left",
          label: "Docs",
        },
        {
          to: "/blog",
          label: "Blog",
          position: "left",
        },
        {
          href: "https://github.com/myorg/repo",
          label: "GitHub",
          position: "right",
        },
      ],
    },
    footer: {
      style: "dark",
      links: [
        {
          title: "Docs",
          items: [
            {
              label: "Getting Started",
              to: "/docs/intro",
            },
            {
              label: "API Reference",
              to: "/docs/api/reference",
            },
          ],
        },
        {
          title: "Community",
          items: [
            {
              label: "Discord",
              href: "https://discord.gg/example",
            },
            {
              label: "Twitter",
              href: "https://twitter.com/example",
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} My Company.`,
    },
    prism: {
      theme: require("prism-react-renderer/themes/github"),
      darkTheme: require("prism-react-renderer/themes/dracula"),
      additionalLanguages: ["bash", "diff", "json"],
    },
    algolia: {
      appId: "YOUR_APP_ID",
      apiKey: "YOUR_SEARCH_API_KEY",
      indexName: "YOUR_INDEX_NAME",
    },
  },
};
```


## Table of Contents

```markdown
# Summary

- [Introduction](README.md)
