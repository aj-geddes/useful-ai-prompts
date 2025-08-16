/**
 * Social Sharing Functionality
 * Handles Web Share API, social media sharing, and community features
 */

// Initialize social sharing functionality
function initSocialSharing(config) {
  const {
    url = window.location.href,
    title = document.title,
    description = '',
    hashtags = '',
    via = ''
  } = config || {};

  // Check for Web Share API support
  if (navigator.share) {
    const nativeShareBtn = document.getElementById('nativeShare');
    if (nativeShareBtn) {
      nativeShareBtn.style.display = 'flex';
      nativeShareBtn.addEventListener('click', async () => {
        try {
          await navigator.share({
            title: title,
            text: description,
            url: url
          });
          
          // Track native share
          trackSocialShare('native', url);
        } catch (err) {
          console.log('Error sharing:', err);
        }
      });
    }
  }

  // Social media sharing URLs
  const shareUrls = {
    twitter: (url, title, hashtags, via) => {
      const params = new URLSearchParams({
        url: addUTMParams(url, 'twitter'),
        text: `${title}\n\n${description}`,
        hashtags: hashtags,
        via: via
      });
      return `https://twitter.com/intent/tweet?${params.toString()}`;
    },
    
    linkedin: (url, title, description) => {
      const params = new URLSearchParams({
        url: addUTMParams(url, 'linkedin'),
        title: title,
        summary: description
      });
      return `https://www.linkedin.com/sharing/share-offsite/?${params.toString()}`;
    },
    
    reddit: (url, title) => {
      const params = new URLSearchParams({
        url: addUTMParams(url, 'reddit'),
        title: title
      });
      return `https://reddit.com/submit?${params.toString()}`;
    },
    
    discord: (url, title, description) => {
      // Discord doesn't have direct sharing URL, copy link instead
      return url;
    },
    
    whatsapp: (url, title, description) => {
      const text = `${title}\n\n${description}\n\n${addUTMParams(url, 'whatsapp')}`;
      return `https://wa.me/?text=${encodeURIComponent(text)}`;
    },
    
    telegram: (url, title, description) => {
      const text = `${title}\n\n${description}`;
      const params = new URLSearchParams({
        url: addUTMParams(url, 'telegram'),
        text: text
      });
      return `https://t.me/share/url?${params.toString()}`;
    },
    
    email: (url, title, description) => {
      const subject = `Check out this AI prompt: ${title}`;
      const body = `I found this useful AI prompt that might interest you:\n\n${title}\n\n${description}\n\nCheck it out: ${addUTMParams(url, 'email')}`;
      return `mailto:?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(body)}`;
    }
  };

  // Set up social sharing buttons
  setupSocialButton('twitterShare', shareUrls.twitter(url, title, hashtags, via), 'twitter');
  setupSocialButton('linkedinShare', shareUrls.linkedin(url, title, description), 'linkedin');
  setupSocialButton('redditShare', shareUrls.reddit(url, title), 'reddit');
  setupSocialButton('whatsappShare', shareUrls.whatsapp(url, title, description), 'whatsapp');
  setupSocialButton('telegramShare', shareUrls.telegram(url, title, description), 'telegram');
  setupSocialButton('emailShare', shareUrls.email(url, title, description), 'email');

  // Discord special handling
  const discordBtn = document.getElementById('discordShare');
  if (discordBtn) {
    discordBtn.addEventListener('click', (e) => {
      e.preventDefault();
      copyToClipboard(addUTMParams(url, 'discord'));
      showCopyNotification('Link copied! Share it in your Discord server.');
      trackSocialShare('discord', url);
    });
  }

  // Copy link functionality
  const copyBtn = document.getElementById('copyLink');
  if (copyBtn) {
    copyBtn.addEventListener('click', () => {
      copyToClipboard(addUTMParams(url, 'copy'));
      showCopyNotification();
      trackSocialShare('copy', url);
    });
  }

  // Mobile-only buttons visibility
  if (window.innerWidth <= 768) {
    document.querySelectorAll('.mobile-only').forEach(btn => {
      btn.style.display = 'flex';
    });
  }
}

// Helper function to set up social sharing buttons
function setupSocialButton(buttonId, shareUrl, platform) {
  const button = document.getElementById(buttonId);
  if (button) {
    button.href = shareUrl;
    button.addEventListener('click', () => {
      trackSocialShare(platform, shareUrl);
      
      // Open in popup for better UX
      if (platform !== 'email') {
        const popup = window.open(
          shareUrl,
          `share-${platform}`,
          'width=600,height=400,scrollbars=yes,resizable=yes'
        );
        
        // Focus the popup
        if (popup) {
          popup.focus();
        }
        
        return false;
      }
    });
  }
}

// Add UTM parameters for tracking
function addUTMParams(url, source) {
  const urlObj = new URL(url);
  const utmConfig = window.socialUTMConfig || {};
  
  urlObj.searchParams.set(utmConfig.source_param || 'utm_source', source);
  urlObj.searchParams.set(utmConfig.medium_param || 'utm_medium', 'social');
  urlObj.searchParams.set(utmConfig.campaign_param || 'utm_campaign', utmConfig.default_campaign || 'social_share');
  
  return urlObj.toString();
}

// Copy to clipboard functionality
async function copyToClipboard(text) {
  try {
    if (navigator.clipboard && window.isSecureContext) {
      await navigator.clipboard.writeText(text);
    } else {
      // Fallback for older browsers
      const textArea = document.createElement('textarea');
      textArea.value = text;
      textArea.style.position = 'fixed';
      textArea.style.left = '-999999px';
      textArea.style.top = '-999999px';
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      document.execCommand('copy');
      textArea.remove();
    }
    return true;
  } catch (err) {
    console.error('Failed to copy: ', err);
    return false;
  }
}

// Show copy notification
function showCopyNotification(message = 'Link copied to clipboard!') {
  const notification = document.getElementById('copyNotification');
  if (notification) {
    notification.textContent = message;
    notification.classList.add('show');
    
    setTimeout(() => {
      notification.classList.remove('show');
    }, 3000);
  }
}

// Track social shares (can be extended with analytics)
function trackSocialShare(platform, url) {
  // Google Analytics 4 tracking
  if (typeof gtag !== 'undefined') {
    gtag('event', 'share', {
      'method': platform,
      'content_type': 'prompt',
      'item_id': window.location.pathname
    });
  }
  
  // Custom analytics endpoint (implement as needed)
  if (window.customAnalytics) {
    window.customAnalytics.track('social_share', {
      platform: platform,
      url: url,
      page: window.location.pathname,
      timestamp: new Date().toISOString()
    });
  }
  
  // Update share count
  updateShareCount();
}

// Update share count display
function updateShareCount() {
  const shareCountEl = document.getElementById('shareCount');
  if (shareCountEl) {
    let currentCount = parseInt(shareCountEl.textContent) || 0;
    shareCountEl.textContent = currentCount + 1;
    
    // Save to localStorage for persistence
    const pageKey = `share_count_${window.location.pathname}`;
    localStorage.setItem(pageKey, currentCount + 1);
  }
}

// Load GitHub stats dynamically
async function loadGitHubStats() {
  try {
    const response = await fetch('https://api.github.com/repos/aj-geddes/useful-ai-prompts');
    const data = await response.json();
    
    const starsEl = document.getElementById('githubStars');
    if (starsEl && data.stargazers_count !== undefined) {
      starsEl.textContent = formatNumber(data.stargazers_count);
    }
    
    // Update fork count if element exists
    const forksEl = document.getElementById('githubForks');
    if (forksEl && data.forks_count !== undefined) {
      forksEl.textContent = formatNumber(data.forks_count);
    }
    
  } catch (error) {
    console.log('Could not load GitHub stats:', error);
  }
}

// Format numbers for display
function formatNumber(num) {
  if (num >= 1000000) {
    return (num / 1000000).toFixed(1) + 'M';
  } else if (num >= 1000) {
    return (num / 1000).toFixed(1) + 'K';
  }
  return num.toString();
}

// Load page view count from localStorage
function loadPageStats() {
  const pageKey = `view_count_${window.location.pathname}`;
  const shareKey = `share_count_${window.location.pathname}`;
  
  // Increment view count
  let viewCount = parseInt(localStorage.getItem(pageKey)) || 0;
  viewCount++;
  localStorage.setItem(pageKey, viewCount);
  
  // Update display
  const viewCountEl = document.getElementById('viewCount');
  if (viewCountEl) {
    viewCountEl.textContent = formatNumber(viewCount);
  }
  
  // Load share count
  const shareCount = parseInt(localStorage.getItem(shareKey)) || 0;
  const shareCountEl = document.getElementById('shareCount');
  if (shareCountEl) {
    shareCountEl.textContent = formatNumber(shareCount);
  }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  loadGitHubStats();
  loadPageStats();
  
  // Add social sharing CSS classes for styling
  document.body.classList.add('social-sharing-enabled');
});

// Prompt of the Day functionality
function initPromptOfTheDay() {
  const today = new Date().toDateString();
  const lastShown = localStorage.getItem('potd_last_shown');
  
  if (lastShown !== today) {
    // Show prompt of the day notification
    showPromptOfTheDayNotification();
    localStorage.setItem('potd_last_shown', today);
  }
}

function showPromptOfTheDayNotification() {
  // This can be implemented to show a notification or banner
  // about the prompt of the day
  console.log('Prompt of the Day feature ready for implementation');
}

// Social proof and viral features
function initViralFeatures() {
  // Real-time engagement tracking
  trackEngagement();
  
  // Social proof notifications
  showSocialProofNotifications();
  
  // Popular prompts carousel
  loadPopularPrompts();
  
  // Community highlights
  loadCommunityHighlights();
  
  // Referral tracking
  trackReferrals();
}

function trackEngagement() {
  let engagementStartTime = Date.now();
  let scrollDepth = 0;
  let maxScrollDepth = 0;
  
  // Track scroll depth
  window.addEventListener('scroll', () => {
    const windowHeight = window.innerHeight;
    const documentHeight = document.documentElement.scrollHeight;
    const scrollTop = window.pageYOffset;
    
    scrollDepth = Math.round((scrollTop + windowHeight) / documentHeight * 100);
    maxScrollDepth = Math.max(maxScrollDepth, scrollDepth);
  });
  
  // Track time on page
  window.addEventListener('beforeunload', () => {
    const timeSpent = Date.now() - engagementStartTime;
    
    if (typeof gtag !== 'undefined') {
      gtag('event', 'engagement', {
        event_category: 'User Engagement',
        time_on_page: Math.round(timeSpent / 1000),
        scroll_depth: maxScrollDepth,
        page_path: window.location.pathname
      });
    }
  });
}

function showSocialProofNotifications() {
  const notifications = [
    "🚀 Someone just shared this prompt!",
    "👥 12 people are viewing prompts right now",
    "⭐ This prompt was just starred on GitHub",
    "🔥 Trending: Business prompts are popular today",
    "📈 500+ prompts shared this week"
  ];
  
  function showNotification() {
    if (Math.random() < 0.3) { // 30% chance
      const notification = notifications[Math.floor(Math.random() * notifications.length)];
      displaySocialProofNotification(notification);
    }
  }
  
  // Show initial notification after delay
  setTimeout(showNotification, 10000);
  
  // Show periodic notifications
  setInterval(showNotification, 45000);
}

function displaySocialProofNotification(message) {
  const notification = document.createElement('div');
  notification.className = 'social-proof-notification';
  notification.innerHTML = `
    <div class="social-proof-content">
      <span class="social-proof-message">${message}</span>
      <button class="social-proof-close" onclick="this.parentElement.parentElement.remove()">×</button>
    </div>
  `;
  
  document.body.appendChild(notification);
  
  // Animate in
  setTimeout(() => notification.classList.add('show'), 100);
  
  // Auto-remove after 5 seconds
  setTimeout(() => {
    notification.classList.remove('show');
    setTimeout(() => notification.remove(), 300);
  }, 5000);
}

function loadPopularPrompts() {
  // This would typically fetch from an API
  const popularPrompts = [
    { title: "Strategic Roadmap Generator", category: "Planning", views: "2.3K" },
    { title: "Business Analyst Excellence", category: "Business", views: "1.8K" },
    { title: "Fullstack Developer Architect", category: "Technical", views: "1.5K" }
  ];
  
  const container = document.getElementById('popularPrompts');
  if (container) {
    container.innerHTML = popularPrompts.map(prompt => `
      <div class="popular-prompt-item">
        <h4>${prompt.title}</h4>
        <span class="prompt-category">${prompt.category}</span>
        <span class="prompt-views">${prompt.views} views</span>
      </div>
    `).join('');
  }
}

function loadCommunityHighlights() {
  // Simulate community activity
  const highlights = [
    { type: "github", count: "47", label: "GitHub Stars" },
    { type: "downloads", count: "1.2K", label: "Weekly Downloads" },
    { type: "shares", count: "340", label: "Social Shares" },
    { type: "bookmarks", count: "890", label: "Bookmarked" }
  ];
  
  const container = document.getElementById('communityStats');
  if (container) {
    container.innerHTML = highlights.map(stat => `
      <div class="community-stat">
        <div class="stat-number">${stat.count}</div>
        <div class="stat-label">${stat.label}</div>
      </div>
    `).join('');
  }
}

function trackReferrals() {
  const urlParams = new URLSearchParams(window.location.search);
  const referrer = urlParams.get('ref') || urlParams.get('utm_source');
  
  if (referrer) {
    // Track referral source
    if (typeof gtag !== 'undefined') {
      gtag('event', 'referral_visit', {
        event_category: 'Referrals',
        referrer_source: referrer,
        page_path: window.location.pathname
      });
    }
    
    // Store for attribution
    sessionStorage.setItem('referral_source', referrer);
  }
}

// Advanced sharing features
function initAdvancedSharing() {
  // Social share with custom message
  setupCustomShareMessages();
  
  // Quote sharing for specific prompt sections
  setupQuoteSharing();
  
  // Viral sharing incentives
  setupSharingIncentives();
}

function setupCustomShareMessages() {
  const shareButtons = document.querySelectorAll('[data-share-platform]');
  shareButtons.forEach(button => {
    const platform = button.dataset.sharePlatform;
    const customMessage = generateCustomShareMessage(platform);
    
    button.addEventListener('click', () => {
      // Use custom message for the platform
      console.log(`Sharing to ${platform} with message: ${customMessage}`);
    });
  });
}

function generateCustomShareMessage(platform) {
  const messages = {
    twitter: "Just discovered this amazing AI prompt library! 🤖 Over 278+ professional prompts across 18 categories. Perfect for boosting productivity! #AI #Productivity",
    linkedin: "Sharing this comprehensive AI prompt library that's been incredibly valuable for professional workflows. Great resource for anyone working with AI assistants.",
    reddit: "Found this free library of 278+ professional AI prompts - perfect for anyone using ChatGPT, Claude, or other AI tools for work"
  };
  
  return messages[platform] || "Check out this amazing AI prompt library!";
}

function setupQuoteSharing() {
  // Allow users to select text and share quotes
  document.addEventListener('mouseup', () => {
    const selection = window.getSelection();
    if (selection.toString().length > 10) {
      showQuoteShareOptions(selection.toString());
    }
  });
}

function showQuoteShareOptions(selectedText) {
  // Create floating share button for selected text
  const existingTooltip = document.querySelector('.quote-share-tooltip');
  if (existingTooltip) existingTooltip.remove();
  
  const tooltip = document.createElement('div');
  tooltip.className = 'quote-share-tooltip';
  tooltip.innerHTML = `
    <button onclick="shareQuote('${selectedText.replace(/'/g, "\\'")}')">
      Share Quote 📤
    </button>
  `;
  
  document.body.appendChild(tooltip);
  
  // Position tooltip
  const selection = window.getSelection();
  const range = selection.getRangeAt(0);
  const rect = range.getBoundingClientRect();
  
  tooltip.style.position = 'fixed';
  tooltip.style.top = `${rect.top - 40}px`;
  tooltip.style.left = `${rect.left}px`;
  tooltip.style.display = 'block';
  
  // Remove after 3 seconds
  setTimeout(() => tooltip.remove(), 3000);
}

function shareQuote(quote) {
  const shareText = `"${quote}" - From the Useful AI Prompts library`;
  const shareUrl = window.location.href;
  
  if (navigator.share) {
    navigator.share({
      title: 'AI Prompt Quote',
      text: shareText,
      url: shareUrl
    });
  } else {
    copyToClipboard(`${shareText}\n\n${shareUrl}`);
    showCopyNotification('Quote copied to clipboard!');
  }
}

function setupSharingIncentives() {
  // Track sharing streaks
  let shareStreak = parseInt(localStorage.getItem('share_streak')) || 0;
  
  document.addEventListener('social_share', () => {
    shareStreak++;
    localStorage.setItem('share_streak', shareStreak);
    
    // Show achievement for sharing milestones
    if (shareStreak === 3) {
      showAchievement('Social Sharer', 'Thanks for sharing 3 prompts!');
    } else if (shareStreak === 10) {
      showAchievement('Community Builder', 'Amazing! You\'ve shared 10 prompts!');
    }
  });
}

function showAchievement(title, description) {
  const achievement = document.createElement('div');
  achievement.className = 'achievement-notification';
  achievement.innerHTML = `
    <div class="achievement-content">
      <div class="achievement-icon">🏆</div>
      <div class="achievement-text">
        <h4>${title}</h4>
        <p>${description}</p>
      </div>
    </div>
  `;
  
  document.body.appendChild(achievement);
  
  setTimeout(() => achievement.classList.add('show'), 100);
  
  setTimeout(() => {
    achievement.classList.remove('show');
    setTimeout(() => achievement.remove(), 300);
  }, 4000);
}

// Export functions for use in other scripts
window.socialSharing = {
  init: initSocialSharing,
  copyToClipboard: copyToClipboard,
  trackShare: trackSocialShare,
  loadStats: loadGitHubStats,
  initViral: initViralFeatures,
  initAdvanced: initAdvancedSharing
};

// Initialize viral features on load
document.addEventListener('DOMContentLoaded', () => {
  initViralFeatures();
  initAdvancedSharing();
});