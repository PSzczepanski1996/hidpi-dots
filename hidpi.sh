#!/bin/bash
gsettings set org.gnome.desktop.interface scaling-factor 2
export DISPLAY=:0
{ `gnome-shell --replace &> /dev/null`; } < /dev/stdin &
export DISPLAY=:1
{ `gnome-shell --replace &> /dev/null`; } < /dev/stdin &
sleep 1
xrandr --output HDMI-A-1 --auto --pos 0x0 --scale 2x2 --output DisplayPort-1 --auto --scale 1x1 --pos 3840x0
