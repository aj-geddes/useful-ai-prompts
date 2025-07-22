---
layout: default
title: Home
description: "Discover 200+ practical, ready-to-use AI prompts organized by workflow and profession. Copy, paste, and enhance your productivity with expert-crafted prompts."
---

<div class="hero-section">
    <div class="container">
        <div class="hero-content">
            <h1 class="hero-title">
                Useful AI Prompts
                <span class="hero-subtitle">Your comprehensive library of professional AI prompts</span>
            </h1>
            
            <p class="hero-description">
                Discover 200+ practical, ready-to-use AI prompts designed for professionals across all industries. 
                From content creation to technical analysis, find the perfect prompt to enhance your workflow.
            </p>
            
            <div class="hero-stats">
                <div class="stat">
                    <span class="stat-number">{{ site.prompts | size }}</span>
                    <span class="stat-label">Expert Prompts</span>
                </div>
                <div class="stat">
                    <span class="stat-number">14</span>
                    <span class="stat-label">Categories</span>
                </div>
                <div class="stat">
                    <span class="stat-number">100%</span>
                    <span class="stat-label">Ready to Use</span>
                </div>
            </div>
            
            <div class="hero-actions">
                <a href="#featured-prompts" class="btn btn-primary btn-large">
                    <i class="fas fa-rocket"></i>
                    Browse Prompts
                </a>
                <a href="{{ '/categories/' | relative_url }}" class="btn btn-secondary btn-large">
                    <i class="fas fa-th-large"></i>
                    View Categories
                </a>
            </div>
        </div>
    </div>
</div>

<div class="features-section">
    <div class="container">
        <h2 class="section-title">Why Choose Our Prompts?</h2>
        <div class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-copy"></i>
                </div>
                <h3>Copy & Paste Ready</h3>
                <p>Every prompt is formatted and ready to use immediately. No setup required.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-user-tie"></i>
                </div>
                <h3>Real-World Ready</h3>
                <p>Tested and refined for actual business tasks and daily workflows.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-search"></i>
                </div>
                <h3>Easy Discovery</h3>
                <p>Find exactly what you need with powerful search and filtering capabilities.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-robot"></i>
                </div>
                <h3>Multi-Model Support</h3>
                <p>Compatible with GPT-4, Claude, Gemini, and other leading AI models.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-sync-alt"></i>
                </div>
                <h3>Regularly Updated</h3>
                <p>Fresh prompts added regularly to keep up with evolving best practices.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fab fa-github"></i>
                </div>
                <h3>Open Source</h3>
                <p>Fully open source with community contributions welcome.</p>
            </div>
        </div>
    </div>
</div>

<div class="categories-section">
    <div class="container">
        <h2 class="section-title">Browse by Category</h2>
        <div class="categories-grid">
            <a href="{{ '/categories/analysis/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-chart-bar"></i>
                </div>
                <h3>Analysis</h3>
                <p>Data analysis, market research, competitive intelligence</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "analysis" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/creation/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-palette"></i>
                </div>
                <h3>Creation</h3>
                <p>Content creation, copywriting, documentation</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "creation" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/planning/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-calendar-alt"></i>
                </div>
                <h3>Planning</h3>
                <p>Project planning, strategic planning, resource allocation</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "planning" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/communication/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-comments"></i>
                </div>
                <h3>Communication</h3>
                <p>Presentations, meetings, stakeholder management</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "communication" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/problem-solving/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-tools"></i>
                </div>
                <h3>Problem Solving</h3>
                <p>Debugging, troubleshooting, optimization</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "problem-solving" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/decision-making/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-balance-scale"></i>
                </div>
                <h3>Decision Making</h3>
                <p>Option evaluation, prioritization, strategic choices</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "decision-making" | size }} prompts</span>
            </a>
        </div>
        
        <div class="categories-footer">
            <a href="{{ '/categories/' | relative_url }}" class="btn btn-primary">
                View All Categories
                <i class="fas fa-arrow-right"></i>
            </a>
        </div>
    </div>
</div>

<div id="featured-prompts" class="featured-section">
    <div class="container">
        <h2 class="section-title">Featured Prompts</h2>
        <div class="featured-grid">
            {% assign featured_prompts = site.prompts | where: "featured", true | limit: 6 %}
            {% if featured_prompts.size == 0 %}
                {% assign featured_prompts = site.prompts | sample: 6 %}
            {% endif %}
            
            {% for prompt in featured_prompts %}
            <div class="prompt-card featured">
                <div class="card-header">
                    <h3 class="card-title">
                        <a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a>
                    </h3>
                    <span class="category-badge">{{ prompt.category | capitalize }}</span>
                </div>
                
                {% if prompt.description %}
                <p class="card-description">{{ prompt.description | truncate: 100 }}</p>
                {% endif %}
                
                <div class="card-meta">
                    {% if prompt.tags %}
                    <div class="card-tags">
                        {% for tag in prompt.tags limit:2 %}
                            <span class="tag">{{ tag }}</span>
                        {% endfor %}
                    </div>
                    {% endif %}
                </div>
                
                <div class="card-actions">
                    <a href="{{ prompt.url | relative_url }}" class="btn btn-primary">
                        View Prompt
                    </a>
                    {% if prompt.prompt %}
                    <button class="btn btn-secondary copy-btn" 
                            data-clipboard-text="{{ prompt.prompt | strip }}">
                        <i class="fas fa-copy"></i>
                    </button>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
    </div>
</div>

<div class="cta-section">
    <div class="container">
        <div class="cta-content">
            <h2>Ready to Supercharge Your Workflow?</h2>
            <p>Join thousands of professionals using our AI prompts to enhance their productivity.</p>
            <div class="cta-actions">
                <a href="{{ '/categories/' | relative_url }}" class="btn btn-primary btn-large">
                    Start Browsing
                    <i class="fas fa-arrow-right"></i>
                </a>
                <a href="{{ site.github_url }}" class="btn btn-secondary btn-large">
                    <i class="fab fa-github"></i>
                    View on GitHub
                </a>
            </div>
        </div>
    </div>
</div>