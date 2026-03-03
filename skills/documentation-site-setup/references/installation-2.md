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
