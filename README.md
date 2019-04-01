# hidpi-dots
My dual monitors setup script and some protips for high resolution monitors.

### Script for my desktop:
* `hidpi.sh` - setup 4k resolution on left FullHD monitor because single 
monitor scaling is not supported on Xorg.
* `lodpi.sh` - do otherwise that do hidpi.sh - set FullHD resolution on 4k monitor.

##### Both scripts uses xrandr, overwrites gnome-shell scaling and restart it.

### Issues:
* My monitors when go into sleep state or I shutdown them are unplugged 
from Linux causing xrandr script revert. To fix it, install autorandr 
and create main, global setup - everything works fine.
* Autorandr also remembers your config - no need to autorun any xrandr script.
* Discord can launch without HiDPI scaling, though about it because of
racing condition under autorandr startup, but this is probably not the
global case, thus slack is working fine.
* Setting scaling under gnome xorg is somewhat buggy and can cause 
artifacts on monitor, just try to launch script again etc.
I use 200% because of ~24 inch based monitors.
* HydraPaper for now is buggy and can't setup wallpaper for each 
monitor, you should use built-in gnome selector - needs to be fixed by 
author. Confirmed that the same issue appears on Deepin 
(https://github.com/GabMus/HydraPaper/issues/31).

# Pretty much above content is outdated. Now I use wayland.
So there is an problem when using Wayland on my machine that causes random display names...
And because of that configuration of sway displays is hard. Also I have Lenovo Explorer...
So, there is my solution:

* `disp.py` - Convert `swaymsg -t get_outputs` pretty string to JSON, and after that find
my displays, set correct configs and disable lenovo explorer.

### Issues:
* I hate bash.
* I really hate bash.
* Python is better lol'd.
* I don't know about more issues.
