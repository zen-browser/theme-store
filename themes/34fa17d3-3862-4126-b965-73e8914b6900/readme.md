
# Arc Like Sidebar

Two small tweaks that make Zen's vertical sidebar feel closer to Arc on macOS:

## 1. No fade when the window loses focus
By default, Zen applies an opacity/filter to the sidebar and toolbar when the window is blurred, which makes tab text render really thin and washed out —
almost unreadable at a glance. This mod removes that effect so your sidebar stays crisp and fully legible. The active tab pill is left slightly translucent
(70%) as a subtle hint that the window isn't focused, similar to how Arc handles its unfocused state.

## 2. Arc-like tab label rendering
Bumps tab labels to system font (-apple-system / SF Pro Text), size 14px, weight 450, with native macOS font smoothing. The default Zen rendering looks
noticeably thinner and smaller than Arc; this brings them in line.

## What it doesn't touch
- Border radius, colors, spacing, or layout.
- Behavior when the window is focused (other than label font).
- Non-macOS systems will still get the size/weight changes — the system font stack falls back gracefully.
