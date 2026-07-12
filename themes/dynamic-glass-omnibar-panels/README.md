# Dynamic Glass OmniBar & Panels for Zen Browser

Enhance your Zen Browser interface with a premium, modern, and adaptive glassmorphism layout. This mod injects a flawless glass blur effect into your popups and the expanded OmniBar (address bar) panel while strictly respecting your active theme's visual identity.

## ✨ Features

*   **Adaptive Theme Matching:** Automatically grabs your active theme's accent colors using advanced `color-mix()` syntax. If your theme changes, your panels instantly adapt.
*   **Pure Glass OmniBar:** Transforms the expanded address bar (OmniBar popup) into a lightweight 35% translucent glass surface with a rich `25px` backdrop blur.
*   **Frosty & Clean Panels:** Re-engineers the Extension and Identity panels with a carefully balanced opacity to prevent layout clipping while maintaining a beautiful frosted look.
*   **Context-Aware Design:** Keeps the default, closed state of your address bar completely untouched, respecting your theme's original toolbar design until triggered.

## 🚀 Installation

### For Users
This mod is fully compatible with the official **Zen Mods Store**. Simply find **Dynamic Glass OmniBar & Panels** in the store and click **Install**.

### For Developers / Local Testing
1. Copy the `metadata.json` and `theme.css` into your Zen Profile's `chrome/zen-themes/dynamic-glass-omnibar-panels/` directory.
2. Ensure `toolkit.legacyUserProfileCustomizations.stylesheets` is set to `true` in `about:config`.
3. Restart Zen Browser and enable it via **Settings → Zen Mods**.

## 🛠 Technical Details

Built using clean, high-specificity CSS targeting native Gecko/XUL layout components. It resolves common multi-view layering issues and bypasses hardware-accelerated clipping bugs inside detached browser popups.

---
Developed with passion for a cleaner web browsing experience. Feel free to open an issue or submit a pull request!