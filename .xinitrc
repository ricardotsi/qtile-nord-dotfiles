#!/bin/bash
#export DESKTOP_SESSION=plasma
#exec startplasma-x11
setxkbmap -layout br
picom -f &
qtile start
