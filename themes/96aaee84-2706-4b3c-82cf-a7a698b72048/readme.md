
# Zen Cleaned URL Bar (Maintained Fork)

A maintained fork of [zen-cleaned-url-bar](https://github.com/dinnoyow/zen-cleaned-url-bar) by [@Dinno-DEV](https://github.com/dinnoyow), with bug fixes for recent Zen/Firefox versions.

## What's different

- **Fix transparent URL bar** — adds a no-op `backdrop-filter` on `#browser` to re-establish the stacking context removed upstream. Refs:
  - https://github.com/zen-browser/desktop/issues/13389
  - https://github.com/zen-browser/desktop/pull/13424
- **Fix class selector** — `#urlbar-background` was converted to a class in Zen 1.16; updated selector to `.urlbar-background`

## Customization

- URL panel color
- URL panel transparency
- Selected result color
- Selected result font color
