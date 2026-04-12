
# Zen Loading Bar

Adds a mobile-style loading indicator to Zen Browser - a purple gradient bar at the top of the screen plus a subtle white fill that grows inside each tab as pages load.

## Features

- **Top loading bar** - 6px gradient bar (purple → pink) sweeps across the top of the viewport during page load
- **Tab progress fill** - semi-transparent white fill grows behind the tab label for all tabs including background tabs
- **4 real progress stages** using Zen's native tab attributes (`busy`, `pendingicon`, `progress`)
- **Smooth completion** - on page load finish, bar fills to 100% then fades out
- **Compact mode support** - works correctly when the toolbar is hidden
- **Glance mode aware** - adjusts correctly for Zen Glance overlay

## Compatibility

Tested on Zen Browser v1.19.8b. Works in compact mode and fullscreen.

## How it works

The top bar uses `::before` on `.browserSidebarContainer` and reads CSS variables set by `:root:has()` selectors that detect the active tab's loading state. The tab fill targets each tab's `.tab-content::before` independently so all tabs animate simultaneously.

## Screensh