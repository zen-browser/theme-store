
# Firefox DevTools Minimalist Theme

A revitalized, minimalist theme for Firefox DevTools, inspired by Zen's design. Includes CSS transitions and supports both light and dark modes.

## Preview

Here's a quick look at the theme:

![Merged Screenshot](https://github.com/ArjiAmin/firefox-devtools/blob/main/images/screenshot_0_merged.png)

## Installation

1. Download or clone the repository.
2. In Firefox/Zen browser, navigate to `about:config`, accept the risk warning, and search for `toolkit.legacyUserProfileCustomizations.stylesheets`. Ensure it's set to **true** (this should be the default in Zen).
3. Navigate to `about:profiles` in your browser.
4. Locate the section that says "This is the profile in use and it cannot be deleted." Find the "Root Directory" and click the **Open Folder** button.
5. Navigate to the `chrome` folder and paste the downloaded `UserContent.css` file.
6. Return to `about:profiles` and click "Restart normally...". After restart, open DevTools to see the applied theme.

## Development

If you want to customize the theme or make your own changes:

1. Open DevTools by pressing `F12`.
2. Click the three horizontal dots in the top-right corner to access Settings, or press F1.
3. Scroll down to "Advanced settings" and enable the "Enable browser chrome and add-on debugging toolboxes" and "Enable remote debugging" checkboxes.
4. Close and reopen DevTools.
5. Press `Ctrl + Shift + Alt + I` to open the Browser Toolbox, which allows you to inspect the DevTools interface itself.
6. Use the element inspector to identify elements you want to modify and test CSS changes in real-time.

**Note:** Changes made directly in the Browser Toolbox are temporary. To make permanent changes, update your `UserContent.css` file with your modifications. Remember that changes to `UserContent.css` require a browser restart to take effect.
