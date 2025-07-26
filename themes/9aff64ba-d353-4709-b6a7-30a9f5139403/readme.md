
# Hide Sidebar

> Conceal the sidebar and Sidebery title bar.

1.  Install the `Sidebery` add-on.
2.  Right-click on the sidebar and select `Compact mode -> Hide sidebar -> Enable compact mode`.
3.  Activate the mode configuration.

Tips:

1.  Add `user.js` to your `Profiles` directory to enable `Browser Toolbox Mode`.

// user.js

user_pref("devtools.chrome.enabled", true);
    user_pref("devtools.debugger.remote-enabled", true);

user_pref("xpinstall.signatures.required", false);
    user_pref("config.trim_on_minimize", true);

2.  `Browser Toolbox Mode` is located under `Tools -> Browser Tools`.
3.  For quick style previews, utilize the `Style Editor`.
4.  Customize navigation and sidebar colors via `about:config -> zen.theme.gradient.show-custom-colors -> true`.
5.  Disable transparent backgrounds: `about:config -> transparent -> false`.
