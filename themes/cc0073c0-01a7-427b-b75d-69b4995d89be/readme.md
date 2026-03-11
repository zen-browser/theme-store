
# Container Border Loader

Restores the visual loading indicator to Zen Browser with a modern, integrated touch.

This mod replaces the deprecated "Fluid URL" with a "snake" border animation that perfectly traces the geometry of your active tab.

## Features
* **Context Aware:** Automatically detects your Container color (e.g., Blue for Personal, Orange for Work) and matches the loading animation to it.
* **Smart Geometry:** Uses CSS `@property` to trace your tab's exact shape—whether you use square tabs or rounded corners.
* **Native Feel:** Designed to look like a built-in part of the Zen interface.

## How it works
The mod adds a `conic-gradient` border that spins only when a tab is in the `[busy]` state. It uses the `var(--identity-icon-color)` variable to sync with your container settings automatically.
