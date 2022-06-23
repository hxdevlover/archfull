# imports
import os
import subprocess
import libqtile
from libqtile import bar, layout, widget, qtile, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from libqtile import extension
from libqtile.widget import keyboardlayout
import libqtile.widget.keyboardlayout


# Variables
mod = "mod4"
alt = "mod1"
ctrl = "control"
terminal = "kitty"

# Key Bindings
keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    Key([mod], "f", lazy.window.toggle_floating()),
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    # Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "a", lazy.spawn(terminal)),
    Key([mod], "d", lazy.spawn("pcmanfm")),
    Key([mod], "e", lazy.spawn("/usr/bin/emacsclient -c -a 'emacs'")),

    # Keyboard layout changing
    Key([ctrl], "space", lazy.spawn("setxkbmap -layout 'us,ir' -option 'grp:alt_shift_toggle' ") ),

    # Toggle between different layouts as defined below
    Key([mod], "space", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    # Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "s", lazy.spawn("rofi -show drun")),
    Key([mod, "shift"], "s", lazy.spawn("rofi -show window")),
    Key([mod, "shift"], "f", lazy.spawn("firefox")),
    Key([ctrl, "shift"], "s", lazy.spawn("poweroff")),
    Key([alt], "j", lazy.spawn("brightnessctl set 10%-")),
    Key([alt], "k", lazy.spawn("brightnessctl set 10%+")),
    Key([], "Print", lazy.spawn("flameshot gui")),
]


groups = [
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
          
    Group("",
          layout="monadtall"),
]

for k, group in zip(["1", "2", "3", "4", "5", "6", "7", "8"], groups):
  keys.append(Key([mod], (k), lazy.group[group.name].toscreen()))
  keys.append(Key([mod, "shift"], (k), lazy.window.togroup(group.name)))


layouts = [
    #layout.Tile(border_focus="#a663cc", border_normal="#a4a4a4" , border_width=3, margin=8),
    #layout.Columns(border_focus="#a663cc", border_normal="#a4a4a4" , border_width=3, margin=8),
    layout.MonadTall(border_focus="#a663cc", border_normal="#a4a4a4" , border_width=2, margin=14),
    layout.Max(),
    # layout.Floating(border_focus="#a663cc", border_normal="#a4a4a4" , border_width=1),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    background='#2b2b2b',
    foreground='#e6e6e6',
    font="Mononoki Nerd Font Bold",
    #font='Ubuntu Mono',
    fontsize=13,
    padding=3,
    #icon_size=14,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Bar(
            [

                widget.Image(
                    filename="/home/hx/.config/qtile/python.png",
                    mouse_callbacks=({
                        "Button1": lambda: qtile.cmd_spawn("rofi -show drun"),
                        "Button3": lambda: qtile.cmd_spawn("rofi -show run"),}),
                    scale=True,
                    ),

                widget.Sep(
                    foreground="#535965",
                    linewidth=1,
                    padding=10
                    ),

                widget.GroupBox(
                    active='#576997',
                    inactive='#5b5b5b',
                    this_current_screen_border='#9ee6ff',
                    disable_drag=True,
                    highlight_method='text',
                    font='FontAwesome 6 Free',
                    fontsize=18,
                    padding=1,
                    ),
                
                widget.Sep(
                    foreground="#535965",
                    linewidth=1,
                    padding=10
                    ),

                widget.CurrentLayout(foreground="#c8a2ff", font='Ubuntu semiBold'),
        

                widget.Sep(
                    foreground="#535965",
                    linewidth=1,
                    padding=10
                    ),
                widget.Prompt(),
                
                widget.WindowName(font='Ubuntu semiBold' ,max_chars=20),
                
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                #widget.TextBox("default config", name="default"),
                #widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
                widget.Systray(),

                #widget.CPUGraph(core=all, friquency=1, line_width=2),
                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    #background = '#282c34',
                    foreground = '#583a81',
                    padding = 0,
                    fontsize = 57
                    ),
                
                widget.CPU(
                    background = '#583a81',
                    foreground='#ffffff',
                    format=" {load_percent}%",
                    update_interval=1.0,
                    padding=0),
                    
                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    background = '#583a81',
                    foreground = '#5477bf',
                    padding = 0,
                    fontsize = 57
                    ),

                widget.Memory(
                    background = '#5477bf',
                    foreground='#ffffff',
                    format=" {MemUsed:.0f} MB",
                    update_interval=1.0,
                    padding=0),

                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    background = '#5477bf',
                    foreground = '#583a81',
                    padding = 0,
                    fontsize = 57
                    ),

                widget.Net(
                    background = '#583a81',
                    foreground='#ffffff',
                    format=" {down}",
                    interface='wlan0',
                    padding=0),

                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    background = '#583a81',
                    foreground = '#5477bf',
                    padding = 0,
                    fontsize = 57
                    ),

                widget.Battery(
                    background = '#5477bf',
                    foreground='#ffffff',
                    format="{char} {percent:2.0%}",
                    charge_char=" ",
                    discharge_char=" ",
                    empty_char=" ",
                    full_char=" ",
                    unknown_char=" ",
                    low_foreground='#e55561',
                    low_percentage=0.15,
                    show_short_text=False,
                    notify_below=15,
                    padding=0
                    ),
        

                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    background = '#5477bf',
                    foreground = '#583a81',
                    padding = 0,
                    fontsize = 57
                    ),

                widget.KeyboardLayout(
                    background = '#583a81',
                    foreground='#ffffff',
                    #display_map={'us': 'us', 'ir': 'ir'},
                    #configured_keyboards=['us', 'us,ir'],
                    display_map={'us':'us', 'ir':'ir'},
                    configured_keyboards=['us','ir']
                    ),

                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    background = '#583a81',
                    foreground = '#5477bf',
                    padding = 0,
                    fontsize = 57
                    ),

                widget.Clock(
                    background = '#5477bf',
                    foreground='#ffffff',
                    format=" %a %b %d  %I:%M %P"
                    ),
                
                widget.TextBox(
                    text = '',
                    font = 'Ubuntu Mono',
                    background = '#5477bf',
                    foreground = '#583a81',
                    padding = 0,
                    fontsize = 57
                    ),

                widget.QuickExit(
                    background = '#583a81',
                    foreground='#ffffff',
                    default_text='[]', 
                    countdown_format='[{}]',
                    padding=0,
                    ),
            ],
            28,
            # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
        ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.Popen([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
        Match(title="galculator"),
        Match(title="Authentication"),
        Match(wm_class="dialog"),
        Match(wm_class="notification"),
        Match(wm_class="error"),
        Match(wm_class="TelegramDesktop"),
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
