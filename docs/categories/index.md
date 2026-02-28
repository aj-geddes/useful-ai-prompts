---
layout: default
title: "Browse AI Prompt Categories | 679 Prompts Across 47 Categories"
description: "Browse 679 expert AI prompts organized across 47 professional categories. Find prompts for development, security, finance, HR, healthcare, and more."
---

<div class="categories-page">
    <div class="container">
        <!-- Page Header -->
        <div class="page-header">
            <h1>Browse Prompt Categories</h1>
            <p class="page-subtitle">
                679 expert prompts organized across 47 specialized categories for professional workflows across every major industry and function.
            </p>
        </div>

        <!-- Stats Bar -->
        <div class="stats-bar">
            {% assign total_prompts = site.prompts | size %}
            {% assign categories_count = site.categories | size %}
            <div class="stat-item">
                <span class="stat-number">47</span>
                <span class="stat-label">Categories</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">679</span>
                <span class="stat-label">Total Prompts</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">14</span>
                <span class="stat-label">Professional Domains</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">100%</span>
                <span class="stat-label">Free & Open Source</span>
            </div>
        </div>

        <!-- Core Professional Categories -->
        <div class="categories-section">
            <h2 class="section-heading">Core Professional Domains</h2>
            <p class="section-subheading">Prompts organized by profession and industry, each covering a complete domain in depth.</p>
            <div class="categories-grid core-grid">

                <a href="{{ '/categories/development/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-code"></i></div>
                        <span class="category-count">14 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Development & Engineering</h3>
                        <p class="category-description">Code review, API design, debugging, architecture, DevOps, and technical documentation for software engineers.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/security/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-shield-alt"></i></div>
                        <span class="category-count">14 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Cybersecurity</h3>
                        <p class="category-description">Threat modeling, incident response, penetration testing, zero-trust architecture, and compliance analysis.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/finance/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-chart-line"></i></div>
                        <span class="category-count">14 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Finance & Financial Analysis</h3>
                        <p class="category-description">Financial modeling, investment research, M&A analysis, budgeting, and risk assessment for finance professionals.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/human-resources/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-users"></i></div>
                        <span class="category-count">14 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Human Resources</h3>
                        <p class="category-description">Talent acquisition, performance management, compensation benchmarking, DEI strategy, and workforce planning.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/healthcare/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-heartbeat"></i></div>
                        <span class="category-count">14 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Healthcare</h3>
                        <p class="category-description">Clinical documentation, quality improvement, patient education, compliance, and hospital operations.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/education/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-graduation-cap"></i></div>
                        <span class="category-count">12 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Education & Teaching</h3>
                        <p class="category-description">Lesson planning, assessment design, curriculum development, and differentiated instruction for educators.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/project-management/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-calendar-alt"></i></div>
                        <span class="category-count">15 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Project Management</h3>
                        <p class="category-description">Project charters, risk registers, sprint planning, stakeholder communication, and retrospective facilitation.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/operations/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-cogs"></i></div>
                        <span class="category-count">14 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Operations Management</h3>
                        <p class="category-description">Process optimization, capacity planning, KPI dashboards, vendor management, and quality systems.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/engineering/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-drafting-compass"></i></div>
                        <span class="category-count">15 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Engineering</h3>
                        <p class="category-description">Failure analysis, FMEA, technical specifications, design review, reliability engineering, and materials selection.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/customer-service/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-headset"></i></div>
                        <span class="category-count">15 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Customer Service</h3>
                        <p class="category-description">Complaint resolution, customer journey mapping, knowledge base content, and service recovery design.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/creative/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-paint-brush"></i></div>
                        <span class="category-count">12 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Creative & Marketing</h3>
                        <p class="category-description">Brand storytelling, marketing campaigns, copywriting, content strategy, UX design, and creative briefs.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/research/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-search"></i></div>
                        <span class="category-count">11 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Research & Analysis</h3>
                        <p class="category-description">Primary research design, competitive intelligence, data synthesis, and hypothesis testing for analysts.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/administrative/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-briefcase"></i></div>
                        <span class="category-count">15 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Administrative & Office</h3>
                        <p class="category-description">SOPs, correspondence, meeting management, scheduling, vendor relations, and records management.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

                <a href="{{ '/categories/academic/' | relative_url }}" class="category-card featured">
                    <div class="category-header">
                        <div class="category-icon"><i class="fas fa-university"></i></div>
                        <span class="category-count">13 prompts</span>
                    </div>
                    <div class="category-body">
                        <h3 class="category-title">Academic Research</h3>
                        <p class="category-description">Literature reviews, research proposals, grant writing, academic writing, peer review, and dissertation support.</p>
                    </div>
                    <div class="category-footer">
                        <span class="view-link">View Category <i class="fas fa-arrow-right"></i></span>
                    </div>
                </a>

            </div>
        </div>

        <!-- All Other Categories -->
        <div class="categories-section">
            <h2 class="section-heading">All Categories</h2>
            <p class="section-subheading">The complete library organized alphabetically — including specialized, emerging, and cross-functional categories.</p>
            <div class="categories-grid">
                {% assign sorted_categories = site.categories | sort: 'title' %}
                {% for category in sorted_categories %}
                    {% assign category_prompts = site.prompts | where: "category", category.slug %}
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
                                        <i class="fas fa-piggy-bank"></i>
                                    {% when 'government-digital' %}
                                        <i class="fas fa-landmark"></i>
                                    {% when 'healthcare-digital' %}
                                        <i class="fas fa-hospital-symbol"></i>
                                    {% when 'learning-development' %}
                                        <i class="fas fa-chalkboard-teacher"></i>
                                    {% when 'learning-skills' %}
                                        <i class="fas fa-book-reader"></i>
                                    {% when 'management-leadership' %}
                                        <i class="fas fa-sitemap"></i>
                                    {% when 'optimization' %}
                                        <i class="fas fa-tachometer-alt"></i>
                                    {% when 'personal-productivity' %}
                                        <i class="fas fa-tasks"></i>
                                    {% when 'planning' %}
                                        <i class="fas fa-map"></i>
                                    {% when 'problem-solving' %}
                                        <i class="fas fa-puzzle-piece"></i>
                                    {% when 'quantum-computing' %}
                                        <i class="fas fa-atom"></i>
                                    {% when 'renewable-energy' %}
                                        <i class="fas fa-solar-panel"></i>
                                    {% when 'research-workflows' %}
                                        <i class="fas fa-microscope"></i>
                                    {% when 'space-economy' %}
                                        <i class="fas fa-rocket"></i>
                                    {% when 'supply-chain' %}
                                        <i class="fas fa-truck"></i>
                                    {% when 'technical-workflows' %}
                                        <i class="fas fa-terminal"></i>
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
            <p>Browse by job role or use our search to find specific prompts across the full library.</p>
            <div class="action-buttons">
                <a href="{{ '/use-cases/' | relative_url }}" class="btn-primary">
                    <i class="fas fa-user-tie"></i> Browse by Job Role
                </a>
                <a href="{{ '/' | relative_url }}" class="btn-secondary">
                    <i class="fas fa-search"></i> Search All Prompts
                </a>
                <a href="{{ site.github_url }}/issues/new" class="btn-secondary" target="_blank" rel="noopener">
                    <i class="fas fa-lightbulb"></i> Suggest a Category
                </a>
            </div>
        </div>
    </div>

</div>

<style>
  /* Categories page — uses redesign.css CSS variables for full theme support */
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
    color: var(--text-base);
    margin: 0 0 1rem;
    letter-spacing: -0.02em;
  }

  .page-subtitle {
    font-size: 1.125rem;
    color: var(--text-muted);
    line-height: 1.7;
    max-width: 700px;
    margin: 0 auto;
  }

  /* Stats bar */
  .stats-bar {
    display: flex;
    justify-content: center;
    gap: 3rem;
    margin-bottom: 4rem;
    padding: 2rem;
    background: var(--surface-raised);
    border: 1px solid var(--border-base);
    border-radius: var(--radius-xl);
  }

  .stat-item {
    text-align: center;
  }

  .stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--color-primary);
    margin-bottom: 0.5rem;
    letter-spacing: -0.02em;
  }

  .stat-label {
    display: block;
    font-size: 0.9375rem;
    color: var(--text-muted);
    font-weight: 500;
  }

  /* Section headings */
  .categories-section {
    margin-bottom: 4rem;
  }

  .section-heading {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text-base);
    margin: 0 0 0.5rem;
    letter-spacing: -0.02em;
  }

  .section-subheading {
    font-size: 1rem;
    color: var(--text-muted);
    margin: 0 0 2rem;
  }

  /* Grid — override redesign.css auto-fill with explicit columns */
  .categories-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.5rem;
  }

  .core-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  /* Cards — extend redesign.css .category-card */
  .category-card {
    background: var(--surface-base);
    border: 1px solid var(--border-base);
    border-radius: var(--radius-lg);
    padding: 1.75rem;
    text-decoration: none;
    color: var(--text-base);
    transition:
      transform var(--transition-base),
      box-shadow var(--transition-base),
      border-color var(--transition-base);
    display: flex !important;
    flex-direction: column;
  }

  .category-card:hover {
    border-color: var(--color-primary);
    box-shadow: var(--shadow-md);
    transform: translateY(-2px);
  }

  .category-card.featured {
    border-color: var(--color-primary-ring);
    background: linear-gradient(
      135deg,
      var(--surface-base) 0%,
      var(--color-primary-light) 100%
    );
  }

  .category-card.featured:hover {
    border-color: var(--color-primary);
    box-shadow: 0 4px 16px var(--color-primary-ring);
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
    background: var(--color-primary-light);
    border-radius: var(--radius-lg);
    display: flex;
    align-items: center;
    justify-content: center;
    color: var(--color-primary);
    font-size: 1.5rem;
    margin-bottom: 0;
  }

  .category-count {
    font-size: 0.875rem;
    color: var(--text-muted);
    font-weight: 500;
    margin: 0;
  }

  .category-body {
    flex-grow: 1;
    margin-bottom: 1.25rem;
  }

  .category-card h3,
  .category-title {
    font-size: 1.125rem;
    font-weight: 600;
    color: var(--text-base);
    margin: 0 0 0.75rem;
  }

  .category-card.featured .category-title {
    font-size: 1.25rem;
  }

  .category-description {
    font-size: 0.9375rem;
    color: var(--text-muted);
    line-height: 1.6;
    margin: 0 0 1rem;
  }

  .category-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
  }

  .category-tag {
    background: var(--tag-bg);
    color: var(--tag-text);
    border: 1px solid var(--tag-border);
    padding: 0.25rem 0.625rem;
    border-radius: var(--radius-sm);
    font-size: 0.8125rem;
    font-weight: 500;
  }

  .category-tag-more {
    color: var(--text-muted);
    font-size: 0.8125rem;
    font-weight: 500;
  }

  .category-footer {
    padding-top: 1rem;
    border-top: 1px solid var(--border-base);
  }

  .view-link {
    color: var(--color-primary);
    font-size: 0.875rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
  }

  .category-card:hover .view-link {
    color: var(--color-primary-hover);
  }

  .view-link i {
    font-size: 0.75rem;
    transition: transform var(--transition-base);
  }

  .category-card:hover .view-link i {
    transform: translateX(4px);
  }

  /* Quick actions */
  .quick-actions {
    text-align: center;
    padding: 3rem 2rem;
    background: var(--surface-raised);
    border: 1px solid var(--border-base);
    border-radius: var(--radius-xl);
  }

  .quick-actions h2 {
    font-size: 1.75rem;
    font-weight: 700;
    color: var(--text-base);
    margin: 0 0 1rem;
    letter-spacing: -0.02em;
  }

  .quick-actions p {
    font-size: 1.125rem;
    color: var(--text-muted);
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
    border-radius: var(--radius-md);
    font-weight: 600;
    font-size: 1rem;
    text-decoration: none;
    transition: all var(--transition-base);
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
  }

  .btn-primary {
    background: var(--color-primary);
    color: var(--text-on-primary);
  }

  .btn-primary:hover {
    background: var(--color-primary-hover);
    transform: translateY(-1px);
    box-shadow: 0 4px 12px var(--color-primary-ring);
    color: var(--text-on-primary);
    text-decoration: none;
  }

  .btn-secondary {
    background: var(--surface-base);
    color: var(--text-muted);
    border: 2px solid var(--border-base);
  }

  .btn-secondary:hover {
    border-color: var(--border-strong);
    background: var(--surface-raised);
    color: var(--text-base);
    text-decoration: none;
  }

  /* Responsive */
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

    .stats-bar {
      flex-direction: column;
      gap: 1.5rem;
      padding: 1.5rem;
    }

    .stat-number {
      font-size: 2rem;
    }

    .categories-grid,
    .core-grid {
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

    .section-heading {
      font-size: 1.5rem;
    }
  }
</style>
