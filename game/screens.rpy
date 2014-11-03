# This file is in the public domain. Feel free to modify it as a basis
# for your own screens.

# Note that many of these screens may be given additional arguments in the
# future. The use of **kwargs in the parameter list ensures your code will
# work in the future.

##############################################################################
# Say
#
# Screen that's used to display adv-mode dialogue.
# http://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what, side_image=None, two_window=False):

    # Decide if we want to use the one-window or two-window variant.
    if not two_window:

        # The one window variant.
        window:
            id "window"

            has vbox:
                style "say_vbox"

            if who:
                text who id "who"

            text what id "what"

    else:

        # The two window variant.
        vbox:
            style "say_two_window_vbox"

            if who:
                window:
                    style "say_who_window"

                    text who:
                        id "who"

            window:
                id "window"

                has vbox:
                    style "say_vbox"

                text what id "what"

    # If there's a side image, display it above the text.
    if side_image:
        add side_image
    else:
        add SideImage() xalign 0.0 yalign 1.0

    # Use the quick menu.
    use quick_menu


##############################################################################
# Choice
#
# Screen that's used to display in-game menus.
# http://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):

    window:
        style "menu_window"
        xalign 0.5
        yalign 0.5

        vbox:
            style "menu"
            spacing 2

            for caption, action, chosen in items:

                if action:

                    button:
                        action action
                        style "menu_choice_button"

                        text caption style "menu_choice"

                else:
                    text caption style "menu_caption"

init -2:
    $ config.narrator_menu = True

    style menu_window is default

    style menu_choice is button_text:
        clear

    style menu_choice_button is button:
        xminimum int(config.screen_width * 0.75)
        xmaximum int(config.screen_width * 0.75)


##############################################################################
# Input
#
# Screen that's used to display renpy.input()
# http://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):

    window style "input_window":
        has vbox

        text prompt style "input_prompt"
        input id "input" style "input_text"

    use quick_menu

##############################################################################
# Nvl
#
# Screen used for nvl-mode dialogue and menus.
# http://www.renpy.org/doc/html/screen_special.html#nvl

screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            style "nvl_vbox"

        # Display dialogue.
        for who, what, who_id, what_id, window_id in dialogue:
            window:
                id window_id

                has hbox:
                    spacing 10

                if who is not None:
                    text who id who_id

                text what id what_id

        # Display a menu, if given.
        if items:

            vbox:
                id "menu"

                for caption, action, chosen in items:

                    if action:

                        button:
                            style "nvl_menu_choice_button"
                            action action

                            text caption style "nvl_menu_choice"

                    else:

                        text caption style "nvl_dialogue"

    add SideImage() xalign 0.0 yalign 1.0

    use quick_menu

##############################################################################
# Main Menu
#
# Screen that's used to display the main menu, when Ren'Py first starts
# http://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        ground "menu/mm_ground.png"
        idle "menu/mm_idle.png"
        hover "menu/mm_hover.png"
        hotspot (560, 335, 190, 35) action Start()
        hotspot (570, 370, 190, 35) action ShowMenu("load")
        hotspot (570, 400, 190, 35) action ShowMenu("cg_gallery")
        hotspot (570, 435, 190, 35) action ShowMenu("preferences")
        hotspot (570, 475, 190, 35) action ShowMenu("test")
        hotspot (570, 505, 190, 45) action Quit(confirm=True)

##############################################################################
# Navigation
#
# Screen that's included in other screens to display the game menu
# navigation and background.
# http://www.renpy.org/doc/html/screen_special.html#navigation
screen navigation():
    
        imagemap:
            ground "return/return_idle.png"
            idle "return/return_idle.png"
            hover "return/return_hover.png"
            alpha False

            hotspot (1051, 633, 115, 26) action Return()



##############################################################################
# Save, Load
#
# Screens that allow the user to save and load the game.
# http://www.renpy.org/doc/html/screen_special.html#save
# http://www.renpy.org/doc/html/screen_special.html#load

# Since saving and loading are so similar, we combine them into
# a single screen, file_picker. We then use the file_picker screen
# from simple load and save screens.

screen file_picker():

    frame:
        style "file_picker_frame"

        has vbox

        # The buttons at the top allow the user to pick a
        # page of files.
        hbox:
            style_group "file_picker_nav"

            textbutton _("Previous"):
                action FilePagePrevious()

            textbutton _("Auto"):
                action FilePage("auto")

            textbutton _("Quick"):
                action FilePage("quick")

            for i in range(1, 9):
                textbutton str(i):
                    action FilePage(i)

            textbutton _("Next"):
                action FilePageNext()

        $ columns = 2
        $ rows = 5

        # Display a grid of file slots.
        grid columns rows:
            transpose True
            xfill True
            style_group "file_picker"

            # Display ten file slots, numbered 1 - 10.
            for i in range(1, columns * rows + 1):

                # Each file slot is a button.
                button:
                    action FileAction(i)
                    xfill True

                    has hbox

                    # Add the screenshot.
                    add FileScreenshot(i)

                    $ file_name = FileSlotName(i, columns * rows)
                    $ file_time = FileTime(i, empty=_("Empty Slot."))
                    $ save_name = FileSaveName(i)

                    text "[file_name]. [file_time!t]\n[save_name!t]"

                    key "save_delete" action FileDelete(i)


screen save():

    # This ensures that any other menu screen is replaced.
    tag menu

    imagemap:
        ground "saveload/saveload_ground.png"
        idle "saveload/saveload_idle.png"
        hover "saveload/saveload_hover.png"
        cache False
     
        hotspot (164,256,58,40) clicked FilePage(1) 
        hotspot (163,325,60,37) clicked FilePage(2) 
        hotspot (164,390,52,41) clicked FilePage(3) 
        hotspot (136,455,93,36) clicked FilePage("auto")

        
        hotspot (271,145,355,180) clicked FileSave(1):
            use load_save_slot(number=1) 
        hotspot (705,145,354,181) clicked FileSave(2):
            use load_save_slot(number=2)
        hotspot (274,405,354,180) clicked FileSave(3):
            use load_save_slot(number=3) 
        hotspot (704,407,355,188) clicked FileSave(4):
            use load_save_slot(number=4)
            #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (1048,361,121,32) action Return()

screen load():

    # This ensures that any other menu screen is replaced.
    tag menu
    
    imagemap:
        ground "saveload/saveload_ground.png"
        idle "saveload/saveload_idle.png"
        hover "saveload/saveload_hover.png"
        cache False
     
        hotspot (164,256,58,40) clicked FilePage(1) 
        hotspot (163,325,60,37) clicked FilePage(2) 
        hotspot (164,390,52,41) clicked FilePage(3) 
        hotspot (136,455,93,36) clicked FilePage("auto")

        
        hotspot (271,145,355,180) clicked FileLoad(1):
            use load_save_slot(number=1) 
        hotspot (705,145,354,181) clicked FileLoad(2):
            use load_save_slot(number=2)
        hotspot (274,405,354,180) clicked FileLoad(3):
            use load_save_slot(number=3) 
        hotspot (704,407,355,188) clicked FileLoad(4):
            use load_save_slot(number=4)
            #activate_sound "FILE NAME HERE" hover_sound "FILE NAME HERE"

        hotspot (1048,361,121,32) action Return()

    


screen load_save_slot:
    $ file_text = "% 2s. %s\n%s" % (
                        FileSlotName(number, 4),
                        FileTime(number, empty=_("Empty Slot")),
                        FileSaveName(number))

    add FileScreenshot(number) xpos 0 ypos 0
    text file_text xpos 0 ypos 10 size 40 color "#ffffff" outlines [ (2, "#302B54") ] kerning 2 font "AppleSpice.ttf"
    
    key "save_delete" action FileDelete(number)
    
init -2 python:
    
    config.thumbnail_width = 355
    config.thumbnail_height = 180


##############################################################################
# Preferences
#
# Screen that allows the user to change the preferences.
# http://www.renpy.org/doc/html/screen_special.html#prefereces

screen preferences():

    tag menu
    imagemap:   
        ground "pref/pref_ground.png"
        idle "pref/pref_idle.png"
        hover "pref/pref_hover.png"
        selected_idle "pref/pref_select_idle.png" 
        selected_hover "pref/pref_select_hover.png" 
        alpha False
        
        hotspot (463, 288, 176,33) action Preference("skip", "seen")
        hotspot (672, 291, 153, 30) action Preference("skip", "all")
        hotspot (1048,361,121,32) action Return()


        
        bar pos (531, 176) value Preference("text speed") style "pref_slider"
        bar pos (531, 405) value Preference("sound volume") style "pref_slider"
        bar pos (531, 520) value Preference("music volume") style "pref_slider"
        

init -2 python:
    style.pref_slider.left_bar = "pref/bar_left.png"
    style.pref_slider.right_bar = "pref/bar_right.png"

    style.pref_slider.xmaximum = 215
    style.pref_slider.ymaximum = 35

    style.pref_slider.thumb = "pref/bar_thumb.png"
    style.pref_slider.thumb_offset = 4
    style.pref_slider.thumb_shadow = None
 
##############################################################################
# Yes/No Prompt
#
# Screen that asks the user a yes or no question.
# http://www.renpy.org/doc/html/screen_special.html#yesno-prompt

screen yesno_prompt(message, yes_action, no_action):

    modal True

    imagemap:
        ground 'yesno/quitconf_ground.png'
        idle 'yesno/quitconf_idle.png' 
        hover 'yesno/quitconf_hover.png'
        
        alpha False
        
        hotspot (515, 343, 95, 33) action yes_action
        hotspot (678, 346, 98, 29) action no_action
    
    if message == layout.ARE_YOU_SURE:
        add "'yesno/sure_quit.png"
 
    elif message == layout.DELETE_SAVE:
        add "'yesno/delete_save_game.png"
        
    elif message == layout.OVERWRITE_SAVE:
        add "'yesno/overwrite_saved_game.png"
        
    elif message == layout.LOADING:
        add "yesno/load_saved_game.png"
        
    elif message == layout.QUIT:
        add "yesno/sure_quit.png"
        
    elif message == layout.MAIN_MENU:
        add "yesno/return_to_menu.png"

##############################################################################
# Quick Menu
#
# A screen that's included by the default say screen, and adds quick access to
# several useful functions.
screen quick_menu():
    imagemap:
        ground "qm/qm_ground.png"
        idle "qm/qm_idle.png"
        hover "qm/qm_hover.png"
        
        alpha False
        
        hotspot (1156, 570, 66, 25) action ShowMenu("save")
        hotspot (1153, 600, 63, 27) action ShowMenu("load")
        hotspot (1153, 632, 90, 27) action ShowMenu("preferences")
        hotspot (1156, 661, 70, 24) action MainMenu()
#############################################################################
#GALLERY
init python:
    #Galleries settings - start
    #list the CG gallery images here:
    gallery_cg_items = ["cg1", "cg2", "cg3", "cg4", "cg5", "cg6", "cg7", "cg8", "cg9", "cg10"]
    #list the BG gallery images here (do not include variations, such as night version):
    gallery_bg_items = ["bg kitchen", "bg road"]
    #how many rows and columns in the gallery screens?
    gal_rows = 3
    gal_cols = 3
    #thumbnail size in pixels:
    thumbnail_x = 267
    thumbnail_y = 150
    #the setting above (267x150) will work well with 16:9 screen ratio. Make sure to adjust it, if your are using 4:3 or something else.
    #Galleries settings - end
    
    gal_cells = gal_rows * gal_cols    
    g_cg = Gallery()
    for gal_item in gallery_cg_items:
        g_cg.button(gal_item + " butt")
        g_cg.image(gal_item)
        g_cg.unlock(gal_item)
    g_cg.transition = fade
    cg_page=0

    g_bg = Gallery()
    for gal_item in gallery_bg_items:
        g_bg.button(gal_item + " butt")
        g_bg.image(gal_item)
        g_bg.unlock(gal_item)
        #if BGs have variations, such as night version, uncomment the lines below and copy paste them for each BG with variations
#        if gal_item == "bg kitchen":
#            g_bg.image("bg kitchen dining")
#            g_bg.unlock("bg kitchen dining")
    g_bg.transition = fade
    bg_page=0
    
init +1 python:
    #Here we create the thumbnails. We create a grayscale thumbnail image for BGs, but we use a special "locked" image for CGs to prevent spoilers.
    for gal_item in gallery_cg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
    for gal_item in gallery_bg_items:
        renpy.image (gal_item + " butt", im.Scale(ImageReference(gal_item), thumbnail_x, thumbnail_y))
        renpy.image (gal_item + " butt dis", im.Grayscale(ImageReference(gal_item + " butt")))
        
screen cg_gallery:
    tag menu
    imagemap:
        ground "menu/background.png"
    use navigation
    frame background None xpos 10:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_cg_page = cg_page + 1            
            if next_cg_page > int(len(gallery_cg_items)/gal_cells):
                $ next_cg_page = 0
            for gal_item in gallery_cg_items:
                $ i += 1
                if i <= (cg_page+1)*gal_cells and i>cg_page*gal_cells:
                    add g_cg.make_button(gal_item + " butt", gal_item + " butt", im.Scale("gallocked.png", thumbnail_x, thumbnail_y), xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (cg_page+1)*gal_cells): #we need this to fully fill the grid
                null
screen bg_gallery:
#The BG gallery screen is more or less copy pasted from the CG screen above, I only changed "make_button" to include a grayscale thumbnail for locked items
    tag menu
    use navigation
    frame background None xpos 10:
        grid gal_rows gal_cols:
            ypos 10
            $ i = 0
            $ next_bg_page = bg_page + 1
            if next_bg_page > int(len(gallery_bg_items)/gal_cells):
                $ next_bg_page = 0
            for gal_item in gallery_bg_items:
                $ i += 1
                if i <= (bg_page+1)*gal_cells and i>bg_page*gal_cells:
                    add g_bg.make_button(gal_item + " butt", gal_item + " butt", gal_item + " butt dis", xalign=0.5, yalign=0.5, idle_border=None, background=None, bottom_margin=24)
            for j in range(i, (bg_page+1)*gal_cells):
                null
        frame:
            yalign 0.97
            vbox:
                if len(gallery_bg_items)>gal_cells:
                    textbutton _("Next Page") action [SetVariable('bg_page', next_bg_page), ShowMenu("bg_gallery")]

