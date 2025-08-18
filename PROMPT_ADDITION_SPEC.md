# Prompt Addition Specification Process

## Overview
This document defines the complete process for adding new prompt categories and expanding the library to 500+ prompts with full documentation and site integration.

## Target: 383 → 500+ Prompts (117+ new prompts needed)

### New Categories to Add (8 categories × 15-20 prompts each)
1. **personal-productivity** (15-20 prompts)
2. **financial-planning** (15-20 prompts) 
3. **career-development** (15-20 prompts)
4. **health-wellness** (15-20 prompts)
5. **content-creation** (15-20 prompts)
6. **learning-skills** (15-20 prompts)
7. **personal-growth** (15-20 prompts)
8. **relationships-communication** (15-20 prompts)

**Total New Prompts**: 120-160 prompts
**Final Count**: 503-543 prompts

## Complete Process for Each Category

### Phase 1: Create Source Prompts
1. **Create category directory**: `/prompts/{category-name}/`
2. **Create category README.md** with description and prompt list
3. **Create 15-20 individual prompt files** using our interactive format:
   ```
   ---
   category: {category-name}
   compatible_models:
   - claude-3.5-sonnet
   - gpt-4
   - gemini-pro
   date: '2025-08-16'
   description: Professional prompt for {category} optimization and expert consultation
   slug: {prompt-slug}
   tags:
   - {category tag}
   title: {Prompt Title}
   use_cases:
   - {category} optimization
   - professional workflow enhancement
   version: 3.0.0
   ---
   
   # {Prompt Title}
   
   ## Metadata
   - **Category**: {Category}
   - **Tags**: {relevant tags}
   - **Created**: 2025-08-16
   - **Version**: 1.0.0
   - **Compatible Models**: GPT-4, Claude 3, Gemini Pro
   
   ## Description
   {Clear description of what this prompt does}
   
   ## Prompt Template
   
   ```
   I'll help you {specific task}. Let me understand your context:
   
   **{Context Section 1}:**
   1. {Question 1}
   2. {Question 2}
   3. {Question 3}
   
   **{Context Section 2}:**
   4. {Question 4}
   5. {Question 5}
   6. {Question 6}
   
   Based on your answers, I'll provide:
   
   **{DELIVERABLE 1}** - {Description}
   **{DELIVERABLE 2}** - {Description}
   **{DELIVERABLE 3}** - {Description}
   **{DELIVERABLE 4}** - {Description}
   
   Share your {context} and let's {action}!
   ```
   
   ## Example Usage
   
   **User Input:**
   ```
   {Realistic example input}
   ```
   
   **Assistant Output:**
   ```
   {Expected structured output}
   ```
   ```

### Phase 2: Create Jekyll Documentation
4. **Create category page**: `/docs/_categories/{category-name}.md`
   ```
   ---
   category: {category-name}
   slug: {category-name}
   icon: fas fa-{relevant-icon}
   description: "{Category description for SEO and navigation}"
   tags: [{relevant}, {tags}, {for}, {category}]
   ---
   ```

5. **Convert prompts to Jekyll format**: `/docs/_prompts/{prompt-slug}.md`
   - Copy source prompt with proper frontmatter
   - Ensure all metadata is correct
   - Verify file naming follows kebab-case

### Phase 3: Update Site Configuration
6. **Update _config.yml** - Add new categories to site config
7. **Update navigation** - Add categories to main navigation
8. **Update filters** - Add to homepage category filters
9. **Update popular categories** - Include in trending/popular sections

### Phase 4: Update Search and Index
10. **Update PROMPT-INDEX.json** - Add all new prompts with metadata
11. **Update search index** - Regenerate search data
12. **Update category counts** - Update homepage stats

### Phase 5: Testing and Deployment
13. **Test category pages** - Verify all new category pages load
14. **Test prompt pages** - Verify all individual prompts load
15. **Test search** - Verify new prompts appear in search results
16. **Test navigation** - Verify category links work
17. **Deploy to production** - Push to GitHub Pages
18. **Verify live site** - Confirm 500+ prompts visible

## Quality Standards for Each Prompt

### Required Elements
- **Interactive Format**: "I'll help you..." opening
- **Question Structure**: 15-20 numbered questions in logical groups
- **Clear Deliverables**: 4-6 specific output sections promised
- **Example Usage**: Realistic input/output example
- **Proper Metadata**: Category, tags, compatible models, version
- **Minimum Length**: 200+ lines of valuable content

### File Naming Convention
- Use kebab-case: `time-management-optimizer.md`
- Include primary function: `debt-elimination-strategist.md`
- Be specific: `professional-networking-strategist.md` not `networking.md`

### Category Organization
```
prompts/
├── personal-productivity/
│   ├── README.md
│   ├── time-management-optimizer.md
│   ├── productivity-system-designer.md
│   ├── work-life-balance-optimizer.md
│   └── ...
├── financial-planning/
│   ├── README.md
│   ├── personal-budget-optimizer.md
│   ├── debt-elimination-strategist.md
│   └── ...
└── ...
```

## Completion Criteria

### Per Category
- [ ] 15-20 high-quality prompts created
- [ ] Category README.md with description and prompt list
- [ ] All prompts follow interactive format
- [ ] Jekyll category page created
- [ ] All prompts converted to Jekyll format
- [ ] Category added to site navigation
- [ ] Search index updated
- [ ] Category page loads correctly
- [ ] All prompt pages load correctly

### Overall Project
- [ ] 500+ total prompts achieved
- [ ] All 8 new categories fully implemented
- [ ] Site navigation updated
- [ ] Homepage statistics updated
- [ ] Search functionality includes all new prompts
- [ ] Popular categories section updated
- [ ] Live site shows 500+ prompts
- [ ] All category pages accessible without 404s

## Success Metrics
- **Prompt Count**: 500+ prompts (currently 383)
- **Category Coverage**: 8 new high-demand categories
- **Site Functionality**: All pages load, search works, navigation complete
- **User Experience**: Clear organization, easy discovery, working features