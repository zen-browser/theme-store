# Zen Traffic Lights

Elegant macOS-inspired circular traffic light buttons for **Zen Browser**.

![Zen Traffic Lights Preview](image.png)

This mod is a modern, improved fork of the original `zen-minimal-exit-menu` by dinnoyow, optimized for Zen's unique sidebar and compact layouts with deep customization.

[![License](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-blue.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)
[![Zen Browser](https://img.shields.io/badge/browser-Zen-purple.svg)](https://zen-browser.app/mods/)

## ✨ Features
- **Minimalist Design**: Replaces bulky system controls with sleek, colored circles.
- **Dynamic Color Modes**: 
  - **Colors on Hover (Default)**: Buttons are subtle grey until you hover over them.
  - **Classic Mode**: Always show the vibrant red/yellow/green colors.
- **Smart Symbols**: macOS-style (X, -, +) symbols that fade in only when you hover over the buttons.
- **Tactile Animations**: Bolder, vertical-expanding hover effects and tactile "click" feedback.
- **Adaptive Sizing**: Mid-size buttons for a perfectly balanced look.
- **Improved Light Mode**: Specifically tuned colors for high visibility on light backgrounds.
- **Sidebar Optimized**: Works perfectly in Zen's sidebar and compact modes.

## 🛠️ Installation

### Step 1: Enable Custom Stylesheets
1. Open Zen Browser.
2. Go to `about:config`.
3. Search for `toolkit.legacyUserProfileCustomizations.stylesheets` and set it to **true**.

### Step 2: Locate your Profile Folder
1. Go to `about:support`.
2. Find the **Profile Folder** entry and click **Open Folder**.

### Step 3: Install the mod
1. Inside your profile folder, navigate to: `chrome/zen-themes/` (create the `zen-themes` folder if it doesn't exist).
2. Copy the **entire** folder `3ffef3a7-cdb7-40a0-9510-96f0db1b1536` into the `zen-themes` directory.
3. To make it appear in the **Zen Mods** settings page:
   - Go to your root **Profile Folder**.
   - Open (or create) a file named `zen-themes.json`.
   - Add the following entry to the JSON object:
```json
{
  "3ffef3a7-cdb7-40a0-9510-96f0db1b1536": {
    "id": "3ffef3a7-cdb7-40a0-9510-96f0db1b1536",
    "name": "Zen Traffic Lights",
    "author": "Rahul",
    "version": "1.3.0",
    "enabled": true,
    "isLocal": true,
    "style": "chrome.css",
    "preferences": "preferences.json"
  }
}
```
4. Restart Zen Browser completely.

## 🎨 Customization
Once installed, you can toggle all features directly from the **Zen Mods** section in Zen Browser's settings:
- **Show Colors only on Hover**
- **Show Symbols on Hover**
- **Use Large Buttons**
- **Enable Tactile Animations**

## 📜 License
This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License**. See the `LICENSE` file for details.

## 🙌 Credits
- Inspired by and based on the original `zen-minimal-exit-menu` by [dinnoyow](https://github.com/dinnoyow/zen-minimal-exit-menu).
- Developed and improved for the Zen community.
