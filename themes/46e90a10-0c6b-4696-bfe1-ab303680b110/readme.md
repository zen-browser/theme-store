
# Tab Memory Hover

Displays memory usage for the currently hovered tab inside Zen Browser's native hover card.

Because this mod uses privileged OS-level memory APIs (`ChromeUtils.requestProcInfo`), it cannot be installed simply via CSS. You must install the JavaScript code manually using `fx-autoconfig`.

## Installation Instructions

1. Ensure you have [fx-autoconfig](https://github.com/MrOtherGuy/fx-autoconfig) set up in your Zen Browser profile.
2. In your profile folder, navigate to the `chrome/JS/` directory.
3. Create a new file named `tab-memory-hover.uc.js`.
4. Copy and paste the script below into that file.
5. Restart your browser!

### The Script (`tab-memory-hover.uc.js`)

// ==UserScript==
// @name           Tab Memory Hover
// @description    Displays memory usage inside the tab hover card.
// @author         Zen Community
// @include        main
// ==/UserScript==

(function() {
  window.addEventListener("popupshowing", async (e) => {
    const panel = e.target;
    if (panel.id !== "tab-preview-panel") return;

let memoryContainer = panel.querySelector(".tab-preview-memory-container");
    let memoryValue;

if (!memoryContainer) {
      memoryContainer = document.createElement("div");
      memoryContainer.className = "tab-preview-memory-container";
      
      Object.assign(memoryContainer.style, {
        display: "flex",
        alignItems: "center",
        gap: "6px",
        marginTop: "4px",
        fontSize: "0.95em",
        color: "var(--text-color-deemphasized, gray)"
      });
      
      const icon = document.createElement("span");
      icon.textContent = "💾";
      icon.style.opacity = "0.8";

memoryValue = document.createElement("span");
      memoryValue.className = "tab-preview-memory-value";
      memoryValue.style.fontWeight = "500";
      
      memoryContainer.appendChild(icon);
      memoryContainer.appendChild(memoryValue);

const textContainer = panel.querySelector(".tab-preview-text-container");
      if (textContainer) {
        textContainer.appendChild(memoryContainer);
      }
    } else {
      memoryValue = memoryContainer.querySelector(".tab-preview-memory-value");
    }
    
    memoryValue.textContent = "Calculating...";
    memoryContainer.hidden = false;

const tab = panel.triggerNode || panel.anchorNode;
    if (!tab || !tab.linkedBrowser) {
      memoryContainer.hidden = true;
      return;
    }

if (tab.getAttribute("pending")) {
      memoryValue.textContent = "Sleeping";
      return;
    }

try {
      const browser = tab.linkedBrowser;
      const osPid = browser.frameLoader?.remoteTab?.osPid || -1;
      const bcId = browser.browsingContext?.id || -1;
      
      const procInfo = await ChromeUtils.requestProcInfo();
      
      let foundBytes = 0;
      
      // Check the parent process first just in case
      if (procInfo.pid === osPid) {
          foundBytes = procInfo.memory || procInfo.residentSetSize || procInfo.memorySize || 0;
      }

// Scan children
      for (const child of procInfo.children) {
        if (child.pid === osPid) {
          foundBytes = child.memory || child.residentSetSize || child.memorySize || 0;
        }
        
        for (const win of child.windows) {
          if (win.outerWindowId === bcId) {
             foundBytes = child.memory || child.residentSetSize || child.memorySize || 0;
          }
        }
      }
      
      if (foundBytes > 0) {
        let str = foundBytes < 1073741824 ? 
          `${Math.round(foundBytes / 1048576)} MB` : 
          `${(foundBytes / 1073741824).toFixed(1)} GB`;
        memoryValue.textContent = str;
      } else {
        memoryContainer.hidden = true;
      }
      
    } catch(err) {
      console.error("TabMemoryHover Error:", err);
      memoryContainer.hidden = true;
    }
  });
})();
