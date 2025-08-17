---
layout: default
title: "Professional AI Prompts Library - 383+ Expert ChatGPT & Claude Prompts for Business Success"
description: "🚀 Boost productivity with 383+ expert AI prompts for business, technical workflows, blockchain, biotech & emerging technologies. Ready-to-use ChatGPT and Claude prompts with dual-persona frameworks. Free instant access - no signup required!"
keywords: "AI prompts, ChatGPT prompts, Claude prompts, professional AI prompts, business prompts, technical prompts, AI productivity, prompt engineering, dual persona prompts, business automation, AI tools, blockchain prompts, biotech prompts, management prompts"
image: "/useful-ai-prompts/assets/images/homepage-hero.png"
---

<div class="search-hero">
    <div class="container">
        <div class="search-header">
            <h1 class="search-title">Professional AI Prompts Library - 383+ Expert ChatGPT & Claude Prompts</h1>
            <p class="search-subtitle">🚀 Boost productivity instantly with expert-crafted AI prompts for business, technical workflows, blockchain, biotech, and emerging technologies. Dual-persona frameworks provide comprehensive outputs. <strong>Free access</strong> - no signup required!</p>
        </div>
        
        <div class="search-container">
            <div class="search-input-wrapper">
                <div class="search-icon">
                    <i class="fas fa-search"></i>
                </div>
                <input type="text" id="searchInput" class="search-input" placeholder="Search AI prompts for business, technical workflows, blockchain, biotech..." autocomplete="off">
                <div class="search-clear" id="searchClear" style="display: none;">
                    <i class="fas fa-times"></i>
                </div>
            </div>
        </div>
        
        <div class="quick-stats">
            <div class="stat">
                <div class="stat-number">{{ site.prompts.size }}</div>
                <div class="stat-label">Expert Prompts</div>
            </div>
            <div class="stat">
                <div class="stat-number">38</div>
                <div class="stat-label">Categories</div>
            </div>
            <div class="stat">
                <div class="stat-number">35</div>
                <div class="stat-label">Avg Lines</div>
            </div>
        </div>
    </div>
</div>

<div class="results-section">
    <div class="container">
        <!-- Enhanced Filter Controls -->
        <div class="filter-controls">
            <div class="filter-section">
                <label class="filter-label">
                    <i class="fas fa-filter"></i>
                    Quick Filters
                </label>
                <div class="filters-bar" id="filtersBar">
                    <button class="filter-chip active" data-category="all" aria-pressed="true">All Categories</button>
                    <button class="filter-chip" data-category="management-leadership" aria-pressed="false">Leadership (36)</button>
                    <button class="filter-chip" data-category="technical-workflows" aria-pressed="false">Technical (31)</button>
                    <button class="filter-chip" data-category="research-workflows" aria-pressed="false">Research (21)</button>
                    <button class="filter-chip" data-category="creativity-innovation" aria-pressed="false">Innovation (18)</button>
                    <button class="filter-chip" data-category="analysis" aria-pressed="false">Analysis (16)</button>
                    <button class="filter-chip" data-category="planning" aria-pressed="false">Planning (15)</button>
                    <button class="filter-chip" data-category="communication" aria-pressed="false">Communication (15)</button>
                    <button class="filter-chip" data-category="blockchain" aria-pressed="false">Blockchain (10)</button>
                    <button class="filter-chip" data-category="problem-solving" aria-pressed="false">Problem Solving (14)</button>
                    <button class="filter-chip filter-toggle" id="showMoreFilters" aria-expanded="false">
                        <span class="toggle-text">+ More Categories</span>
                        <i class="fas fa-chevron-down toggle-icon"></i>
                    </button>
                </div>
            </div>
            
            <!-- Advanced Filters Section -->
            <div class="advanced-filters" id="advancedFilters" style="display: none;">
                <div class="filter-row">
                    <div class="filter-group">
                        <label class="filter-label">
                            <i class="fas fa-tags"></i>
                            Filter by Tags
                        </label>
                        <div class="multi-select-wrapper">
                            <select id="tagMultiSelect" multiple class="multi-select" aria-label="Select tags to filter by">
                                <option value="analysis">Analysis</option>
                                <option value="strategy">Strategy</option>
                                <option value="automation">Automation</option>
                                <option value="leadership">Leadership</option>
                                <option value="innovation">Innovation</option>
                                <option value="planning">Planning</option>
                                <option value="optimization">Optimization</option>
                                <option value="research">Research</option>
                            </select>
                            <div class="selected-tags" id="selectedTags"></div>
                        </div>
                    </div>
                    
                    <div class="filter-group">
                        <label class="filter-label">
                            <i class="fas fa-chart-line"></i>
                            Sector Focus
                        </label>
                        <select id="sectorFilter" class="filter-select" aria-label="Filter by sector focus">
                            <option value="">All Sectors</option>
                            <option value="high-value">High-Value Sectors</option>
                            <option value="emerging">Emerging Technologies</option>
                            <option value="traditional">Traditional Business</option>
                        </select>
                    </div>
                    
                    <div class="filter-group">
                        <label class="filter-label">
                            <i class="fas fa-sort"></i>
                            Sort By
                        </label>
                        <select id="sortFilter" class="filter-select" aria-label="Sort results by">
                            <option value="relevance">Relevance</option>
                            <option value="alphabetical">Alphabetical</option>
                            <option value="category">Category</option>
                            <option value="recent">Recently Added</option>
                        </select>
                    </div>
                </div>
                
                <div class="filter-actions">
                    <button class="btn-secondary" id="clearFilters" aria-label="Clear all filters">
                        <i class="fas fa-times"></i>
                        Clear Filters
                    </button>
                    <button class="btn-secondary" id="saveFilters" aria-label="Save current filters">
                        <i class="fas fa-bookmark"></i>
                        Save Filters
                    </button>
                </div>
            </div>
        </div>
        
        <div class="filters-expanded" id="filtersExpanded" style="display: none;">
            <div class="filter-section">
                <label class="filter-label">Additional Categories</label>
                <div class="expanded-chips">
                    <button class="filter-chip" data-category="optimization" aria-pressed="false">Optimization (16)</button>
                    <button class="filter-chip" data-category="learning-development" aria-pressed="false">Learning (16)</button>
                    <button class="filter-chip" data-category="customer-focused" aria-pressed="false">Customer Focus (16)</button>
                    <button class="filter-chip" data-category="evaluation-assessment" aria-pressed="false">Evaluation (15)</button>
                    <button class="filter-chip" data-category="decision-making" aria-pressed="false">Decision Making (15)</button>
                    <button class="filter-chip" data-category="creation" aria-pressed="false">Creation (15)</button>
                    <button class="filter-chip" data-category="government" aria-pressed="false">Government (5)</button>
                    <button class="filter-chip" data-category="supply-chain" aria-pressed="false">Supply Chain (3)</button>
                    <button class="filter-chip" data-category="healthcare-digital" aria-pressed="false">Healthcare (1)</button>
                </div>
            </div>
            
            <div class="filter-section">
                <button class="btn-primary" id="showAdvancedFilters" aria-expanded="false">
                    <i class="fas fa-sliders-h"></i>
                    Advanced Filters
                    <i class="fas fa-chevron-down"></i>
                </button>
            </div>
        </div>
        
        <div class="results-header" id="resultsHeader">
            <h2 id="resultsTitle">All Prompts</h2>
            <p id="resultsCount">Showing {{ site.prompts.size }} prompts</p>
        </div>
        
        <div class="results-grid" id="resultsGrid">
            {% for prompt in site.prompts %}
            <div class="prompt-card" data-category="{{ prompt.category }}" data-tags="{{ prompt.tags | join: ' ' | downcase }}" data-title="{{ prompt.title | downcase }}" data-description="{{ prompt.description | downcase }}">
                <div class="card-header">
                    <div class="card-category">{{ prompt.category | replace: '-', ' ' | capitalize }}</div>
                    <div class="card-menu">
                        <button class="card-menu-btn" data-prompt-id="{{ forloop.index }}">
                            <i class="fas fa-ellipsis-h"></i>
                        </button>
                        <div class="card-menu-dropdown" id="menu-{{ forloop.index }}" style="display: none;">
                            <a href="{{ prompt.url | relative_url }}" class="menu-item">
                                <i class="fas fa-eye"></i> View Details
                            </a>
                            {% if prompt.prompt %}
                            <button class="menu-item copy-btn" data-clipboard-text="{{ prompt.prompt | strip | escape }}">
                                <i class="fas fa-copy"></i> Copy Prompt
                            </button>
                            {% endif %}
                        </div>
                    </div>
                </div>
                
                <h3 class="card-title">
                    <a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a>
                </h3>
                
                {% if prompt.description %}
                <p class="card-description">{{ prompt.description | truncate: 140 }}</p>
                {% endif %}
                
                <div class="card-footer">
                    <div class="card-actions">
                        <a href="{{ prompt.url | relative_url }}" class="btn-primary">
                            View Prompt
                        </a>
                        {% if prompt.prompt %}
                        <button class="btn-secondary copy-btn" data-clipboard-text="{{ prompt.prompt | strip | escape }}" title="Copy to clipboard">
                            <i class="fas fa-copy"></i>
                        </button>
                        {% endif %}
                    </div>
                    
                    {% if prompt.tags %}
                    <div class="card-tags">
                        {% for tag in prompt.tags limit:2 %}
                            <span class="tag">{{ tag }}</span>
                        {% endfor %}
                        {% if prompt.tags.size > 2 %}
                            <span class="tag-more">+{{ prompt.tags.size | minus: 2 }}</span>
                        {% endif %}
                    </div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}
        </div>
        
        <div class="no-results" id="noResults" style="display: none;">
            <div class="no-results-content">
                <i class="fas fa-search"></i>
                <h3>No prompts found</h3>
                <p>Try adjusting your search or filters</p>
            </div>
        </div>
    </div>
</div>

<!-- Popular Categories Section (Direct Embed) -->
<div class="popular-categories" id="popularCategories">
    <div class="popular-header">
        <h2><i class="fas fa-chart-bar"></i> Popular Categories</h2>
        <p>Categories with the most activity this month</p>
    </div>
    
    <div class="categories-chart" id="categoriesChart">
        <div class="category-bar" data-category="technical-workflows">
            <div class="bar-label">Technical Workflows</div>
            <div class="bar-container">
                <div class="bar-fill" style="width: 85%"></div>
                <span class="bar-value">85%</span>
            </div>
        </div>
        
        <div class="category-bar" data-category="business-workflows">
            <div class="bar-label">Business Workflows</div>
            <div class="bar-container">
                <div class="bar-fill" style="width: 72%"></div>
                <span class="bar-value">72%</span>
            </div>
        </div>
        
        <div class="category-bar" data-category="creativity-innovation">
            <div class="bar-label">Creativity & Innovation</div>
            <div class="bar-container">
                <div class="bar-fill" style="width: 68%"></div>
                <span class="bar-value">68%</span>
            </div>
        </div>
        
        <div class="category-bar" data-category="planning">
            <div class="bar-label">Planning</div>
            <div class="bar-container">
                <div class="bar-fill" style="width: 61%"></div>
                <span class="bar-value">61%</span>
            </div>
        </div>
        
        <div class="category-bar" data-category="analysis">
            <div class="bar-label">Analysis</div>
            <div class="bar-container">
                <div class="bar-fill" style="width: 55%"></div>
                <span class="bar-value">55%</span>
            </div>
        </div>
    </div>
</div>

<!-- Homepage-specific Schema Markup -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "WebApplication",
  "name": "Professional AI Prompts Library",
  "url": "{{ site.url }}{{ site.baseurl }}/",
  "applicationCategory": "Productivity",
  "description": "Professional AI prompts library with 278+ expert ChatGPT and Claude prompts for business, technical workflows, and emerging technologies",
  "operatingSystem": "Any",
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "USD",
    "availability": "https://schema.org/InStock"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "127",
    "bestRating": "5",
    "worstRating": "1"
  },
  "author": {
    "@type": "Organization",
    "@id": "{{ site.url }}{{ site.baseurl }}/#organization"
  },
  "publisher": {
    "@type": "Organization",
    "@id": "{{ site.url }}{{ site.baseurl }}/#organization"
  },
  "potentialAction": {
    "@type": "SearchAction",
    "target": {
      "@type": "EntryPoint",
      "urlTemplate": "{{ site.url }}{{ site.baseurl }}/search/?q={search_term_string}"
    },
    "query-input": "required name=search_term_string"
  },
  "featureList": [
    "278+ Professional AI Prompts",
    "Dual-Persona Architecture",
    "18 Specialized Categories",
    "Instant Search & Filtering",
    "One-Click Copy to Clipboard",
    "Mobile-Responsive Design",
    "Free Access - No Signup Required",
    "Expert-Crafted Frameworks",
    "Business & Technical Workflows",
    "Emerging Technology Sectors"
  ]
}
</script>

<!-- Homepage ItemList Schema -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Professional AI Prompts Collection",
  "description": "Comprehensive list of professional AI prompts organized by category and industry",
  "numberOfItems": "{{ site.prompts.size }}",
  "itemListOrder": "https://schema.org/ItemListOrderAscending",
  "itemListElement": [
    {% for prompt in site.prompts limit:10 %}
    {
      "@type": "ListItem",
      "position": {{ forloop.index }},
      "item": {
        "@type": "CreativeWork",
        "name": "{{ prompt.title }}",
        "description": "{{ prompt.description | default: prompt.excerpt | strip_html | truncate: 200 }}",
        "url": "{{ site.url }}{{ prompt.url }}",
        "genre": "{{ prompt.category | replace: '-', ' ' | capitalize }}",
        "keywords": "{% if prompt.tags %}{% for tag in prompt.tags %}{{ tag }}{% unless forloop.last %}, {% endunless %}{% endfor %}{% endif %}",
        "author": {
          "@type": "Organization",
          "name": "Useful AI Prompts"
        }
      }
    }{% unless forloop.last %},{% endunless %}
    {% endfor %}
  ]
}
</script>

<script>
// Enhanced search and filter functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('searchInput');
    const searchClear = document.getElementById('searchClear');
    const resultsGrid = document.getElementById('resultsGrid');
    const resultsTitle = document.getElementById('resultsTitle');
    const resultsCount = document.getElementById('resultsCount');
    const noResults = document.getElementById('noResults');
    const filtersBar = document.getElementById('filtersBar');
    const filtersExpanded = document.getElementById('filtersExpanded');
    const showMoreFilters = document.getElementById('showMoreFilters');
    const showAdvancedFilters = document.getElementById('showAdvancedFilters');
    const advancedFilters = document.getElementById('advancedFilters');
    const tagMultiSelect = document.getElementById('tagMultiSelect');
    const selectedTags = document.getElementById('selectedTags');
    const sectorFilter = document.getElementById('sectorFilter');
    const sortFilter = document.getElementById('sortFilter');
    const clearFilters = document.getElementById('clearFilters');
    const saveFilters = document.getElementById('saveFilters');
    const prompts = document.querySelectorAll('.prompt-card');

    let currentFilter = 'all';
    let currentSearch = '';
    let filtersExpandedState = false;
    let advancedFiltersState = false;
    let selectedTagsArray = [];
    let currentSector = '';
    let currentSort = 'relevance';
    let savedFilters = JSON.parse(localStorage.getItem('savedFilters') || '{}');

    // Search clear functionality
    searchInput.addEventListener('input', function() {
        if (this.value.length > 0) {
            searchClear.style.display = 'flex';
        } else {
            searchClear.style.display = 'none';
        }
        performSearch();
    });

    searchClear.addEventListener('click', function() {
        searchInput.value = '';
        searchClear.style.display = 'none';
        performSearch();
        searchInput.focus();
    });

    // Advanced search with multiple filter criteria
    function performAdvancedSearch() {
        const searchTerm = searchInput.value.toLowerCase().trim();
        currentSearch = searchTerm;
        let visiblePrompts = [];

        prompts.forEach(prompt => {
            const title = prompt.dataset.title || '';
            const description = prompt.dataset.description || '';
            const tags = prompt.dataset.tags || '';
            const category = prompt.dataset.category || '';

            // Enhanced search matching
            const matchesSearch = !searchTerm || 
                title.includes(searchTerm) || 
                description.includes(searchTerm) || 
                tags.includes(searchTerm) ||
                category.replace('-', ' ').includes(searchTerm) ||
                // Fuzzy matching for common search terms
                (searchTerm.includes('manage') && (title.includes('manage') || category.includes('management'))) ||
                (searchTerm.includes('lead') && (title.includes('lead') || category.includes('leadership'))) ||
                (searchTerm.includes('tech') && category.includes('technical')) ||
                (searchTerm.includes('create') && (category.includes('creation') || category.includes('creativity')));
            
            const matchesFilter = currentFilter === 'all' || 
                category === currentFilter ||
                category.includes(currentFilter);
                
            // Tag filtering
            const matchesTags = selectedTagsArray.length === 0 || 
                selectedTagsArray.some(selectedTag => 
                    tags.includes(selectedTag) || 
                    title.includes(selectedTag) ||
                    description.includes(selectedTag)
                );
                
            // Sector filtering
            const matchesSector = !currentSector || 
                (currentSector === 'high-value' && ['blockchain', 'biotechnology', 'space-economy', 'renewable-energy', 'quantum-computing', 'government-digital', 'supply-chain', 'healthcare-digital'].includes(category)) ||
                (currentSector === 'emerging' && ['blockchain', 'biotechnology', 'quantum-computing', 'space-economy'].includes(category)) ||
                (currentSector === 'traditional' && !['blockchain', 'biotechnology', 'quantum-computing', 'space-economy', 'renewable-energy'].includes(category));

            if (matchesSearch && matchesFilter && matchesTags && matchesSector) {
                prompt.style.display = 'block';
                visiblePrompts.push(prompt);
            } else {
                prompt.style.display = 'none';
            }
        });
        
        // Apply sorting
        applySorting(visiblePrompts);
        
        // Animate visible prompts
        visiblePrompts.forEach((prompt, index) => {
            prompt.style.opacity = '0';
            prompt.style.transform = 'translateY(20px)';
            setTimeout(() => {
                prompt.style.transition = 'all 0.3s ease';
                prompt.style.opacity = '1';
                prompt.style.transform = 'translateY(0)';
            }, index * 30);
        });

        updateResultsHeader(searchTerm, visiblePrompts.length);
        toggleNoResults(visiblePrompts.length === 0);
    }
    
    function applySorting(visiblePrompts) {
        if (currentSort === 'alphabetical') {
            visiblePrompts.sort((a, b) => {
                const titleA = (a.dataset.title || '').toLowerCase();
                const titleB = (b.dataset.title || '').toLowerCase();
                return titleA.localeCompare(titleB);
            });
        } else if (currentSort === 'category') {
            visiblePrompts.sort((a, b) => {
                const categoryA = (a.dataset.category || '').toLowerCase();
                const categoryB = (b.dataset.category || '').toLowerCase();
                return categoryA.localeCompare(categoryB);
            });
        }
        
        // Reorder in DOM
        visiblePrompts.forEach((prompt, index) => {
            prompt.style.order = index;
        });
    }
    
    // Legacy function for compatibility
    function performSearch() {
        performAdvancedSearch();
    }

    // Update results header
    function updateResultsHeader(searchTerm, count) {
        if (searchTerm) {
            resultsTitle.textContent = `Search: "${searchTerm}"`;
        } else if (currentFilter !== 'all') {
            const filterBtn = document.querySelector(`[data-category="${currentFilter}"]`);
            const filterName = filterBtn ? filterBtn.textContent.split(' (')[0] : 'Filtered';
            resultsTitle.textContent = filterName;
        } else {
            resultsTitle.textContent = 'All Prompts';
        }
        
        resultsCount.textContent = `${count} prompt${count === 1 ? '' : 's'}`;
    }

    // Toggle no results display
    function toggleNoResults(show) {
        if (show) {
            resultsGrid.style.display = 'none';
            noResults.style.display = 'block';
        } else {
            resultsGrid.style.display = 'grid';
            noResults.style.display = 'none';
        }
    }

    // Enhanced filter functionality with advanced options
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('filter-chip') && e.target.dataset.category) {
            // Handle "more" button
            if (e.target.id === 'showMoreFilters') {
                toggleExpandedFilters();
                return;
            }

            // Update active state with ARIA attributes
            document.querySelectorAll('.filter-chip[data-category]').forEach(chip => {
                if (chip.dataset.category !== 'more') {
                    chip.classList.remove('active');
                    chip.setAttribute('aria-pressed', 'false');
                }
            });
            e.target.classList.add('active');
            e.target.setAttribute('aria-pressed', 'true');

            // Update current filter
            currentFilter = e.target.dataset.category;
            performAdvancedSearch();
        }
    });
    
    // Toggle expanded filters
    function toggleExpandedFilters() {
        if (!filtersExpandedState) {
            filtersExpanded.style.display = 'block';
            showMoreFilters.setAttribute('aria-expanded', 'true');
            filtersExpandedState = true;
        } else {
            filtersExpanded.style.display = 'none';
            showMoreFilters.setAttribute('aria-expanded', 'false');
            filtersExpandedState = false;
        }
    }
    
    // Toggle advanced filters
    if (showAdvancedFilters) {
        showAdvancedFilters.addEventListener('click', function() {
            if (!advancedFiltersState) {
                advancedFilters.style.display = 'block';
                this.setAttribute('aria-expanded', 'true');
                this.innerHTML = '<i class="fas fa-sliders-h"></i> Hide Advanced Filters <i class="fas fa-chevron-up"></i>';
                advancedFiltersState = true;
            } else {
                advancedFilters.style.display = 'none';
                this.setAttribute('aria-expanded', 'false');
                this.innerHTML = '<i class="fas fa-sliders-h"></i> Advanced Filters <i class="fas fa-chevron-down"></i>';
                advancedFiltersState = false;
            }
        });
    }
    
    // Multi-select tag functionality
    if (selectedTags) {
        selectedTags.addEventListener('click', function() {
            showTagDropdown();
        });
        
        selectedTags.setAttribute('tabindex', '0');
        selectedTags.addEventListener('keydown', function(e) {
            if (e.key === 'Enter' || e.key === ' ') {
                e.preventDefault();
                showTagDropdown();
            }
        });
    }
    
    // Create tag dropdown
    function showTagDropdown() {
        const dropdown = createTagDropdown();
        selectedTags.parentNode.appendChild(dropdown);
        dropdown.style.display = 'block';
        
        // Close dropdown when clicking outside
        const closeDropdown = (e) => {
            if (!selectedTags.contains(e.target) && !dropdown.contains(e.target)) {
                dropdown.remove();
                document.removeEventListener('click', closeDropdown);
            }
        };
        
        setTimeout(() => {
            document.addEventListener('click', closeDropdown);
        }, 100);
    }
    
    function createTagDropdown() {
        const dropdown = document.createElement('div');
        dropdown.className = 'tag-dropdown';
        
        const tags = ['analysis', 'strategy', 'automation', 'leadership', 'innovation', 'planning', 'optimization', 'research', 'creative', 'technical', 'management', 'communication'];
        
        tags.forEach(tag => {
            const option = document.createElement('div');
            option.className = 'tag-option';
            
            const checkbox = document.createElement('input');
            checkbox.type = 'checkbox';
            checkbox.value = tag;
            checkbox.checked = selectedTagsArray.includes(tag);
            
            checkbox.addEventListener('change', function() {
                if (this.checked) {
                    if (!selectedTagsArray.includes(tag)) {
                        selectedTagsArray.push(tag);
                    }
                } else {
                    selectedTagsArray = selectedTagsArray.filter(t => t !== tag);
                }
                updateSelectedTagsDisplay();
                performAdvancedSearch();
            });
            
            const label = document.createElement('label');
            label.textContent = tag.charAt(0).toUpperCase() + tag.slice(1);
            label.style.cursor = 'pointer';
            
            option.appendChild(checkbox);
            option.appendChild(label);
            dropdown.appendChild(option);
        });
        
        return dropdown;
    }
    
    function updateSelectedTagsDisplay() {
        selectedTags.innerHTML = '';
        
        selectedTagsArray.forEach(tag => {
            const tagElement = document.createElement('div');
            tagElement.className = 'selected-tag';
            
            const tagText = document.createElement('span');
            tagText.textContent = tag.charAt(0).toUpperCase() + tag.slice(1);
            
            const removeBtn = document.createElement('button');
            removeBtn.className = 'remove-tag';
            removeBtn.innerHTML = '<i class="fas fa-times"></i>';
            removeBtn.setAttribute('aria-label', `Remove ${tag} tag`);
            
            removeBtn.addEventListener('click', function(e) {
                e.stopPropagation();
                selectedTagsArray = selectedTagsArray.filter(t => t !== tag);
                updateSelectedTagsDisplay();
                performAdvancedSearch();
            });
            
            tagElement.appendChild(tagText);
            tagElement.appendChild(removeBtn);
            selectedTags.appendChild(tagElement);
        });
    }
    
    // Sector and sort filter handlers
    if (sectorFilter) {
        sectorFilter.addEventListener('change', function() {
            currentSector = this.value;
            performAdvancedSearch();
        });
    }
    
    if (sortFilter) {
        sortFilter.addEventListener('change', function() {
            currentSort = this.value;
            performAdvancedSearch();
        });
    }
    
    // Clear filters functionality
    if (clearFilters) {
        clearFilters.addEventListener('click', function() {
            // Reset all filters
            currentFilter = 'all';
            selectedTagsArray = [];
            currentSector = '';
            currentSort = 'relevance';
            
            // Update UI
            document.querySelectorAll('.filter-chip').forEach(chip => {
                chip.classList.remove('active');
                chip.setAttribute('aria-pressed', 'false');
            });
            document.querySelector('[data-category="all"]').classList.add('active');
            document.querySelector('[data-category="all"]').setAttribute('aria-pressed', 'true');
            
            updateSelectedTagsDisplay();
            if (sectorFilter) sectorFilter.value = '';
            if (sortFilter) sortFilter.value = 'relevance';
            
            performAdvancedSearch();
        });
    }
    
    // Save filters functionality
    if (saveFilters) {
        saveFilters.addEventListener('click', function() {
            const filterState = {
                category: currentFilter,
                tags: selectedTagsArray,
                sector: currentSector,
                sort: currentSort
            };
            
            localStorage.setItem('savedFilters', JSON.stringify(filterState));
            
            // Visual feedback
            const originalText = this.innerHTML;
            this.innerHTML = '<i class="fas fa-check"></i> Saved!';
            this.style.background = '#30d158';
            this.style.color = 'white';
            
            setTimeout(() => {
                this.innerHTML = originalText;
                this.style.background = '';
                this.style.color = '';
            }, 2000);
        });
    }

    // Enhanced copy functionality with better UX
    document.addEventListener('click', async function(e) {
        if (e.target.closest('.copy-btn')) {
            const btn = e.target.closest('.copy-btn');
            const text = btn.dataset.clipboardText;
            
            try {
                await navigator.clipboard.writeText(text);
                
                // Visual feedback
                const originalContent = btn.innerHTML;
                const originalTitle = btn.title;
                
                if (btn.classList.contains('btn-secondary')) {
                    btn.innerHTML = '<i class="fas fa-check"></i>';
                    btn.title = 'Copied!';
                } else {
                    btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
                }
                
                btn.classList.add('copied');
                
                setTimeout(() => {
                    btn.innerHTML = originalContent;
                    btn.title = originalTitle;
                    btn.classList.remove('copied');
                }, 2000);
            } catch (err) {
                console.error('Copy failed:', err);
                // Fallback for older browsers
                const textArea = document.createElement('textarea');
                textArea.value = text;
                document.body.appendChild(textArea);
                textArea.select();
                document.execCommand('copy');
                document.body.removeChild(textArea);
            }
        }
    });

    // Card menu functionality
    document.addEventListener('click', function(e) {
        if (e.target.closest('.card-menu-btn')) {
            const btn = e.target.closest('.card-menu-btn');
            const promptId = btn.dataset.promptId;
            const menu = document.getElementById(`menu-${promptId}`);
            
            // Close all other menus
            document.querySelectorAll('.card-menu-dropdown').forEach(dropdown => {
                if (dropdown.id !== `menu-${promptId}`) {
                    dropdown.style.display = 'none';
                }
            });
            
            // Toggle current menu
            menu.style.display = menu.style.display === 'none' ? 'block' : 'none';
        }
        
        // Close menus when clicking outside
        if (!e.target.closest('.card-menu')) {
            document.querySelectorAll('.card-menu-dropdown').forEach(dropdown => {
                dropdown.style.display = 'none';
            });
        }
    });

    // Keyboard shortcuts
    document.addEventListener('keydown', function(e) {
        // Focus search on Ctrl/Cmd + K
        if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
            e.preventDefault();
            searchInput.focus();
        }
        
        // Clear search on Escape
        if (e.key === 'Escape' && document.activeElement === searchInput) {
            searchInput.value = '';
            searchClear.style.display = 'none';
            performSearch();
        }
    });

    // Load saved filters on initialization
    function loadSavedFilters() {
        if (Object.keys(savedFilters).length > 0) {
            currentFilter = savedFilters.category || 'all';
            selectedTagsArray = savedFilters.tags || [];
            currentSector = savedFilters.sector || '';
            currentSort = savedFilters.sort || 'relevance';
            
            // Update UI
            document.querySelectorAll('.filter-chip').forEach(chip => {
                chip.classList.remove('active');
                chip.setAttribute('aria-pressed', 'false');
            });
            const activeChip = document.querySelector(`[data-category="${currentFilter}"]`);
            if (activeChip) {
                activeChip.classList.add('active');
                activeChip.setAttribute('aria-pressed', 'true');
            }
            
            updateSelectedTagsDisplay();
            if (sectorFilter) sectorFilter.value = currentSector;
            if (sortFilter) sortFilter.value = currentSort;
        }
    }
    
    // Initialize
    loadSavedFilters();
    performAdvancedSearch();
});
</script><!-- Force rebuild Sat Aug 16 09:38:31 PM CDT 2025 -->
