# Install Prompt and App Installation

## Install Prompt and App Installation

```typescript
// hooks/useInstallPrompt.ts
import { useState, useEffect } from 'react';

interface BeforeInstallPromptEvent extends Event {
  prompt: () => Promise<void>;
  userChoice: Promise<{ outcome: 'accepted' | 'dismissed' }>;
}

export const useInstallPrompt = () => {
  const [promptEvent, setPromptEvent] = useState<BeforeInstallPromptEvent | null>(null);
  const [isInstalled, setIsInstalled] = useState(false);
  const [isIOSInstalled, setIsIOSInstalled] = useState(false);

  useEffect(() => {
    const handleBeforeInstallPrompt = (e: Event) => {
      e.preventDefault();
      setPromptEvent(e as BeforeInstallPromptEvent);
    };

    const handleAppInstalled = () => {
      setIsInstalled(true);
      setPromptEvent(null);
    };

    window.addEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
    window.addEventListener('appinstalled', handleAppInstalled);

    // Check if running as installed app
    if (window.matchMedia('(display-mode: standalone)').matches) {
      setIsInstalled(true);
    }

    // Check iOS
    const isIOSDevice = /iPad|iPhone|iPod/.test(navigator.userAgent);
    const isIOSApp = navigator.standalone === true;
    if (isIOSDevice && !isIOSApp) {
      setIsIOSInstalled(false);
    }

    return () => {
      window.removeEventListener('beforeinstallprompt', handleBeforeInstallPrompt);
      window.removeEventListener('appinstalled', handleAppInstalled);
    };
  }, []);

  const installApp = async () => {
    if (promptEvent) {
      await promptEvent.prompt();
      const { outcome } = await promptEvent.userChoice;
      if (outcome === 'accepted') {
        setIsInstalled(true);
      }
      setPromptEvent(null);
    }
  };

  return {
    promptEvent,
    canInstall: promptEvent !== null,
    isInstalled,
    isIOSInstalled,
    installApp
  };
};

// components/InstallPrompt.tsx
export const InstallPrompt: React.FC = () => {
  const { canInstall, isInstalled, installApp } = useInstallPrompt();

  if (isInstalled || !canInstall) return null;

  return (
    <div className="install-prompt">
      <h2>Install App</h2>
      <p>Install our app for quick access and offline support</p>
      <button onClick={installApp}>Install</button>
    </div>
  );
};
```
