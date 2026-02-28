/**
 * Community Integration JavaScript
 * Handles Discord, Reddit, Twitter, and GitHub community features
 */

// Initialize community integration features
function initCommunityIntegration() {
  initRedditSharing();
  initTwitterIntegration();
  initDiscordFeatures();
  initGitHubDiscussions();
  initProductHuntIntegration();
  loadCommunityStats();
}

// Reddit sharing and cross-posting functionality
function initRedditSharing() {
  const redditShareBtn = document.getElementById("redditShareBtn");
  const redditCrossPostBtn = document.getElementById("redditCrossPostBtn");

  if (redditShareBtn) {
    redditShareBtn.addEventListener("click", () => {
      showRedditShareModal();
    });
  }

  if (redditCrossPostBtn) {
    redditCrossPostBtn.addEventListener("click", () => {
      showCrossPostModal();
    });
  }
}

// Show Reddit share modal with subreddit suggestions
function showRedditShareModal() {
  const modal = createRedditShareModal();
  document.body.appendChild(modal);

  // Show modal
  setTimeout(() => modal.classList.add("show"), 100);
}

function createRedditShareModal() {
  const modal = document.createElement("div");
  modal.className = "reddit-share-modal";
  modal.innerHTML = `
    <div class="modal-overlay"></div>
    <div class="modal-content">
      <div class="modal-header">
        <h3><i class="fab fa-reddit"></i> Share to Reddit</h3>
        <button class="modal-close">&times;</button>
      </div>
      
      <div class="modal-body">
        <div class="share-preview">
          <h4>Share: ${document.title}</h4>
          <p>${document.querySelector('meta[name="description"]')?.content || ""}</p>
          <small>${window.location.href}</small>
        </div>
        
        <div class="subreddit-suggestions">
          <h4>Suggested Subreddits:</h4>
          <div class="subreddit-options">
            <button class="subreddit-option" data-subreddit="ChatGPT">
              <i class="fab fa-reddit"></i>
              r/ChatGPT
              <span class="members">1.2M members</span>
            </button>
            <button class="subreddit-option" data-subreddit="artificial">
              <i class="fab fa-reddit"></i>
              r/artificial
              <span class="members">854K members</span>
            </button>
            <button class="subreddit-option" data-subreddit="productivity">
              <i class="fab fa-reddit"></i>
              r/productivity
              <span class="members">1.5M members</span>
            </button>
            <button class="subreddit-option" data-subreddit="MachineLearning">
              <i class="fab fa-reddit"></i>
              r/MachineLearning
              <span class="members">2.8M members</span>
            </button>
          </div>
        </div>
        
        <div class="custom-subreddit">
          <label for="customSubreddit">Or enter a specific subreddit:</label>
          <input type="text" id="customSubreddit" placeholder="r/yoursubreddit">
        </div>
        
        <div class="share-title">
          <label for="shareTitle">Post Title:</label>
          <input type="text" id="shareTitle" value="${document.title}" maxlength="300">
          <small class="char-count">300 characters remaining</small>
        </div>
      </div>
      
      <div class="modal-actions">
        <button class="btn-secondary cancel-btn">Cancel</button>
        <button class="btn-primary submit-btn">Share to Reddit</button>
      </div>
    </div>
  `;

  // Event listeners
  modal
    .querySelector(".modal-close")
    .addEventListener("click", () => closeModal(modal));
  modal
    .querySelector(".modal-overlay")
    .addEventListener("click", () => closeModal(modal));
  modal
    .querySelector(".cancel-btn")
    .addEventListener("click", () => closeModal(modal));
  modal
    .querySelector(".submit-btn")
    .addEventListener("click", () => submitRedditShare(modal));

  // Subreddit option selection
  modal.querySelectorAll(".subreddit-option").forEach((option) => {
    option.addEventListener("click", () => {
      // Remove active class from others
      modal
        .querySelectorAll(".subreddit-option")
        .forEach((opt) => opt.classList.remove("active"));
      option.classList.add("active");

      // Clear custom input
      modal.querySelector("#customSubreddit").value = "";
    });
  });

  // Character counter for title
  const titleInput = modal.querySelector("#shareTitle");
  const charCount = modal.querySelector(".char-count");
  titleInput.addEventListener("input", () => {
    const remaining = 300 - titleInput.value.length;
    charCount.textContent = `${remaining} characters remaining`;
    charCount.style.color = remaining < 50 ? "#e74c3c" : "";
  });

  return modal;
}

function submitRedditShare(modal) {
  const selectedSubreddit = modal.querySelector(".subreddit-option.active")
    ?.dataset.subreddit;
  const customSubreddit = modal
    .querySelector("#customSubreddit")
    .value.replace("r/", "");
  const shareTitle = modal.querySelector("#shareTitle").value;

  const subreddit = selectedSubreddit || customSubreddit;

  if (!subreddit) {
    alert("Please select or enter a subreddit");
    return;
  }

  if (!shareTitle.trim()) {
    alert("Please enter a title for your post");
    return;
  }

  // Construct Reddit URL
  const redditUrl = `https://www.reddit.com/r/${subreddit}/submit?${new URLSearchParams(
    {
      url: addUTMParams(window.location.href, "reddit"),
      title: shareTitle,
      text: `Found this useful collection of AI prompts. Thought you might find it helpful!`,
    },
  )}`;

  // Open Reddit in new tab
  window.open(redditUrl, "_blank");

  // Track the share
  trackCommunityEvent("reddit_share", {
    subreddit: subreddit,
    title: shareTitle,
  });

  closeModal(modal);
}

// Twitter/X integration functionality
function initTwitterIntegration() {
  const tweetPromptBtn = document.getElementById("tweetPromptBtn");
  const tweetThreadBtn = document.getElementById("tweetThreadBtn");

  if (tweetPromptBtn) {
    tweetPromptBtn.addEventListener("click", () => {
      tweetCurrentPrompt();
    });
  }

  if (tweetThreadBtn) {
    tweetThreadBtn.addEventListener("click", () => {
      createTwitterThread();
    });
  }
}

function tweetCurrentPrompt() {
  const promptTitle =
    document.querySelector("h1")?.textContent || document.title;
  const hashtags = ["UsefulAIPrompts", "AIProductivity", "ChatGPT"];

  const tweetText = `🚀 Just discovered this useful AI prompt: "${promptTitle}"\n\nCheck it out: ${addUTMParams(window.location.href, "twitter")}\n\n${hashtags.map((tag) => `#${tag}`).join(" ")}`;

  const twitterUrl = `https://twitter.com/intent/tweet?${new URLSearchParams({
    text: tweetText,
  })}`;

  window.open(twitterUrl, "_blank", "width=600,height=400");

  trackCommunityEvent("twitter_share", {
    type: "single_prompt",
    prompt: promptTitle,
  });
}

function createTwitterThread() {
  showTwitterThreadModal();
}

function showTwitterThreadModal() {
  const modal = createTwitterThreadModal();
  document.body.appendChild(modal);

  setTimeout(() => modal.classList.add("show"), 100);
}

function createTwitterThreadModal() {
  const modal = document.createElement("div");
  modal.className = "twitter-thread-modal";
  modal.innerHTML = `
    <div class="modal-overlay"></div>
    <div class="modal-content">
      <div class="modal-header">
        <h3><i class="fab fa-twitter"></i> Create Twitter Thread</h3>
        <button class="modal-close">&times;</button>
      </div>
      
      <div class="modal-body">
        <div class="thread-templates">
          <h4>Thread Templates:</h4>
          <div class="template-options">
            <button class="template-option" data-template="top5">
              🧵 Top 5 AI Prompts for [Category]
            </button>
            <button class="template-option" data-template="workflow">
              🔄 My AI-Powered Workflow Using These Prompts
            </button>
            <button class="template-option" data-template="before-after">
              📈 Before vs After: How AI Prompts Transformed My [Work]
            </button>
            <button class="template-option" data-template="custom">
              ✏️ Custom Thread
            </button>
          </div>
        </div>
        
        <div class="thread-preview" id="threadPreview">
          <div class="tweet-preview">
            <strong>1/</strong> Select a template to see preview
          </div>
        </div>
      </div>
      
      <div class="modal-actions">
        <button class="btn-secondary cancel-btn">Cancel</button>
        <button class="btn-primary create-btn" disabled>Create Thread</button>
      </div>
    </div>
  `;

  // Event listeners
  modal
    .querySelector(".modal-close")
    .addEventListener("click", () => closeModal(modal));
  modal
    .querySelector(".modal-overlay")
    .addEventListener("click", () => closeModal(modal));
  modal
    .querySelector(".cancel-btn")
    .addEventListener("click", () => closeModal(modal));
  modal
    .querySelector(".create-btn")
    .addEventListener("click", () => createThreadFromTemplate(modal));

  // Template selection
  modal.querySelectorAll(".template-option").forEach((option) => {
    option.addEventListener("click", () => {
      modal
        .querySelectorAll(".template-option")
        .forEach((opt) => opt.classList.remove("active"));
      option.classList.add("active");

      const template = option.dataset.template;
      updateThreadPreview(modal, template);

      modal.querySelector(".create-btn").disabled = false;
    });
  });

  return modal;
}

function updateThreadPreview(modal, template) {
  const preview = modal.querySelector("#threadPreview");
  const baseUrl = addUTMParams(window.location.href, "twitter");

  const templates = {
    top5: [
      "🧵 5 AI prompts that completely changed how I work:\n\nThread 👇",
      "1/ Strategic Planning Prompt 📊\n\nHelps create comprehensive roadmaps with stakeholder alignment\n\nLink: " +
        baseUrl,
      "2/ Code Review Expert 💻\n\nThorough code analysis with security & performance insights\n\nGame-changer for developers!",
      "3/ Creative Problem Solving 💡\n\nBreakthrough ideation using advanced thinking methodologies\n\nUnlocks innovation potential",
      "4/ Customer Journey Mapping 🗺️\n\nOptimizes touchpoints and improves user experience\n\nEssential for UX teams",
      "5/ Risk Assessment Specialist ⚖️\n\nComprehensive analysis with mitigation strategies\n\nCritical for decision-making",
      "That's the thread! 🎯\n\nAll these prompts and 250+ more at:\n" +
        baseUrl +
        "\n\n#UsefulAIPrompts #AIProductivity #ChatGPT",
    ],
    workflow: [
      "🔄 How I built an AI-powered workflow that saves me 10+ hours/week:\n\nThread 👇",
      "1/ Started with these AI prompts from @aj_geddes collection\n\n259+ professional prompts for every use case\n\n" +
        baseUrl,
      "2/ Morning Planning (5 mins) ⏰\n\nUse Strategic Planning prompts to map my day\nPrioritize tasks based on impact\nSet clear objectives",
      "3/ Content Creation (30 mins) ✍️\n\nCreative prompts help generate ideas\nStructured frameworks ensure quality\nConsistent output every time",
      "4/ Problem Solving (as needed) 🧠\n\nSystematic approach to challenges\nMultiple solution perspectives\nRisk assessment built-in",
      "5/ Results? 📈\n\n• 40% faster planning\n• 60% more creative output\n• 80% better decision-making\n• 100% more confidence",
      "The key: Having the right prompts ready 🔑\n\nCheck out the full collection:\n" +
        baseUrl +
        "\n\n#AIWorkflow #Productivity #ChatGPT",
    ],
    "before-after": [
      "📈 Before vs After: How AI prompts transformed my business workflow\n\nA thread 👇",
      "BEFORE 😓\n\n• 3 hours for strategic planning\n• Inconsistent quality\n• Analysis paralysis\n• Missed opportunities\n• Burnout from repetitive tasks",
      "AFTER (using AI prompts) 🚀\n\n• 30 minutes for better plans\n• Consistent framework\n• Clear decision criteria\n• Spot opportunities faster\n• Focus on high-value work",
      "The game-changer? 🎯\n\nDiscovered this collection of 259+ professional AI prompts\n\n" +
        baseUrl,
      "Key prompts that made the difference:\n\n✅ Strategic Planning Expert\n✅ Risk Assessment Specialist\n✅ Decision-Making Framework\n✅ Problem-Solving Expert",
      "Results after 30 days:\n\n📊 50% faster planning\n🎯 30% better outcomes\n⚡ 70% less decision fatigue\n🚀 2x project completion rate",
      "Want similar results? 💪\n\nStart with these proven prompts:\n" +
        baseUrl +
        "\n\n#AITransformation #ProductivityHack #BusinessGrowth",
    ],
  };

  const threadContent = templates[template] || [
    "Custom thread - create your own!",
  ];

  preview.innerHTML = threadContent
    .map(
      (tweet, index) =>
        `<div class="tweet-preview">
      <strong>${index + 1}/${threadContent.length}</strong> ${tweet}
    </div>`,
    )
    .join("");
}

function createThreadFromTemplate(modal) {
  const selectedTemplate = modal.querySelector(".template-option.active")
    ?.dataset.template;

  if (!selectedTemplate) {
    alert("Please select a template");
    return;
  }

  const firstTweet = modal
    .querySelector(".tweet-preview")
    .textContent.replace(/^\d+\/\d+\s/, "");

  const twitterUrl = `https://twitter.com/intent/tweet?${new URLSearchParams({
    text: firstTweet,
  })}`;

  window.open(twitterUrl, "_blank", "width=600,height=400");

  trackCommunityEvent("twitter_thread", {
    template: selectedTemplate,
  });

  closeModal(modal);
}

// Discord integration features
function initDiscordFeatures() {
  // Load Discord member count and online status
  loadDiscordStats();

  // Add Discord share functionality
  const discordElements = document.querySelectorAll('[href*="discord"]');
  discordElements.forEach((element) => {
    element.addEventListener("click", () => {
      trackCommunityEvent("discord_click", {
        source: element.textContent || "unknown",
      });
    });
  });
}

// GitHub Discussions integration
function initGitHubDiscussions() {
  loadGitHubDiscussionStats();

  // Track discussion clicks
  const discussionLinks = document.querySelectorAll('[href*="discussions"]');
  discussionLinks.forEach((link) => {
    link.addEventListener("click", () => {
      trackCommunityEvent("github_discussion_click", {
        category: link.href.split("/").pop() || "general",
      });
    });
  });
}

// Product Hunt integration
function initProductHuntIntegration() {
  // Load Product Hunt stats (if available)
  // This would typically connect to Product Hunt API

  const phLinks = document.querySelectorAll('[href*="producthunt"]');
  phLinks.forEach((link) => {
    link.addEventListener("click", () => {
      trackCommunityEvent("product_hunt_click", {
        source: "community_widget",
      });
    });
  });
}

// Load community statistics
async function loadCommunityStats() {
  try {
    // Load Discord member count
    await loadDiscordStats();

    // Load GitHub discussion stats
    await loadGitHubDiscussionStats();

    // Load Reddit subscriber counts (if available)
    await loadRedditStats();
  } catch (error) {
    console.log("Could not load community stats:", error);
  }
}

async function loadDiscordStats() {
  // Simulate Discord API call (replace with actual Discord widget or API)
  const memberCount = document.getElementById("discordMemberCount");
  if (memberCount) {
    // Simulate growing member count
    const baseCount = 1247;
    const randomGrowth = Math.floor(Math.random() * 50);
    memberCount.textContent = (baseCount + randomGrowth).toLocaleString();
  }
}

async function loadGitHubDiscussionStats() {
  try {
    // This could load from GitHub API if needed
    const discussionCount = document.getElementById("discussionCount");
    const contributorCount = document.getElementById("contributorCount");

    if (discussionCount) {
      discussionCount.textContent = "24";
    }

    if (contributorCount) {
      contributorCount.textContent = "156";
    }
  } catch (error) {
    console.log("Could not load GitHub discussion stats:", error);
  }
}

async function loadRedditStats() {
  // This would load actual subscriber counts from Reddit API if available
  console.log("Reddit stats loading...");
}

// Utility functions
function closeModal(modal) {
  modal.classList.remove("show");
  setTimeout(() => {
    if (modal.parentNode) {
      modal.parentNode.removeChild(modal);
    }
  }, 300);
}

function addUTMParams(url, source) {
  const urlObj = new URL(url);
  urlObj.searchParams.set("utm_source", source);
  urlObj.searchParams.set("utm_medium", "community");
  urlObj.searchParams.set("utm_campaign", "social_share");
  return urlObj.toString();
}

function trackCommunityEvent(eventName, data) {
  // Google Analytics 4
  if (typeof gtag !== "undefined") {
    gtag("event", eventName, {
      community_platform:
        data.subreddit || data.template || data.category || "general",
      event_category: "community_engagement",
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

  console.log(`Community event tracked: ${eventName}`, data);
}

// Export functions
window.communityIntegration = {
  init: initCommunityIntegration,
  shareToReddit: showRedditShareModal,
  tweetPrompt: tweetCurrentPrompt,
  createThread: createTwitterThread,
  trackEvent: trackCommunityEvent,
};

// Auto-initialize if DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initCommunityIntegration);
} else {
  initCommunityIntegration();
}
