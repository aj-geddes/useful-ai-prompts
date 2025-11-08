---
layout: default
title: Claude Code Hooks Library
description: "6 production-ready hooks for automated validation, testing, formatting, and security. Integrate quality control into your Claude Code workflow."
---

<div class="hooks-page">
    <div class="container">
        <div class="hooks-header">
            <h1 class="page-title">Claude Code Hooks Library</h1>
            <p class="page-description">
                6 production-ready hooks for automated quality control, security scanning, testing, and environment setup. Execute custom automation at key points in your Claude Code workflow following <a href="https://code.claude.com/docs/en/hooks" target="_blank">official hooks specifications</a>.
            </p>
            <div class="search-stats">
                <div class="search-stat">
                    <span class="stat-number">6</span>
                    <span class="stat-label">Production Hooks</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">6,135+</span>
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
                <!-- Security Scan -->
                <div class="hook-card">
                    <div class="hook-icon security">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h3>security-scan</h3>
                    <p class="hook-event">PreToolUse (Bash)</p>
                    <p class="hook-description">Scans for exposed secrets, API keys, and sensitive data before commits. Prevents credential leaks with pattern detection.</p>
                    <div class="hook-features">
                        <span class="feature-badge">AWS Keys</span>
                        <span class="feature-badge">API Tokens</span>
                        <span class="feature-badge">Private Keys</span>
                        <span class="feature-badge">15+ Patterns</span>
                    </div>
                    <div class="hook-stats">
                        <span><i class="fas fa-code"></i> 450 lines</span>
                        <span><i class="fas fa-language"></i> Bash</span>
                    </div>
                </div>

                <!-- Test Runner -->
                <div class="hook-card">
                    <div class="hook-icon testing">
                        <i class="fas fa-check-circle"></i>
                    </div>
                    <h3>test-runner</h3>
                    <p class="hook-event">PreToolUse (Bash)</p>
                    <p class="hook-description">Automatically runs tests before commits with smart framework detection. Supports Jest, pytest, RSpec, Go, Rust, and more.</p>
                    <div class="hook-features">
                        <span class="feature-badge">Jest</span>
                        <span class="feature-badge">pytest</span>
                        <span class="feature-badge">RSpec</span>
                        <span class="feature-badge">6+ Frameworks</span>
                    </div>
                    <div class="hook-stats">
                        <span><i class="fas fa-code"></i> 520 lines</span>
                        <span><i class="fas fa-language"></i> Bash</span>
                    </div>
                </div>

                <!-- Session Setup -->
                <div class="hook-card">
                    <div class="hook-icon setup">
                        <i class="fas fa-rocket"></i>
                    </div>
                    <h3>session-setup</h3>
                    <p class="hook-event">SessionStart</p>
                    <p class="hook-description">Initializes development environment on session start. Loads env vars, checks dependencies, verifies connections, displays status.</p>
                    <div class="hook-features">
                        <span class="feature-badge">.env Loading</span>
                        <span class="feature-badge">Dependency Check</span>
                        <span class="feature-badge">DB Verification</span>
                        <span class="feature-badge">Status Dashboard</span>
                    </div>
                    <div class="hook-stats">
                        <span><i class="fas fa-code"></i> 580 lines</span>
                        <span><i class="fas fa-language"></i> Bash</span>
                    </div>
                </div>

                <!-- Auto Format -->
                <div class="hook-card">
                    <div class="hook-icon format">
                        <i class="fas fa-magic"></i>
                    </div>
                    <h3>auto-format</h3>
                    <p class="hook-event">PostToolUse (Edit|Write)</p>
                    <p class="hook-description">Auto-formats code after edits using appropriate formatters. Supports Prettier, Black, RuboCop, gofmt, rustfmt, and more.</p>
                    <div class="hook-features">
                        <span class="feature-badge">Prettier</span>
                        <span class="feature-badge">Black</span>
                        <span class="feature-badge">gofmt</span>
                        <span class="feature-badge">8+ Languages</span>
                    </div>
                    <div class="hook-stats">
                        <span><i class="fas fa-code"></i> 565 lines</span>
                        <span><i class="fas fa-language"></i> Bash</span>
                    </div>
                </div>

                <!-- Breaking Change Detection -->
                <div class="hook-card">
                    <div class="hook-icon warning">
                        <i class="fas fa-exclamation-triangle"></i>
                    </div>
                    <h3>breaking-change-detection</h3>
                    <p class="hook-event">PreToolUse (Bash)</p>
                    <p class="hook-description">Detects breaking API changes before commits. Compares signatures, identifies removed exports, warns about parameter changes.</p>
                    <div class="hook-features">
                        <span class="feature-badge">Signature Comparison</span>
                        <span class="feature-badge">Export Tracking</span>
                        <span class="feature-badge">SemVer Integration</span>
                    </div>
                    <div class="hook-stats">
                        <span><i class="fas fa-code"></i> 540 lines</span>
                        <span><i class="fas fa-language"></i> Bash</span>
                    </div>
                </div>

                <!-- Dependency Check -->
                <div class="hook-card">
                    <div class="hook-icon dependencies">
                        <i class="fas fa-box"></i>
                    </div>
                    <h3>dependency-check</h3>
                    <p class="hook-event">PreToolUse (Bash)</p>
                    <p class="hook-description">Checks for vulnerable dependencies before commits. Runs npm audit, pip-audit, bundle audit with severity-based blocking.</p>
                    <div class="hook-features">
                        <span class="feature-badge">npm audit</span>
                        <span class="feature-badge">pip-audit</span>
                        <span class="feature-badge">bundle audit</span>
                        <span class="feature-badge">5+ Package Managers</span>
                    </div>
                    <div class="hook-stats">
                        <span><i class="fas fa-code"></i> 600 lines</span>
                        <span><i class="fas fa-language"></i> Bash</span>
                    </div>
                </div>
            </div>
        </div>

        <div class="hooks-usage">
            <h2>How to Use Hooks</h2>

            <div class="usage-steps">
                <div class="usage-step">
                    <div class="step-number">1</div>
                    <h3>Copy Hooks to Your Project</h3>
                    <p>Copy the hooks you need to your project's <code>.claude/hooks/</code> directory.</p>
                    <pre><code>cp -r hooks/security-scan /path/to/project/.claude/hooks/
cp -r hooks/test-runner /path/to/project/.claude/hooks/</code></pre>
                </div>

                <div class="usage-step">
                    <div class="step-number">2</div>
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

                <div class="usage-step">
                    <div class="step-number">3</div>
                    <h3>Make Scripts Executable</h3>
                    <p>Ensure hook scripts have execute permissions.</p>
                    <pre><code>chmod +x .claude/hooks/*/hook.sh</code></pre>
                    <p><strong>That's it!</strong> Hooks will now execute automatically at configured events.</p>
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
                <a href="{{ site.baseurl }}/HOOKS-LIBRARY" class="resource-card">
                    <i class="fas fa-book"></i>
                    <h3>Complete Hooks Reference</h3>
                    <p>Comprehensive documentation with all 6 hooks, configurations, and best practices</p>
                </a>
                <a href="https://code.claude.com/docs/en/hooks" target="_blank" class="resource-card">
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
                <a href="{{ site.baseurl }}/HOOKS-LIBRARY" class="btn-secondary-large">
                    <i class="fas fa-book"></i> View Documentation
                </a>
            </div>
        </div>
    </div>
</div>

<style>
/* Hook Cards */
.hooks-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
}

.hook-card {
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 12px;
    padding: 1.5rem;
    transition: all 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94);
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

.hook-icon.security {
    background: linear-gradient(135deg, #ef4444, #dc2626);
}

.hook-icon.testing {
    background: linear-gradient(135deg, #10b981, #059669);
}

.hook-icon.setup {
    background: linear-gradient(135deg, #3b82f6, #2563eb);
}

.hook-icon.format {
    background: linear-gradient(135deg, #8b5cf6, #7c3aed);
}

.hook-icon.warning {
    background: linear-gradient(135deg, #f59e0b, #d97706);
}

.hook-icon.dependencies {
    background: linear-gradient(135deg, #06b6d4, #0891b2);
}

.hook-card h3 {
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
    line-height: 1.6;
    margin-bottom: 1rem;
}

.hook-features {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 1rem;
}

.feature-badge {
    font-size: 0.75rem;
    background: var(--hover-overlay);
    color: var(--accent-primary);
    padding: 0.25rem 0.625rem;
    border-radius: 4px;
    font-weight: 500;
}

.hook-stats {
    display: flex;
    gap: 1.5rem;
    font-size: 0.875rem;
    color: var(--text-secondary);
    padding-top: 1rem;
    border-top: 1px solid var(--border-primary);
}

.hook-stats i {
    margin-right: 0.25rem;
}

/* Configuration Cards */
.config-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 1.5rem;
    margin: 2rem 0;
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

/* Responsive */
@media (max-width: 768px) {
    .hooks-grid {
        grid-template-columns: 1fr;
    }

    .config-grid {
        grid-template-columns: 1fr;
    }
}
</style>
