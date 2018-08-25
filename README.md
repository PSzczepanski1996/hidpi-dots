# hidpi_dots
My dual monitors setup script, autorunner for it (.desktop), and some 
protips for high resolution monitors.

### Files in project:
* `hidpi.sh` - setup 4k resolution on left FullHD monitor because single 
monitor scaling is not supported on Xorg.
* `HiDPI.desktop` - shortcut for launching it under `.config/autostart` 
(edit your user name in path).

### Issues:
* Discord can launch without HiDPI scaling, though about it because of 
racing condition under autostart apps, but this is probably not the 
global case, thus slack is working fine.
* My monitors when go into sleep state or I shutdown them are unplugged 
from Linux causing xrandr script revert. To fix it, install autorandr 
and create main, global setup - everything works fine.
* Setting scaling under gnome xorg is somewhat buggy and can cause 
artifacts on monitor, just try to launch script again etc.
I use 200% because of ~24 inch based monitors.
* HydraPaper for now is buggy and can't setup wallpaper for each 
monitor, you should use built-in gnome selector - needs to be fixed by 
author. Confirmed that the same issue appears on Deepin 
(https://github.com/GabMus/HydraPaper/issues/31).

*To be continued...*
