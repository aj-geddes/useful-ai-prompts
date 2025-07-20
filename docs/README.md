# Docs/Website Deployment Guide

This directory contains a static website for browsing the Useful AI Prompts library. Named `docs` for easy GitHub Pages deployment.

## Features

- **Browse All Prompts**: View all 65+ prompts in a card layout
- **Search**: Find prompts by title, description, tags, or use cases
- **Filter**: Filter by category or complexity level
- **Categories**: Browse prompts organized by professional domain
- **Responsive**: Works on desktop, tablet, and mobile devices
- **No Backend Required**: Pure static site that reads from PROMPT-INDEX.json

## Local Development

1. **Install a local server** (if you don't have one):
   ```bash
   npm install -g http-server
   ```

2. **Navigate to the repository root**:
   ```bash
   cd useful-ai-prompts
   ```

3. **Start the server**:
   ```bash
   http-server -p 8080
   ```

4. **Open in browser**:
   ```
   http://localhost:8080/docs/
   ```

## Deployment Options

### Option 1: GitHub Pages

1. Enable GitHub Pages in repository settings
2. Set source to main branch, `/docs` folder
3. Access at: `https://[username].github.io/useful-ai-prompts/`

### Option 2: Netlify

1. Connect GitHub repository to Netlify
2. Set build settings:
   - Build command: (leave empty)
   - Publish directory: `docs`
3. Deploy

### Option 3: Vercel

1. Import GitHub repository to Vercel
2. Set root directory to `docs`
3. Deploy

### Option 4: Static Host

Upload the following files to any static host:
- `docs/index.html`
- `docs/styles.css`
- `docs/app.js`
- `PROMPT-INDEX.json` (in root)

## File Structure

```
docs/
├── index.html     # Main HTML structure
├── styles.css     # All styling
├── app.js         # JavaScript functionality
└── README.md      # This file

../PROMPT-INDEX.json  # Prompt data (loaded by app.js)
```

## Customization

### Styling
- Edit `styles.css` to change colors, fonts, or layout
- CSS variables are defined at the top for easy theming

### Content
- Update hero text in `index.html`
- Modify category descriptions and icons
- Add new sections as needed

### Functionality
- `app.js` contains all interactive features
- Add new filters or search capabilities
- Integrate with APIs if needed

## Features for AI Agents

The website is designed to be AI-friendly:

1. **Structured Data**: PROMPT-INDEX.json provides machine-readable metadata
2. **Clear Navigation**: Predictable URL patterns for prompts
3. **Semantic HTML**: Properly structured content for parsing
4. **API-Ready**: Can be extended with REST endpoints

## Browser Support

- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers

## Performance

- Lightweight: ~15KB total (excluding prompt data)
- No external dependencies
- Lazy loading for prompt details
- Responsive images and layout

## Future Enhancements

- [ ] Add prompt preview in modal
- [ ] Implement favorites/bookmarks
- [ ] Add copy-to-clipboard for full prompts
- [ ] Create prompt comparison tool
- [ ] Add usage analytics
- [ ] Implement prompt rating system

## Troubleshooting

**Prompts not loading?**
- Check that PROMPT-INDEX.json exists in the parent directory
- Verify no CORS issues (use a local server)
- Check browser console for errors

**Search not working?**
- Ensure JavaScript is enabled
- Check that promptIndex is loaded
- Verify search terms match prompt content

**Styling issues?**
- Clear browser cache
- Check for CSS conflicts
- Verify responsive breakpoints