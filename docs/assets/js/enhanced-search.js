// Enhanced Search with Smart Dropdown and Discovery Features
(function() {
    'use strict';

    let searchIndex = [];
    let searchInput, searchResults, searchOverlay, categoryFilter, tagFilter;
    let searchDropdown;
    let searchHistory = JSON.parse(localStorage.getItem('searchHistory') || '[]');
    let favorites = JSON.parse(localStorage.getItem('promptFavorites') || '[]');
    let currentFilters = {
        category: '',
        tags: [],
        sector: ''
    };
    let dropdownSelectedIndex = -1;
    let isDropdownOpen = false;

    // Initialize enhanced search functionality
    function initializeEnhancedSearch() {
        searchInput = document.getElementById('searchInput') || document.getElementById('searchPageInput');
        searchResults = document.getElementById('searchResults') || document.getElementById('searchPageResults');
        searchOverlay = document.getElementById('searchOverlay');
        categoryFilter = document.getElementById('categoryFilter');
        tagFilter = document.getElementById('tagFilter');
        
        if (searchInput) {
            createSearchDropdown();
            setupSearchHandlers();
            setupKeyboardShortcuts();
            loadSearchIndex();
        }
    }

    // Create smart search dropdown
    function createSearchDropdown() {
        if (!searchInput) return;
        
        // Create dropdown container
        searchDropdown = document.createElement('div');
        searchDropdown.className = 'search-dropdown';
        searchDropdown.innerHTML = '';
        
        // Position dropdown relative to search input
        const inputContainer = searchInput.closest('.search-input-wrapper, .search-input-container') || searchInput.parentNode;
        inputContainer.style.position = 'relative';
        inputContainer.appendChild(searchDropdown);
        
        // Initially hidden
        hideSearchDropdown();
    }

    // Setup search input handlers
    function setupSearchHandlers() {
        let searchTimeout;
        
        // Input handler with debounce
        searchInput.addEventListener('input', (e) => {
            clearTimeout(searchTimeout);
            const query = e.target.value.trim();
            
            searchTimeout = setTimeout(() => {
                if (query.length >= 2) {
                    showSmartSuggestions(query);
                    performSearch(query);
                } else if (query.length === 0) {
                    hideSearchDropdown();
                    clearSearchResults();
                } else {
                    hideSearchDropdown();
                }
            }, 200);
        });

        // Focus handler - show suggestions if query exists
        searchInput.addEventListener('focus', (e) => {
            const query = e.target.value.trim();
            if (query.length >= 2) {
                showSmartSuggestions(query);
            } else if (query.length === 0 && searchHistory.length > 0) {
                showRecentSearches();
            }
        });

        // Keyboard navigation
        searchInput.addEventListener('keydown', handleKeyNavigation);

        // Click outside to hide dropdown
        document.addEventListener('click', (e) => {
            if (!searchInput.contains(e.target) && !searchDropdown.contains(e.target)) {
                hideSearchDropdown();
            }
        });

        // Filter handlers
        if (categoryFilter) {
            categoryFilter.addEventListener('change', (e) => {
                currentFilters.category = e.target.value;
                const query = searchInput.value.trim();
                if (query) performSearch(query);
            });
        }

        if (tagFilter) {
            tagFilter.addEventListener('change', (e) => {
                currentFilters.tags = Array.from(e.target.selectedOptions).map(opt => opt.value);
                const query = searchInput.value.trim();
                if (query) performSearch(query);
            });
        }
    }

    // Show smart search suggestions
    function showSmartSuggestions(query) {
        if (!searchDropdown || !searchIndex.length) return;

        const suggestions = generateSmartSuggestions(query);
        if (!suggestions || (suggestions.prompts.length === 0 && suggestions.categories.length === 0 && suggestions.tags.length === 0)) {
            hideSearchDropdown();
            return;
        }

        let html = '<div class="suggestions-container">';

        // Matching prompts section
        if (suggestions.prompts.length > 0) {
            html += '<div class="suggestion-section">';
            html += '<div class="suggestion-header"><i class="fas fa-file-alt"></i>Prompts</div>';
            suggestions.prompts.forEach((prompt, index) => {
                html += createPromptSuggestionHTML(prompt, query, index);
            });
            html += '</div>';
        }

        // Categories section
        if (suggestions.categories.length > 0) {
            html += '<div class="suggestion-section">';
            html += '<div class="suggestion-header"><i class="fas fa-folder"></i>Categories</div>';
            suggestions.categories.forEach((category, index) => {
                const globalIndex = suggestions.prompts.length + index;
                html += createCategorySuggestionHTML(category, query, globalIndex);
            });
            html += '</div>';
        }

        // Tags section
        if (suggestions.tags.length > 0) {
            html += '<div class="suggestion-section">';
            html += '<div class="suggestion-header"><i class="fas fa-tags"></i>Tags</div>';
            suggestions.tags.forEach((tag, index) => {
                const globalIndex = suggestions.prompts.length + suggestions.categories.length + index;
                html += createTagSuggestionHTML(tag, query, globalIndex);
            });
            html += '</div>';
        }

        html += '</div>';

        searchDropdown.innerHTML = html;
        showSearchDropdown();
        attachSuggestionHandlers();
    }

    // Show recent searches
    function showRecentSearches() {
        if (!searchDropdown || searchHistory.length === 0) return;

        let html = '<div class="suggestions-container">';
        html += '<div class="suggestion-section">';
        html += '<div class="suggestion-header"><i class="fas fa-history"></i>Recent Searches</div>';
        
        searchHistory.slice(0, 5).forEach((historyItem, index) => {
            html += `
                <div class="suggestion-item history-suggestion" data-index="${index}" data-type="history" data-query="${escapeHtml(historyItem)}">
                    <div class="suggestion-content">
                        <div class="suggestion-title">${escapeHtml(historyItem)}</div>
                        <div class="suggestion-meta">Recent search</div>
                    </div>
                    <div class="suggestion-actions">
                        <button class="suggestion-remove" title="Remove from history" onclick="removeFromHistory('${escapeHtml(historyItem)}')">
                            <i class="fas fa-times"></i>
                        </button>
                    </div>
                </div>
            `;
        });
        html += '</div></div>';

        searchDropdown.innerHTML = html;
        showSearchDropdown();
        attachSuggestionHandlers();
    }

    // Generate smart suggestions
    function generateSmartSuggestions(query) {
        const lowerQuery = query.toLowerCase();
        const words = lowerQuery.split(/\s+/).filter(w => w.length > 2);

        const suggestions = {
            prompts: [],
            categories: new Set(),
            tags: new Set()
        };

        // Find matching prompts with fuzzy matching
        const promptMatches = searchIndex.map(item => {
            let score = 0;
            const titleLower = item.title.toLowerCase();
            const descLower = item.description.toLowerCase();
            const categoryLower = item.category.toLowerCase();
            const tagsLower = item.tags.map(t => t.toLowerCase());

            // Exact matches (highest priority)
            if (titleLower.includes(lowerQuery)) score += 100;
            if (descLower.includes(lowerQuery)) score += 50;
            if (categoryLower.includes(lowerQuery)) score += 30;
            
            // Tag matches
            tagsLower.forEach(tag => {
                if (tag.includes(lowerQuery)) score += 40;
            });

            // Word-based fuzzy matching
            words.forEach(word => {
                if (titleLower.includes(word)) score += 20;
                if (descLower.includes(word)) score += 10;
                tagsLower.forEach(tag => {
                    if (tag.includes(word)) score += 15;
                });
            });

            // Boost for title prefix matches
            if (titleLower.startsWith(lowerQuery)) score += 50;

            return { ...item, score };
        }).filter(item => item.score > 0)
          .sort((a, b) => b.score - a.score)
          .slice(0, 6);

        suggestions.prompts = promptMatches;

        // Find matching categories
        searchIndex.forEach(item => {
            if (item.category.toLowerCase().includes(lowerQuery)) {
                suggestions.categories.add(item.category);
            }
        });

        // Find matching tags
        searchIndex.forEach(item => {
            item.tags.forEach(tag => {
                if (tag.toLowerCase().includes(lowerQuery)) {
                    suggestions.tags.add(tag);
                }
            });
        });

        return {
            prompts: suggestions.prompts,
            categories: Array.from(suggestions.categories).slice(0, 4),
            tags: Array.from(suggestions.tags).slice(0, 6)
        };
    }

    // Create HTML for prompt suggestion
    function createPromptSuggestionHTML(prompt, query, index) {
        return `
            <div class="suggestion-item prompt-suggestion" data-index="${index}" data-type="prompt" data-url="${prompt.url}">
                <div class="suggestion-icon"><i class="fas fa-file-alt"></i></div>
                <div class="suggestion-content">
                    <div class="suggestion-title">${highlightText(prompt.title, query)}</div>
                    <div class="suggestion-meta">${prompt.category}</div>
                </div>
                <div class="suggestion-actions">
                    <button class="suggestion-favorite ${favorites.includes(prompt.url) ? 'active' : ''}" 
                            title="Add to favorites" onclick="toggleFavorite('${prompt.url}')">
                        <i class="fas fa-heart"></i>
                    </button>
                </div>
            </div>
        `;
    }

    // Create HTML for category suggestion
    function createCategorySuggestionHTML(category, query, index) {
        return `
            <div class="suggestion-item category-suggestion" data-index="${index}" data-type="category" data-query="${escapeHtml(category)}">
                <div class="suggestion-icon"><i class="fas fa-folder"></i></div>
                <div class="suggestion-content">
                    <div class="suggestion-title">${highlightText(category, query)}</div>
                    <div class="suggestion-meta">Category</div>
                </div>
                <div class="suggestion-arrow">
                    <i class="fas fa-arrow-right"></i>
                </div>
            </div>
        `;
    }

    // Create HTML for tag suggestion
    function createTagSuggestionHTML(tag, query, index) {
        return `
            <div class="suggestion-item tag-suggestion" data-index="${index}" data-type="tag" data-query="${escapeHtml(tag)}">
                <div class="suggestion-icon"><i class="fas fa-tag"></i></div>
                <div class="suggestion-content">
                    <div class="suggestion-title">${highlightText(tag, query)}</div>
                    <div class="suggestion-meta">Tag</div>
                </div>
                <div class="suggestion-arrow">
                    <i class="fas fa-arrow-right"></i>
                </div>
            </div>
        `;
    }

    // Attach event handlers to suggestion items
    function attachSuggestionHandlers() {
        searchDropdown.querySelectorAll('.suggestion-item').forEach(item => {
            item.addEventListener('click', (e) => {
                if (!e.target.closest('.suggestion-favorite, .suggestion-remove')) {
                    handleSuggestionClick(item);
                }
            });
        });
    }

    // Handle suggestion click
    function handleSuggestionClick(item) {
        const type = item.dataset.type;
        const url = item.dataset.url;
        const query = item.dataset.query;

        hideSearchDropdown();

        if (type === 'prompt' && url) {
            window.location.href = url;
        } else if (query) {
            searchInput.value = query;
            addToSearchHistory(query);
            performSearch(query);
        }
    }

    // Keyboard navigation handler
    function handleKeyNavigation(e) {
        if (!isDropdownOpen) {
            if (e.key === 'Enter') {
                e.preventDefault();
                const query = searchInput.value.trim();
                if (query) {
                    addToSearchHistory(query);
                    performSearch(query);
                }
            }
            return;
        }

        const suggestions = searchDropdown.querySelectorAll('.suggestion-item');
        
        switch (e.key) {
            case 'ArrowDown':
                e.preventDefault();
                dropdownSelectedIndex = Math.min(dropdownSelectedIndex + 1, suggestions.length - 1);
                updateSelectionHighlight(suggestions);
                break;
                
            case 'ArrowUp':
                e.preventDefault();
                dropdownSelectedIndex = Math.max(dropdownSelectedIndex - 1, -1);
                updateSelectionHighlight(suggestions);
                break;
                
            case 'Enter':
                e.preventDefault();
                if (dropdownSelectedIndex >= 0 && suggestions[dropdownSelectedIndex]) {
                    handleSuggestionClick(suggestions[dropdownSelectedIndex]);
                } else {
                    const query = searchInput.value.trim();
                    if (query) {
                        hideSearchDropdown();
                        addToSearchHistory(query);
                        performSearch(query);
                    }
                }
                break;
                
            case 'Escape':
                e.preventDefault();
                hideSearchDropdown();
                searchInput.blur();
                break;
        }
    }

    // Update selection highlight
    function updateSelectionHighlight(suggestions) {
        suggestions.forEach((item, index) => {
            item.classList.toggle('selected', index === dropdownSelectedIndex);
        });
    }

    // Show search dropdown
    function showSearchDropdown() {
        if (searchDropdown) {
            searchDropdown.style.display = 'block';
            isDropdownOpen = true;
            dropdownSelectedIndex = -1;
        }
    }

    // Hide search dropdown
    function hideSearchDropdown() {
        if (searchDropdown) {
            searchDropdown.style.display = 'none';
            isDropdownOpen = false;
            dropdownSelectedIndex = -1;
        }
    }

    // Load search index
    async function loadSearchIndex() {
        try {
            const response = await fetch('/useful-ai-prompts/assets/data/search-index.json');
            if (response.ok) {
                searchIndex = await response.json();
            } else {
                // Fallback to PROMPT-INDEX.json
                const fallbackResponse = await fetch('/useful-ai-prompts/PROMPT-INDEX.json');
                if (fallbackResponse.ok) {
                    const promptData = await fallbackResponse.json();
                    searchIndex = buildSearchIndexFromPromptData(promptData);
                }
            }
        } catch (error) {
            console.warn('Could not load search index:', error);
            buildMinimalSearchIndex();
        }
    }

    // Build search index from prompt data
    function buildSearchIndexFromPromptData(promptData) {
        return promptData.map(prompt => ({
            title: prompt.title || '',
            description: prompt.description || '',
            category: prompt.category || '',
            tags: prompt.tags || [],
            url: `/useful-ai-prompts/prompts/${prompt.slug}/`,
            content: (prompt.prompt || '').toLowerCase(),
            searchText: [
                prompt.title || '',
                prompt.description || '',
                prompt.category || '',
                ...(prompt.tags || []),
                (prompt.use_cases || []).join(' ')
            ].join(' ').toLowerCase()
        }));
    }

    // Build minimal search index from page elements
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

    // Perform search with filters
    function performSearch(query) {
        if (!searchResults) return;
        
        const trimmedQuery = query.trim().toLowerCase();
        
        if (trimmedQuery.length === 0) {
            clearSearchResults();
            return;
        }
        
        const results = searchPrompts(trimmedQuery);
        displaySearchResults(results, trimmedQuery);
    }

    // Search prompts with enhanced scoring
    function searchPrompts(query) {
        const queryWords = query.split(/\s+/).filter(word => word.length > 0);
        
        return searchIndex
            .filter(item => applyFilters(item))
            .map(item => calculateSearchScore(item, query, queryWords))
            .filter(item => item.score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, 20);
    }

    // Apply current filters
    function applyFilters(item) {
        // Category filter
        if (currentFilters.category && currentFilters.category !== 'all') {
            if (!item.category.toLowerCase().includes(currentFilters.category.toLowerCase())) {
                return false;
            }
        }
        
        // Tag filters
        if (currentFilters.tags.length > 0) {
            const hasMatchingTag = currentFilters.tags.some(filterTag => 
                item.tags.some(itemTag => 
                    itemTag.toLowerCase().includes(filterTag.toLowerCase())
                )
            );
            if (!hasMatchingTag) return false;
        }
        
        // Sector filter
        if (currentFilters.sector) {
            const highValueSectors = ['biotechnology', 'space-economy', 'renewable-energy', 'quantum-computing', 'blockchain', 'government-digital', 'supply-chain', 'healthcare-digital'];
            if (currentFilters.sector === 'high-value' && !highValueSectors.includes(item.category)) {
                return false;
            }
        }
        
        return true;
    }

    // Calculate search score
    function calculateSearchScore(item, query, queryWords) {
        let score = 0;
        const titleLower = item.title.toLowerCase();
        const descriptionLower = item.description.toLowerCase();
        const categoryLower = item.category.toLowerCase();
        
        // Exact matches
        if (titleLower === query) score += 100;
        else if (titleLower.includes(query)) score += 50;
        
        // Title prefix match
        if (titleLower.startsWith(query)) score += 40;
        
        // Category match
        if (categoryLower === query || categoryLower.includes(query)) score += 30;
        
        // Description match
        if (descriptionLower.includes(query)) score += 20;
        
        // Tag matches
        item.tags.forEach(tag => {
            const tagLower = tag.toLowerCase();
            if (tagLower === query) score += 25;
            else if (tagLower.includes(query)) score += 15;
        });
        
        // Word-based matching
        queryWords.forEach(word => {
            if (item.searchText && item.searchText.includes(word)) score += 10;
        });
        
        // Multi-word boost
        if (queryWords.length > 1 && item.searchText) {
            const matchCount = queryWords.filter(word => item.searchText.includes(word)).length;
            score += (matchCount / queryWords.length) * 20;
        }
        
        return { ...item, score };
    }

    // Display search results
    function displaySearchResults(results, query) {
        if (!searchResults) return;
        
        if (results.length === 0) {
            searchResults.innerHTML = createNoResultsHTML(query);
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
        
        // Add related prompts section
        if (results.length > 0) {
            addRelatedPromptsSection(results[0], query);
        }
    }

    // Create no results HTML
    function createNoResultsHTML(query) {
        const suggestions = getSearchSuggestions();
        return `
            <div class="no-results">
                <div class="no-results-content">
                    <i class="fas fa-search"></i>
                    <h3>No results found</h3>
                    <p>No prompts match your search for "<strong>${escapeHtml(query)}</strong>"</p>
                    <div class="search-suggestions">
                        <p>Try searching for:</p>
                        <div class="suggestion-tags">
                            ${suggestions.map(suggestion => 
                                `<button class="suggestion-tag" onclick="searchByKeyword('${suggestion}')">${suggestion}</button>`
                            ).join('')}
                        </div>
                    </div>
                </div>
            </div>
        `;
    }

    // Get search suggestions for no results
    function getSearchSuggestions() {
        return ['analysis', 'creation', 'planning', 'debugging', 'presentation', 'management', 'communication', 'strategy'];
    }

    // Create search result HTML
    function createSearchResultHTML(result, query) {
        const highlightedTitle = highlightText(result.title, query);
        const highlightedDescription = highlightText(result.description.substring(0, 200), query);
        const isFavorite = favorites.includes(result.url);
        
        return `
            <div class="search-result">
                <div class="result-header">
                    <h3 class="result-title">
                        <a href="${result.url}">${highlightedTitle}</a>
                    </h3>
                    <div class="result-actions">
                        <button class="favorite-btn ${isFavorite ? 'active' : ''}" 
                                onclick="toggleFavorite('${result.url}')" 
                                title="${isFavorite ? 'Remove from' : 'Add to'} favorites">
                            <i class="fas fa-heart"></i>
                        </button>
                        <span class="result-category">${result.category}</span>
                    </div>
                </div>
                <p class="result-description">${highlightedDescription}${result.description.length > 200 ? '...' : ''}</p>
                ${result.tags && result.tags.length > 0 ? `
                    <div class="result-tags">
                        ${result.tags.slice(0, 4).map(tag => `<span class="tag" onclick="searchByKeyword('${tag}')">${tag}</span>`).join('')}
                        ${result.tags.length > 4 ? `<span class="tag-more">+${result.tags.length - 4}</span>` : ''}
                    </div>
                ` : ''}
            </div>
        `;
    }

    // Add related prompts section
    function addRelatedPromptsSection(topResult, query) {
        if (!topResult || !searchResults) return;
        
        const relatedPrompts = getRelatedPrompts(topResult, 4);
        if (relatedPrompts.length === 0) return;
        
        const relatedHTML = `
            <div class="related-section">
                <h3 class="related-title">
                    <i class="fas fa-lightbulb"></i>
                    Related Prompts
                </h3>
                <div class="related-prompts">
                    ${relatedPrompts.map(prompt => `
                        <div class="related-prompt">
                            <h4><a href="${prompt.url}">${prompt.title}</a></h4>
                            <span class="related-category">${prompt.category}</span>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
        
        searchResults.insertAdjacentHTML('beforeend', relatedHTML);
    }

    // Get related prompts
    function getRelatedPrompts(currentPrompt, count = 4) {
        if (!currentPrompt || !searchIndex.length) return [];
        
        const currentTags = currentPrompt.tags || [];
        const currentCategory = currentPrompt.category || '';
        
        return searchIndex
            .filter(prompt => prompt.title !== currentPrompt.title)
            .map(prompt => {
                let score = 0;
                
                // Category match
                if (prompt.category === currentCategory) score += 10;
                
                // Tag matches
                const commonTags = prompt.tags.filter(tag => currentTags.includes(tag));
                score += commonTags.length * 5;
                
                // Title similarity
                const currentWords = currentPrompt.title.toLowerCase().split(/\s+/);
                const promptWords = prompt.title.toLowerCase().split(/\s+/);
                const commonWords = currentWords.filter(word => promptWords.includes(word) && word.length > 3);
                score += commonWords.length * 2;
                
                return { ...prompt, score };
            })
            .filter(prompt => prompt.score > 0)
            .sort((a, b) => b.score - a.score)
            .slice(0, count);
    }

    // Utility functions
    function highlightText(text, query) {
        if (!text || !query) return escapeHtml(text || '');
        
        const words = query.toLowerCase().split(/\s+/).filter(word => word.length > 0);
        let highlightedText = escapeHtml(text);
        
        words.forEach(word => {
            const regex = new RegExp(`(${escapeRegExp(word)})`, 'gi');
            highlightedText = highlightedText.replace(regex, '<mark>$1</mark>');
        });
        
        return highlightedText;
    }

    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    function escapeRegExp(string) {
        return string.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
    }

    function clearSearchResults() {
        if (searchResults) {
            searchResults.innerHTML = '';
        }
    }

    // Search history management
    function addToSearchHistory(query) {
        if (query.length < 2) return;
        
        searchHistory = searchHistory.filter(item => item !== query);
        searchHistory.unshift(query);
        searchHistory = searchHistory.slice(0, 10);
        
        localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
    }

    // Favorites management
    function toggleFavorite(url) {
        if (favorites.includes(url)) {
            favorites = favorites.filter(fav => fav !== url);
        } else {
            favorites.push(url);
        }
        localStorage.setItem('promptFavorites', JSON.stringify(favorites));
        
        // Update UI
        document.querySelectorAll(`.favorite-btn, .suggestion-favorite`).forEach(btn => {
            if (btn.onclick && btn.onclick.toString().includes(url)) {
                btn.classList.toggle('active', favorites.includes(url));
                const icon = btn.querySelector('i');
                if (icon) {
                    icon.className = favorites.includes(url) ? 'fas fa-heart' : 'far fa-heart';
                }
            }
        });
    }

    function removeFromHistory(query) {
        searchHistory = searchHistory.filter(item => item !== query);
        localStorage.setItem('searchHistory', JSON.stringify(searchHistory));
        
        // Refresh dropdown if open
        if (isDropdownOpen && searchInput.value.trim() === '') {
            showRecentSearches();
        }
    }

    // Setup keyboard shortcuts
    function setupKeyboardShortcuts() {
        document.addEventListener('keydown', (e) => {
            // Ctrl+K or Cmd+K for search
            if ((e.ctrlKey || e.metaKey) && e.key === 'k') {
                e.preventDefault();
                if (searchInput) {
                    searchInput.focus();
                    searchInput.select();
                }
            }
        });
    }

    // Global search functions
    window.searchByKeyword = function(keyword) {
        if (searchInput) {
            searchInput.value = keyword;
            addToSearchHistory(keyword);
            performSearch(keyword);
            hideSearchDropdown();
        }
    };

    window.toggleFavorite = toggleFavorite;
    window.removeFromHistory = removeFromHistory;

    // Initialize on DOM load
    document.addEventListener('DOMContentLoaded', () => {
        initializeEnhancedSearch();
        
        // Initialize search page functionality
        if (document.body.classList.contains('search-page')) {
            const searchPageInput = document.getElementById('searchPageInput');
            if (searchPageInput) {
                // Handle URL query parameter
                const urlParams = new URLSearchParams(window.location.search);
                const searchQuery = urlParams.get('q');
                if (searchQuery) {
                    searchPageInput.value = searchQuery;
                    performSearch(searchQuery);
                }
            }
        }
    });

})();