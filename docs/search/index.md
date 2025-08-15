---
layout: default
title: Search Prompts
description: "Search through 278+ enterprise-grade AI prompts across 18 specialized sectors. Filter by high-value sectors, categories, tags, or keywords."
---

<div class="search-page">
    <div class="container">
        <div class="search-header">
            <h1 class="page-title">Search 278+ Enterprise AI Prompts</h1>
            <p class="page-description">
                Discover the perfect AI prompt from our massive collection spanning 18 specialized sectors from Biotechnology to Space Economy. 
                Search across $50+ trillion in market opportunities with dual-persona expert prompts.
            </p>
            <div class="search-stats">
                <div class="search-stat">
                    <span class="stat-number">278+</span>
                    <span class="stat-label">Expert Prompts</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">18</span>
                    <span class="stat-label">Specialized Sectors</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">350+</span>
                    <span class="stat-label">Lines Per Output</span>
                </div>
            </div>
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
                    <h3>🚀 High-Value New Sectors</h3>
                    <div class="quick-filters high-value-sectors">
                        <button class="filter-btn new-sector" onclick="document.getElementById('searchPageInput').value='biotechnology'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            🧬 Biotechnology
                        </button>
                        <button class="filter-btn new-sector" onclick="document.getElementById('searchPageInput').value='space economy'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            🚀 Space Economy
                        </button>
                        <button class="filter-btn new-sector" onclick="document.getElementById('searchPageInput').value='renewable energy'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            ⚡ Renewable Energy
                        </button>
                        <button class="filter-btn new-sector" onclick="document.getElementById('searchPageInput').value='quantum computing'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            ⚛️ Quantum Computing
                        </button>
                        <button class="filter-btn new-sector" onclick="document.getElementById('searchPageInput').value='blockchain'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            🔗 Blockchain
                        </button>
                        <button class="filter-btn new-sector" onclick="document.getElementById('searchPageInput').value='government digital'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            🏛️ Government Digital
                        </button>
                    </div>
                </div>
                
                <div class="filter-section">
                    <h3>Core Business Categories</h3>
                    <div class="quick-filters">
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='analysis'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-chart-bar"></i> Analysis
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='management leadership'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-users-cog"></i> Management & Leadership
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='technical workflows'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-code"></i> Technical Workflows
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='communication'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-comments"></i> Communication
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='decision making'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-balance-scale"></i> Decision Making
                        </button>
                        <button class="filter-btn" onclick="document.getElementById('searchPageInput').value='customer focused'; document.getElementById('searchPageInput').dispatchEvent(new Event('input'))">
                            <i class="fas fa-heart"></i> Customer-Focused
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
                            <h4>🔥 Trending Searches:</h4>
                            <div class="example-searches trending">
                                <button class="example-search trending-search" onclick="searchByKeyword('market research')">
                                    <i class="fas fa-chart-line"></i> market research
                                </button>
                                <button class="example-search trending-search" onclick="searchByKeyword('content creation')">
                                    <i class="fas fa-pen-fancy"></i> content creation
                                </button>
                                <button class="example-search trending-search" onclick="searchByKeyword('project management')">
                                    <i class="fas fa-tasks"></i> project management
                                </button>
                                <button class="example-search trending-search" onclick="searchByKeyword('debugging')">
                                    <i class="fas fa-bug"></i> debugging
                                </button>
                                <button class="example-search trending-search" onclick="searchByKeyword('presentation')">
                                    <i class="fas fa-presentation-screen"></i> presentation
                                </button>
                                <button class="example-search trending-search" onclick="searchByKeyword('strategic planning')">
                                    <i class="fas fa-chess"></i> strategic planning
                                </button>
                            </div>
                            
                            <h4>💡 Popular Use Cases:</h4>
                            <div class="example-searches use-cases">
                                <button class="example-search use-case-search" onclick="searchByKeyword('API design')">
                                    API Design & Documentation
                                </button>
                                <button class="example-search use-case-search" onclick="searchByKeyword('financial analysis')">
                                    Financial Analysis & Modeling
                                </button>
                                <button class="example-search use-case-search" onclick="searchByKeyword('customer research')">
                                    Customer Research & Insights
                                </button>
                                <button class="example-search use-case-search" onclick="searchByKeyword('risk assessment')">
                                    Risk Assessment & Management
                                </button>
                                <button class="example-search use-case-search" onclick="searchByKeyword('team leadership')">
                                    Team Leadership & Management
                                </button>
                                <button class="example-search use-case-search" onclick="searchByKeyword('technical documentation')">
                                    Technical Documentation
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
                        <li><a href="{{ '/categories/' | relative_url }}">View all categories</a></li>
                        <li><a href="{{ '/categories/analysis/' | relative_url }}">Analysis prompts</a></li>
                        <li><a href="{{ '/categories/creation/' | relative_url }}">Creation prompts</a></li>
                        <li><a href="{{ '/categories/technical-workflows/' | relative_url }}">Technical prompts</a></li>
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

.search-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.5rem;
    margin-top: 2rem;
    padding: 2rem;
    background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
    border-radius: 12px;
}

.search-stat {
    text-align: center;
}

.search-stat .stat-number {
    display: block;
    font-size: 2rem;
    font-weight: 700;
    color: var(--primary-color);
    line-height: 1;
}

.search-stat .stat-label {
    display: block;
    font-size: 0.875rem;
    color: var(--text-secondary);
    margin-top: 0.5rem;
}

.high-value-sectors {
    margin-bottom: 2rem;
    padding: 1.5rem;
    background: linear-gradient(135deg, #ecfdf5 0%, #f0fdf4 100%);
    border-radius: 12px;
    border: 2px solid #10b981;
}

.filter-btn.new-sector {
    background: linear-gradient(135deg, #34d399 0%, #10b981 100%);
    color: white;
    border: none;
    font-weight: 600;
}

.filter-btn.new-sector:hover {
    background: linear-gradient(135deg, #10b981 0%, #059669 100%);
    transform: translateY(-2px);
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

.example-searches.trending {
    margin-bottom: 2rem;
}

.trending-search {
    background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
    color: white;
    border: none;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1rem;
}

.trending-search:hover {
    background: linear-gradient(135deg, #ff5252 0%, #ff7043 100%);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
}

.use-case-search {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    border: none;
    font-weight: 500;
    padding: 0.75rem 1.25rem;
    white-space: nowrap;
}

.use-case-search:hover {
    background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%);
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(102, 126, 234, 0.3);
}

.search-examples h4 {
    font-size: 1.125rem;
    color: var(--text-primary);
    margin: 1.5rem 0 1rem 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
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