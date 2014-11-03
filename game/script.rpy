﻿# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Eileen', color="#c8ffc8")
init python hide:
    for file in renpy.list_files():
        if file.startswith('bg') and file.endswith('.jpg'):
            name = file.replace('BG/','').replace('/', ' ').replace('.jpg','')
            renpy.image(name, Image(file))
    config.empty_window = nvl_show_core
    config.window_hide_transition = dissolve
    config.window_show_transition = dissolve
    style.nvl_window.background = "nvl/textbox.png"
    style.nvl_window.xpadding = 140
    style.nvl_window.ypadding = 50

init:
    $ narrator = Character(None, kind=nvl)
    image cg1 = "cg/test.png"
    image cg2 = "cg/test.png"
    image cg3 = "cg/test.png"
    image cg4 = "cg/test.png"
    image cg5 = "cg/test.png"
    image cg6 = "cg/test.png"
    image cg7 = "cg/test.png"
    image cg8 = "cg/test.png"
    image cg9 = "cg/test.png"
    image cg10 = "cg/test.png"
# The game starts here.
label start:
    scene bg kitchen
    "You've created a new Ren'Py game."
    #scene bg kitchen dining
    scene cg2
    "Once you add a story, pictures, and music, you can release it to the world!"
    return
