/**
 * Viral Features JavaScript
 * Handles Prompt of the Day, trending content, and viral mechanics
 */

// Prompt of the Day data and functionality
const promptOfTheDayData = [
  {
    title: "Strategic Roadmap Generator",
    category: "planning",
    description:
      "Create comprehensive strategic roadmaps with stakeholder alignment and milestone tracking.",
    url: "/useful-ai-prompts/prompts/planning/strategic-roadmap-generator/",
    tags: ["strategy", "planning", "roadmap"],
    popularity: 95,
  },
  {
    title: "Code Review Expert",
    category: "technical-workflows",
    description:
      "Conduct thorough code reviews with security, performance, and maintainability analysis.",
    url: "/useful-ai-prompts/prompts/technical-workflows/code-review-expert/",
    tags: ["development", "code review", "quality"],
    popularity: 88,
  },
  {
    title: "Breakthrough Ideation Expert",
    category: "creativity-innovation",
    description:
      "Generate innovative solutions using advanced creative thinking methodologies.",
    url: "/useful-ai-prompts/prompts/creativity-innovation/breakthrough-ideation-expert/",
    tags: ["innovation", "creativity", "brainstorming"],
    popularity: 82,
  },
  {
    title: "Customer Journey Mapping Expert",
    category: "customer-focused",
    description:
      "Map comprehensive customer journeys with touchpoint optimization strategies.",
    url: "/useful-ai-prompts/prompts/customer-focused/customer-journey-mapping-expert/",
    tags: ["customer experience", "journey mapping", "UX"],
    popularity: 79,
  },
  {
    title: "Risk Assessment Specialist",
    category: "analysis",
    description:
      "Conduct comprehensive risk assessments with mitigation strategies and impact analysis.",
    url: "/useful-ai-prompts/prompts/analysis/risk-assessment-specialist/",
    tags: ["risk management", "analysis", "mitigation"],
    popularity: 75,
  },
];

// Trending prompts data (would normally come from analytics)
const trendingPromptsData = [
  {
    title: "API Design Expert",
    category: "technical-workflows",
    views: 2847,
    shares: 156,
    trend: "+23%",
    url: "/useful-ai-prompts/prompts/technical-workflows/api-design-expert/",
  },
  {
    title: "Content Calendar Planning Expert",
    category: "business-workflows",
    views: 2134,
    shares: 198,
    trend: "+31%",
    url: "/useful-ai-prompts/prompts/business-workflows/content-calendar-planning-expert/",
  },
  {
    title: "Crisis Management Expert",
    category: "management-leadership",
    views: 1876,
    shares: 142,
    trend: "+18%",
    url: "/useful-ai-prompts/prompts/management-leadership/crisis-management-expert/",
  },
  {
    title: "User Experience Design Expert",
    category: "customer-focused",
    views: 1654,
    shares: 201,
    trend: "+45%",
    url: "/useful-ai-prompts/prompts/customer-focused/user-experience-design-expert/",
  },
  {
    title: "Financial Model Builder",
    category: "analysis",
    views: 1432,
    shares: 89,
    trend: "+12%",
    url: "/useful-ai-prompts/prompts/analysis/financial-model-builder/",
  },
  {
    title: "Team Building Expert",
    category: "management-leadership",
    views: 1298,
    shares: 167,
    trend: "+28%",
    url: "/useful-ai-prompts/prompts/management-leadership/team-building-expert/",
  },
];

// Initialize viral features
function initViralFeatures() {
  initPromptOfTheDay();
  initTrendingPrompts();
  initNewsletterSignup();
  initEmbedWidget();
  initCommunityHighlights();
  loadViralAnalytics();
}

// Prompt of the Day functionality
function initPromptOfTheDay() {
  const today = new Date();
  const dayOfYear = Math.floor(
    (today - new Date(today.getFullYear(), 0, 0)) / 86400000,
  );
  const selectedPrompt =
    promptOfTheDayData[dayOfYear % promptOfTheDayData.length];

  const potdContent = document.getElementById("potdPrompt");
  const potdLink = document.getElementById("potdLink");
  const potdShare = document.getElementById("potdShare");

  if (potdContent && selectedPrompt) {
    potdContent.innerHTML = `
      <h3>${selectedPrompt.title}</h3>
      <p class="potd-description">${selectedPrompt.description}</p>
      <div class="potd-meta">
        <span class="potd-category">${selectedPrompt.category.replace("-", " ")}</span>
        <div class="potd-tags">
          ${selectedPrompt.tags.map((tag) => `<span class="tag">${tag}</span>`).join("")}
        </div>
      </div>
      <div class="potd-popularity">
        <div class="popularity-bar">
          <div class="popularity-fill" style="width: ${selectedPrompt.popularity}%"></div>
        </div>
        <span class="popularity-text">${selectedPrompt.popularity}% community approval</span>
      </div>
    `;

    if (potdLink) {
      potdLink.href = selectedPrompt.url;
    }

    if (potdShare) {
      potdShare.addEventListener("click", () => {
        sharePromptOfTheDay(selectedPrompt);
      });
    }
  }
}

// Share Prompt of the Day
function sharePromptOfTheDay(prompt) {
  const shareText = `🌟 Today's Featured AI Prompt: ${prompt.title}\n\n${prompt.description}\n\nCheck it out: ${window.location.origin}${prompt.url}?utm_source=potd_share`;

  if (navigator.share) {
    navigator.share({
      title: `Prompt of the Day: ${prompt.title}`,
      text: shareText,
      url: `${window.location.origin}${prompt.url}?utm_source=potd_share`,
    });
  } else {
    // Fallback to copy to clipboard
    if (typeof copyToClipboard === "function") {
      copyToClipboard(shareText);
      showNotification("✨ Prompt of the Day link copied to clipboard!");
    }
  }

  // Track POTD share
  trackViralEvent("potd_share", {
    prompt: prompt.title,
    category: prompt.category,
  });
}

// Initialize trending prompts
function initTrendingPrompts() {
  const trendingGrid = document.getElementById("trendingGrid");

  if (trendingGrid && trendingPromptsData.length > 0) {
    const trendingHTML = trendingPromptsData
      .slice(0, 3)
      .map(
        (prompt) => `
      <div class="trending-card" data-category="${prompt.category}">
        <div class="trending-badge ${getTrendingBadgeClass(prompt.trend)}">
          <i class="fas fa-trending-up"></i>
          ${prompt.trend}
        </div>
        
        <div class="trending-content">
          <h4><a href="${prompt.url}">${prompt.title}</a></h4>
          <p class="trending-category">${prompt.category.replace("-", " ")}</p>
          
          <div class="trending-stats">
            <div class="stat">
              <i class="fas fa-eye"></i>
              <span>${formatNumber(prompt.views)} views</span>
            </div>
            <div class="stat">
              <i class="fas fa-share"></i>
              <span>${formatNumber(prompt.shares)} shares</span>
            </div>
          </div>
        </div>
        
        <div class="trending-actions">
          <a href="${prompt.url}" class="trending-link">
            View Prompt <i class="fas fa-arrow-right"></i>
          </a>
        </div>
      </div>
    `,
      )
      .join("");

    trendingGrid.innerHTML = trendingHTML;

    // Add click tracking for trending prompts
    trendingGrid.querySelectorAll(".trending-card").forEach((card) => {
      card.addEventListener("click", (e) => {
        if (!e.target.closest("a")) {
          const category = card.dataset.category;
          const link = card.querySelector("a");
          if (link) {
            trackViralEvent("trending_click", { category });
            window.location.href = link.href;
          }
        }
      });
    });
  }
}

// Get trending badge class based on trend percentage
function getTrendingBadgeClass(trend) {
  const percent = parseInt(trend.replace("%", "").replace("+", ""));
  if (percent >= 30) return "hot";
  if (percent >= 20) return "warm";
  return "trending";
}

// Newsletter signup functionality
function initNewsletterSignup() {
  const newsletterForm = document.getElementById("newsletterForm");
  const emailInput = document.getElementById("emailInput");

  if (newsletterForm) {
    newsletterForm.addEventListener("submit", async (e) => {
      e.preventDefault();

      const email = emailInput.value.trim();
      if (!email || !isValidEmail(email)) {
        showNotification("Please enter a valid email address.", "error");
        return;
      }

      // Disable form during submission
      const submitBtn = newsletterForm.querySelector(".subscribe-btn");
      const originalText = submitBtn.innerHTML;
      submitBtn.innerHTML =
        '<i class="fas fa-spinner fa-spin"></i> Subscribing...';
      submitBtn.disabled = true;

      try {
        // Simulate API call (replace with actual endpoint)
        await simulateNewsletterSignup(email);

        showNotification(
          "🎉 Successfully subscribed! Check your email for confirmation.",
          "success",
        );
        emailInput.value = "";

        // Track newsletter signup
        trackViralEvent("newsletter_signup", {
          email_domain: email.split("@")[1],
        });
      } catch (error) {
        showNotification(
          "Subscription failed. Please try again later.",
          "error",
        );
      } finally {
        submitBtn.innerHTML = originalText;
        submitBtn.disabled = false;
      }
    });
  }
}

// Simulate newsletter signup (replace with actual API)
async function simulateNewsletterSignup(email) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      // Simulate success rate
      if (Math.random() > 0.1) {
        resolve({ success: true });
      } else {
        reject(new Error("Subscription failed"));
      }
    }, 1000);
  });
}

// Initialize embed widget
function initEmbedWidget() {
  const copyEmbedBtn = document.getElementById("copyEmbedCode");
  const embedCode = document.getElementById("embedCode");

  if (copyEmbedBtn && embedCode) {
    copyEmbedBtn.addEventListener("click", () => {
      if (typeof copyToClipboard === "function") {
        copyToClipboard(embedCode.textContent);
        showNotification("📋 Embed code copied to clipboard!");

        // Track embed code copy
        trackViralEvent("embed_copy", {});
      }
    });
  }
}

// Initialize community highlights
function initCommunityHighlights() {
  const highlightCards = document.querySelectorAll(".highlight-card");

  highlightCards.forEach((card) => {
    card.addEventListener("click", (e) => {
      if (!e.target.closest("a")) {
        const link = card.querySelector("a");
        if (link) {
          trackViralEvent("community_highlight_click", {
            prompt: link.textContent,
          });
          window.location.href = link.href;
        }
      }
    });
  });
}

// Load viral analytics data
async function loadViralAnalytics() {
  try {
    // Update category popularity based on real data
    updateCategoryPopularity();

    // Update social proof numbers
    updateSocialProofNumbers();

    // Load recent activity
    loadRecentActivity();
  } catch (error) {
    console.log("Could not load viral analytics:", error);
  }
}

// Update category popularity chart
function updateCategoryPopularity() {
  const categoryBars = document.querySelectorAll(".category-bar");

  categoryBars.forEach((bar) => {
    const category = bar.dataset.category;
    const fillElement = bar.querySelector(".bar-fill");
    const valueElement = bar.querySelector(".bar-value");

    // Animate bar fill
    if (fillElement && valueElement) {
      const targetWidth = parseInt(fillElement.style.width) || 0;
      animateBar(fillElement, valueElement, targetWidth);
    }

    // Add click handler
    bar.addEventListener("click", () => {
      window.location.href = `/useful-ai-prompts/categories/${category}/`;
      trackViralEvent("category_popularity_click", { category });
    });
  });
}

// Animate category bar
function animateBar(fillElement, valueElement, targetWidth) {
  let currentWidth = 0;
  const increment = targetWidth / 50;

  const animation = setInterval(() => {
    currentWidth += increment;
    if (currentWidth >= targetWidth) {
      currentWidth = targetWidth;
      clearInterval(animation);
    }

    fillElement.style.width = `${currentWidth}%`;
    valueElement.textContent = `${Math.round(currentWidth)}%`;
  }, 20);
}

// Update social proof numbers
function updateSocialProofNumbers() {
  // Update GitHub stars, Discord members, etc.
  const githubStars = document.getElementById("githubStars");
  const discordMembers = document.getElementById("discordMembers");

  if (githubStars) {
    animateNumber(githubStars, 0, parseInt(githubStars.textContent) || 0);
  }

  if (discordMembers) {
    animateNumber(
      discordMembers,
      0,
      parseFloat(discordMembers.textContent) * 1000 || 1200,
    );
  }
}

// Animate number counting
function animateNumber(element, start, end) {
  const duration = 2000;
  const increment = (end - start) / (duration / 50);
  let current = start;

  const animation = setInterval(() => {
    current += increment;
    if (current >= end) {
      current = end;
      clearInterval(animation);
    }

    element.textContent = formatNumber(Math.round(current));
  }, 50);
}

// Load recent activity
function loadRecentActivity() {
  // This would typically load from an API
  // For now, we'll simulate some activity
  console.log("Recent activity loaded");
}

// Utility functions
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function formatNumber(num) {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + "M";
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + "K";
  }
  return num.toString();
}

function showNotification(message, type = "info") {
  // Create notification element
  const notification = document.createElement("div");
  notification.className = `viral-notification ${type}`;
  notification.innerHTML = `
    <div class="notification-content">
      <span>${message}</span>
      <button class="notification-close">
        <i class="fas fa-times"></i>
      </button>
    </div>
  `;

  // Add to page
  document.body.appendChild(notification);

  // Show notification
  setTimeout(() => notification.classList.add("show"), 100);

  // Auto-hide after 5 seconds
  setTimeout(() => hideNotification(notification), 5000);

  // Close button handler
  notification
    .querySelector(".notification-close")
    .addEventListener("click", () => {
      hideNotification(notification);
    });
}

function hideNotification(notification) {
  notification.classList.remove("show");
  setTimeout(() => {
    if (notification.parentNode) {
      notification.parentNode.removeChild(notification);
    }
  }, 300);
}

// Track viral events
function trackViralEvent(eventName, data) {
  // Google Analytics 4
  if (typeof gtag !== "undefined") {
    gtag("event", eventName, {
      custom_parameter_1: data.category || "",
      custom_parameter_2: data.prompt || "",
      value: 1,
    });
  }

  // Custom analytics
  if (window.customAnalytics) {
    window.customAnalytics.track(eventName, {
      ...data,
      timestamp: new Date().toISOString(),
      page: window.location.pathname,
    });
  }

  console.log(`Viral event tracked: ${eventName}`, data);
}

// Export functions
window.viralFeatures = {
  init: initViralFeatures,
  sharePromptOfTheDay: sharePromptOfTheDay,
  trackEvent: trackViralEvent,
};

// Auto-initialize if DOM is already loaded
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initViralFeatures);
} else {
  initViralFeatures();
}
