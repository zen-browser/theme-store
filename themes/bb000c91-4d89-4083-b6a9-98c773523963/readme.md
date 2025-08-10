
# Gruvbox Zen Theme

A **Gruvbox-inspired CSS theme** for [Zen Browser](https://zen-browser.app/) (and Firefox-based browsers).  
This theme brings the warm, retro feel of Gruvbox to the Zen browsing experience, with consistent colors, accent highlights, and polished UI spacing.

![Screenshot Preview](ss.png)

## Features
- 🎨 **Gruvbox Dark palette** applied to the Zen UI
- 🔴 Optional **Gruvbox Red** backgrounds for toolbars and main browser UI
- ✨ Matching accent colors for selected items
- 📐 Maintains Zen’s spacing and rounded edges
- 🖌 `!important` applied to ensure proper overrides

## Installation
1. **Enable userChrome.css support** in Zen / Firefox:
   - Go to `about:config`
   - Set `toolkit.legacyUserProfileCustomizations.stylesheets` to `true`
2. **Find your profile folder**:
   - Go to `about:support`
   - Under **Profile Folder**, click **Open Folder**
3. **Create the `chrome` folder** (if it doesn’t exist)
4. Place `userChrome.css` inside the `chrome` folder with the contents of this theme.
5. Restart Zen Browser.

## Customization
You can tweak the theme colors in `:root { ... }` variables inside the CSS:
- `--zen-primary-color` → Text color
- `--zen-main-browser-background` → Main UI background
- `--toolbox-textcolor` → Toolbar text color

For Gruvbox palette reference:
- **fg:** `#ebdbb2`
- **bg dark0:** `#282828`
- **bg dark1:** `#32302f`
- **red:** `#cc241d` (normal), `#fb4934` (bright)

## License
This project is licensed under the [MIT License](LICENSE).

---
**Author:** Your Name  
**Theme Base:** Gruvbox Color Scheme by [Pavel Pertsev](https://github.com/morhetz/gruvbox)
