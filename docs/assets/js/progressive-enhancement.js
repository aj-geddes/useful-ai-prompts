// Progressive Enhancement Features
(function () {
  "use strict";

  // Feature Detection
  const hasIntersectionObserver = "IntersectionObserver" in window;
  const hasLocalStorage = "localStorage" in window;
  const hasServiceWorker = "serviceWorker" in navigator;
  const hasNotifications = "Notification" in window;
  const hasShareAPI = "share" in navigator;

  // Progressive Enhancement Manager
  class ProgressiveEnhancement {
    constructor() {
      this.features = new Map();
      this.init();
    }

    init() {
      this.setupLazyLoading();
      this.setupOfflineSupport();
      this.setupShareAPI();
      this.setupKeyboardShortcuts();
      this.setupDataPersistence();
      this.setupPerformanceOptimizations();
      this.setupAccessibilityEnhancements();
      this.setupNotifications();
    }

    // Lazy Loading for Images and Content
    setupLazyLoading() {
      if (!hasIntersectionObserver) return;

      const lazyImages = document.querySelectorAll("img[data-src]");
      const lazyContent = document.querySelectorAll(".lazy-content");

      const imageObserver = new IntersectionObserver(
        (entries, observer) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const img = entry.target;
              img.src = img.dataset.src;
              img.classList.remove("lazy");
              img.classList.add("loaded");
              observer.unobserve(img);
            }
          });
        },
        {
          rootMargin: "50px 0px",
          threshold: 0.1,
        },
      );

      const contentObserver = new IntersectionObserver(
        (entries, observer) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              const element = entry.target;
              element.classList.add("animate-in");
              observer.unobserve(element);
            }
          });
        },
        {
          rootMargin: "20px 0px",
          threshold: 0.1,
        },
      );

      lazyImages.forEach((img) => imageObserver.observe(img));
      lazyContent.forEach((content) => contentObserver.observe(content));

      this.features.set("lazyLoading", true);
    }

    // Offline Support and Caching
    setupOfflineSupport() {
      if (!hasServiceWorker) return;

      // Register service worker
      navigator.serviceWorker
        .register("/useful-ai-prompts/sw.js")
        .then((registration) => {
          console.log("SW registered:", registration);
          this.features.set("serviceWorker", true);

          // Listen for updates
          registration.addEventListener("updatefound", () => {
            const newWorker = registration.installing;
            newWorker.addEventListener("statechange", () => {
              if (
                newWorker.state === "installed" &&
                navigator.serviceWorker.controller
              ) {
                this.showUpdateNotification();
              }
            });
          });
        })
        .catch((error) => console.log("SW registration failed:", error));

      // Listen for offline/online events
      window.addEventListener("online", () =>
        this.handleOnlineStatusChange(true),
      );
      window.addEventListener("offline", () =>
        this.handleOnlineStatusChange(false),
      );

      // Initial status check
      this.updateOnlineStatus();
    }

    handleOnlineStatusChange(isOnline) {
      const statusIndicator =
        document.getElementById("connectionStatus") ||
        this.createStatusIndicator();

      if (isOnline) {
        statusIndicator.classList.remove("offline");
        statusIndicator.classList.add("online");
        statusIndicator.innerHTML = '<i class="fas fa-wifi"></i> Online';
        this.syncOfflineData();
      } else {
        statusIndicator.classList.remove("online");
        statusIndicator.classList.add("offline");
        statusIndicator.innerHTML =
          '<i class="fas fa-wifi-slash"></i> Offline Mode';
      }
    }

    createStatusIndicator() {
      const indicator = document.createElement("div");
      indicator.id = "connectionStatus";
      indicator.className = "connection-status";
      document.body.appendChild(indicator);
      return indicator;
    }

    updateOnlineStatus() {
      this.handleOnlineStatusChange(navigator.onLine);
    }

    showUpdateNotification() {
      const notification = document.createElement("div");
      notification.className = "update-notification";
      notification.innerHTML = `
                <div class="notification-content">
                    <i class="fas fa-download"></i>
                    <span>A new version is available!</span>
                    <button class="btn-primary" onclick="window.location.reload()">Update</button>
                    <button class="btn-secondary" onclick="this.parentElement.parentElement.remove()">
                        <i class="fas fa-times"></i>
                    </button>
                </div>
            `;
      document.body.appendChild(notification);

      // Auto-hide after 10 seconds
      setTimeout(() => {
        if (notification.parentElement) {
          notification.remove();
        }
      }, 10000);
    }

    // Native Share API
    setupShareAPI() {
      if (!hasShareAPI) return;

      const shareButtons = document.querySelectorAll(".share-btn");
      shareButtons.forEach((button) => {
        button.addEventListener("click", async (e) => {
          e.preventDefault();

          const url = button.dataset.url || window.location.href;
          const title = button.dataset.title || document.title;
          const text = button.dataset.text || "Check out this AI prompt:";

          try {
            await navigator.share({ title, text, url });
            this.trackEvent("share", "native_api", title);
          } catch (error) {
            // Fallback to clipboard
            this.fallbackShare(url, title);
          }
        });
      });

      this.features.set("shareAPI", true);
    }

    fallbackShare(url, title) {
      navigator.clipboard
        .writeText(url)
        .then(() => {
          this.showToast("Link copied to clipboard!", "success");
        })
        .catch(() => {
          // Ultimate fallback - select text
          const textArea = document.createElement("textarea");
          textArea.value = url;
          document.body.appendChild(textArea);
          textArea.select();
          document.execCommand("copy");
          document.body.removeChild(textArea);
          this.showToast("Link copied to clipboard!", "success");
        });
    }

    // Enhanced Keyboard Shortcuts
    setupKeyboardShortcuts() {
      const shortcuts = new Map([
        ["ctrl+k,cmd+k", () => this.focusSearch()],
        ["ctrl+/,cmd+/", () => this.showKeyboardShortcuts()],
        ["ctrl+shift+f,cmd+shift+f", () => this.toggleFilters()],
        ["ctrl+shift+s,cmd+shift+s", () => this.saveCurrentFilters()],
        ["escape", () => this.handleEscape()],
        ["ctrl+1,cmd+1", () => this.switchToCategory("all")],
        ["ctrl+2,cmd+2", () => this.switchToCategory("technical-workflows")],
        ["ctrl+3,cmd+3", () => this.switchToCategory("management-leadership")],
        ["f", () => this.toggleFavorites()],
        ["r", () => this.refreshSearch()],
      ]);

      document.addEventListener("keydown", (e) => {
        const isMac = navigator.platform.toUpperCase().indexOf("MAC") >= 0;
        const ctrlKey = isMac ? e.metaKey : e.ctrlKey;

        const combination = [
          ctrlKey && "ctrl",
          e.metaKey && "cmd",
          e.shiftKey && "shift",
          e.altKey && "alt",
          e.key.toLowerCase(),
        ]
          .filter(Boolean)
          .join("+");

        // Check for matches
        for (const [shortcut, action] of shortcuts) {
          if (shortcut.split(",").includes(combination)) {
            e.preventDefault();
            action();
            break;
          }
        }
      });

      this.features.set("keyboardShortcuts", true);
    }

    focusSearch() {
      const searchInput =
        document.getElementById("searchInput") ||
        document.getElementById("searchPageInput");
      if (searchInput) {
        searchInput.focus();
        searchInput.select();
      }
    }

    showKeyboardShortcuts() {
      const modal = this.createShortcutsModal();
      document.body.appendChild(modal);
    }

    createShortcutsModal() {
      const modal = document.createElement("div");
      modal.className = "shortcuts-modal";
      modal.innerHTML = `
                <div class="modal-overlay">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h3>Keyboard Shortcuts</h3>
                            <button class="modal-close" onclick="this.closest('.shortcuts-modal').remove()">
                                <i class="fas fa-times"></i>
                            </button>
                        </div>
                        <div class="modal-body">
                            <div class="shortcuts-grid">
                                <div class="shortcut-item">
                                    <kbd>Ctrl/Cmd + K</kbd>
                                    <span>Focus search</span>
                                </div>
                                <div class="shortcut-item">
                                    <kbd>Ctrl/Cmd + /</kbd>
                                    <span>Show shortcuts</span>
                                </div>
                                <div class="shortcut-item">
                                    <kbd>Ctrl/Cmd + Shift + F</kbd>
                                    <span>Toggle filters</span>
                                </div>
                                <div class="shortcut-item">
                                    <kbd>Escape</kbd>
                                    <span>Close modals/clear search</span>
                                </div>
                                <div class="shortcut-item">
                                    <kbd>F</kbd>
                                    <span>Toggle favorites</span>
                                </div>
                                <div class="shortcut-item">
                                    <kbd>R</kbd>
                                    <span>Refresh search</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            `;
      return modal;
    }

    // Data Persistence and Sync
    setupDataPersistence() {
      if (!hasLocalStorage) return;

      // Auto-save user preferences
      this.preferences = this.loadPreferences();

      // Save preferences on visibility change
      document.addEventListener("visibilitychange", () => {
        if (document.visibilityState === "hidden") {
          this.savePreferences();
        }
      });

      // Save on page unload
      window.addEventListener("beforeunload", () => {
        this.savePreferences();
      });

      this.features.set("dataPersistence", true);
    }

    loadPreferences() {
      try {
        return JSON.parse(localStorage.getItem("userPreferences") || "{}");
      } catch (error) {
        return {};
      }
    }

    savePreferences() {
      try {
        const currentPrefs = {
          searchHistory: JSON.parse(
            localStorage.getItem("searchHistory") || "[]",
          ),
          favorites: JSON.parse(
            localStorage.getItem("promptFavorites") || "[]",
          ),
          filters: JSON.parse(localStorage.getItem("savedFilters") || "{}"),
          theme: localStorage.getItem("theme"),
          viewPreference: localStorage.getItem("viewPreference"),
          lastVisit: new Date().toISOString(),
        };

        localStorage.setItem("userPreferences", JSON.stringify(currentPrefs));
      } catch (error) {
        console.warn("Failed to save preferences:", error);
      }
    }

    // Performance Optimizations
    setupPerformanceOptimizations() {
      // Preload critical resources
      this.preloadCriticalResources();

      // Memory cleanup
      this.setupMemoryCleanup();

      // Performance monitoring
      this.setupPerformanceMonitoring();

      this.features.set("performanceOptimizations", true);
    }

    preloadCriticalResources() {
      const criticalResources = [
        "/useful-ai-prompts/assets/data/search-index.json",
        "/useful-ai-prompts/PROMPT-INDEX.json",
      ];

      criticalResources.forEach((resource) => {
        const link = document.createElement("link");
        link.rel = "preload";
        link.href = resource;
        link.as = "fetch";
        link.crossOrigin = "anonymous";
        document.head.appendChild(link);
      });
    }

    setupMemoryCleanup() {
      // Clean up event listeners and observers
      const cleanupInterval = 5 * 60 * 1000; // 5 minutes

      setInterval(() => {
        // Remove unused event listeners
        const unusedElements = document.querySelectorAll(".removed, .hidden");
        unusedElements.forEach((element) => {
          const clonedElement = element.cloneNode(true);
          element.parentNode.replaceChild(clonedElement, element);
        });
      }, cleanupInterval);
    }

    setupPerformanceMonitoring() {
      if ("PerformanceObserver" in window) {
        // Monitor largest contentful paint
        const lcpObserver = new PerformanceObserver((entryList) => {
          const entries = entryList.getEntries();
          const lastEntry = entries[entries.length - 1];

          if (lastEntry.startTime > 2500) {
            console.warn("LCP is slow:", lastEntry.startTime);
          }
        });

        lcpObserver.observe({ entryTypes: ["largest-contentful-paint"] });

        // Monitor cumulative layout shift
        const clsObserver = new PerformanceObserver((entryList) => {
          let cls = 0;
          entryList.getEntries().forEach((entry) => {
            if (!entry.hadRecentInput) {
              cls += entry.value;
            }
          });

          if (cls > 0.1) {
            console.warn("CLS is high:", cls);
          }
        });

        clsObserver.observe({ entryTypes: ["layout-shift"] });
      }
    }

    // Accessibility Enhancements
    setupAccessibilityEnhancements() {
      // High contrast mode detection
      if (window.matchMedia("(prefers-contrast: high)").matches) {
        document.documentElement.classList.add("high-contrast");
      }

      // Reduced motion detection
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        document.documentElement.classList.add("reduced-motion");
      }

      // Focus management
      this.setupFocusManagement();

      // Screen reader optimizations
      this.setupScreenReaderOptimizations();

      this.features.set("accessibilityEnhancements", true);
    }

    setupFocusManagement() {
      // Skip to content link
      const skipLink = document.createElement("a");
      skipLink.href = "#main-content";
      skipLink.className = "skip-link";
      skipLink.textContent = "Skip to main content";
      document.body.insertBefore(skipLink, document.body.firstChild);

      // Focus trap for modals
      document.addEventListener("keydown", (e) => {
        if (e.key === "Tab" && document.querySelector(".modal-overlay")) {
          this.handleModalFocusTrap(e);
        }
      });
    }

    setupScreenReaderOptimizations() {
      // Add live regions for dynamic content
      const liveRegion = document.createElement("div");
      liveRegion.setAttribute("aria-live", "polite");
      liveRegion.setAttribute("aria-atomic", "true");
      liveRegion.className = "sr-only";
      liveRegion.id = "live-region";
      document.body.appendChild(liveRegion);

      // Announce search results
      const observer = new MutationObserver(() => {
        const resultsCount = document.getElementById("resultsCount");
        if (resultsCount) {
          liveRegion.textContent = resultsCount.textContent;
        }
      });

      const resultsContainer = document.getElementById("resultsGrid");
      if (resultsContainer) {
        observer.observe(resultsContainer, { childList: true, subtree: true });
      }
    }

    // Notifications
    setupNotifications() {
      if (!hasNotifications) return;

      // Request permission if needed
      if (Notification.permission === "default") {
        this.requestNotificationPermission();
      }

      this.features.set("notifications", Notification.permission === "granted");
    }

    async requestNotificationPermission() {
      const permission = await Notification.requestPermission();
      this.features.set("notifications", permission === "granted");
    }

    // Utility Methods
    showToast(message, type = "info", duration = 3000) {
      const toast = document.createElement("div");
      toast.className = `toast toast-${type}`;
      toast.innerHTML = `
                <div class="toast-content">
                    <i class="fas fa-${type === "success" ? "check" : type === "error" ? "exclamation-triangle" : "info"}"></i>
                    <span>${message}</span>
                </div>
            `;

      const container =
        document.getElementById("toast-container") ||
        this.createToastContainer();
      container.appendChild(toast);

      // Animate in
      requestAnimationFrame(() => {
        toast.classList.add("show");
      });

      // Auto remove
      setTimeout(() => {
        toast.classList.remove("show");
        setTimeout(() => toast.remove(), 300);
      }, duration);
    }

    createToastContainer() {
      const container = document.createElement("div");
      container.id = "toast-container";
      container.className = "toast-container";
      document.body.appendChild(container);
      return container;
    }

    trackEvent(category, action, label) {
      // Analytics tracking would go here
      console.log("Event tracked:", { category, action, label });
    }

    // Public API
    getFeatures() {
      return Object.fromEntries(this.features);
    }

    hasFeature(featureName) {
      return this.features.get(featureName) || false;
    }
  }

  // Initialize Progressive Enhancement
  const pe = new ProgressiveEnhancement();

  // Make available globally
  window.ProgressiveEnhancement = pe;

  // Debug info
  console.log("Progressive Enhancement Features:", pe.getFeatures());
})();
