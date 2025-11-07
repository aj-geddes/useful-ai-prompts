---
layout: default
title: Search Prompts
description: "Search through 486+ professional AI prompts across 22 specialized categories. Filter by sectors, categories, tags, or keywords."
---

<div class="search-page">
    <div class="container">
        <div class="search-header">
            <h1 class="page-title">Search 486+ Professional AI Prompts</h1>
            <p class="page-description">
                Discover the perfect AI prompt from our comprehensive collection spanning 22 specialized categories.
                Search across professional workflows with expert-designed conversational prompts.
            </p>
            <div class="search-stats">
                <div class="search-stat">
                    <span class="stat-number">486+</span>
                    <span class="stat-label">Expert Prompts</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">22</span>
                    <span class="stat-label">Categories</span>
                </div>
                <div class="search-stat">
                    <span class="stat-number">100%</span>
                    <span class="stat-label">Ready to Use</span>
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
                    <h3>🚀 Specialized Sectors</h3>
                    <div class="quick-filters high-value-sectors">
                        <button class="filter-btn new-sector" onclick="searchByKeyword('biotechnology')">🧬 Biotechnology</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('space economy')">🚀 Space Economy</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('renewable energy')">⚡ Renewable Energy</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('quantum computing')">⚛️ Quantum Computing</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('blockchain')">🔗 Blockchain</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('healthcare digital')">❤️ Healthcare</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('government digital')">🏛️ Government</button>
                        <button class="filter-btn new-sector" onclick="searchByKeyword('supply chain')">🚚 Supply Chain</button>
                    </div>
                </div>

                <div class="filter-section">
                    <h3>Core Business Categories</h3>
                    <div class="quick-filters">
                        <button class="filter-btn" onclick="searchByKeyword('analysis')"><i class="fas fa-chart-bar"></i> Analysis</button>
                        <button class="filter-btn" onclick="searchByKeyword('management leadership')"><i class="fas fa-users-cog"></i> Management</button>
                        <button class="filter-btn" onclick="searchByKeyword('technical workflows')"><i class="fas fa-code"></i> Technical</button>
                        <button class="filter-btn" onclick="searchByKeyword('communication')"><i class="fas fa-comments"></i> Communication</button>
                        <button class="filter-btn" onclick="searchByKeyword('decision making')"><i class="fas fa-balance-scale"></i> Decision Making</button>
                        <button class="filter-btn" onclick="searchByKeyword('customer focused')"><i class="fas fa-heart"></i> Customer-Focused</button>
                        <button class="filter-btn" onclick="searchByKeyword('planning')"><i class="fas fa-calendar-alt"></i> Planning</button>
                        <button class="filter-btn" onclick="searchByKeyword('creation')"><i class="fas fa-palette"></i> Creation</button>
                    </div>
                </div>
            </div>

            <div class="search-results-section">
                <div id="searchPageResults" class="search-results-container">
                    <div class="search-placeholder">
                        <i class="fas fa-search"></i>
                        <h3>Ready to Search</h3>
                        <p>Enter a search term above or click a category button to find relevant prompts.</p>

                        <div class="search-examples">
                            <h4>🔥 Trending Searches:</h4>
                            <div class="example-searches trending">
                                <button class="example-search trending-search" onclick="searchByKeyword('market research')"><i class="fas fa-chart-line"></i> market research</button>
                                <button class="example-search trending-search" onclick="searchByKeyword('content creation')"><i class="fas fa-pen-fancy"></i> content creation</button>
                                <button class="example-search trending-search" onclick="searchByKeyword('project management')"><i class="fas fa-tasks"></i> project management</button>
                                <button class="example-search trending-search" onclick="searchByKeyword('debugging')"><i class="fas fa-bug"></i> debugging</button>
                                <button class="example-search trending-search" onclick="searchByKeyword('presentation')"><i class="fas fa-presentation-screen"></i> presentation</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="search-help">
            <h2>Search Help</h2>
            <div class="help-grid">
                <div class="help-item">
                    <h3><i class="fas fa-keyboard"></i> Keyboard Shortcuts</h3>
                    <ul>
                        <li><kbd>Ctrl</kbd> + <kbd>K</kbd> - Open search</li>
                        <li><kbd>Esc</kbd> - Close search</li>
                    </ul>
                </div>
                <div class="help-item">
                    <h3><i class="fas fa-filter"></i> Search Tips</h3>
                    <ul>
                        <li>Use specific keywords like "SWOT analysis"</li>
                        <li>Search by category like "communication"</li>
                        <li>Click category buttons for instant filtering</li>
                    </ul>
                </div>
                <div class="help-item">
                    <h3><i class="fas fa-tags"></i> Browse by Category</h3>
                    <ul>
                        <li><a href="{{ '/categories/' | relative_url }}">View all categories</a></li>
                        <li><a href="{{ '/categories/analysis/' | relative_url }}">Analysis prompts</a></li>
                        <li><a href="{{ '/categories/technical-workflows/' | relative_url }}">Technical prompts</a></li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>

<style>
.search-page { padding: 2rem 0 4rem; }
.search-header { text-align: center; margin-bottom: 3rem; }
.page-title {
    font-size: clamp(2rem, 5vw, 3rem);
    font-weight: 700;
    letter-spacing: -0.03em;
    margin-bottom: 1rem;
    color: var(--text-primary);
}
.page-description {
    font-size: 1.125rem;
    color: var(--text-secondary);
    max-width: 800px;
    margin: 0 auto 2rem;
    line-height: 1.6;
}
.search-stats {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 1.5rem;
    max-width: 600px;
    margin: 0 auto;
    padding: 2rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 16px;
}
.search-stat { text-align: center; }
.search-stat .stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    color: var(--accent-primary);
    line-height: 1;
    margin-bottom: 0.5rem;
}
.search-stat .stat-label {
    display: block;
    font-size: 0.875rem;
    color: var(--text-secondary);
    font-weight: 500;
}
.search-main { max-width: 1000px; margin: 0 auto; }
.search-form { margin-bottom: 2.5rem; }
.search-input-container { position: relative; margin-bottom: 1rem; }
.search-input-main {
    width: 100%;
    padding: 1.125rem 4rem 1.125rem 1.25rem;
    border: 2px solid var(--border-primary);
    border-radius: 12px;
    font-size: 1.125rem;
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    transition: all 0.2s ease;
    font-family: inherit;
}
.search-input-main:focus {
    outline: none;
    border-color: var(--accent-primary);
    box-shadow: 0 0 0 3px rgba(0, 122, 255, 0.1);
}
.search-button {
    position: absolute;
    right: 0.75rem;
    top: 50%;
    transform: translateY(-50%);
    background: var(--accent-primary);
    border: none;
    color: white;
    cursor: pointer;
    padding: 0.75rem 1rem;
    border-radius: 8px;
    transition: all 0.2s ease;
}
.search-button:hover { background: var(--accent-secondary); }
.search-tips { text-align: center; margin-bottom: 2rem; }
.search-tips p { font-size: 0.9375rem; color: var(--text-secondary); }
.filter-section { margin-bottom: 2rem; }
.filter-section h3 { margin-bottom: 1rem; color: var(--text-primary); font-size: 1.125rem; font-weight: 600; }
.high-value-sectors {
    padding: 1.5rem;
    background: var(--bg-secondary);
    border-radius: 12px;
    border: 1px solid var(--border-primary);
}
.quick-filters { display: flex; flex-wrap: wrap; gap: 0.75rem; }
.filter-btn {
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
    padding: 0.75rem 1.25rem;
    border: 1px solid var(--border-primary);
    background-color: var(--bg-secondary);
    color: var(--text-primary);
    border-radius: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
    font-size: 0.9375rem;
    font-weight: 500;
    font-family: inherit;
}
.filter-btn:hover {
    background-color: var(--accent-primary);
    border-color: var(--accent-primary);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 122, 255, 0.2);
}
.filter-btn.new-sector {
    background: var(--accent-primary);
    color: white;
    border-color: var(--accent-primary);
}
.filter-btn.new-sector:hover {
    background: var(--accent-secondary);
    box-shadow: 0 4px 12px rgba(0, 122, 255, 0.3);
}
.search-placeholder {
    text-align: center;
    padding: 4rem 2rem;
    color: var(--text-secondary);
}
.search-placeholder i {
    font-size: 4rem;
    margin-bottom: 1.5rem;
    opacity: 0.3;
    color: var(--accent-primary);
}
.search-placeholder h3 { font-size: 1.5rem; color: var(--text-primary); margin-bottom: 0.5rem; }
.search-placeholder p { font-size: 1.0625rem; margin-bottom: 2rem; }
.search-examples { margin-top: 3rem; }
.search-examples h4 {
    font-size: 1.125rem;
    color: var(--text-primary);
    margin: 2rem 0 1rem 0;
    font-weight: 600;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
}
.example-searches {
    display: flex;
    flex-wrap: wrap;
    gap: 0.75rem;
    justify-content: center;
    margin-top: 1rem;
}
.example-search {
    background-color: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    color: var(--accent-primary);
    padding: 0.625rem 1rem;
    border-radius: 8px;
    cursor: pointer;
    font-size: 0.9375rem;
    font-weight: 500;
    transition: all 0.2s ease;
    font-family: inherit;
}
.example-search:hover {
    background-color: var(--accent-primary);
    color: white;
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(0, 122, 255, 0.2);
}
.trending-search {
    background: linear-gradient(135deg, #ff6b6b 0%, #ff8e53 100%);
    color: white;
    border: none;
    display: inline-flex;
    align-items: center;
    gap: 0.5rem;
}
.trending-search:hover {
    background: linear-gradient(135deg, #ff5252 0%, #ff7043 100%);
    box-shadow: 0 4px 12px rgba(255, 107, 107, 0.3);
}
.search-help {
    margin-top: 4rem;
    padding: 2.5rem;
    background: var(--bg-secondary);
    border: 1px solid var(--border-primary);
    border-radius: 16px;
}
.search-help h2 { font-size: 1.75rem; margin-bottom: 1.5rem; color: var(--text-primary); }
.help-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
}
.help-item h3 {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    margin-bottom: 1rem;
    color: var(--text-primary);
    font-size: 1.125rem;
}
.help-item ul { list-style: none; padding: 0; }
.help-item li { margin-bottom: 0.75rem; color: var(--text-secondary); line-height: 1.6; }
.help-item a { color: var(--accent-primary); text-decoration: none; }
.help-item a:hover { text-decoration: underline; }
kbd {
    background-color: var(--bg-primary);
    color: var(--text-primary);
    padding: 0.25rem 0.5rem;
    border-radius: 4px;
    font-size: 0.8125rem;
    font-family: monospace;
    border: 1px solid var(--border-primary);
}
@media (max-width: 768px) {
    .search-stats { grid-template-columns: repeat(3, 1fr); padding: 1.5rem 1rem; }
    .stat-number { font-size: 2rem !important; }
    .quick-filters { justify-content: center; }
    .example-searches { flex-direction: column; align-items: stretch; }
}
</style>

<script>
document.body.classList.add('search-page');
</script>
