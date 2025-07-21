---
layout: default
title: Search Prompts
description: "Search through 200+ AI prompts to find exactly what you need. Filter by category, tags, or keywords."
---

<div class="search-page">
    <div class="container">
        <div class="search-header">
            <h1 class="page-title">Search Prompts</h1>
            <p class="page-description">
                Find the perfect AI prompt from our collection of 200+ professional prompts. 
                Search by keyword, category, or tag to discover exactly what you need.
            </p>
        </div>
        
        <div class="search-main">
            <div class="search-form">
                <div class="search-input-container">
                    <input type="text" 
                           id="searchPageInput" 
                           class="search-input-main" 
                           placeholder="Search prompts by keyword, category, or use case..."
                           autocomplete="off">
                    <button class="search-button" onclick="document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                        <i class="fas fa-search"></i>
                    </button>
                </div>
                <div class="search-tips">
                    <p><strong>Search tips:</strong> Try keywords like "analysis", "presentation", "debugging", or "strategy"</p>
                </div>
            </div>
            
            <div class="search-filters">
                <div class="filter-section">
                    <h3>Quick Filters</h3>
                    <div class="quick-filters">
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='analysis'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-chart-bar"></i> Analysis
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='creation'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-palette"></i> Creation
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='planning'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-calendar-alt"></i> Planning
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='communication'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-comments"></i> Communication
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='problem solving'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-tools"></i> Problem Solving
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='decision making'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-balance-scale"></i> Decision Making
                        </button>
                    </div>
                </div>
            </div>
            
            <div class="search-results-section">
                <div id="searchPageResults" class="search-results-container">
                    <div class="search-placeholder">
                        <i class="fas fa-search"></i>
                        <h3>Ready to Search</h3>
                        <p>Enter a search term above to find relevant prompts from our comprehensive collection.</p>
                        
                        <div class="search-examples">
                            <h4>Popular Searches:</h4>
                            <div class="example-searches">
                                <button class="example-search" onclick="document.getElementById('searchPageInput').value='market research'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                                    market research
                                </button>
                                <button class="example-search" onclick="document.getElementById('searchPageInput').value='content writing'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                                    content writing
                                </button>
                                <button class="example-search" onclick="document.getElementById('searchPageInput').value='project management'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                                    project management
                                </button>
                                <button class="example-search" onclick="document.getElementById('searchPageInput').value='debugging'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                                    debugging
                                </button>
                                <button class="example-search" onclick="document.getElementById('searchPageInput').value='presentation'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                                    presentation
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="popular-tags-section">
                <div id="popularTags"></div>
            </div>
        </div>
        
        <div class="search-help">
            <h2>Search Help</h2>
            <div class="help-grid">
                <div class="help-item">
                    <h3><i class="fas fa-keyboard"></i> Keyboard Shortcuts</h3>
                    <ul>
                        <li><kbd>Ctrl</kbd> + <kbd>K</kbd> - Open search from anywhere</li>
                        <li><kbd>Esc</kbd> - Close search overlay</li>
                    </ul>
                </div>
                
                <div class="help-item">
                    <h3><i class="fas fa-filter"></i> Search Tips</h3>
                    <ul>
                        <li>Use specific keywords like "SWOT analysis" or "user research"</li>
                        <li>Search by category names like "communication" or "planning"</li>
                        <li>Try use case terms like "debugging" or "presentation"</li>
                    </ul>
                </div>
                
                <div class="help-item">
                    <h3><i class="fas fa-tags"></i> Browse by Category</h3>
                    <ul>
                        <li><a href="/categories/">View all categories</a></li>
                        <li><a href="/categories/analysis/">Analysis prompts</a></li>
                        <li><a href="/categories/creation/">Creation prompts</a></li>
                        <li><a href="/categories/technical-workflows/">Technical prompts</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.search-page {
    padding: 2rem 0;
}

.search-header {
    text-align: center;
    margin-bottom: 3rem;
}

.search-input-container {
    position: relative;
    margin-bottom: 1rem;
}

.search-input-main {
    width: 100%;
    padding: 1rem 3rem 1rem 1rem;
    border: 2px solid var(--border-color);
    border-radius: 0.5rem;
    font-size: 1.125rem;
    background-color: var(--bg-primary);
    color: var(--text-primary);
    transition: border-color 0.2s ease;
}

.search-input-main:focus {
    outline: none;
    border-color: var(--primary-color);
    box-shadow: 0 0 0 3px var(--primary-color)15;
}

.search-button {
    position: absolute;
    right: 0.75rem;
    top: 50%;
    transform: translateY(-50%);
    background: none;
    border: none;
    color: var(--text-secondary);
    cursor: pointer;
    padding: 0.5rem;
    border-radius: 0.25rem;
}

.search-tips {
    text-align: center;
    margin-bottom: 2rem;
}

.search-tips p {
    font-size: 0.875rem;
    color: var(--text-secondary);
}

.filter-section h3 {
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.quick-filters {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    margin-bottom: 2rem;
}

.filter-btn {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.5rem 1rem;
    border: 1px solid var(--border-color);
    background-color: var(--bg-secondary);
    color: var(--text-secondary);
    border-radius: 0.375rem;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 0.875rem;
}

.filter-btn:hover {
    background-color: var(--bg-tertiary);
    border-color: var(--border-hover);
    color: var(--text-primary);
}

.search-placeholder {
    text-align: center;
    padding: 3rem 1rem;
    color: var(--text-secondary);
}

.search-placeholder i {
    font-size: 3rem;
    margin-bottom: 1rem;
    opacity: 0.5;
}

.search-examples {
    margin-top: 2rem;
}

.example-searches {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
    justify-content: center;
    margin-top: 1rem;
}

.example-search {
    background-color: var(--bg-secondary);
    border: 1px solid var(--border-color);
    color: var(--primary-color);
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    cursor: pointer;
    font-size: 0.875rem;
    transition: all 0.2s ease;
}

.example-search:hover {
    background-color: var(--primary-color);
    color: white;
}

.search-results-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
}

.search-result-card {
    background-color: var(--bg-secondary);
    border: 1px solid var(--border-color);
    border-radius: 0.5rem;
    padding: 1.5rem;
    transition: all 0.2s ease;
}

.search-result-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow);
    border-color: var(--border-hover);
}

.tag-cloud {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.tag-button {
    background-color: var(--bg-secondary);
    border: 1px solid var(--border-color);
    color: var(--text-secondary);
    padding: 0.25rem 0.75rem;
    border-radius: 1rem;
    cursor: pointer;
    font-size: 0.75rem;
    transition: all 0.2s ease;
}

.tag-button:hover {
    background-color: var(--primary-color);
    color: white;
    border-color: var(--primary-color);
}

.help-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    margin-top: 2rem;
}

.help-item h3 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
}

.help-item ul {
    list-style: none;
    padding: 0;
}

.help-item li {
    margin-bottom: 0.5rem;
    color: var(--text-secondary);
}

kbd {
    background-color: var(--bg-tertiary);
    color: var(--text-primary);
    padding: 0.125rem 0.25rem;
    border-radius: 0.25rem;
    font-size: 0.75rem;
    font-family: monospace;
}

mark {
    background-color: var(--accent-color);
    color: var(--text-primary);
    padding: 0.125rem;
    border-radius: 0.125rem;
}

@media (max-width: 768px) {
    .search-results-grid {
        grid-template-columns: 1fr;
    }
    
    .quick-filters {
        justify-content: center;
    }
    
    .example-searches {
        flex-direction: column;
        align-items: center;
    }
}
</style>

<script>
document.body.classList.add('search-page');
</script>