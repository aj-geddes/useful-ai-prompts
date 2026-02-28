---
layout: default
title: Claude Code Hooks Library
description: "7 production-ready hooks for automated validation, testing, formatting, and security. Integrate quality control into your Claude Code workflow."
---

<div class="hooks-page">
    <div class="container">
        <div class="hooks-header">
            <h1 class="page-title">Claude Code Hooks Library</h1>
            <p class="page-description">
                {{ site.hooks.size }} production-ready hooks for automated quality control, security scanning, testing, and environment setup. Execute custom automation at key points in your Claude Code workflow following <a href="https://docs.anthropic.com/en/docs/claude-code/hooks" target="_blank">official hooks specifications</a>.
            </p>
            <div class="search-stats">
                <div class="search-stat">
                    <span class="stat-number">{{ site.hooks.size }}</span>
                    <span class="stat-label">Production Hooks</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">3,000+</span>
                    <span class="stat-label">Lines of Code</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">100%</span>
                    <span class="stat-label">Ready to Use</span>
                </div>
            </div>
        </div>

        <div class="hooks-intro">
            <h2>What are Hooks?</h2>
            <p>Hooks are automated scripts that execute at specific events in Claude Code's workflow. They enable:</p>
            <ul>
                <li><strong>Automated Quality Control:</strong> Run linters, tests, and security scans automatically</li>
                <li><strong>Environment Setup:</strong> Initialize development environment on session start</li>
                <li><strong>Code Formatting:</strong> Auto-format code after edits</li>
                <li><strong>Security:</strong> Prevent commits with exposed secrets or vulnerable dependencies</li>
                <li><strong>Breaking Change Detection:</strong> Warn before committing API-breaking changes</li>
            </ul>
        </div>

        <div class="hooks-navigation">
            <h2>Available Hooks</h2>

            <div class="hooks-grid">
                {% for hook in site.hooks | sort: 'title' %}
                <a href="{{ hook.url | relative_url }}" class="hook-card">
                    <div class="hook-icon {{ hook.icon_class | default: 'default' }}">
                        <i class="fas {{ hook.icon | default: 'fa-code' }}"></i>
                    </div>
                    <div class="hook-info">
                        <h3>{{ hook.title }}</h3>
                        <p class="hook-event">{{ hook.event_type }}</p>
                        <p class="hook-description">{{ hook.description | truncate: 100 }}</p>
                        {% if hook.features %}
                        <div class="hook-features">
                            {% for feature in hook.features limit: 3 %}
                            <span class="feature-badge">{{ feature }}</span>
                            {% endfor %}
                        </div>
                        {% endif %}
                        <div class="hook-stats">
                            <span><i class="fas fa-code"></i> {{ hook.lines_of_code }} lines</span>
                            <span><i class="fas fa-language"></i> Bash</span>
                        </div>
                    </div>
                </a>
                {% endfor %}
            </div>
        </div>

        <div class="hooks-usage">
            <h2>How to Use Hooks</h2>

            <div class="usage-steps">
                <div class="usage-step">
                    <div class="step-number">1</div>
                    <div class="step-content">
                        <h3>Copy Hooks to Your Project</h3>
                        <p>Copy the hooks you need to your project's <code>.claude/hooks/</code> directory.</p>
                        <pre><code>cp -r hooks/security-scan /path/to/project/.claude/hooks/

cp -r hooks/test-runner /path/to/project/.claude/hooks/</code></pre>
</div>
</div>

                <div class="usage-step">
                    <div class="step-number">2</div>
                    <div class="step-content">
                        <h3>Configure in Settings</h3>
                        <p>Add hook configuration to <code>.claude/settings.json</code> in your project.</p>
                        <pre><code>{

"hooks": {
"PreToolUse": [{
"matcher": "Bash",
"hooks": [{
"type": "command",
"command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan/hook.sh"
}]
}]
}
}</code></pre>
</div>
</div>

                <div class="usage-step">
                    <div class="step-number">3</div>
                    <div class="step-content">
                        <h3>Make Scripts Executable</h3>
                        <p>Ensure hook scripts have execute permissions.</p>
                        <pre><code>chmod +x .claude/hooks/*/hook.sh</code></pre>
                        <p><strong>That's it!</strong> Hooks will now execute automatically at configured events.</p>
                    </div>
                </div>
            </div>
        </div>

        <div class="hooks-configurations">
            <h2>Recommended Configurations</h2>

            <div class="config-grid">
                <div class="config-card">
                    <h3>Minimal Setup</h3>
                    <p class="config-desc">Security + Testing - Essential quality control</p>
                    <div class="config-includes">
                        <span class="config-hook"><i class="fas fa-shield-alt"></i> security-scan</span>
                        <span class="config-hook"><i class="fas fa-check-circle"></i> test-runner</span>
                        <span class="config-hook"><i class="fas fa-rocket"></i> session-setup</span>
                    </div>
                    <p class="config-ideal">Ideal for: All projects</p>
                </div>

                <div class="config-card">
                    <h3>Full Stack Development</h3>
                    <p class="config-desc">Complete automation suite</p>
                    <div class="config-includes">
                        <span class="config-hook"><i class="fas fa-shield-alt"></i> security-scan</span>
                        <span class="config-hook"><i class="fas fa-check-circle"></i> test-runner</span>
                        <span class="config-hook"><i class="fas fa-box"></i> dependency-check</span>
                        <span class="config-hook"><i class="fas fa-magic"></i> auto-format</span>
                        <span class="config-hook"><i class="fas fa-rocket"></i> session-setup</span>
                    </div>
                    <p class="config-ideal">Ideal for: Large applications</p>
                </div>

                <div class="config-card">
                    <h3>API/Library Development</h3>
                    <p class="config-desc">Breaking change detection + quality</p>
                    <div class="config-includes">
                        <span class="config-hook"><i class="fas fa-exclamation-triangle"></i> breaking-change-detection</span>
                        <span class="config-hook"><i class="fas fa-check-circle"></i> test-runner</span>
                        <span class="config-hook"><i class="fas fa-magic"></i> auto-format</span>
                    </div>
                    <p class="config-ideal">Ideal for: Libraries, APIs, SDKs</p>
                </div>
            </div>
        </div>

        <div class="hooks-resources">
            <h2>Resources</h2>
            <div class="resource-links">
                <a href="https://docs.anthropic.com/en/docs/claude-code/hooks" target="_blank" class="resource-card">
                    <i class="fas fa-external-link-alt"></i>
                    <h3>Official Hooks Documentation</h3>
                    <p>Claude Code's official guide to creating and using hooks</p>
                </a>
                <a href="https://github.com/aj-geddes/useful-ai-prompts" target="_blank" class="resource-card">
                    <i class="fab fa-github"></i>
                    <h3>GitHub Repository</h3>
                    <p>Access the source code, contribute hooks, and stay updated</p>
                </a>
            </div>
        </div>

        <div class="hooks-cta">
            <h2>Start Using Hooks Today</h2>
            <p>Download hooks and integrate quality control into your workflow in minutes.</p>
            <div class="cta-buttons">
                <a href="https://github.com/aj-geddes/useful-ai-prompts/tree/main/hooks" class="btn-primary-large" target="_blank">
                    <i class="fab fa-github"></i> Download Hooks
                </a>
            </div>
        </div>
    </div>

</div>

<style>
.hooks-page {
    padding: 2rem 0;
}

.hooks-header {
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

.hooks-intro {
    background: var(--bg-secondary);
    padding: 2rem;
    border-radius: 12px;
    margin-bottom: 3rem;
    border-left: 4px solid var(--accent-primary);
}

.hooks-intro h2 {
    margin-top: 0;
    color: var(--text-primary);
}

.hooks-intro ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.hooks-intro li {
    padding: 0.5rem 0;
    padding-left: 1.5rem;
    position: relative;
}

.hooks-intro li:before {
    content: "✓";
    position: absolute;
    left: 0;
    color: var(--accent-primary);
    font-weight: bold;
}

.hooks-navigation {
    margin-bottom: 3rem;
}

.hooks-navigation h2 {
    margin-bottom: 1.5rem;
    color: var(--text-primary);
}

/* Hook Cards */
.hooks-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
}

.hook-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    text-decoration: none;
    display: block;
}

.hook-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--card-shadow);
    border-color: var(--accent-primary);
}

.hook-icon {
    width: 56px;
    height: 56px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 1rem;
}

.hook-icon i {
    font-size: 1.75rem;
    color: white;
}

.hook-icon.security { background: linear-gradient(135deg, #ef4444, #dc2626); }
.hook-icon.testing { background: linear-gradient(135deg, #10b981, #059669); }
.hook-icon.setup { background: linear-gradient(135deg, #3b82f6, #2563eb); }
.hook-icon.format { background: linear-gradient(135deg, #8b5cf6, #7c3aed); }
.hook-icon.warning { background: linear-gradient(135deg, #f59e0b, #d97706); }
.hook-icon.dependencies { background: linear-gradient(135deg, #06b6d4, #0891b2); }
.hook-icon.default { background: linear-gradient(135deg, #6b7280, #4b5563); }

.hook-info h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
    font-family: 'Monaco', 'Courier New', monospace;
}

.hook-event {
    font-size: 0.875rem;
    color: var(--accent-primary);
    font-weight: 600;
    margin-bottom: 0.75rem;
}

.hook-description {
    color: var(--text-secondary);
    line-height: 1.5;
    margin-bottom: 1rem;
    font-size: 0.875rem;
}

.hook-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.feature-badge {
    font-size: 0.7rem;
    background: var(--hover-overlay);
    color: var(--accent-primary);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-weight: 500;
}

.hook-stats {
    display: flex;
    gap: 1.5rem;
    font-size: 0.75rem;
    color: var(--text-secondary);
    padding-top: 1rem;
    border-top: 1px solid var(--border-primary);
}

.hook-stats i {
    margin-right: 0.25rem;
}

/* Usage Steps */
.hooks-usage {
    margin-bottom: 3rem;
}

.hooks-usage h2 {
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

/* Configuration Cards */
.hooks-configurations {
    margin-bottom: 3rem;
}

.hooks-configurations h2 {
    text-align: center;
    margin-bottom: 2rem;
    color: var(--text-primary);
}

.config-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
}

.config-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 12px;
    padding: 1.5rem;
}

.config-card h3 {
    font-size: 1.25rem;
    margin-bottom: 0.5rem;
    color: var(--text-primary);
}

.config-desc {
    color: var(--text-secondary);
    margin-bottom: 1rem;
    font-size: 0.875rem;
}

.config-includes {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.config-hook {
    font-size: 0.875rem;
    color: var(--text-primary);
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.config-hook i {
    width: 20px;
    color: var(--accent-primary);
}

.config-ideal {
    font-size: 0.875rem;
    color: var(--accent-primary);
    font-weight: 600;
    padding-top: 0.75rem;
    border-top: 1px solid var(--border-primary);
}

/* Resources */
.hooks-resources {
    margin-bottom: 3rem;
}

.hooks-resources h2 {
    text-align: center;
    margin-bottom: 2rem;
    color: var(--text-primary);
}

.resource-links {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
}

.resource-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 12px;
    padding: 1.5rem;
    text-decoration: none;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
    display: block;
}

.resource-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--card-shadow);
    border-color: var(--accent-primary);
}

.resource-card i {
    font-size: 2rem;
    color: var(--accent-primary);
    margin-bottom: 1rem;
}

.resource-card h3 {
    margin: 0 0 0.5rem;
    color: var(--text-primary);
}

.resource-card p {
    margin: 0;
    color: var(--text-secondary);
    font-size: 0.9rem;
}

/* CTA */
.hooks-cta {
    background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary, #667eea));
    color: white;
    padding: 3rem;
    border-radius: 16px;
    text-align: center;
}

.hooks-cta h2 {
    margin-top: 0;
    color: white;
}

.cta-buttons {
    display: flex;
    justify-content: center;
    gap: 1rem;
    margin-top: 1.5rem;
}

.btn-primary-large {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 1rem 2rem;
    background: white;
    color: var(--accent-primary);
    border-radius: 8px;
    text-decoration: none;
    font-weight: 600;
    transition: transform 0.2s;
}

.btn-primary-large:hover {
    transform: translateY(-2px);
}

/* Responsive */
@media (max-width: 768px) {
    .hooks-grid {
        grid-template-columns: 1fr;
    }

    .config-grid {
        grid-template-columns: 1fr;
    }

    .usage-step {
        flex-direction: column;
        gap: 1rem;
    }
}
</style>
