
# Active Tab Emoji Focus for Zen Browser

Make the current tab obvious at a glance.

This mod adds a centered emoji marker, a stronger border, and glow to the active tab while slightly dimming inactive tabs.

![Preview](https://raw.githubusercontent.com/constansino/zen-active-tab-emoji-focus/master/image.png)

## Features

- Center emoji marker on the active tab.
- Accent color follows each tab's container color (`--identity-icon-color`).
- Stronger active border and glow.
- Subtle dimming for inactive tabs.
- User-customizable options in Zen Mod preferences.

## Preferences

- `mod.active_tab_emoji_focus.active_marker`
  Example: `✨`, `🔥`, `✅`, `🧠`
- `mod.active_tab_emoji_focus.marker_size`
  Number in px, example: `11`, `13`, `16`
- `mod.active_tab_emoji_focus.inactive_opacity`
  Number from `0` to `100`
- `mod.active_tab_emoji_focus.border_width`
  Number in px, example: `2`, `3`

## Manual Install

1. Open your Zen profile folder.
2. Open `chrome/` (create it if missing).
3. Copy content from `chrome.manual.css` into `userChrome.css`.
4. Ensure `toolkit.legacyUserProfileCustomizations.stylesheets=true`.
5. Restart Zen Browser completely.

## Files for Zen Theme Store Submission

- `chrome.css`
- `preferences.json`
- `README.md`
- `image.png` (`600x400` PNG)
