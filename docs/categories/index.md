---
layout: default
title: Browse Categories
description: "Explore all workflow categories containing 486+ AI prompts organized by professional function and use case."
---

<div class="categories-page">
    <div class="container">
        <div class="page-header">
            <h1 class="page-title">Browse Categories</h1>
            <p class="page-description">
                Explore our comprehensive collection of AI prompts organized by workflow and professional function.
                Each category contains specialized prompts designed for specific use cases and industries.
            </p>
        </div>

        {% assign total_prompts = site.prompts | size %}
        {% assign categories_count = site.categories | size %}

        <div class="categories-overview">
            <div class="overview-stats">
                <div class="stat">
                    <span class="stat-number">{{ categories_count }}</span>
                    <span class="stat-label">Categories</span>
                </div>
                <div class="stat">
                    <span class="stat-number">{{ total_prompts }}+</span>
                    <span class="stat-label">Total Prompts</span>
                </div>
                <div class="stat">
                    <span class="stat-number">100%</span>
                    <span class="stat-label">Ready to Use</span>
                </div>
            </div>
        </div>

        <div class="categories-grid-container">
            <h2 class="section-subtitle">All Categories</h2>
            <div class="categories-grid">
                {% assign sorted_categories = site.categories | sort: 'title' %}
                {% for category in sorted_categories %}
                    {% assign category_prompts = site.prompts | where: "category", category.category %}
                    {% assign prompt_count = category_prompts | size %}

                    {% if prompt_count > 0 %}
                    <a href="{{ category.url | relative_url }}" class="category-card detailed">
                        <div class="category-icon">
                            {% case category.category %}
                                {% when 'analysis' %}
                                    <i class="fas fa-chart-bar"></i>
                                {% when 'biotechnology' %}
                                    <i class="fas fa-dna"></i>
                                {% when 'blockchain' %}
                                    <i class="fas fa-cubes"></i>
                                {% when 'communication' %}
                                    <i class="fas fa-comments"></i>
                                {% when 'creation' %}
                                    <i class="fas fa-palette"></i>
                                {% when 'creativity-innovation' %}
                                    <i class="fas fa-lightbulb"></i>
                                {% when 'customer-focused' %}
                                    <i class="fas fa-heart"></i>
                                {% when 'decision-making' %}
                                    <i class="fas fa-balance-scale"></i>
                                {% when 'evaluation-assessment' %}
                                    <i class="fas fa-clipboard-check"></i>
                                {% when 'government-digital' %}
                                    <i class="fas fa-landmark"></i>
                                {% when 'healthcare-digital' %}
                                    <i class="fas fa-heartbeat"></i>
                                {% when 'learning-development' %}
                                    <i class="fas fa-graduation-cap"></i>
                                {% when 'management-leadership' %}
                                    <i class="fas fa-users"></i>
                                {% when 'optimization' %}
                                    <i class="fas fa-tachometer-alt"></i>
                                {% when 'planning' %}
                                    <i class="fas fa-calendar-alt"></i>
                                {% when 'problem-solving' %}
                                    <i class="fas fa-tools"></i>
                                {% when 'quantum-computing' %}
                                    <i class="fas fa-atom"></i>
                                {% when 'renewable-energy' %}
                                    <i class="fas fa-solar-panel"></i>
                                {% when 'research-workflows' %}
                                    <i class="fas fa-search"></i>
                                {% when 'space-economy' %}
                                    <i class="fas fa-rocket"></i>
                                {% when 'supply-chain' %}
                                    <i class="fas fa-truck"></i>
                                {% when 'technical-workflows' %}
                                    <i class="fas fa-code"></i>
                                {% else %}
                                    <i class="fas fa-folder"></i>
                            {% endcase %}
                        </div>
                        <div class="category-content">
                            <h3>{{ category.title }}</h3>
                            <p>{{ category.description }}</p>
                            {% if category.tags %}
                            <div class="category-tags">
                                {% for tag in category.tags limit:3 %}
                                    <span class="tag">{{ tag }}</span>
                                {% endfor %}
                            </div>
                            {% endif %}
                        </div>
                        <div class="category-footer">
                            <span class="prompt-count">{{ prompt_count }} prompt{% if prompt_count != 1 %}s{% endif %}</span>
                            <i class="fas fa-arrow-right"></i>
                        </div>
                    </a>
                    {% endif %}
                {% endfor %}
            </div>
        </div>

        <div class="help-section">
            <h2>Need Help Finding the Right Prompt?</h2>
            <p>Can't find what you're looking for? Try our search function or browse by tags to discover prompts that match your specific needs.</p>
            <div class="help-actions">
                <a href="{{ '/search/' | relative_url }}" class="btn btn-primary">
                    <i class="fas fa-search"></i>
                    Search Prompts
                </a>
                <a href="{{ site.github_url }}/issues/new" class="btn btn-secondary">
                    <i class="fas fa-plus"></i>
                    Suggest a Prompt
                </a>
            </div>
        </div>
    </div>
</div>
