/**
 * Keyboard Shortcuts and PWA Features
 * Enhances user experience with power-user shortcuts and progressive web app functionality
 */

(function () {
  "use strict";

  // Keyboard shortcuts configuration
  const shortcuts = {
    search: { key: "/", ctrl: false, alt: false, description: "Focus search" },
    searchCtrl: {
      key: "k",
      ctrl: true,
      alt: false,
      description: "Focus search (Ctrl+K)",
    },
    home: { key: "h", ctrl: false, alt: false, description: "Go to home" },
    categories: {
      key: "c",
      ctrl: false,
      alt: false,
      description: "Browse categories",
    },
    randomPrompt: {
      key: "r",
      ctrl: false,
      alt: false,
      description: "Random prompt",
    },
    toggleTheme: {
      key: "t",
      ctrl: false,
      alt: false,
      description: "Toggle dark mode",
    },
    help: { key: "?", ctrl: false, alt: false, description: "Show help" },
    copy: {
      key: "c",
      ctrl: true,
      alt: false,
      description: "Copy current prompt",
    },
    bookmark: {
      key: "b",
      ctrl: false,
      alt: false,
      description: "Bookmark current prompt",
    },
    share: {
      key: "s",
      ctrl: false,
      alt: false,
      description: "Share current prompt",
    },
    nextPage: {
      key: "ArrowRight",
      ctrl: false,
      alt: false,
      description: "Next page",
    },
    prevPage: {
      key: "ArrowLeft",
      ctrl: false,
      alt: false,
      description: "Previous page",
    },
    escape: {
      key: "Escape",
      ctrl: false,
      alt: false,
      description: "Close overlays",
    },
  };

  let isHelpVisible = false;
  let isModalOpen = false;

  // Initialize keyboard shortcuts
  function initKeyboardShortcuts() {
    document.addEventListener("keydown", handleKeydown);
    createHelpOverlay();
    initPWAFeatures();
    initAdvancedShortcuts();

    // Show keyboard shortcut hint on first visit
    if (!localStorage.getItem("keyboard_shortcuts_hint_shown")) {
      setTimeout(showKeyboardHint, 3000);
      localStorage.setItem("keyboard_shortcuts_hint_shown", "true");
    }
  }

  // Handle keydown events
  function handleKeydown(event) {
    // Don't trigger shortcuts when typing in input fields
    if (isTypingInInput(event.target)) {
      return;
    }

    // Don't trigger shortcuts when modals are open
    if (isModalOpen && event.key !== "Escape") {
      return;
    }

    const { key, ctrlKey, altKey, metaKey } = event;
    const isCmd = ctrlKey || metaKey;

    // Check each shortcut
    for (const [action, shortcut] of Object.entries(shortcuts)) {
      if (
        key === shortcut.key &&
        isCmd === shortcut.ctrl &&
        altKey === shortcut.alt
      ) {
        event.preventDefault();
        executeShortcut(action);
        break;
      }
    }
  }

  // Execute shortcut action
  function executeShortcut(action) {
    switch (action) {
      case "search":
      case "searchCtrl":
        focusSearch();
        break;
      case "home":
        navigateToHome();
        break;
      case "categories":
        navigateToCategories();
        break;
      case "randomPrompt":
        navigateToRandomPrompt();
        break;
      case "toggleTheme":
        toggleTheme();
        break;
      case "help":
        toggleHelp();
        break;
      case "copy":
        copyCurrentPrompt();
        break;
      case "bookmark":
        bookmarkCurrentPrompt();
        break;
      case "share":
        shareCurrentPrompt();
        break;
      case "nextPage":
        navigateToNextPage();
        break;
      case "prevPage":
        navigateToPreviousPage();
        break;
      case "escape":
        closeOverlays();
        break;
    }
  }

  // Shortcut implementations
  function focusSearch() {
    const searchInput = document.querySelector(
      "#searchInput, #searchPageInput, .search-input",
    );
    if (searchInput) {
      searchInput.focus();
      searchInput.select();
      showToast("Search focused");
    }
  }

  function navigateToHome() {
    if (window.location.pathname !== "/useful-ai-prompts/") {
      window.location.href = "/useful-ai-prompts/";
    } else {
      showToast("Already at home");
    }
  }

  function navigateToCategories() {
    window.location.href = "/useful-ai-prompts/categories/";
  }

  function navigateToRandomPrompt() {
    // Get random prompt from search index or fallback
    if (window.searchIndex && window.searchIndex.length > 0) {
      const randomIndex = Math.floor(Math.random() * window.searchIndex.length);
      const randomPrompt = window.searchIndex[randomIndex];
      window.location.href = randomPrompt.url;
    } else {
      showToast("Random prompt feature not available");
    }
  }

  function toggleTheme() {
    const html = document.documentElement;
    const isDark = html.classList.contains("dark");

    if (isDark) {
      html.classList.remove("dark");
      localStorage.setItem("theme", "light");
      showToast("Light mode enabled");
    } else {
      html.classList.add("dark");
      localStorage.setItem("theme", "dark");
      showToast("Dark mode enabled");
    }
  }

  function copyCurrentPrompt() {
    const promptContent = document.querySelector(
      ".prompt-content, .code-container pre",
    );
    if (promptContent) {
      const text = promptContent.textContent || promptContent.innerText;
      copyToClipboard(text);
      showToast("Prompt copied to clipboard");
    } else {
      showToast("No prompt content found");
    }
  }

  function bookmarkCurrentPrompt() {
    const url = window.location.href;
    const title = document.title;

    if (window.toggleFavorite) {
      window.toggleFavorite(url);
      showToast("Bookmark toggled");
    } else {
      // Fallback to browser bookmark
      if (navigator.userAgent.indexOf("Chrome") > -1) {
        showToast("Use Ctrl+D to bookmark in Chrome");
      } else {
        showToast("Use your browser's bookmark function");
      }
    }
  }

  function shareCurrentPrompt() {
    const url = window.location.href;
    const title = document.title;

    if (navigator.share) {
      navigator
        .share({
          title: title,
          url: url,
        })
        .then(() => {
          showToast("Shared successfully");
        })
        .catch(() => {
          copyToClipboard(url);
          showToast("URL copied to clipboard");
        });
    } else {
      copyToClipboard(url);
      showToast("URL copied to clipboard");
    }
  }

  function navigateToNextPage() {
    const nextButton = document.querySelector(
      '.pagination-btn:contains("Next"), .next-prompt, [aria-label="Next"]',
    );
    if (nextButton) {
      nextButton.click();
    } else {
      showToast("No next page available");
    }
  }

  function navigateToPreviousPage() {
    const prevButton = document.querySelector(
      '.pagination-btn:contains("Previous"), .prev-prompt, [aria-label="Previous"]',
    );
    if (prevButton) {
      prevButton.click();
    } else {
      showToast("No previous page available");
    }
  }

  function closeOverlays() {
    // Close help overlay
    if (isHelpVisible) {
      toggleHelp();
      return;
    }

    // Close search dropdown
    if (window.hideSearchDropdown) {
      window.hideSearchDropdown();
    }

    // Close any open modals
    const modals = document.querySelectorAll(".modal, .overlay, .dropdown");
    modals.forEach((modal) => {
      if (modal.style.display !== "none") {
        modal.style.display = "none";
      }
    });

    // Blur focused elements
    if (document.activeElement && document.activeElement.blur) {
      document.activeElement.blur();
    }

    showToast("Overlays closed");
  }

  // Create help overlay
  function createHelpOverlay() {
    const helpOverlay = document.createElement("div");
    helpOverlay.id = "keyboardHelpOverlay";
    helpOverlay.className = "keyboard-help-overlay";
    helpOverlay.innerHTML = `
            <div class="help-content">
                <div class="help-header">
                    <h3>Keyboard Shortcuts</h3>
                    <button class="help-close" onclick="window.keyboardShortcuts.toggleHelp()">×</button>
                </div>
                <div class="help-body">
                    <div class="help-section">
                        <h4>Navigation</h4>
                        <div class="shortcut-list">
                            <div class="shortcut-item">
                                <kbd>H</kbd>
                                <span>Go to home</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>C</kbd>
                                <span>Browse categories</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>R</kbd>
                                <span>Random prompt</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>←</kbd><kbd>→</kbd>
                                <span>Navigate pages</span>
                            </div>
                        </div>
                    </div>
                    <div class="help-section">
                        <h4>Search & Actions</h4>
                        <div class="shortcut-list">
                            <div class="shortcut-item">
                                <kbd>/</kbd>
                                <span>Focus search</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>Ctrl</kbd><kbd>K</kbd>
                                <span>Focus search</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>Ctrl</kbd><kbd>C</kbd>
                                <span>Copy prompt</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>B</kbd>
                                <span>Bookmark</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>S</kbd>
                                <span>Share</span>
                            </div>
                        </div>
                    </div>
                    <div class="help-section">
                        <h4>Interface</h4>
                        <div class="shortcut-list">
                            <div class="shortcut-item">
                                <kbd>T</kbd>
                                <span>Toggle theme</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>?</kbd>
                                <span>Show this help</span>
                            </div>
                            <div class="shortcut-item">
                                <kbd>Esc</kbd>
                                <span>Close overlays</span>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="help-footer">
                    <p>Press <kbd>?</kbd> anytime to show this help</p>
                </div>
            </div>
        `;

    document.body.appendChild(helpOverlay);
  }

  // Toggle help overlay
  function toggleHelp() {
    const helpOverlay = document.getElementById("keyboardHelpOverlay");
    if (helpOverlay) {
      isHelpVisible = !isHelpVisible;
      helpOverlay.style.display = isHelpVisible ? "flex" : "none";

      if (isHelpVisible) {
        isModalOpen = true;
        helpOverlay.setAttribute("aria-hidden", "false");
        // Focus first element for accessibility
        const closeButton = helpOverlay.querySelector(".help-close");
        if (closeButton) closeButton.focus();
      } else {
        isModalOpen = false;
        helpOverlay.setAttribute("aria-hidden", "true");
      }
    }
  }

  // PWA Features
  function initPWAFeatures() {
    // Install prompt
    let deferredPrompt;

    window.addEventListener("beforeinstallprompt", (e) => {
      e.preventDefault();
      deferredPrompt = e;
      showInstallButton();
    });

    // Install button click handler
    window.addEventListener("appinstalled", () => {
      hideInstallButton();
      showToast("App installed successfully!");
    });

    // Offline detection
    window.addEventListener("online", () => {
      showToast("Back online");
      document.documentElement.classList.remove("offline");
    });

    window.addEventListener("offline", () => {
      showToast("You are offline");
      document.documentElement.classList.add("offline");
    });

    // PWA update detection
    if ("serviceWorker" in navigator) {
      navigator.serviceWorker.addEventListener("controllerchange", () => {
        showUpdateNotification();
      });
    }
  }

  function showInstallButton() {
    let installButton = document.getElementById("pwa-install-button");
    if (!installButton) {
      installButton = document.createElement("button");
      installButton.id = "pwa-install-button";
      installButton.className = "pwa-install-button";
      installButton.innerHTML = `
                <i class="fas fa-download"></i>
                Install App
            `;
      installButton.addEventListener("click", installPWA);

      // Add to header or create floating button
      const header = document.querySelector("header, .header");
      if (header) {
        header.appendChild(installButton);
      } else {
        installButton.style.position = "fixed";
        installButton.style.bottom = "20px";
        installButton.style.right = "20px";
        installButton.style.zIndex = "1000";
        document.body.appendChild(installButton);
      }
    }
    installButton.style.display = "flex";
  }

  function hideInstallButton() {
    const installButton = document.getElementById("pwa-install-button");
    if (installButton) {
      installButton.style.display = "none";
    }
  }

  async function installPWA() {
    const deferredPrompt = window.deferredPrompt;
    if (deferredPrompt) {
      deferredPrompt.prompt();
      const { outcome } = await deferredPrompt.userChoice;

      if (outcome === "accepted") {
        showToast("App installation started");
      } else {
        showToast("App installation cancelled");
      }

      window.deferredPrompt = null;
      hideInstallButton();
    }
  }

  function showUpdateNotification() {
    const notification = document.createElement("div");
    notification.className = "update-notification";
    notification.innerHTML = `
            <div class="update-content">
                <span>New version available!</span>
                <button onclick="window.location.reload()">Update</button>
                <button onclick="this.parentElement.parentElement.remove()">Later</button>
            </div>
        `;

    document.body.appendChild(notification);

    setTimeout(() => {
      notification.classList.add("show");
    }, 100);
  }

  // Advanced shortcuts
  function initAdvancedShortcuts() {
    // Quick filter shortcuts
    document.addEventListener("keydown", (e) => {
      if (isTypingInInput(e.target)) return;

      // Number keys for quick category filtering
      if (e.key >= "1" && e.key <= "9" && !e.ctrlKey && !e.altKey) {
        const categoryIndex = parseInt(e.key) - 1;
        const categoryLinks = document.querySelectorAll(
          ".category-link, .category-card a",
        );
        if (categoryLinks[categoryIndex]) {
          e.preventDefault();
          categoryLinks[categoryIndex].click();
        }
      }
    });

    // Vim-style navigation
    document.addEventListener("keydown", (e) => {
      if (isTypingInInput(e.target)) return;

      switch (e.key.toLowerCase()) {
        case "j":
          if (!e.ctrlKey && !e.altKey) {
            e.preventDefault();
            scrollDown();
          }
          break;
        case "k":
          if (!e.ctrlKey && !e.altKey) {
            e.preventDefault();
            scrollUp();
          }
          break;
        case "g":
          if (!e.ctrlKey && !e.altKey) {
            e.preventDefault();
            scrollToTop();
          }
          break;
      }
    });
  }

  // Scroll functions
  function scrollDown() {
    window.scrollBy(0, 100);
  }

  function scrollUp() {
    window.scrollBy(0, -100);
  }

  function scrollToTop() {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }

  // Utility functions
  function isTypingInInput(target) {
    const inputTypes = ["INPUT", "TEXTAREA", "SELECT"];
    return (
      inputTypes.includes(target.tagName) ||
      target.contentEditable === "true" ||
      target.isContentEditable
    );
  }

  function copyToClipboard(text) {
    if (navigator.clipboard && window.isSecureContext) {
      return navigator.clipboard.writeText(text);
    } else {
      // Fallback for older browsers
      const textArea = document.createElement("textarea");
      textArea.value = text;
      textArea.style.position = "fixed";
      textArea.style.left = "-999999px";
      textArea.style.top = "-999999px";
      document.body.appendChild(textArea);
      textArea.focus();
      textArea.select();
      document.execCommand("copy");
      textArea.remove();
      return Promise.resolve();
    }
  }

  function showToast(message) {
    // Remove existing toast
    const existingToast = document.querySelector(".keyboard-toast");
    if (existingToast) {
      existingToast.remove();
    }

    const toast = document.createElement("div");
    toast.className = "keyboard-toast";
    toast.textContent = message;

    document.body.appendChild(toast);

    setTimeout(() => {
      toast.classList.add("show");
    }, 100);

    setTimeout(() => {
      toast.classList.remove("show");
      setTimeout(() => {
        toast.remove();
      }, 300);
    }, 2000);
  }

  function showKeyboardHint() {
    const hint = document.createElement("div");
    hint.className = "keyboard-hint";
    hint.innerHTML = `
            <div class="hint-content">
                <span>💡 Pro tip: Press <kbd>?</kbd> for keyboard shortcuts</span>
                <button onclick="this.parentElement.parentElement.remove()">Got it</button>
            </div>
        `;

    document.body.appendChild(hint);

    setTimeout(() => {
      hint.classList.add("show");
    }, 100);

    setTimeout(() => {
      hint.classList.remove("show");
      setTimeout(() => {
        hint.remove();
      }, 300);
    }, 5000);
  }

  // Export functions
  window.keyboardShortcuts = {
    init: initKeyboardShortcuts,
    toggleHelp: toggleHelp,
    executeShortcut: executeShortcut,
    showToast: showToast,
  };

  // Initialize on DOM load
  document.addEventListener("DOMContentLoaded", initKeyboardShortcuts);
})();
