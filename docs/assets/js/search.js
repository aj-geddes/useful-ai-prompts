// Enhanced search functionality for 278+ prompts across 18 sectors
(function() {
    'use strict';

    let searchIndex = [];
    let searchInput, searchResults, searchOverlay, categoryFilter, tagFilter;
    let searchDropdown, searchSuggestions;
    let searchHistory = JSON.parse(localStorage.getItem('searchHistory') || '[]');
    let favorites = JSON.parse(localStorage.getItem('promptFavorites') || '[]');
    let currentFilters = {
        category: '',
        tags: [],
        sector: ''
    };
    let dropdownSelectedIndex = -1;
    let isDropdownOpen = false;
    
    // Initialize search functionality
    function initializeSearch() {
        searchInput = document.getElementById('searchInput');
        searchResults = document.getElementById('searchResults');
        searchOverlay = document.getElementById('searchOverlay');
        categoryFilter = document.getElementById('categoryFilter');
        tagFilter = document.getElementById('tagFilter');
        
        if (searchInput) {
            // Load search index
            loadSearchIndex();
            
            // Set up search input handler with debounce
            let searchTimeout;
            searchInput.addEventListener('input', (e) => {
                clearTimeout(searchTimeout);
                searchTimeout = setTimeout(() => {
                    performSearch(e.target.value);
                }, 150); // Faster response for large collection
            });
            
            // Handle Enter key
            searchInput.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    e.preventDefault();
                    performSearch(searchInput.value);
                }
            });
            
            // Set up filter handlers
            if (categoryFilter) {
                categoryFilter.addEventListener('change', (e) => {
                    currentFilters.category = e.target.value;
                    performSearch(searchInput.value);
                });
            }
            
            if (tagFilter) {
                tagFilter.addEventListener('change', (e) => {
                    currentFilters.tags = Array.from(e.target.selectedOptions).map(opt => opt.value);
                    performSearch(searchInput.value);
                });
            }
        }
    }
    
    // Load the search index
    async function loadSearchIndex() {
        try {
            const response = await fetch('/useful-ai-prompts/assets/data/search-index.json');
            if (response.ok) {
                searchIndex = await response.json();
            } else {
                // Fallback to building index from PROMPT-INDEX.json
                const fallbackResponse = await fetch('/useful-ai-prompts/PROMPT-INDEX.json');
                if (fallbackResponse.ok) {
                    const promptData = await fallbackResponse.json();
                    searchIndex = buildSearchIndex(promptData);
                }
            }
        } catch (error) {
            console.warn('Could not load search index:', error);
            // Try to build a minimal index from page content
            buildMinimalSearchIndex();
        }
    }
    
    // Build search index from PROMPT-INDEX.json
    function buildSearchIndex(promptData) {
        return promptData.map(prompt => ({
            title: prompt.title,
            description: prompt.description || '',
            category: prompt.category,
            tags: prompt.tags || [],
            url: `/useful-ai-prompts/prompts/${prompt.slug}/`,
            content: (prompt.prompt || '').toLowerCase(),
            searchText: [
                prompt.title,
                prompt.description || '',
                prompt.category,
                ...(prompt.tags || []),
                prompt.use_cases ? prompt.use_cases.join(' ') : ''
            ].join(' ').toLowerCase()
        }));
    }
    
    // Build minimal search index from current page if JSON not available
    function buildMinimalSearchIndex() {
        const promptCards = document.querySelectorAll('.prompt-card, .category-card');
        searchIndex = Array.from(promptCards).map(card => {
            const titleElement = card.querySelector('h3 a, .card-title a');
            const descElement = card.querySelector('.card-description, p');
            const categoryElement = card.querySelector('.category-badge, .prompt-count');
            const tagsElements = card.querySelectorAll('.tag');
            
            return {
                title: titleElement ? titleElement.textContent.trim() : '',
                description: descElement ? descElement.textContent.trim() : '',
                category: categoryElement ? categoryElement.textContent.trim() : '',
                tags: Array.from(tagsElements).map(tag => tag.textContent.trim()),
                url: titleElement ? titleElement.href : '#',
                searchText: [
                    titleElement ? titleElement.textContent.trim() : '',
                    descElement ? descElement.textContent.trim() : '',
                    ...Array.from(tagsElements).map(tag => tag.textContent.trim())
                ].join(' ').toLowerCase()
            };
        }).filter(item => item.title);
    }
    
    // Perform search
    function performSearch(query) {
        if (!searchResults) return;
        
        const trimmedQuery = query.trim().toLowerCase();
        
        if (trimmedQuery.length === 0) {
            clearSearchResults();
            return;
        }
        
        if (trimmedQuery.length < 2) {
            searchResults.innerHTML = '<p class="search-hint">Type at least 2 characters to search...</p>';
            return;
        }
        
        const results = searchPrompts(trimmedQuery);
        displaySearchResults(results, trimmedQuery);
    }
    
    // Search through prompts with enhanced filtering
    function searchPrompts(query) {
        const queryWords = query.split(/\s+/).filter(word => word.length > 0);
        
        return searchIndex
            .filter(item => {
                // Apply category filter
                if (currentFilters.category && currentFilters.category !== 'all') {
                    if (!item.category.toLowerCase().includes(currentFilters.category.toLowerCase())) {
                        return false;
                    }
                }
                
                // Apply tag filters
                if (currentFilters.tags.length > 0) {
                    const hasMatchingTag = currentFilters.tags.some(filterTag => 
                        item.tags.some(itemTag => 
                            itemTag.toLowerCase().includes(filterTag.toLowerCase())
                        )
                    );
                    if (!hasMatchingTag) return false;
                }
                
                // Apply high-value sector filter
                if (currentFilters.sector) {
                    const highValueSectors = ['biotechnology', 'space-economy', 'renewable-energy', 'quantum-computing', 'blockchain', 'government-digital', 'supply-chain', 'healthcare-digital'];
                    if (currentFilters.sector === 'high-value' && !highValueSectors.includes(item.category)) {
                        return false;
                    }
                }
                
                return true;
            })
            .map(item => {
                let score = 0;
                const titleLower = item.title.toLowerCase();
                const descriptionLower = item.description.toLowerCase();
                const categoryLower = item.category.toLowerCase();
                
                // Exact title match gets highest score
                if (titleLower === query) {
                    score += 100;
                } else if (titleLower.includes(query)) {
                    score += 50;
                }
                
                // Category match
                if (categoryLower === query || categoryLower.includes(query)) {
                    score += 30;
                }
                
                // Description match
                if (descriptionLower.includes(query)) {
                    score += 20;
                }
                
                // Tag matches
                item.tags.forEach(tag => {
                    if (tag.toLowerCase() === query) {
                        score += 25;
                    } else if (tag.toLowerCase().includes(query)) {
                        score += 15;
                    }
                });
                
                // Word-based matching
                queryWords.forEach(word => {
                    if (item.searchText.includes(word)) {
                        score += 10;
                    }
                });
                
                // Boost score for multiple word matches
                if (queryWords.length > 1) {
                    const matchCount = queryWords.filter(word => item.searchText.includes(word)).length;
                    score += (matchCount / queryWords.length) * 20;
                }
                
                return { ...item, score };
            })
            .filter(item => item.score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, 20); // Limit to top 20 results
    }
    
    // Display search results
    function displaySearchResults(results, query) {
        if (!searchResults) return;
        
        if (results.length === 0) {
            searchResults.innerHTML = `
                <div class="no-results">
                    <i class="fas fa-search"></i>
                    <h3>No results found</h3>
                    <p>No prompts match your search for "<strong>${escapeHtml(query)}</strong>"</p>
                    <div class="search-suggestions">
                        <p>Try searching for:</p>
                        <div class="suggestion-tags">
                            <span class="suggestion-tag">analysis</span>
                            <span class="suggestion-tag">creation</span>
                            <span class="suggestion-tag">planning</span>
                            <span class="suggestion-tag">debugging</span>
                            <span class="suggestion-tag">presentation</span>
                        </div>
                    </div>
                </div>
            `;
            return;
        }
        
        const resultsHTML = `
            <div class="search-summary">
                <p>Found <strong>${results.length}</strong> result${results.length === 1 ? '' : 's'} for "<strong>${escapeHtml(query)}</strong>"</p>
            </div>
            <div class="search-results-list">
                ${results.map(result => createSearchResultHTML(result, query)).join('')}
            </div>
        `;
        
        searchResults.innerHTML = resultsHTML;
    }
    
    // Create HTML for a single search result
    function createSearchResultHTML(result, query) {
        const highlightedTitle = highlightText(result.title, query);
        const highlightedDescription = highlightText(result.description, query);
        
        return `
            <div class="search-result">
                <div class="result-header">
                    <h3 class="result-title">
                        <a href="${result.url}">${highlightedTitle}</a>
                    </h3>
                    <span class="result-category">${result.category}</span>
                </div>
                <p class="result-description">${highlightedDescription}</p>
                ${result.tags && result.tags.length > 0 ? `
                    <div class="result-tags">
                        ${result.tags.slice(0, 4).map(tag => `<span class="tag">${tag}</span>`).join('')}
                        ${result.tags.length > 4 ? `<span class="tag-more">+${result.tags.length - 4}</span>` : ''}
                    </div>
                ` : ''}
            </div>
        `;
    }
    
    // Highlight search terms in text
    function highlightText(text, query) {
        if (!text || !query) return escapeHtml(text);
        
        const words = query.toLowerCase().split(/\s+/).filter(word => word.length > 0);
        let highlightedText = escapeHtml(text);
        
        words.forEach(word => {
            const regex = new RegExp(`(${escapeRegExp(word)})`, 'gi');
            highlightedText = highlightedText.replace(regex, '<mark>$1</mark>');
        });
        
        return highlightedText;
    }
    
    // Escape HTML
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
    
    // Escape special regex characters
    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }
    
    // Clear search results
    function clearSearchResults() {
        if (searchResults) {
            searchResults.innerHTML = '';
        }
    }
    
    // Create search page functionality
    function initializeSearchPage() {
        const searchPageInput = document.getElementById('searchPageInput');
        const searchPageResults = document.getElementById('searchPageResults');
        const popularTags = document.getElementById('popularTags');
        
        if (searchPageInput && searchPageResults) {
            loadSearchIndex().then(() => {
                // Set up search input
                let searchTimeout;
                searchPageInput.addEventListener('input', (e) => {
                    clearTimeout(searchTimeout);
                    searchTimeout = setTimeout(() => {
                        const results = searchPrompts(e.target.value);
                        displaySearchPageResults(results, e.target.value);
                    }, 300);
                });
                
                // Handle URL query parameter
                const urlParams = new URLSearchParams(window.location.search);
                const searchQuery = urlParams.get('q');
                if (searchQuery) {
                    searchPageInput.value = searchQuery;
                    const results = searchPrompts(searchQuery);
                    displaySearchPageResults(results, searchQuery);
                }
                
                // Show popular tags
                if (popularTags) {
                    displayPopularTags();
                }
            });
        }
    }
    
    // Display results on search page
    function displaySearchPageResults(results, query) {
        const searchPageResults = document.getElementById('searchPageResults');
        if (!searchPageResults) return;
        
        if (!query || query.trim().length === 0) {
            searchPageResults.innerHTML = '<p class="search-hint">Enter a search term to find prompts...</p>';
            return;
        }
        
        if (results.length === 0) {
            searchPageResults.innerHTML = `
                <div class="no-results-page">
                    <i class="fas fa-search"></i>
                    <h2>No results found</h2>
                    <p>No prompts match your search for "<strong>${escapeHtml(query)}</strong>"</p>
                </div>
            `;
            return;
        }
        
        searchPageResults.innerHTML = `
            <div class="search-results-header">
                <h2>Search Results</h2>
                <p>Found <strong>${results.length}</strong> result${results.length === 1 ? '' : 's'} for "<strong>${escapeHtml(query)}</strong>"</p>
            </div>
            <div class="search-results-grid">
                ${results.map(result => createSearchPageResultHTML(result, query)).join('')}
            </div>
        `;
    }
    
    // Create HTML for search page result
    function createSearchPageResultHTML(result, query) {
        const highlightedTitle = highlightText(result.title, query);
        const highlightedDescription = highlightText(result.description, query);
        
        return `
            <div class="search-result-card">
                <div class="card-header">
                    <h3 class="card-title">
                        <a href="${result.url}">${highlightedTitle}</a>
                    </h3>
                    <span class="category-badge">${result.category}</span>
                </div>
                <p class="card-description">${highlightedDescription}</p>
                ${result.tags && result.tags.length > 0 ? `
                    <div class="card-tags">
                        ${result.tags.slice(0, 3).map(tag => `<span class="tag">${tag}</span>`).join('')}
                        ${result.tags.length > 3 ? `<span class="tag-more">+${result.tags.length - 3}</span>` : ''}
                    </div>
                ` : ''}
                <div class="card-actions">
                    <a href="${result.url}" class="btn btn-primary">View Prompt</a>
                </div>
            </div>
        `;
    }
    
    // Display popular tags
    function displayPopularTags() {
        const popularTags = document.getElementById('popularTags');
        if (!popularTags || !searchIndex.length) return;
        
        const tagCounts = {};
        searchIndex.forEach(item => {
            item.tags.forEach(tag => {
                tagCounts[tag] = (tagCounts[tag] || 0) + 1;
            });
        });
        
        const sortedTags = Object.entries(tagCounts)
            .sort((a, b) => b[1] - a[1])
            .slice(0, 20);
        
        if (sortedTags.length > 0) {
            popularTags.innerHTML = `
                <h3>Popular Tags</h3>
                <div class="tag-cloud">
                    ${sortedTags.map(([tag, count]) => `
                        <button class="tag-button" onclick="searchByTag('${tag}')" title="${count} prompts">
                            ${tag} (${count})
                        </button>
                    `).join('')}
                </div>
            `;
        }
    }
    
    // Search by tag
    window.searchByTag = function(tag) {
        const searchPageInput = document.getElementById('searchPageInput');
        if (searchPageInput) {
            searchPageInput.value = tag;
            const results = searchPrompts(tag);
            displaySearchPageResults(results, tag);
        }
    };
    
    // Initialize when DOM is loaded
    document.addEventListener('DOMContentLoaded', () => {
        initializeSearch();
        
        // Initialize search page if we're on it
        if (document.body.classList.contains('search-page')) {
            initializeSearchPage();
        }
    });
    
})();