# My own tool to overwrite display - there is bug in Linux kernel that is causing random names of display
# Causing probably configuration problems due to i915 racing condition
import os, json, subprocess

data, err = subprocess.Popen(
	['swaymsg', '-t', 'get_outputs', '|', 'cat'], stdout=subprocess.PIPE
).communicate()
disp_json = json.loads(data)
for display in disp_json:
	if display['model'] == 'LG Ultra HD':
		os.system(('swaymsg output {0} pos 1920 0 res 3840x2160').format(display['name']))
		os.system(('swaymsg output {0} scale 2').format(display['name']))
		os.system(('swaymsg output {0} background /home/hoshi/sway/4.png fill').format(display['name']))
	elif display['model'] == 'LG IPS FULLHD':
		os.system(('swaymsg output {0} pos 0 0 res 1920x1080').format(display['name']))
		os.system(('swaymsg output {0} background /home/hoshi/sway/5.png fill').format(display['name']))
	elif display['model'] == 'ANX7530':
		os.system(('swaymsg output {0} disable').format(display['name']))