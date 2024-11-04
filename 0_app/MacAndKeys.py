# --------------------------------------------------------
# Aélis Héraud
# aelis_heraud@hotmail.com

# version: 0.1.0
# date: 01 November 2024

#version = "0.1.0"
#releaseDate = "November 1st 2024"


# importing module -----------------
import nuke

import os
import re
import sys
import shutil
import platform
import subprocess



##########################################################
## VARIABLES ##

TITLE = "Load"

preferences_node = nuke.toNode('preferences')
operating_system = platform.system()


# -------------------------------------------------------
# FUNCTIONS 
# -------------------------------------------------------

def addToPreferences(knobObj, tooltip = None):
    """
    Purpose: add a knob to the Preferences Node in Nuke
    """
    
    if knobObj.name() not in preferences_node.knobs().keys():

        preferences_node.addKnob(knobObj)
        return preferences_node.knob(knobObj.name())
# end def


def addPreferences():
    """
    Purpose: add all the knobs to the Preferences Node in Nuke
    """
    
    # knob dictionary
    preferences_knobs = {}
    profile_list = ['default']
    
    addToPreferences(nuke.Tab_Knob('mnk_tab_label','Mac&Keys'))
    addToPreferences(nuke.Text_Knob('mnk_general_label', '<b>General</b>'))

    # pref knob: [File] folder location #---------------------------------------------
    knob = nuke.File_Knob('mnk_app_location', 'Mac&Keys folder location')
    knob.setValue(user_home_folder_path + '/' + app_folder_name)
    tooltip = "The folder on disk where all the other folders and configuration files"
    addToPreferences(knob, tooltip)
    
    # pref knob: [button] open folder location in explorer #-------------------
    # TODO : function to open in explorer Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_app_folder', ' open app folder ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the subfolders and configuration files"
    addToPreferences(knob, tooltip)


    # pref knob: [File] scripts folder location #-------------------------------------
    knob = nuke.File_Knob('mnk_scripts_location', 'scripts folder location')
    knob.setValue(user_home_folder_path + '/' + app_folder_name + '/pyscripts')
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where to find the python script for the macros command"
    addToPreferences(knob, tooltip)

    # pref knob: [button] open scripts folder location in explorer #-----------
    # TODO : function to open in explorer Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_scripts_folder', ' open scripts folder ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the macros python scripts"
    addToPreferences(knob, tooltip)

    # pref knob: [Divider] empty label divider line #------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_divider','<b> </b>'))


    # pref knob: [button] reset preferences #----------------------------------
    # TODO function to reset the preferences Mac&Keys.resetPreferences()
    knob = nuke.PyScript_Knob('mnk_reset_preferences', ' reset preferences ', 'Mac&Keys.resetPreferences(True)')
    knob.setFlag(nuke.STARTLINE)
    tooltip = "Reset preferences to the default values"
    addToPreferences(knob, tooltip)

    # pref knob: [Text] Profile Label #-----------------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_profile_label','<b>Profile</b>'))
    
    # pref knob: [File] user profile folder location #--------------------------------
    knob = nuke.File_Knob('mnk_user_profile_location', 'user profile location')
    knob.setValue(user_home_folder_path + '/' + app_folder_name + '/profiles')
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where to find the user profile config files"
    addToPreferences(knob, tooltip)

    # pref knob: [button] open profile folder in explorer #--------------------
    # TODO function to reset the preferences Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_profile_folder', ' open profile folder ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the user profile config files"
    addToPreferences(knob, tooltip)

    # pref knob: [combobox] default profile
    knob = nuke.Enumeration_Knob('mnk_default_profile', 'default profile', profile_list)
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The Default Profile config file"
    addToPreferences(knob, tooltip)

    # pref knob: [button] refresh user profile list  #--------------------
    # TODO function to reset the preferences Mac&Keys.refreshUserProfileList(True)
    knob = nuke.PyScript_Knob('mnk_refresh_profile_list', ' refresh profile list ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Refresh the list of user profile files"
    addToPreferences(knob, tooltip)




    # pref knob: Launch Label #-----------------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_launch_label','<b>Launch</b>'))

    # pref knob: [String] trigger shortcut 
    knob = nuke.String_Knob('mnk_shortcut','Shortcut')
    knob.setValue('~')
    tooltip = ("The key that triggers the config window from the selected node. Nuke needs be restarted in order for the changes to take effect.")
    addToPreferences(knob, tooltip)

    # pref knob: [combobox] panel mode
    knob = nuke.Enumeration_Knob('mnk_panel_mode', 'panel mode', ['Floating Panel','Properties Panel'])
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The Mode in which the config panel opens when triggered"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] save when closing
    knob = nuke.Boolean_Knob('mnk_save_on_closing','Save on Closing')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Autosave config on closing the node config window"
    addToPreferences(knob, tooltip)



    # pref knob: [Text] Exculsion Rules Label #-----------------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_exclusion_label','<b>Exclusion Rules</b>'))

    # pref knob: [Text] F-Keys to ban Label #-----------------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_fkeys_ban_label','F-Keys to ban'))

    # pref knob: [checkbox] F1 Key
    knob = nuke.Boolean_Knob('mnk_f1_ban','F1')
    knob.setValue(False)
    knob.setFlag(nuke.STARTLINE)
    tooltip = "Ban F1 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F2 Key
    knob = nuke.Boolean_Knob('mnk_f2_ban','F2')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F2 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F3 Key
    knob = nuke.Boolean_Knob('mnk_f3_ban','F3')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F3 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F4 Key
    knob = nuke.Boolean_Knob('mnk_f4_ban','F4')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F4 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F5 Key
    knob = nuke.Boolean_Knob('mnk_f5_ban','F5')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F5 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F6 Key
    knob = nuke.Boolean_Knob('mnk_f6_ban','F6')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F6 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F7 Key
    knob = nuke.Boolean_Knob('mnk_f7_ban','F7')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F7 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F8 Key
    knob = nuke.Boolean_Knob('mnk_f8_ban','F8')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F8 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F9 Key
    knob = nuke.Boolean_Knob('mnk_f9_ban','F9')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F9 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F10 Key
    knob = nuke.Boolean_Knob('mnk_f10_ban','F10')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F10 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F11 Key
    knob = nuke.Boolean_Knob('mnk_f11_ban','F11')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F11 from the list of available F-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] F12 Key
    knob = nuke.Boolean_Knob('mnk_f12_ban','F12')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban F12 from the list of available F-Keys"
    addToPreferences(knob, tooltip)




    # pref knob: [Text] N-Keys to ban Label #-----------------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_nkeys_ban_label','n-Keys to ban'))

    # pref knob: [checkbox] Arrows Up and Down
    knob = nuke.Boolean_Knob('mnk_vertical_arrows_ban','Arrows Up / Down')
    knob.setValue(False)
    knob.setFlag(nuke.STARTLINE)
    tooltip = "Ban vertical arrows from the list of available N-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] Arrows Left and Right
    knob = nuke.Boolean_Knob('mnk_horizontal_arrows_ban','Arrows Left / Right')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban horizontal arrows from the list of available N-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] Page Up and Down
    knob = nuke.Boolean_Knob('mnk_pg_ban','PgUp / PgDn')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban PgUp/PgDn from the list of available N-Keys"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] Home and End
    knob = nuke.Boolean_Knob('mnk_home_end_ban','Home / End')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Ban Home/End from the list of available N-Keys"
    addToPreferences(knob, tooltip)




    # save all added preferences to the preference file in HOME folder
    #savePreferencesToFile() 
# end def




def setAppFolder():
    """
    Purpose: makes sure the folders and sub folder structure exists or creates them within the user home folder (/.nuke)
    """
    #user_home_folder_path = os.getenv('HOME').replace('\\','/') + '/.nuke'
    #app_folder_name = "MacAndKeys"
    app_sub_folders = ['','profiles', 'pyscripts', 'presets', 'preferences']

    #preferences_node = nuke.toNode('preferences')
    pref_app_folder_path = preferences_node.knob("mnk_app_location").getValue().replace('\\', '/')


    if not pref_app_folder_path:
        # app location knob is empty => assigning the default value
        pref_app_folder_path = user_home_folder_path + '/' + app_folder_name
        preferences_node.knob("mnk_app_location").setValue(pref_app_folder_path)
    
    if pref_app_folder_path[-1] != '/': pref_app_folder_path += '/'

    for app_sub_folder in app_sub_folders:
        app_sub_folder_path = pref_app_folder_path + app_sub_folder

        # create a sub folder if inexistent
        if not os.path.isdir(app_sub_folder_path):
            os.mkdir(app_sub_folder_path)
        else:
            pass


# end def



################################################################################

# -------------------------------------------------------
# EXECUTION / START
# -------------------------------------------------------

# initiate the preferences at launch
preferences_node = nuke.toNode('preferences')
user_home_folder_path = os.getenv('HOME').replace('\\', '/') + '/.nuke'
app_folder_name = "MacAndKeys"

# Populate the Preferences panel
#updatePreferences()
addPreferences()

# Set the folder and sub folders on disk
setAppFolder()

# Add the app folder to the python path repo for python execution
# TODO

# Add the menu items and shortcut commands in the menu.py
# TODO


