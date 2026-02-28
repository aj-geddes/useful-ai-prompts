---
layout: default
title: "Browse All AI Prompts — 679 Expert Prompts"
description: "Browse 679 professionally crafted AI prompts organized by category. Filter by development, security, finance, HR, healthcare, education, and 40+ more categories."
permalink: /prompts/
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "CollectionPage",
  "name": "Browse All AI Prompts",
  "description": "679 expert AI prompts across 47 categories. Free, copy-paste ready for Claude, ChatGPT, and any AI model.",
  "url": "https://aj-geddes.github.io/useful-ai-prompts/prompts/",
  "numberOfItems": 679,
  "breadcrumb": {
    "@type": "BreadcrumbList",
    "itemListElement": [
      { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://aj-geddes.github.io/useful-ai-prompts/" },
      { "@type": "ListItem", "position": 2, "name": "All Prompts", "item": "https://aj-geddes.github.io/useful-ai-prompts/prompts/" }
    ]
  }
}
</script>

<div class="browse-page">
  <div class="container">

    <nav aria-label="Breadcrumb" class="breadcrumb">
      <a href="{{ '/' | relative_url }}">Home</a>
      <span aria-hidden="true"> / </span>
      <span>All Prompts</span>
    </nav>

    <div class="browse-header">
      <h1 class="browse-title">Browse All AI Prompts</h1>
      <p class="browse-subtitle">{{ site.prompts.size }} expert prompts, free to copy and use with Claude, ChatGPT, or any AI model.</p>
      <div class="browse-search-wrap">
        <input
          type="search"
          id="browseSearch"
          class="browse-search"
          placeholder="Search prompts by title, category, or keyword…"
          aria-label="Search prompts"
          autocomplete="off"
        />
      </div>
    </div>

    <div class="filter-bar" role="group" aria-label="Filter by category">
      <button class="filter-chip active" data-category="all">All ({{ site.prompts.size }})</button>
      <button class="filter-chip" data-category="development">Development</button>
      <button class="filter-chip" data-category="security">Security</button>
      <button class="filter-chip" data-category="finance">Finance</button>
      <button class="filter-chip" data-category="human-resources">HR</button>
      <button class="filter-chip" data-category="healthcare">Healthcare</button>
      <button class="filter-chip" data-category="education">Education</button>
      <button class="filter-chip" data-category="project-management">Project Mgmt</button>
      <button class="filter-chip" data-category="operations">Operations</button>
      <button class="filter-chip" data-category="engineering">Engineering</button>
      <button class="filter-chip" data-category="customer-service">Customer Service</button>
      <button class="filter-chip" data-category="creative">Creative</button>
      <button class="filter-chip" data-category="research">Research</button>
      <button class="filter-chip" data-category="administrative">Administrative</button>
      <button class="filter-chip" data-category="academic">Academic</button>
      <button class="filter-chip more-btn" id="showMoreFilters">More <i class="fas fa-chevron-down"></i></button>
    </div>

    <div class="additional-filters" id="additionalFilters" style="display:none;">
      <button class="filter-chip" data-category="analysis">Analysis</button>
      <button class="filter-chip" data-category="management-leadership">Leadership</button>
      <button class="filter-chip" data-category="technical-workflows">Technical</button>
      <button class="filter-chip" data-category="research-workflows">Research Workflows</button>
      <button class="filter-chip" data-category="biotechnology">Biotech</button>
      <button class="filter-chip" data-category="blockchain">Blockchain</button>
      <button class="filter-chip" data-category="renewable-energy">Energy</button>
      <button class="filter-chip" data-category="supply-chain">Supply Chain</button>
    </div>

    <div class="browse-stats-bar" id="browseStatsBar">
      <span id="visibleCount">{{ site.prompts.size }}</span> prompts shown
    </div>

    <div class="prompts-grid" id="promptsGrid">
      {% for prompt in site.prompts %}
      <div class="prompt-card"
           data-category="{{ prompt.category }}"
           data-title="{{ prompt.title | downcase }}"
           data-description="{{ prompt.description | downcase | default: '' }}">
        <div class="prompt-category">{{ prompt.category | replace: '-', ' ' | replace: '/', ' · ' | capitalize }}</div>
        <h2 class="prompt-title">
          <a href="{{ prompt.url | relative_url }}">{{ prompt.title }}</a>
        </h2>
        {% if prompt.description %}
        <p class="prompt-description">{{ prompt.description | truncate: 130 }}</p>
        {% endif %}
        <div class="prompt-footer">
          <a href="{{ prompt.url | relative_url }}" class="prompt-link">View Details →</a>
          {% if prompt.prompt %}
          <button class="copy-btn-small"
                  data-clipboard-text="{{ prompt.prompt | strip | escape }}"
                  aria-label="Copy prompt to clipboard"
                  title="Copy prompt">
            <i class="fas fa-copy"></i>
          </button>
          {% endif %}
        </div>
      </div>
      {% endfor %}
    </div>

    <div class="no-results" id="noResults" style="display:none;">
      <i class="fas fa-search" aria-hidden="true"></i>
      <p>No prompts match your search. Try a different term or clear the filter.</p>
      <button class="btn-primary" id="clearFilters">Clear filters</button>
    </div>

  </div>
</div>

<script>
(function () {
  var search = document.getElementById('browseSearch');
  var grid = document.getElementById('promptsGrid');
  var noResults = document.getElementById('noResults');
  var statsBar = document.getElementById('visibleCount');
  var filterChips = document.querySelectorAll('.filter-chip:not(.more-btn)');
  var showMoreBtn = document.getElementById('showMoreFilters');
  var additionalFilters = document.getElementById('additionalFilters');
  var clearBtn = document.getElementById('clearFilters');
  var cards = document.querySelectorAll('.prompt-card');

  var currentFilter = 'all';
  var currentSearch = '';

  // Read ?category= from URL on load
  var params = new URLSearchParams(window.location.search);
  var urlCat = params.get('category');
  if (urlCat) {
    currentFilter = urlCat;
    filterChips.forEach(function (c) {
      if (c.dataset.category === urlCat) {
        c.classList.add('active');
        // Show additional filters panel if needed
        if (c.closest('#additionalFilters')) {
          additionalFilters.style.display = 'flex';
        }
      } else {
        c.classList.remove('active');
      }
    });
    filterPrompts();
  }

  if (search) {
    search.addEventListener('input', function () {
      currentSearch = this.value.toLowerCase().trim();
      filterPrompts();
    });
  }

  filterChips.forEach(function (chip) {
    chip.addEventListener('click', function () {
      filterChips.forEach(function (c) { c.classList.remove('active'); });
      this.classList.add('active');
      currentFilter = this.dataset.category;
      filterPrompts();
      // Update URL without reload
      var url = new URL(window.location);
      if (currentFilter === 'all') {
        url.searchParams.delete('category');
      } else {
        url.searchParams.set('category', currentFilter);
      }
      history.replaceState({}, '', url);
    });
  });

  if (showMoreBtn) {
    showMoreBtn.addEventListener('click', function () {
      var open = additionalFilters.style.display === 'flex';
      additionalFilters.style.display = open ? 'none' : 'flex';
      this.innerHTML = open
        ? 'More <i class="fas fa-chevron-down"></i>'
        : 'Less <i class="fas fa-chevron-up"></i>';
    });
  }

  if (clearBtn) {
    clearBtn.addEventListener('click', function () {
      currentFilter = 'all';
      currentSearch = '';
      if (search) search.value = '';
      filterChips.forEach(function (c) { c.classList.remove('active'); });
      var allChip = document.querySelector('.filter-chip[data-category="all"]');
      if (allChip) allChip.classList.add('active');
      filterPrompts();
    });
  }

  function filterPrompts() {
    var count = 0;
    cards.forEach(function (card) {
      var title = card.dataset.title || '';
      var desc = card.dataset.description || '';
      var cat = card.dataset.category || '';

      var matchSearch = !currentSearch ||
        title.indexOf(currentSearch) !== -1 ||
        desc.indexOf(currentSearch) !== -1 ||
        cat.indexOf(currentSearch) !== -1;

      var matchFilter = currentFilter === 'all' ||
        cat === currentFilter ||
        cat.indexOf(currentFilter) !== -1;

      if (matchSearch && matchFilter) {
        card.style.display = '';
        count++;
      } else {
        card.style.display = 'none';
      }
    });

    if (statsBar) statsBar.textContent = count;
    if (noResults) noResults.style.display = count === 0 ? 'block' : 'none';
    if (grid) grid.style.display = count === 0 ? 'none' : 'grid';
  }

  // Copy button
  document.addEventListener('click', async function (e) {
    var btn = e.target.closest('.copy-btn-small');
    if (!btn) return;
    var text = btn.dataset.clipboardText;
    if (!text) return;
    try {
      await navigator.clipboard.writeText(text);
      var icon = btn.querySelector('i');
      if (icon) { icon.className = 'fas fa-check'; setTimeout(function() { icon.className = 'fas fa-copy'; }, 2000); }
    } catch (_) {}
  });
})();
</script>
