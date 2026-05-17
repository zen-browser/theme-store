
# Zen Mac Buttons

Mac-style titlebar buttons (close, minimize, maximize) for Zen Browser.

## Preview
![Preview](https://raw.githubusercontent.com/MiguelRequenaR/zen-mac-buttons/main/image.png)

## Installation

### Via Zen Mods (recommended)
Search for "Zen Mac Buttons" in `about:addons` inside Zen Browser.

### Manual
1. Go to `about:config` and enable `toolkit.legacyUserProfileCustomizations.stylesheets`
2. Find your profile folder at `about:profiles`
3. Create a `chrome/` folder inside it
4. Add a `userChrome.css` with: `@import "theme.css";`
5. Copy `theme.css` into the `chrome/` folder
6. Restart Zen Browser

## Compatibility
Tested on Zen Browser 1.19.13b — Ubuntu 26.04 LTS.

## Important Note: Button Positioning
By default, Linux places window controls on the right. To enjoy the macOS experience, you must move them to the left:

* **Ubuntu/GNOME:** Install the "GNOME Tweaks" application. Go to the "Windows" section and change the "Title bar button position" option to "Left".
