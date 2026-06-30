
# Lock Pinned Tabs

Pinned tabs in a workspace are **assets**, not disposable tabs. This mod removes
the hover `×` close button on **pinned tabs** so they can't be dismissed by an
accidental click. Normal (unpinned) tabs are unaffected and keep their `×`.

## Closing a pinned tab on purpose

Right-click → **Close Tab**, or **middle-click** the tab.

## Optional: also stop ⌘W from closing pinned tabs

Zen Mods are CSS-only and can't rebind keys. If you want ⌘W to leave pinned tabs
alone, set `zen.pinned-tab-manager.close-shortcut-behavior` in `about:config` to
e.g. `reset-unload-switch` — Zen resets/unloads the pinned tab instead of closing
it, while ⌘W keeps working normally on other tabs.
