if status is-login
    if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
	exec startx
    end
end
status --is-login; and status --is-interactive; and exec byobu-launcher
