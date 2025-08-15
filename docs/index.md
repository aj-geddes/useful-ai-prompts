---
layout: default
title: Home
description: "Search and discover 278+ professional AI prompts across specialized sectors. Easy-to-use document library with instant search."
---

<div class="search-hero">
    <div class="container">
        <div class="search-header">
            <h1 class="search-title">Useful AI Prompts</h1>
            <p class="search-subtitle">Professional AI prompts for every workflow. Clean, powerful, instant.</p>
        </div>
        
        <div class="search-container">
            <div class="search-input-wrapper">
                <div class="search-icon">
                    <i class="fas fa-search"></i>
                </div>
                <input type="text" id="searchInput" class="search-input" placeholder="Search 278 expert prompts..." autocomplete="off">
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
                <div class="stat-number">18</div>
                <div class="stat-label">Categories</div>
            </div>
            <div class="stat">
                <div class="stat-number">350+</div>
                <div class="stat-label">Lines Each</div>
            </div>
        </div>
    </div>
</div>

<div class="results-section">
    <div class="container">
        <div class="filters-bar" id="filtersBar">
            <button class="filter-chip active" data-category="all">All Categories</button>
            <button class="filter-chip" data-category="management-leadership">Leadership (36)</button>
            <button class="filter-chip" data-category="technical-workflows">Technical (31)</button>
            <button class="filter-chip" data-category="research-workflows">Research (21)</button>
            <button class="filter-chip" data-category="creativity-innovation">Innovation (18)</button>
            <button class="filter-chip" data-category="analysis">Analysis (16)</button>
            <button class="filter-chip" data-category="planning">Planning (15)</button>
            <button class="filter-chip" data-category="communication">Communication (15)</button>
            <button class="filter-chip" data-category="blockchain">Blockchain (10)</button>
            <button class="filter-chip" data-category="problem-solving">Problem Solving (14)</button>
            <button class="filter-chip" data-category="more" id="showMoreFilters">+ More Categories</button>
        </div>
        
        <div class="filters-expanded" id="filtersExpanded" style="display: none;">
            <button class="filter-chip" data-category="optimization">Optimization (16)</button>
            <button class="filter-chip" data-category="learning-development">Learning (16)</button>
            <button class="filter-chip" data-category="customer-focused">Customer Focus (16)</button>
            <button class="filter-chip" data-category="evaluation-assessment">Evaluation (15)</button>
            <button class="filter-chip" data-category="decision-making">Decision Making (15)</button>
            <button class="filter-chip" data-category="creation">Creation (15)</button>
            <button class="filter-chip" data-category="government">Government (5)</button>
            <button class="filter-chip" data-category="supply-chain">Supply Chain (3)</button>
            <button class="filter-chip" data-category="healthcare-digital">Healthcare (1)</button>
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
    const prompts = document.querySelectorAll('.prompt-card');

    let currentFilter = 'all';
    let currentSearch = '';
    let filtersExpandedState = false;

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

    // Enhanced search functionality with fuzzy matching
    function performSearch() {
        const searchTerm = searchInput.value.toLowerCase().trim();
        currentSearch = searchTerm;
        let visibleCount = 0;

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

            if (matchesSearch && matchesFilter) {
                prompt.style.display = 'block';
                // Add smooth fade-in animation
                prompt.style.opacity = '0';
                prompt.style.transform = 'translateY(20px)';
                setTimeout(() => {
                    prompt.style.transition = 'all 0.3s ease';
                    prompt.style.opacity = '1';
                    prompt.style.transform = 'translateY(0)';
                }, visibleCount * 50);
                visibleCount++;
            } else {
                prompt.style.display = 'none';
            }
        });

        updateResultsHeader(searchTerm, visibleCount);
        toggleNoResults(visibleCount === 0);
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

    // Filter functionality with smooth animations
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('filter-chip') && e.target.dataset.category) {
            // Handle "more" button
            if (e.target.id === 'showMoreFilters') {
                if (!filtersExpandedState) {
                    document.getElementById('filtersExpanded').style.display = 'flex';
                    e.target.textContent = '- Less Categories';
                    filtersExpandedState = true;
                } else {
                    document.getElementById('filtersExpanded').style.display = 'none';
                    e.target.textContent = '+ More Categories';
                    filtersExpandedState = false;
                }
                return;
            }

            // Update active state with smooth transition
            document.querySelectorAll('.filter-chip').forEach(chip => {
                chip.classList.remove('active');
            });
            e.target.classList.add('active');

            // Update current filter
            currentFilter = e.target.dataset.category;
            performSearch();
        }
    });

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

    // Initialize
    performSearch();
});
</script>