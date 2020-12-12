###################################
# Qtile Config Created by Bojofil
#
# https://github.com/Bojofil
#
# bojofil@protonmail.com
###################################

import os
import re
import socket
import subprocess
from libqtile.config import Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from typing import List 


mod = "mod4"                                     
myTerm = "alacritty"                                    
myConfig = "/home/justin/.config/qtile/config.py"
PROMPT = "rofi -lines 12 -padding 18 -width 60 -location 0 -show drun -sidebar-mode -columns 3"
Browser = "chromium"    


keys = [
         Key(
             [mod], "Return",
             lazy.spawn(myTerm),
             desc='Launches Terminal'
             ),
         Key(
             [mod], "d", 
             lazy.spawn(PROMPT),
             desc='Rofi Application Launcher'
             ),
         Key(
             [mod], "Tab",
             lazy.next_layout(),
             desc='Toggle through layouts'
             ),
         Key(
             [mod], "c",
             lazy.window.kill(),
             desc='Kill active window'
             ),
         Key(
             [mod, "shift"], "r",
             lazy.restart(),
             desc='Restart Qtile'
             ),
        Key(
             [mod, "shift"], "w",
             lazy.spawn(Browser),
             desc='Launch Chromium'
             ),
         Key(
             [mod, "shift"], "q",
             lazy.shutdown(),
             desc='Shutdown Qtile'
             ),
         Key([mod], "e",
             lazy.to_screen(0),
             desc='Keyboard focus to monitor 1'
             ),
         Key([mod], "w",
             lazy.to_screen(1),
             desc='Keyboard focus to monitor 2'
             ),
         Key([mod], "r",
             lazy.to_screen(2),
             desc='Keyboard focus to monitor 3'
             ),
         Key([mod], "period",
             lazy.next_screen(),
             desc='Move focus to next monitor'
             ),
         Key([mod], "comma",
             lazy.prev_screen(),
             desc='Move focus to prev monitor'
             ),
         Key([mod, "control"], "k",
             lazy.layout.section_up(),
             desc='Move up a section in treetab'
             ),
         Key([mod, "control"], "j",
             lazy.layout.section_down(),
             desc='Move down a section in treetab'
             ),
         Key(
             [mod], "k",
             lazy.layout.down(),
             desc='Move focus down in current stack pane'
             ),
         Key(
             [mod], "j",
             lazy.layout.up(),
             desc='Move focus up in current stack pane'
             ),
         Key(
             [mod, "shift"], "k",
             lazy.layout.shuffle_down(),
             desc='Move windows down in current stack'
             ),
         Key(
             [mod, "shift"], "j",
             lazy.layout.shuffle_up(),
             desc='Move windows up in current stack'
             ),
         Key(
             [mod], "h",
             lazy.layout.grow(),
             lazy.layout.increase_nmaster(),
             desc='Expand window (MonadTall), increase number in master pane (Tile)'
             ),
         Key(
             [mod], "l",
             lazy.layout.shrink(),
             lazy.layout.decrease_nmaster(),
             desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
             ),
         Key(
             [mod], "n",
             lazy.layout.normalize(),
             desc='normalize window size ratios'
             ),
         Key(
             [mod], "m",
             lazy.layout.maximize(),
             desc='toggle window between minimum and maximum sizes'
             ),
         Key(
             [mod, "shift"], "f",
             lazy.window.toggle_floating(),
             desc='toggle floating'
             ),
         Key(
             [mod, "shift"], "space",
             lazy.layout.rotate(),
             lazy.layout.flip(),
             desc='Switch which side main pane occupies (XmonadTall)'
             ),
         Key(
             [mod], "space",
             lazy.layout.next(),
             desc='Switch window focus to other pane(s) of stack'
             ),
         Key(
             [mod, "control"], "Return",
             lazy.layout.toggle_split(),
             desc='Toggle between split and unsplit sides of stack'
             ),

]


group_names = [("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),
               ("", {'layout': 'monadtall'}),]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name)))

layout_theme = {"border_width": 0,
                "margin": 6,
                "border_focus": "#0D1E33",
                "border_normal": "#0D1E33"
                }


layouts = [
    #layout.MonadWide(**layout_theme),
    #layout.Bsp(**layout_theme),
    #layout.Stack(stacks=2, **layout_theme),
    #layout.Columns(**layout_theme),
    #layout.RatioTile(**layout_theme),
    #layout.VerticalTile(**layout_theme),
    #layout.Matrix(**layout_theme),
    #layout.Zoomy(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    #layout.Tile(shift_windows=True, **layout_theme),
    #layout.Stack(num_stacks=2),
    layout.TreeTab(
         font = "FiraGO Medium",
         fontsize = 10,
         sections = ["FIRST", "SECOND"],
         section_fontsize = 11,
         bg_color = "#0D1E33",
         active_bg = "#3473AC",
         active_fg = "#C6E0E8",
         inactive_bg = "#0D1E33",
         inactive_fg = "#8A9CA2",
         padding_y = 5,
         section_top = 10,
         panel_width = 320
         ),
     #layout.Floating(**layout_theme)
]


colors = [["#0D1E33", "#0D1E33"], 
          ["#3473AC", "#3473AC"], 
          ["#C6E0E8", "#C6E0E8"], 
          ["#0D1E33", "#0D1E33"], 
          ["#2A5D8C", "#2A5D8C"], 
          ["#3473AC", "#3473AC"], 
          ["#C6E0E8", "#C6E0E8"],
          ["#5BAFD5", "#5BAFD5"]]


widget_defaults = dict(
    font="FiraGO Nerd Font Medium",
    fontsize = 12,
    padding = 2,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()



def init_widgets_list():
    widgets_list = [
               widget.GroupBox(font="FiraGO Nerd Font Medium",
                        fontsize = 24,
                        margin_y = 3,
                        margin_x = 0,
                        padding_y = 3,
                        padding_x = 1,
                        borderwidth = 2,
                        active = colors[2],
                        inactive = colors[2],
                        rounded = False,
                        highlight_color = colors[4],
                        highlight_method = "line",
                        this_current_screen_border = colors[7],
                        this_screen_border = colors [7],
                        other_current_screen_border = colors[7],
                        other_screen_border = colors[7],
                        foreground = colors[2],
                        background = colors[4]
                        ),
               widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[4],
                        padding=0,
                        fontsize=36
                        ),          
               widget.WindowName(
                        foreground = colors[2],
                        background = colors[0],
                        padding = 0,
                        font= "Fira Sans Medium",
                        fontsize = 12
                        ),
                #widget.TextBox(
                 #       text='',
                  #      background = colors[0],
                   #     foreground = colors[4],
                    #    padding=0,
                     #   fontsize=36
                      #  ),
               #widget.CPU(
                #        foreground=colors[2],
                 #       background=colors[4],
                  #      padding = 0,
                   #     fontsize=12,
                    #    update_interval = 3,
                     #   format = '  {load_percent} %'
                      # ),
               widget.TextBox(
                        text='',
                        background = colors[0],
                        foreground = colors[5],
                        padding=0,
                        fontsize=36
                        ),
               widget.TextBox(
                        text=" ",
                        padding = 2,
                        foreground=colors[2],
                        background=colors[5],
                        fontsize=12
                        ),
              # widget.ThermalSensor(
               #         foreground=colors[2],
                #        background=colors[5],
                 #       padding = 5,
                  #      update_interval = 2
                  #      ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=36
                        ),
               #widget.Memory(
                #        foreground = colors[2],
                 #       background = colors[4],
                  #      padding = 5,
                   #     update_interval = 2,
                    #    format = '  {MemUsed}M'
                        #),
               #widget.TextBox(
                #        text='',
                 #       background = colors[4],
                  #      foreground = colors[5],
                   #     padding=0,
                    #    fontsize=36
                      #  ),
                widget.TextBox(
                        text = '  Updates:' ,
                        padding = 3 , 
                        foreground = colors[2] ,
                        background = colors [5] ,
                        mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e yay -Syyu')} 
                        ),          
                #widget.CheckUpdates(
                 #      display_format = '{updates}',
                  #     distro = 'Arch_checkupdates', 
                   #    update_interval = 60,
                    #   padding = 1,
                     #  foreground = colors[2],
                      # background = colors[5],
                       #colour_have_updates = colors[2],
                    #   colour_no_updates = colors[2],
                     #  mouse_callbacks = {'Button1': lambda qtile: qtile.cmd_spawn(myTerm + ' -e yay -Syyu')}
                      # ),
            #  widget.Net(
                #        interface = "eno2",
                 #       format = ' {down}   {up}',
                  #      foreground = colors[2],
                   #     background = colors[4],
                    #    padding = 5,
                     #   update_interval = 2
                       # ),
               widget.TextBox(
                        text='',
                        background = colors[5],
                        foreground = colors[4],
                        padding=0,
                        fontsize=36
                        ),
              # widget.CurrentLayout(
               #         foreground = colors[2],
                #        background = colors[4],
                 #       padding = 5
                  #      ),
                widget.TextBox(
                        text='',
                        background = colors[4],
                        foreground = colors[5],
                        padding=0,
                        fontsize=36
                        ),
               widget.TextBox(
                       text=" ",
                        foreground=colors[2],
                        background=colors[5],
                        padding = 0
                        ),
               #widget.Volume(
                #        foreground = colors[2],
                 #       background = colors[5],
                  #      padding = 5,
                   #     update_interval = 5
                    #    ),         
               #widget.TextBox(
                #        text='',
                 #       background = colors[5],
                  #      foreground = colors[4],
                   #     padding=0,
                    #    fontsize=36
                     #   ),
               #widget.Clock(
                #        foreground = colors[2],
                 #       background = colors[4],
                  #      format="  %A %B %d, %Y    %l:%M %p "
                   #     ),
               widget.Sep(
                        linewidth = 0,
                        padding = 10,
                        foreground = colors[0],
                        background = colors[4]
                        ),
              ]
    return widgets_list

# Screens

def init_widgets_screen1():
    widgets_screen1 = init_widgets_list()
    return widgets_screen1                       

def init_widgets_screen2():
    widgets_screen2 = init_widgets_list()
    return widgets_screen2                       

def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0, size=20)),
            Screen(top=bar.Bar(widgets=init_widgets_screen1(), opacity=0, size=20))]

if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen1 = init_widgets_screen1()
    widgets_screen2 = init_widgets_screen1()


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []


@hook.subscribe.client_new
def assign_app_group(client):
     d = {}
     d[""] = ["Chromium", "chromium", ]
     d[""] = [ "Alacritty", "alacritty", ]
     d[""] = ["Thunar", "Ranger", "Nitrogen", "thunar", "ranger", "nitrogen",  ]
     d[""] = ["code-oss", "Code-oss", "Code", "code", ]
     d[""] = ["net-runelite-launcher-Launcher", ]
     d[""] = ["Spotify","spotify", "Discord", "discord", ]
     d[""] = ["google-chrome" , "Google-chrome" ,]
     d[""] = ["Thunderbird", "thunderbird", ]
     wm_class = client.window.get_wm_class()[0]

     for i in range(len(d)):
         if wm_class in list(d.values())[i]:
             group = list(d.keys())[i]
             client.togroup(group)

main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False


auto_fullscreen = True
focus_on_window_activation = "urgent"


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/autostart.sh'])
wmname = "Qtile"
