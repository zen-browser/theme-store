# No Gaps  
Removes gaps between a browser tab and browser window when the view isn't split.  
Also implements miscellaneous fixes listed below.  
  
## Options  
- Gaps in single-tab view  
Prevents the theme from removing **gaps** in **single-tab** view mode.  
Default: Off  
  
- Gaps in multi-tab view  
Prevents the theme from removing **gaps** in **multi-tab** view mode.  
Default: On  
  
- Rounded corners in single-tab view  
Prevents the theme from removing **rounded corners** in **single-tab** view mode.  
Default: Off  
  
- Rounded corners in multi-tab view  
Prevents the theme from removing **rounded corners** in **multi-tab** view mode.  
Default: On  
  
- Shadow in single-tab view  
Prevents the theme from removing **shadows around the tab** in **single-tab** view mode.  
Default: On  
  
- Shadow in multi-tab view  
Prevents the theme from removing **shadows around the tab** in **single-tab** view mode.  
Default: On  
  
- Outline in multi-tab view  
Prevents the theme from removing the **highlighted outline/border around** the **active tab** in **multi-tab** view mode  
Default: On  
  
- Fix: Fix URL bar outline issue (1.0.2-b.1)  
Fixes the issue of active tab outline going partly invisible under URL bar that presents itself when:
  - Browser version is 1.0.2-b.1 (the issue also appears in 1.0.2-b.0 but differently and the current theme implementation is not designed to fix it)  
  - User is in multi-tab view  
  - User is using compact toolbar mode  
  - Outline is enabled  
  - Multi-tab view gaps are disabled  

  Default: Off  
  
- Fix: Make margin in different view modes consistent (1.0.2-b.1)  
Tries to make margin consistent no matter how many tabs you have open in the same view  
Default: Off  
  
- Misc: Bring back old URL bar behaviour  
Brings back old URL bar behaviour from versions pre-1.0.2-b.0 (works in versions 1.0.2-b.1+)  
Default: Off  