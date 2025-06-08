# Repository Documentation Generator

Generate comprehensive, enterprise-grade README documentation for any GitHub repository with professional subfolder organization and root overview.

## User Input Required

**Repository URL**: Provide GitHub repository URL in format `https://github.com/owner/repo`

## Execution Workflow

### Phase 1: Repository Setup & Analysis

**Initial Setup**
```
1. Extract owner/repo from URL
2. Check list_allowed_directories for workspace boundaries  
3. Use lc-project-context(repo_path, "lc-code") for comprehensive overview
4. Use directory_tree(repo_path) for structure analysis
5. Use git_status(repo_path) to understand current git state
```

**Content Analysis**
```
1. Identify all subfolders containing substantial content
2. Use read_multiple_files to analyze folder contents systematically
3. Categorize folders by purpose: development, security, infrastructure, etc.
4. Update memory with add_observations for project context
```

### Phase 2: Content Categorization & Analysis

**Folder Classification Logic**
- **Development**: Code, frameworks, CI/CD, automation, MCP tools
- **Security**: Vulnerability analysis, compliance, security patterns
- **Infrastructure**: Terraform, Docker, cloud deployment, IaC
- **AI/Prompt Engineering**: AI techniques, memory management, prompting
- **Project Management**: Repository automation, workflows, collaboration
- **Research**: Learning frameworks, decision records, methodologies
- **Configuration**: Setup guides, configuration templates

**Content Analysis per Category**
```
For each identified category:
1. Read all files using read_multiple_files([file_paths])
2. Identify key features, technologies, and use cases
3. Determine target audiences and benefits
4. Note integration patterns and related categories
```

### Phase 3: README Generation

**Category README Template**
```markdown
# {emoji} {Category Name}

{2-3 line description of category purpose and scope}

## 📂 Contents

### {Subcategory}
- **[File Name](file-path.md)** - Brief description with key technologies/features

## 🎯 Key Features
- **Feature 1**: Description
- **Feature 2**: Description  
- **Feature 3**: Description

## 🚀 Use Cases

### For {Role 1}
- **Use case**: Description
- **Benefit**: Value proposition

### For {Role 2}  
- **Use case**: Description
- **Benefit**: Value proposition

## 🏆 Benefits
- **Benefit 1**: Value description
- **Benefit 2**: Value description

## 🏷️ Tags
`tag1` `tag2` `tag3` `technology` `category`

## 🔗 Related Categories
- **[Category](../category/)**: Integration description

---
*Professional description emphasizing enterprise readiness and production use*
```

**Root README Template**
```markdown
# {emoji} {Project Name}

{Enterprise-focused description emphasizing production-ready solutions}

## 🌟 Project Overview
{2-3 sentences describing scope, categories, and enterprise focus}

## 📚 Repository Categories

### {emoji} [Category](category/)
{Purpose description}
- **[Key File](category/file.md)** - Feature description

## 🎯 Key Features
### {Feature Group}
- **Feature**: Description with enterprise focus

## 🚀 Quick Start Guide
1. **Choose Category**: Navigation guidance
2. **Select Content**: Selection criteria  
3. **Implement**: Usage instructions

## 🎯 Use Case Matrix
| Role | Cat1 | Cat2 | Cat3 |
|------|------|------|------|
| **Role 1** | ✅ Features | ✅ Benefits | ✅ Tools |

## 🏷️ Technology Coverage
**Category**: `tech1` `tech2` `tech3`

## 🤝 Contributing
{Link to contributing guidelines}

## 📄 License  
{License information}

---
{Professional closing emphasizing community and enterprise value}
```

### Phase 4: Git Operations & Deployment

**File Creation Workflow**
```
1. Create category READMEs using write_file(path, content)
2. Create/update root README using write_file("README.md", content)  
3. Validate all files created successfully
```

**Git Workflow**
```
1. git_status(repo_path) - verify clean state
2. git_add(repo_path, [list_of_readme_files])
3. git_commit(repo_path, "📚 Add comprehensive README documentation\n\n{detailed_description}")
4. Use GitHub MCP tools if available for push, or guide user to push manually
```

**Commit Message Template**
```
📚 Add comprehensive README documentation for all categories

- Created professional README.md for {N} categories: {list}
- Updated root README with enterprise-grade project overview  
- Added use case matrices and technology coverage
- Included professional standards and navigation

Features:
- Enterprise-focused descriptions and value propositions
- Role-based use case guidance and integration patterns
- Comprehensive technology coverage and best practices
- Professional formatting with consistent structure throughout
```

## Quality Standards

**Professional Requirements**
- Enterprise-grade tone and presentation
- Consistent emoji usage and formatting
- Clear value propositions for different user roles
- Technology integration guidance
- Cross-category navigation and relationships

**Content Standards**
- 2-3 sentence descriptions (concise but informative)
- Role-based use case organization
- Technology tags for discoverability  
- Professional benefits focus
- Enterprise adoption readiness

**Technical Standards**
- Consistent markdown formatting
- Working relative links between categories
- Professional emoji usage (not excessive)
- Table formatting for matrices
- Code block formatting for technical content

## Error Handling

**Common Issues & Solutions**
- **Git conflicts**: Use git_status first, resolve systematically
- **Large repositories**: Use lc-project-context with appropriate rules
- **Missing content**: Use search_files to locate relevant files
- **File read errors**: Handle with read_multiple_files error checking
- **Category overlap**: Prioritize primary purpose, note in related sections

**Validation Checkpoints**
- Verify all subfolders have appropriate READMEs
- Check root README includes all categories
- Validate all internal links work properly
- Confirm git operations complete successfully
- Test professional presentation standards

**Memory Management**
- Update add_observations throughout process
- Track category analysis and decisions
- Store successful patterns for future use
- Document any repository-specific insights

## Success Criteria

✅ **Complete Documentation**: README for every significant subfolder  
✅ **Professional Presentation**: Enterprise-grade formatting and content  
✅ **Clear Navigation**: Easy discovery and cross-category linking  
✅ **Role-Based Guidance**: Use cases for different user types  
✅ **Technology Integration**: Clear technology coverage and relationships  
✅ **Git Integration**: Clean commit history with descriptive messages  
✅ **Scalable Structure**: Patterns that work for repositories of any size