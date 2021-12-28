# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401

from libqtile import bar, layout, widget
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

mod = "mod4"
terminal = guess_terminal()

keys = [
    # Switch between windows
    Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "Left", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "Right", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "Left", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "Right", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "Down", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    #Start programs
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn("firefox"), desc="Launch firefox"),
    Key([mod], "e", lazy.spawn("fish -c 'set -e COLUMNS ; set -e LINES; alacritty -e ranger'"), desc="Launch file manager"),
    Key([], "Print", lazy.spawn("fish -c 'maim ~/Pictures/Screenshot/(date +%s).png'"), desc="Print fullscreen"),
    Key([mod], "Print", lazy.spawn("fish -c 'maim -i (xdotool getactivewindow) ~/Pictures/Screenshot/(date +%s).png'"), desc="Print fullscreen"),
    Key(["control"], "Print", lazy.spawn("fish -c 'maim | feh - -x & maim -s (date +%s).png'"), desc="Print fullscreen"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),
#    Key([mod], "m", lazy.window.toggle_fullscreen(), desc="Toogle Fullscreen"),
    Key([mod], "m", lazy.layout.toggle_split(), desc="Toogle Fullscreen"),

    Key([mod, "control"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "shift"], "r", lazy.spawn("reboot"), desc="Restart"),
    Key([mod, "shift"], "q", lazy.spawn("poweroff"), desc="Shutdown Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawn("rofi -show drun -font 'hack 14' -icon-theme 'Papirus' -show-icons"),
        desc="Spawn a command using a prompt widget"),
]

groups = [Group(i) for i in "12345"]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "control"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

# Colors (Nord)
   # Default colors
background = '#2E3440'
foreground = '#D8DEE9'
bg = '#4c566a60'
fg = 'ffffff'

   # Normal colors
normal={
     "black":   '#3B4252',
     "red":     '#BF616A',
     "green":   '#A3BE8C',
     "yellow":  '#EBCB8B',
     "blue":    '#81A1C1',
     "magenta": '#B48EAD',
     "cyan":    '#88C0D0',
     "white":   '#E5E9F0',
     }

   # Bright colors
bright={
     "black":   '#4C566A',
     "red":     '#BF616A',
     "green":   '#A3BE8C',
     "yellow":  '#EBCB8B',
     "blue":    '#81A1C1',
     "magenta": '#B48EAD',
     "cyan":    '#8FBCBB',
     "white":   '#ECEFF4',
    }

layout_theme = {
        "border_width":4,
        "margin":10,
        "border_focus":bright["cyan"],
        "border_normal":normal["black"]
        }

layouts = [
    #layout.MonadTall(),
    layout.Columns(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts iby unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font='Hack',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [
                #First Bar
                widget.TextBox(
                    text="\ue0b6",
                    fontsize=26,
                    foreground=bg,
                    padding=0
                ),
                widget.CurrentLayout(
                    background=bg,
                ),
                widget.CurrentLayoutIcon(
                    background=bg,
                    scale = 0.8,
                ),
                widget.Sep(
                    background=bg,
                    foreground=fg,
                    padding=10,
                ),
                widget.GroupBox(
                    background=bg,
                    disable_drag=True,
                    highlight_method="line",
                    highlight_color=[normal["blue"], normal["blue"]],
                ),
                widget.TextBox(
                    foreground=bg,
                    text="\ue0b4",
                    fontsize=26,
                    padding=0
                ),
                widget.Spacer(
                    length=bar.STRETCH,
                ),


#                #Middle Bar
#                widget.TextBox(
#                    text="\ue0b6\u2588",
#                    fontsize=30,
#                    foreground="#4c566a60",
#                    padding=0,
#                ),
#                widget.TextBox(
#                    text="\ue0b8",
#                    fontsize=30,
#                    foreground="#4c566a66",
#                    background=foreground+"30",
#                    padding=0,
#                ),
#                widget.CheckUpdates(
#                    background=foreground+"30",
#                    colour_have_updates=background,
#                    colour_no_updates=background,
#                    no_update_string="Updated!",
#                ),
#                widget.TextBox(
#                    text="\ue0ba\u2588\ue0bc",
#                    fontsize=30,
#                    foreground="#4c566a66",
#                    background=foreground+"30",
#                    padding=0,
#                ),
#                widget.TextBox(
#                    text="CPU",
#                    foreground=background,
#                    background=foreground+"30",
#                ),
#                widget.CPUGraph(
#                    background=foreground+"30",
#                ),
#                widget.TextBox(
#                    text="\ue0be\u2588\ue0b8",
#                    fontsize=30,
#                    foreground="#4c566a66",
#                    background=foreground+"30",
#                    padding=0,
#                ),
#                widget.TextBox(
#                    text="Memory",
#                    foreground=background,
#                    background=foreground+"30",
#                ),
#                widget.MemoryGraph(
#                    background=foreground+"30",
#                ),
#                widget.TextBox(
#                    text="\ue0ba\u2588\ue0bc",
#                    fontsize=30,
#                    foreground="#4c566a66",
#                    background=foreground+"30",
#                    padding=0,
#                ),
#                widget.TextBox(
#                    text="Vol:",
#                    background=foreground+"30",
#                    foreground=background,
#                ),
#                widget.PulseVolume(
#                    background=foreground+"30",
#                    foreground=background,
#                ),
#                widget.Systray(
#                    background=foreground+"30",
#                    icon_size=30,
#                ),
#                widget.TextBox(
#                    text="\ue0be",
#                    fontsize=30,
#                    foreground="#4c566a66",
#                    background=foreground+"30",
#                    padding=0,
#                ),
#                widget.TextBox(
#                    text="\u2588\ue0b4",
#                    fontsize=30,
#                    foreground="#4c566a66",
#                    padding=0,
#                ),

                #Middle Bar
                widget.TextBox(
                    text="\ue0b6",
                    fontsize=30,
                    foreground=bg,
                    padding=0,
                ),
                widget.CheckUpdates(
                    background=bg,
                    colour_have_updates=fg,
                    colour_no_updates=fg,
                    no_update_string="Updated!",
                ),
                widget.Sep(
                    background=bg,
                    foreground=fg,
                    padding=10,
                ),
                widget.TextBox(
                    text="CPU",
                    background=bg,
                ),
                widget.CPUGraph(
                    background=bg,
                ),
                widget.Sep(
                    background=bg,
                    foreground=fg,
                    padding=10,
                ),
                widget.TextBox(
                    text="Memory",
                    background=bg,
                ),
                widget.MemoryGraph(
                    background=bg,
                ),
                widget.Sep(
                    background=bg,
                    foreground=fg,
                    padding=10,
                ),
                widget.TextBox(
                    text="Vol:",
                    background=bg,
                ),
                widget.PulseVolume(
                    background=bg,
                ),
                widget.Systray(
                    background=bg,
                    icon_size=30,
                ),
                widget.TextBox(
                    text="\ue0b4",
                    fontsize=30,
                    foreground=bg,
                    padding=0,
                ),


                #Last Bar
                widget.Spacer(
                    length=bar.STRETCH,
                ),
                widget.TextBox(
                    text="\ue0b6",
                    fontsize=26,
                    foreground="#4c566a60",
                    padding=0
                ),
                widget.Clock(
                    format='%A, %d de %B %H:%M:%S',
                    background="#4c566a60",
                ),
                widget.TextBox(
                    foreground="#4c566a60",
                    text="\ue0b4",
                    fontsize=26,
                    padding=0
                ),
            ],
            30,
            margin=[9,10,0,10],
            background="00000000",
        ),
        wallpaper="~/Pictures/wp.jpg",
        wallpaper_mode="stretch",
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
#    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
#    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = False
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
