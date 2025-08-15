---
layout: default
title: Home
description: "Search and discover 278+ professional AI prompts across specialized sectors. Easy-to-use document library with instant search."
---

<div class="search-hero">
    <div class="container">
        <div class="search-header">
            <h1 class="search-title">Useful AI Prompts</h1>
            <p class="search-subtitle">Search 278+ expert AI prompts instantly</p>
        </div>
        
        <div class="search-container">
            <div class="search-input-wrapper">
                <input type="text" id="searchInput" class="search-input" placeholder="Search prompts... (e.g., strategic planning, customer service)" autocomplete="off">
                <button class="search-btn" id="searchBtn">
                    <i class="fas fa-search"></i>
                </button>
            </div>
            <div class="search-suggestions" id="searchSuggestions"></div>
        </div>
        
        <div class="quick-stats">
            <span class="stat"><strong>{{ site.prompts.size }}</strong> prompts</span>
            <span class="stat"><strong>18</strong> categories</span>
            <span class="stat"><strong>350+</strong> lines each</span>
        </div>
    </div>
</div>

<div class="results-section">
    <div class="container">
        <div class="filters-bar" id="filtersBar">
            <button class="filter-chip active" data-category="all">All Categories</button>
            <button class="filter-chip" data-category="business">💼 Business</button>
            <button class="filter-chip" data-category="technical">💻 Technical</button>
            <button class="filter-chip" data-category="creative">🎨 Creative</button>
            <button class="filter-chip" data-category="analysis">📊 Analysis</button>
            <button class="filter-chip" data-category="planning">📋 Planning</button>
            <button class="filter-chip" data-category="blockchain">🔗 Blockchain</button>
            <button class="filter-chip" data-category="biotechnology">🧬 Biotech</button>
        </div>
        
        <div class="results-header" id="resultsHeader">
            <h2 id="resultsTitle">All Prompts</h2>
            <p id="resultsCount">Showing {{ site.prompts.size }} prompts</p>
        </div>
        
        <div class="results-grid" id="resultsGrid">
            {% for prompt in site.prompts %}
            <div class="prompt-result" data-category="{{ prompt.category }}" data-tags="{{ prompt.tags | join: ' ' | downcase }}" data-title="{{ prompt.title | downcase }}" data-description="{{ prompt.description | downcase }}">
                <div class="result-header">
                    <h3 class="result-title">
                        <a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a>
                    </h3>
                    <span class="result-category">{{ prompt.category | replace: '-', ' ' | capitalize }}</span>
                </div>
                
                {% if prompt.description %}
                <p class="result-description">{{ prompt.description | truncate: 120 }}</p>
                {% endif %}
                
                <div class="result-actions">
                    <a href="{{ prompt.url | relative_url }}" class="btn btn-primary btn-sm">View Prompt</a>
                    {% if prompt.prompt %}
                    <button class="btn btn-secondary btn-sm copy-btn" data-clipboard-text="{{ prompt.prompt | strip | escape }}">
                        <i class="fas fa-copy"></i> Copy
                    </button>
                    {% endif %}
                </div>
                
                {% if prompt.tags %}
                <div class="result-tags">
                    {% for tag in prompt.tags limit:3 %}
                        <span class="tag">{{ tag }}</span>
                    {% endfor %}
                    {% if prompt.tags.size > 3 %}
                        <span class="tag-more">+{{ prompt.tags.size | minus: 3 }} more</span>
                    {% endif %}
                </div>
                {% endif %}
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
// Search and filter functionality
const searchInput = document.getElementById('searchInput');
const resultsGrid = document.getElementById('resultsGrid');
const resultsTitle = document.getElementById('resultsTitle');
const resultsCount = document.getElementById('resultsCount');
const noResults = document.getElementById('noResults');
const filterChips = document.querySelectorAll('.filter-chip');
const prompts = document.querySelectorAll('.prompt-result');

let currentFilter = 'all';
let currentSearch = '';

// Search functionality
function performSearch() {
    const searchTerm = searchInput.value.toLowerCase().trim();
    currentSearch = searchTerm;
    
    let visibleCount = 0;
    
    prompts.forEach(prompt => {
        const title = prompt.dataset.title;
        const description = prompt.dataset.description || '';
        const tags = prompt.dataset.tags || '';
        const category = prompt.dataset.category;
        
        const matchesSearch = !searchTerm || 
            title.includes(searchTerm) || 
            description.includes(searchTerm) || 
            tags.includes(searchTerm);
            
        const matchesFilter = currentFilter === 'all' || 
            category.includes(currentFilter) ||
            (currentFilter === 'business' && ['management', 'leadership', 'planning', 'analysis'].some(cat => category.includes(cat))) ||
            (currentFilter === 'technical' && ['technical', 'development', 'security'].some(cat => category.includes(cat))) ||
            (currentFilter === 'creative' && ['creation', 'creativity', 'innovation'].some(cat => category.includes(cat)));
        
        if (matchesSearch && matchesFilter) {
            prompt.style.display = 'block';
            visibleCount++;
        } else {
            prompt.style.display = 'none';
        }
    });
    
    // Update results header
    if (searchTerm) {
        resultsTitle.textContent = `Search results for "${searchTerm}"`;
    } else if (currentFilter !== 'all') {
        const filterName = document.querySelector(`[data-category="${currentFilter}"]`).textContent;
        resultsTitle.textContent = filterName + ' Prompts';
    } else {
        resultsTitle.textContent = 'All Prompts';
    }
    
    resultsCount.textContent = `Showing ${visibleCount} prompt${visibleCount === 1 ? '' : 's'}`;
    
    // Show/hide no results
    if (visibleCount === 0) {
        resultsGrid.style.display = 'none';
        noResults.style.display = 'block';
    } else {
        resultsGrid.style.display = 'grid';
        noResults.style.display = 'none';
    }
}

// Search input events
searchInput.addEventListener('input', performSearch);
searchInput.addEventListener('keydown', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        performSearch();
    }
});

// Filter functionality
filterChips.forEach(chip => {
    chip.addEventListener('click', () => {
        // Update active state
        filterChips.forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        
        // Update filter
        currentFilter = chip.dataset.category;
        performSearch();
    });
});

// Copy functionality
document.addEventListener('click', async (e) => {
    if (e.target.closest('.copy-btn')) {
        const btn = e.target.closest('.copy-btn');
        const text = btn.dataset.clipboardText;
        
        try {
            await navigator.clipboard.writeText(text);
            const originalText = btn.innerHTML;
            btn.innerHTML = '<i class="fas fa-check"></i> Copied!';
            btn.classList.add('copied');
            
            setTimeout(() => {
                btn.innerHTML = originalText;
                btn.classList.remove('copied');
            }, 2000);
        } catch (err) {
            console.error('Copy failed:', err);
        }
    }
});

// Initial load
performSearch();
</script>