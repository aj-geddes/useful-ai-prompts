---
layout: default
title: Claude Code Skills Library
description: "259 specialized skills for Claude Code across 20 categories. Focused, actionable guidance for specific technical tasks following Claude Code skills best practices."
---

<div class="skills-page">
    <div class="container">
        <div class="skills-header">
            <h1 class="page-title">Claude Code Skills Library</h1>
            <p class="page-description">
                {{ site.skills.size }} specialized skills designed for Claude Code to handle specific technical tasks. Each skill follows <a href="https://docs.anthropic.com/en/docs/claude-code/skills" target="_blank">Claude Code Skills best practices</a> with focused scope, clear instructions, and actionable examples.
            </p>
            <div class="search-stats">
                <div class="search-stat">
                    <span class="stat-number">{{ site.skills.size }}</span>
                    <span class="stat-label">Specialized Skills</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">20</span>
                    <span class="stat-label">Categories</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">100%</span>
                    <span class="stat-label">Production-Ready</span>
                </div>
            </div>
        </div>

        <!-- Search -->
        <div class="skills-search">
            <input type="text" id="skillSearch" class="search-input" placeholder="Search skills... (e.g., 'docker', 'testing', 'api')" autocomplete="off">
        </div>

        <div class="skills-intro">
            <h2>What are Skills?</h2>
            <p>Skills are specialized capabilities for Claude Code that provide focused, step-by-step guidance for specific technical tasks. Unlike broad prompts, skills are:</p>
            <ul>
                <li><strong>Focused:</strong> Each skill addresses one specific capability</li>
                <li><strong>Automatic:</strong> Claude invokes skills autonomously based on your request</li>
                <li><strong>Actionable:</strong> Clear instructions with code examples and best practices</li>
                <li><strong>Project-Ready:</strong> Located in <code>.claude/skills/</code> for team sharing</li>
            </ul>
        </div>

        <!-- All Skills Grid -->
        <div class="all-skills-section">
            <h2>All Skills</h2>

            <div class="skills-grid" id="skillsGrid">
                {% for skill in site.skills | sort: 'title' %}
                <div class="skill-card" data-title="{{ skill.title | downcase }}" data-description="{{ skill.description | downcase }}" data-category="{{ skill.category }}">
                    <div class="skill-card-header">
                        <span class="skill-category-badge">{{ skill.category | replace: '-', ' ' }}</span>
                    </div>
                    <h3 class="skill-name">
                        <a href="{{ skill.url | relative_url }}">{{ skill.title }}</a>
                    </h3>
                    <p class="skill-description">{{ skill.description | truncate: 120 }}</p>
                    <div class="skill-card-footer">
                        <a href="{{ skill.url | relative_url }}" class="skill-link">View Skill →</a>
                    </div>
                </div>
                {% endfor %}
            </div>

            <div class="no-results" id="noResults" style="display: none;">
                <i class="fas fa-search"></i>
                <p>No skills found. Try a different search term.</p>
            </div>
        </div>

        <div class="skills-usage">
            <h2>How to Use Skills</h2>

            <div class="usage-steps">
                <div class="usage-step">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Copy to Your Project</h3>
                        <p>Copy the <code>skills/</code> directory to <code>.claude/skills/</code> in your project root to make skills available to your team.</p>
                        <pre><code>cp -r skills/ /path/to/your/project/.claude/skills/</code></pre>
                    </div>
                </div>

                <div class="usage-step">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Claude Auto-Discovery</h3>
                        <p>Claude Code automatically discovers and invokes skills based on your requests. Just describe what you need naturally.</p>
                        <div class="example-request">
                            <strong>You:</strong> "Help me refactor this legacy code to use modern patterns"
                            <br>
                            <strong>Claude:</strong> <em>(Automatically invokes refactor-legacy-code skill)</em>
                        </div>
                    </div>
                </div>

                <div class="usage-step">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Follow Skill Guidance</h3>
                        <p>Each skill provides step-by-step instructions, code examples, best practices, and testing strategies specific to the task.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="skills-cta">
            <h2>Create Your Own Skills</h2>
            <p>Have a specialized workflow? Create custom skills for your team following the <a href="https://docs.anthropic.com/en/docs/claude-code/skills" target="_blank">Claude Code Skills specification</a>.</p>
            <pre><code>.claude/skills/your-skill-name/

└── SKILL.md # YAML frontmatter + instructions</code></pre>
</div>
</div>

</div>

<style>
.skills-page {
    padding: 2rem 0;
}

.skills-header {
    text-align: center;
    margin-bottom: 2rem;
}

.page-title {
    font-size: 2.5rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.page-description {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 800px;
    margin: 0 auto 2rem;
    line-height: 1.6;
}

.search-stats {
    display: flex;
    justify-content: center;
    gap: 3rem;
    flex-wrap: wrap;
}

.search-stat {
    text-align: center;
}

.stat-number {
    font-size: 2rem;
    font-weight: bold;
    color: var(--accent-primary);
    display: block;
}

.stat-label {
    font-size: 0.875rem;
    color: var(--text-secondary);
}

.skills-search {
    max-width: 600px;
    margin: 0 auto 2rem;
}

.search-input {
    width: 100%;
    padding: 1rem 1.5rem;
    border: 2px solid var(--border-primary);
    border-radius: 8px;
    font-size: 1rem;
    background: var(--bg-secondary);
    color: var(--text-primary);
    transition: border-color 0.2s;
}

.search-input:focus {
    outline: none;
    border-color: var(--accent-primary);
}

.skills-intro {
    background: var(--bg-secondary);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 3rem;
    border-left: 4px solid var(--accent-primary);
}

.skills-intro h2 {
    margin-top: 0;
    color: var(--text-primary);
}

.skills-intro ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.skills-intro li {
    padding: 0.5rem 0;
    padding-left: 1.5rem;
    position: relative;
}

.skills-intro li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: var(--accent-primary);
    font-weight: bold;
}

.all-skills-section {
    margin-bottom: 3rem;
}

.all-skills-section h2 {
    margin-bottom: 1.5rem;
    color: var(--text-primary);
}

.skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 1.5rem;
}

.skill-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
}

.skill-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--card-shadow);
    border-color: var(--accent-primary);
}

.skill-card-header {
    margin-bottom: 0.75rem;
}

.skill-category-badge {
    font-size: 0.75rem;
    background: var(--hover-overlay);
    color: var(--accent-primary);
    padding: 0.25rem 0.625rem;
    border-radius: 4px;
    text-transform: capitalize;
}

.skill-name {
    margin: 0 0 0.75rem;
    font-size: 1.125rem;
}

.skill-name a {
    color: var(--text-primary);
    text-decoration: none;
}

.skill-name a:hover {
    color: var(--accent-primary);
}

.skill-description {
    color: var(--text-secondary);
    font-size: 0.875rem;
    line-height: 1.5;
    margin-bottom: 1rem;
}

.skill-card-footer {
    padding-top: 1rem;
    border-top: 1px solid var(--border-primary);
}

.skill-link {
    color: var(--accent-primary);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.875rem;
}

.skill-link:hover {
    text-decoration: underline;
}

.no-results {
    text-align: center;
    padding: 3rem;
    color: var(--text-secondary);
}

.no-results i {
    font-size: 3rem;
    margin-bottom: 1rem;
    opacity: 0.5;
}

.skills-usage {
    margin-bottom: 3rem;
}

.skills-usage h2 {
    text-align: center;
    margin-bottom: 2rem;
    color: var(--text-primary);
}

.usage-steps {
    display: grid;
    gap: 1.5rem;
}

.usage-step {
    display: flex;
    gap: 1.5rem;
    background: var(--bg-secondary);
    padding: 1.5rem;
    border-radius: 12px;
    border: 1px solid var(--border-primary);
}

.step-number {
    flex-shrink: 0;
    width: 48px;
    height: 48px;
    background: var(--accent-primary);
    color: white;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    font-weight: bold;
}

.step-content {
    flex: 1;
}

.step-content h3 {
    margin-top: 0;
    color: var(--text-primary);
}

.step-content pre {
    background: var(--hover-overlay);
    padding: 1rem;
    border-radius: 8px;
    overflow-x: auto;
    margin: 1rem 0 0;
}

.step-content code {
    font-family: 'Monaco', 'Courier New', monospace;
    font-size: 0.875rem;
}

.example-request {
    background: var(--hover-overlay);
    padding: 1rem;
    border-radius: 8px;
    border-left: 3px solid var(--accent-primary);
    font-size: 0.9em;
    line-height: 1.6;
}

.skills-cta {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary, #667eea));
    color: white;
    padding: 3rem;
    border-radius: 16px;
    text-align: center;
}

.skills-cta h2 {
    margin-top: 0;
    color: white;
}

.skills-cta a {
    color: white;
    text-decoration: underline;
}

.skills-cta pre {
    background: rgba(0, 0, 0, 0.2);
    padding: 1rem;
    border-radius: 8px;
    display: inline-block;
    text-align: left;
    margin: 1rem 0;
}

.skills-cta code {
    color: white;
    font-family: 'Monaco', 'Courier New', monospace;
}

@media (max-width: 768px) {
    .usage-step {
        flex-direction: column;
        gap: 1rem;
    }

    .skills-grid {
        grid-template-columns: 1fr;
    }
}
</style>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('skillSearch');
    const skillsGrid = document.getElementById('skillsGrid');
    const noResults = document.getElementById('noResults');
    const skills = document.querySelectorAll('.skill-card');

    if (searchInput) {
        searchInput.addEventListener('input', function() {
            const query = this.value.toLowerCase();
            let visibleCount = 0;

            skills.forEach(skill => {
                const title = skill.dataset.title || '';
                const description = skill.dataset.description || '';
                const category = skill.dataset.category || '';

                const matches = !query ||
                    title.includes(query) ||
                    description.includes(query) ||
                    category.includes(query);

                if (matches) {
                    skill.style.display = 'block';
                    visibleCount++;
                } else {
                    skill.style.display = 'none';
                }
            });

            noResults.style.display = visibleCount === 0 ? 'block' : 'none';
            skillsGrid.style.display = visibleCount === 0 ? 'none' : 'grid';
        });
    }
});
</script>
