#!/bin/bash
setxkbmap -layout br
picom -f &
udiskie &
nm-applet &
qtile start
