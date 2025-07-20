// Global variables
let promptIndex = null;
let currentPrompts = [];

// Load prompt index on page load
document.addEventListener('DOMContentLoaded', async () => {
    await loadPromptIndex();
    displayAllPrompts();
});

// Load the prompt index from JSON
async function loadPromptIndex() {
    try {
        const response = await fetch('../PROMPT-INDEX.json');
        const data = await response.json();
        promptIndex = data;
        currentPrompts = data.prompts;
    } catch (error) {
        console.error('Error loading prompt index:', error);
        showError('Failed to load prompts. Please try again later.');
    }
}

// Display all prompts
function displayAllPrompts() {
    const promptList = document.getElementById('promptList');
    if (!currentPrompts || currentPrompts.length === 0) {
        promptList.innerHTML = '<p class="loading">Loading prompts...</p>';
        return;
    }

    promptList.innerHTML = currentPrompts.map(prompt => createPromptCard(prompt)).join('');
}

// Create a prompt card HTML
function createPromptCard(prompt) {
    const tags = prompt.tags ? prompt.tags.slice(0, 3).map(tag => 
        `<span class="tag">${tag}</span>`
    ).join('') : '';

    return `
        <div class="prompt-card" onclick="showPromptDetail('${prompt.id}')">
            <h3>${prompt.title}</h3>
            <div class="prompt-meta">
                <span class="prompt-category">${prompt.category}</span>
                ${prompt.subcategory ? `<span>›</span><span>${prompt.subcategory}</span>` : ''}
            </div>
            <p class="prompt-description">${truncateText(prompt.description, 150)}</p>
            <div class="prompt-tags">${tags}</div>
        </div>
    `;
}

// Truncate text with ellipsis
function truncateText(text, maxLength) {
    if (!text) return '';
    if (text.length <= maxLength) return text;
    return text.substr(0, maxLength).trim() + '...';
}

// Search prompts
function searchPrompts() {
    const searchTerm = document.getElementById('searchInput').value.toLowerCase();
    const categoryFilter = document.getElementById('categoryFilter').value;
    const complexityFilter = document.getElementById('complexityFilter').value;

    if (!promptIndex) return;

    currentPrompts = promptIndex.prompts.filter(prompt => {
        // Text search
        const matchesSearch = !searchTerm || 
            prompt.title.toLowerCase().includes(searchTerm) ||
            prompt.description.toLowerCase().includes(searchTerm) ||
            (prompt.tags && prompt.tags.some(tag => tag.toLowerCase().includes(searchTerm))) ||
            (prompt.use_cases && prompt.use_cases.some(uc => uc.toLowerCase().includes(searchTerm)));

        // Category filter
        const matchesCategory = !categoryFilter || 
            prompt.category === categoryFilter ||
            (categoryFilter === 'specialized' && ['healthcare', 'engineering', 'education', 'research'].includes(prompt.category));

        // Complexity filter (would need to be added to the index)
        const matchesComplexity = !complexityFilter || true; // All prompts are advanced for now

        return matchesSearch && matchesCategory && matchesComplexity;
    });

    displayAllPrompts();
}

// Filter prompts (called by select dropdowns)
function filterPrompts() {
    searchPrompts();
}

// Show prompts by category
function showCategory(category) {
    document.getElementById('categoryFilter').value = category;
    filterPrompts();
    document.getElementById('browse').scrollIntoView({ behavior: 'smooth' });
}

// Show prompt detail modal
async function showPromptDetail(promptId) {
    const prompt = promptIndex.prompts.find(p => p.id === promptId);
    if (!prompt) return;

    const modalContent = document.getElementById('modalContent');
    modalContent.innerHTML = `
        <h2>${prompt.title}</h2>
        <div class="prompt-detail-meta">
            <p><strong>Category:</strong> ${prompt.category} ${prompt.subcategory ? `› ${prompt.subcategory}` : ''}</p>
            <p><strong>Personas:</strong> ${prompt.personas.primary} + ${prompt.personas.secondary}</p>
            ${prompt.frameworks ? `<p><strong>Frameworks:</strong> ${prompt.frameworks.join(', ')}</p>` : ''}
        </div>
        <div class="prompt-detail-description">
            <h3>Description</h3>
            <p>${prompt.description}</p>
        </div>
        ${prompt.use_cases ? `
            <div class="prompt-detail-usecases">
                <h3>Use Cases</h3>
                <ul>
                    ${prompt.use_cases.map(uc => `<li>${uc}</li>`).join('')}
                </ul>
            </div>
        ` : ''}
        <div class="prompt-detail-actions">
            <a href="https://github.com/aj-geddes/useful-ai-prompts/blob/main/prompts/${prompt.path}" 
               target="_blank" class="btn btn-primary">View Full Prompt on GitHub</a>
            <button onclick="copyPromptPath('${prompt.path}')" class="btn btn-secondary">Copy Path</button>
        </div>
        ${prompt.tags ? `
            <div class="prompt-detail-tags">
                <h3>Tags</h3>
                <div class="prompt-tags">
                    ${prompt.tags.map(tag => `<span class="tag">${tag}</span>`).join('')}
                </div>
            </div>
        ` : ''}
    `;

    document.getElementById('promptModal').style.display = 'block';
}

// Close modal
function closeModal() {
    document.getElementById('promptModal').style.display = 'none';
}

// Show quick start modal
function showQuickStart() {
    document.getElementById('quickStartModal').style.display = 'block';
}

// Close quick start modal
function closeQuickStart() {
    document.getElementById('quickStartModal').style.display = 'none';
}

// Copy prompt path to clipboard
function copyPromptPath(path) {
    const fullPath = `prompts/${path}`;
    navigator.clipboard.writeText(fullPath).then(() => {
        alert('Path copied to clipboard!');
    }).catch(err => {
        console.error('Failed to copy:', err);
    });
}

// Show error message
function showError(message) {
    const promptList = document.getElementById('promptList');
    promptList.innerHTML = `<div class="error">${message}</div>`;
}

// Close modals when clicking outside
window.onclick = function(event) {
    if (event.target.classList.contains('modal')) {
        event.target.style.display = 'none';
    }
}

// Enable search on Enter key
document.addEventListener('keyup', function(event) {
    if (event.target.id === 'searchInput' && event.key === 'Enter') {
        searchPrompts();
    }
});

// Add smooth scrolling for anchor links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    });
});