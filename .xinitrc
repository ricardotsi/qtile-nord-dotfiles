#!/bin/bash
setxkbmap -layout br
picom -f &
udiskie &
qtile start
