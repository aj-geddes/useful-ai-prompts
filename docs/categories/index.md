---
layout: default
title: "Browse AI Prompt Categories | 486 Prompts Across 22 Categories"
description: "Browse 486 expert AI prompts organized across 22 professional categories. Find prompts for business, technical workflows, research, emerging technologies, and more."
---

<div class="categories-page">
    <div class="container">
        <!-- Page Header -->
        <div class="page-header">
            <h1>Browse Prompt Categories</h1>
            <p class="page-subtitle">
                486 expert prompts organized across 22 specialized categories for business, technical, and creative workflows.
            </p>
        </div>

        <!-- Stats Bar -->
        <div class="stats-bar">
            {% assign total_prompts = site.prompts | size %}
            {% assign categories_count = site.categories | size %}
            <div class="stat-item">
                <span class="stat-number">{{ categories_count }}</span>
                <span class="stat-label">Categories</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">{{ total_prompts }}</span>
                <span class="stat-label">Total Prompts</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">100%</span>
                <span class="stat-label">Free & Open Source</span>
            </div>
        </div>

        <!-- Categories Grid -->
        <div class="categories-section">
            <div class="categories-grid">
                {% assign sorted_categories = site.categories | sort: 'title' %}
                {% for category in sorted_categories %}
                    {% assign category_prompts = site.prompts | where: "category", category.category %}
                    {% assign prompt_count = category_prompts | size %}

                    {% if prompt_count > 0 %}
                    <a href="{{ category.url | relative_url }}" class="category-card">
                        <div class="category-header">
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
                                    {% when 'content-creation' %}
                                        <i class="fas fa-pen-fancy"></i>
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
                                    {% when 'financial-planning' %}
                                        <i class="fas fa-chart-line"></i>
                                    {% when 'government-digital' %}
                                        <i class="fas fa-landmark"></i>
                                    {% when 'healthcare-digital' %}
                                        <i class="fas fa-heartbeat"></i>
                                    {% when 'learning-development' %}
                                        <i class="fas fa-graduation-cap"></i>
                                    {% when 'learning-skills' %}
                                        <i class="fas fa-book-reader"></i>
                                    {% when 'management-leadership' %}
                                        <i class="fas fa-users"></i>
                                    {% when 'optimization' %}
                                        <i class="fas fa-tachometer-alt"></i>
                                    {% when 'personal-productivity' %}
                                        <i class="fas fa-tasks"></i>
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
                                    {% when 'career-development' %}
                                        <i class="fas fa-briefcase"></i>
                                    {% when 'health-wellness' %}
                                        <i class="fas fa-spa"></i>
                                    {% when 'personal-growth' %}
                                        <i class="fas fa-seedling"></i>
                                    {% when 'relationships-communication' %}
                                        <i class="fas fa-handshake"></i>
                                    {% else %}
                                        <i class="fas fa-folder"></i>
                                {% endcase %}
                            </div>
                            <span class="category-count">{{ prompt_count }} prompt{% if prompt_count != 1 %}s{% endif %}</span>
                        </div>

                        <div class="category-body">
                            <h3 class="category-title">{{ category.title }}</h3>
                            <p class="category-description">{{ category.description | truncate: 120 }}</p>

                            {% if category.tags %}
                            <div class="category-tags">
                                {% for tag in category.tags limit:3 %}
                                    <span class="category-tag">{{ tag }}</span>
                                {% endfor %}
                                {% if category.tags.size > 3 %}
                                    <span class="category-tag-more">+{{ category.tags.size | minus: 3 }}</span>
                                {% endif %}
                            </div>
                            {% endif %}
                        </div>

                        <div class="category-footer">
                            <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                        </div>
                    </a>
                    {% endif %}
                {% endfor %}
            </div>
        </div>

        <!-- Quick Actions -->
        <div class="quick-actions">
            <h2>Can't Find What You're Looking For?</h2>
            <p>Use our search to find specific prompts or explore our complete library.</p>
            <div class="action-buttons">
                <a href="{{ '/' | relative_url }}" class="btn-primary">
                    <i class="fas fa-search"></i> Search All Prompts
                </a>
                <a href="{{ site.github_url }}/issues/new" class="btn-secondary" target="_blank">
                    <i class="fas fa-lightbulb"></i> Suggest a Category
                </a>
            </div>
        </div>
    </div>
</div>

<style>
/* Categories Page Styles */
.categories-page {
    padding: 3rem 0;
}

.page-header {
    text-align: center;
    margin-bottom: 3rem;
}

.page-header h1 {
    font-size: 2.5rem;
    font-weight: 700;
    color: #1a202c;
    margin: 0 0 1rem;
}

.page-subtitle {
    font-size: 1.125rem;
    color: #4a5568;
    line-height: 1.7;
    max-width: 700px;
    margin: 0 auto;
}

/* Stats Bar */
.stats-bar {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-bottom: 4rem;
    padding: 2rem;
    background: #f8f9fa;
    border-radius: 8px;
}

.stat-item {
    text-align: center;
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    color: #2d3748;
    margin-bottom: 0.5rem;
}

.stat-label {
    display: block;
    font-size: 0.9375rem;
    color: #718096;
    font-weight: 500;
}

/* Categories Grid */
.categories-section {
    margin-bottom: 4rem;
}

.categories-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
}

.category-card {
    background: white;
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1.75rem;
    text-decoration: none;
    color: inherit;
    transition: all 0.2s;
    display: flex;
    flex-direction: column;
}

.category-card:hover {
    border-color: #cbd5e0;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
    transform: translateY(-2px);
}

.category-header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-bottom: 1.25rem;
}

.category-icon {
    width: 48px;
    height: 48px;
    background: #edf2f7;
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: #4299e1;
    font-size: 1.5rem;
}

.category-count {
    font-size: 0.875rem;
    color: #718096;
    font-weight: 500;
}

.category-body {
    flex-grow: 1;
    margin-bottom: 1.25rem;
}

.category-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #2d3748;
    margin: 0 0 0.75rem;
}

.category-description {
    font-size: 0.9375rem;
    color: #4a5568;
    line-height: 1.6;
    margin: 0 0 1rem;
}

.category-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.category-tag {
    background: #edf2f7;
    color: #4a5568;
    padding: 0.25rem 0.625rem;
    border-radius: 4px;
    font-size: 0.8125rem;
    font-weight: 500;
}

.category-tag-more {
    color: #718096;
    font-size: 0.8125rem;
    font-weight: 500;
}

.category-footer {
    padding-top: 1rem;
    border-top: 1px solid #f7fafc;
}

.view-link {
    color: #4299e1;
    font-size: 0.875rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}

.category-card:hover .view-link {
    color: #3182ce;
}

.view-link i {
    font-size: 0.75rem;
    transition: transform 0.2s;
}

.category-card:hover .view-link i {
    transform: translateX(4px);
}

/* Quick Actions */
.quick-actions {
    text-align: center;
    padding: 3rem 2rem;
    background: #f8f9fa;
    border-radius: 8px;
}

.quick-actions h2 {
    font-size: 1.75rem;
    font-weight: 700;
    color: #1a202c;
    margin: 0 0 1rem;
}

.quick-actions p {
    font-size: 1.125rem;
    color: #4a5568;
    margin: 0 0 2rem;
}

.action-buttons {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.btn-primary,
.btn-secondary {
    padding: 0.875rem 1.75rem;
    border-radius: 6px;
    font-weight: 600;
    font-size: 1rem;
    text-decoration: none;
    transition: all 0.2s;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}

.btn-primary {
    background: #4299e1;
    color: white;
}

.btn-primary:hover {
    background: #3182ce;
    transform: translateY(-1px);
    box-shadow: 0 4px 12px rgba(66, 153, 225, 0.3);
}

.btn-secondary {
    background: white;
    color: #4a5568;
    border: 2px solid #e2e8f0;
}

.btn-secondary:hover {
    border-color: #cbd5e0;
    background: #f7fafc;
}

/* Responsive Design */
@media (max-width: 1024px) {
    .categories-grid {
        grid-template-columns: repeat(2, 1fr);
    }

    .stats-bar {
        gap: 2rem;
    }
}

@media (max-width: 768px) {
    .categories-page {
        padding: 2rem 0;
    }

    .page-header h1 {
        font-size: 2rem;
    }

    .page-subtitle {
        font-size: 1rem;
    }

    .stats-bar {
        flex-direction: column;
        gap: 1.5rem;
        padding: 1.5rem;
    }

    .stat-number {
        font-size: 2rem;
    }

    .categories-grid {
        grid-template-columns: 1fr;
        gap: 1rem;
    }

    .category-card {
        padding: 1.5rem;
    }

    .quick-actions {
        padding: 2rem 1.5rem;
    }

    .quick-actions h2 {
        font-size: 1.5rem;
    }

    .action-buttons {
        flex-direction: column;
    }

    .btn-primary,
    .btn-secondary {
        width: 100%;
        justify-content: center;
    }
}

@media (max-width: 480px) {
    .page-header h1 {
        font-size: 1.75rem;
    }

    .stat-number {
        font-size: 1.75rem;
    }

    .category-title {
        font-size: 1.125rem;
    }
}
</style>
