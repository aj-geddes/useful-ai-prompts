---
layout: default
title: Home
description: "Discover 278+ professional AI prompts across 18 specialized sectors. Enterprise-grade dual-persona prompts covering $50+ trillion in market opportunities. Transform your workflow with expert-crafted solutions."
---

<div class="hero-section">
    <div class="container">
        <div class="hero-content">
            <h1 class="hero-title">
                Useful AI Prompts
                <span class="hero-subtitle">The definitive enterprise AI prompt library</span>
            </h1>
            
            <p class="hero-description">
                Discover 278+ expert-crafted AI prompts spanning 18 specialized sectors from Biotechnology to Space Economy. 
                Each prompt features dual-persona architecture and professional frameworks, delivering 350+ line comprehensive outputs for real business challenges.
            </p>
            
            <div class="hero-stats">
                <div class="stat">
                    <span class="stat-number">278+</span>
                    <span class="stat-label">Enterprise Prompts</span>
                </div>
                <div class="stat">
                    <span class="stat-number">18</span>
                    <span class="stat-label">Specialized Sectors</span>
                </div>
                <div class="stat">
                    <span class="stat-number">$50T+</span>
                    <span class="stat-label">Market Coverage</span>
                </div>
                <div class="stat">
                    <span class="stat-number">350+</span>
                    <span class="stat-label">Lines Per Output</span>
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

<div class="new-sectors-section">
    <div class="container">
        <h2 class="section-title">🚀 NEW: High-Value Specialty Sectors</h2>
        <p class="section-description">We've massively expanded into cutting-edge industries representing the future of business</p>
        <div class="new-sectors-grid">
            <div class="sector-card">
                <div class="sector-icon">🧬</div>
                <h3>Biotechnology</h3>
                <p>CRISPR, gene therapy, drug discovery, biomarker validation</p>
                <span class="sector-value">$2.44T Market</span>
            </div>
            
            <div class="sector-card">
                <div class="sector-icon">🚀</div>
                <h3>Space Economy</h3>
                <p>Satellite operations, space tourism, asteroid mining, mission planning</p>
                <span class="sector-value">$469B Market</span>
            </div>
            
            <div class="sector-card">
                <div class="sector-icon">⚡</div>
                <h3>Renewable Energy</h3>
                <p>Solar development, energy storage, grid integration, sustainability</p>
                <span class="sector-value">$4.5T Market</span>
            </div>
            
            <div class="sector-card">
                <div class="sector-icon">⚛️</div>
                <h3>Quantum Computing</h3>
                <p>Circuit optimization, cryptography, machine learning, error correction</p>
                <span class="sector-value">$850B Market</span>
            </div>
            
            <div class="sector-card">
                <div class="sector-icon">🔗</div>
                <h3>Blockchain</h3>
                <p>Smart contracts, DeFi, tokenization, enterprise integration</p>
                <span class="sector-value">$163.8B Market</span>
            </div>
            
            <div class="sector-card">
                <div class="sector-icon">🏛️</div>
                <h3>Government Digital</h3>
                <p>Citizen services, digital transformation, smart cities, identity</p>
                <span class="sector-value">$500B+ Market</span>
            </div>
        </div>
    </div>
</div>

<div class="features-section">
    <div class="container">
        <h2 class="section-title">Enterprise-Grade Quality Standards</h2>
        <div class="features-grid">
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-users"></i>
                </div>
                <h3>Dual-Persona Architecture</h3>
                <p>Every prompt combines two expert perspectives with 10-15+ years experience for comprehensive solutions.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-cogs"></i>
                </div>
                <h3>Professional Frameworks</h3>
                <p>Integrates 3-5 proven methodologies per prompt for systematic, enterprise-grade outputs.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-chart-line"></i>
                </div>
                <h3>350+ Line Outputs</h3>
                <p>Comprehensive deliverables with executive summaries, detailed analysis, and implementation roadmaps.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-industry"></i>
                </div>
                <h3>Industry-Specific</h3>
                <p>Specialized prompts for high-growth sectors including biotech, space economy, and quantum computing.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-shield-alt"></i>
                </div>
                <h3>Risk Management</h3>
                <p>Built-in risk assessment and mitigation strategies for enterprise decision-making.</p>
            </div>
            
            <div class="feature-item">
                <div class="feature-icon">
                    <i class="fas fa-rocket"></i>
                </div>
                <h3>Immediate Business Value</h3>
                <p>Ready-to-implement solutions for real business challenges across $50+ trillion in market opportunities.</p>
            </div>
        </div>
    </div>
</div>

<div class="categories-section">
    <div class="container">
        <h2 class="section-title">Browse All 18 Specialized Categories</h2>
        <div class="categories-grid-expanded">
            <!-- High-Value New Sectors -->
            <a href="{{ '/categories/biotechnology/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">🧬</div>
                <h3>Biotechnology</h3>
                <p>CRISPR, gene therapy, drug discovery</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "biotechnology" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/space-economy/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">🚀</div>
                <h3>Space Economy</h3>
                <p>Satellite ops, space tourism, missions</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "space-economy" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/renewable-energy/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">⚡</div>
                <h3>Renewable Energy</h3>
                <p>Solar, storage, grid integration</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "renewable-energy" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/quantum-computing/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">⚛️</div>
                <h3>Quantum Computing</h3>
                <p>Circuits, cryptography, ML algorithms</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "quantum-computing" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/blockchain/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">🔗</div>
                <h3>Blockchain</h3>
                <p>Smart contracts, DeFi, tokenization</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "blockchain" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/government-digital/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">🏛️</div>
                <h3>Government Digital</h3>
                <p>Citizen services, smart cities</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "government-digital" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <!-- Core Business Categories -->
            <a href="{{ '/categories/analysis/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-chart-bar"></i>
                </div>
                <h3>Analysis</h3>
                <p>Data analysis, market research, intelligence</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "analysis" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/management-leadership/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-users-cog"></i>
                </div>
                <h3>Management & Leadership</h3>
                <p>Team building, strategy, performance</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "management-leadership" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/technical-workflows/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-code"></i>
                </div>
                <h3>Technical Workflows</h3>
                <p>DevOps, architecture, system design</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "technical-workflows" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/planning/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-calendar-alt"></i>
                </div>
                <h3>Planning</h3>
                <p>Strategic planning, resource allocation</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "planning" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/communication/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-comments"></i>
                </div>
                <h3>Communication</h3>
                <p>Presentations, stakeholder management</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "communication" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/decision-making/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-balance-scale"></i>
                </div>
                <h3>Decision Making</h3>
                <p>Evaluation, prioritization, strategy</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "decision-making" | size }} prompts</span>
            </a>
            
            <!-- Additional Categories -->
            <a href="{{ '/categories/creation/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-palette"></i>
                </div>
                <h3>Creation</h3>
                <p>Content, documentation, design</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "creation" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/customer-focused/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-heart"></i>
                </div>
                <h3>Customer-Focused</h3>
                <p>Experience, support, engagement</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "customer-focused" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/evaluation-assessment/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-clipboard-check"></i>
                </div>
                <h3>Evaluation & Assessment</h3>
                <p>Reviews, audits, performance metrics</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "evaluation-assessment" | size }} prompts</span>
            </a>
            
            <a href="{{ '/categories/supply-chain/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">🚛</div>
                <h3>Supply Chain</h3>
                <p>Logistics, resilience, optimization</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "supply-chain" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/healthcare-digital/' | relative_url }}" class="category-card new-sector">
                <div class="category-icon">🏥</div>
                <h3>Healthcare Digital</h3>
                <p>Telemedicine, patient engagement, AI</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "healthcare-digital" | size }} prompts</span>
                <span class="new-badge">NEW</span>
            </a>
            
            <a href="{{ '/categories/research-workflows/' | relative_url }}" class="category-card">
                <div class="category-icon">
                    <i class="fas fa-microscope"></i>
                </div>
                <h3>Research Workflows</h3>
                <p>Scientific inquiry, literature review</p>
                <span class="prompt-count">{{ site.prompts | where: "category", "research-workflows" | size }} prompts</span>
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
                            data-clipboard-text="{{ prompt.prompt | strip | escape }}">
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
            <h2>Transform Your Enterprise with AI-Powered Solutions</h2>
            <p>Join industry leaders leveraging our 278+ expert-crafted prompts across cutting-edge sectors worth $50+ trillion in market opportunities. From biotechnology breakthroughs to space economy innovations.</p>
            <div class="cta-stats">
                <div class="cta-stat">
                    <span class="cta-stat-number">278+</span>
                    <span class="cta-stat-label">Enterprise Prompts</span>
                </div>
                <div class="cta-stat">
                    <span class="cta-stat-number">18</span>
                    <span class="cta-stat-label">Specialty Sectors</span>
                </div>
                <div class="cta-stat">
                    <span class="cta-stat-number">350+</span>
                    <span class="cta-stat-label">Lines Per Output</span>
                </div>
            </div>
            <div class="cta-actions">
                <a href="{{ '/categories/' | relative_url }}" class="btn btn-primary btn-large">
                    Explore All 18 Sectors
                    <i class="fas fa-rocket"></i>
                </a>
                <a href="{{ site.github_url }}" class="btn btn-secondary btn-large">
                    <i class="fab fa-github"></i>
                    Open Source on GitHub
                </a>
            </div>
        </div>
    </div>
</div>