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

def clearPreferences():
    """
    Purpose: delete all the custom MnKeys knobs from the Nuke Preferences Panel
    """
    preferences_knobs = preferences_node.knobs()

    for knob in preferences_knobs:
        if 'mnk_' in knob:
            knob_obj = preferences_node.knob(knob)
            preferences_node.removeKnob(knob_obj)
        else:
            pass

# end def



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

    # pref knob: [File] .nuke directory location #---------------------------------------------
    knob = nuke.File_Knob('mnk_nuke_directory_location', '.nuke directory')
    knob.setValue(user_home_folder_path)
    knob.setFlag(nuke.DISABLED)
    addToPreferences(knob)

    # pref knob: [Divider] empty label divider line #------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_divider0','<b> </b>'))

    # pref knob: [File] NodePresets directory location #---------------------------------------------
    knob = nuke.File_Knob('mnk_node_presets_directory_location', 'Node Presets directory')
    knob.setValue('~/NodePresets')
    knob.setFlag(nuke.DISABLED)
    addToPreferences(knob)

    # pref knob: [File] NodePresets directory full path | HIDDEN #---------------------------------------------
    knob = nuke.File_Knob('mnk_node_presets_directory_full_path', 'Node Presets directory full path')
    knob.setValue(user_home_folder_path + '/NodePresets')
    knob.setFlag(nuke.DISABLED)
    knob.setVisible(False)
    addToPreferences(knob)

    # pref knob: [Divider] empty label divider line #------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_divider1','<b> </b>'))



    # pref knob: [File] app directory location #---------------------------------------------
    knob = nuke.File_Knob('mnk_app_directory_location', 'root directory')
    knob.setValue('~/' + app_folder_name)
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where all the other folders and configuration files"
    addToPreferences(knob, tooltip)

    # pref knob: [File] app directory full path | HIDDEN #---------------------------------------------
    knob = nuke.File_Knob('mnk_app_directory_full_path', 'root directory full path')
    knob.setValue(user_home_folder_path + '/' + app_folder_name)
    knob.clearFlag(nuke.STARTLINE)
    knob.setVisible(False)
    addToPreferences(knob)

    
    # pref knob: [button] open app folder location in explorer #-------------------
    # TODO : function to open in explorer Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_app_folder', ' open in explorer ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the subfolders and configuration files"
    addToPreferences(knob, tooltip)





    # pref knob: [File] general preferences files directory location #---------------------------------------------
    knob = nuke.File_Knob('mnk_keys_preferences_directory_location', 'General preferences')
    knob.setValue('~/' + app_folder_name + '/preferences')
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where general preferences files are stored"
    addToPreferences(knob, tooltip)

    # pref knob: [File] general preferences files directory full path | HIDDEN #---------------------------------------------
    knob = nuke.File_Knob('mnk_keys_preferences_directory_full_path', 'General preferences full path')
    knob.setValue(user_home_folder_path + '/' + app_folder_name + '/preferences')
    knob.clearFlag(nuke.STARTLINE)
    knob.setVisible(False)
    addToPreferences(knob)
    
    # pref knob: [button] open general preferences files folder location in explorer #-------------------
    # TODO : function to open in explorer Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_keys_preferences_folder', ' open in explorer ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the MacNKeys preferences files"
    addToPreferences(knob, tooltip)



    # pref knob: [File] Fkeys presets directory location #---------------------------------------------
    knob = nuke.File_Knob('mnk_keys_presets_directory_location', 'F/Nav Keys presets')
    knob.setValue('~/' + app_folder_name + '/presets')
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where each node configs file are stored"
    addToPreferences(knob, tooltip)

    # pref knob: [File] Fkeys presets directory full path | HIDDEN #---------------------------------------------
    knob = nuke.File_Knob('mnk_keys_presets_directory_full_path', 'F/Nav Keys presets full path')
    knob.setValue(user_home_folder_path + '/' + app_folder_name + '/presets')
    knob.clearFlag(nuke.STARTLINE)
    knob.setVisible(False)
    addToPreferences(knob)
    
    # pref knob: [button] open Fkeys presets folder location in explorer #-------------------
    # TODO : function to open in explorer Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_keys_presets_folder', ' open in explorer ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the node configuration files"
    addToPreferences(knob, tooltip)





    # pref knob: [File] pyscripts directory location #-------------------------------------
    knob = nuke.File_Knob('mnk_pyscripts_directory_location', 'pyscripts directory')
    script_folder_path = '~/' + app_folder_name + '/pyscripts'
    print("content of script folder location: {}".format(script_folder_path))
    knob.setValue(script_folder_path)
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where to find the python script for the macros command"
    addToPreferences(knob, tooltip)

    # pref knob: [File] pyscripts directory full path | HIDDEN #-------------------------------------
    knob = nuke.File_Knob('mnk_pyscripts_directory_full_path', 'pyscripts directory full path')
    script_folder_path = user_home_folder_path + '/' + app_folder_name + '/pyscripts'
    print("content of script folder full path: {}".format(script_folder_path))
    knob.setValue(script_folder_path)
    knob.clearFlag(nuke.STARTLINE)
    knob.setVisible(False)
    addToPreferences(knob)

    # pref knob: [button] open pyscripts folder location in explorer #-----------
    # TODO : function to open in explorer Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_scripts_folder', ' open in explorer ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the macros python scripts"
    addToPreferences(knob, tooltip)


    # pref knob: [Divider] empty label divider line #------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_divider2','<b> </b>'))


    # pref knob: [File] user profile folder location #--------------------------------
    knob = nuke.File_Knob('mnk_profiles_directory_location', 'user profiles directory')
    profiles_folder_path = '~/' + app_folder_name + '/profiles'
    knob.setValue(profiles_folder_path)
    print("content of profile folder location: {}".format(profiles_folder_path))
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The folder on disk where to find the user profile config files"
    addToPreferences(knob, tooltip)

    # pref knob: [File] user profile folder full path | HIDDEN #--------------------------------
    knob = nuke.File_Knob('mnk_profiles_directory_full_path', 'user profiles directory full path')
    profiles_folder_path = user_home_folder_path + '/' + app_folder_name + '/profiles'
    knob.setValue(profiles_folder_path)
    print("content of profile folder full path: {}".format(profiles_folder_path))
    knob.clearFlag(nuke.STARTLINE)
    knob.setVisible(False)
    addToPreferences(knob)

    # pref knob: [button] open user profiles folder in explorer #--------------------
    # TODO function to reset the preferences Mac&Keys.openInExplorer(True)
    knob = nuke.PyScript_Knob('mnk_open_profile_folder', ' open in explorer ', 'Mac&Keys.openInExplorer(True)')
    tooltip = "Open the folder containing the user profile config files"
    addToPreferences(knob, tooltip)

    # pref knob: [Divider] empty label divider line #------------------------------------
    knob = nuke.Text_Knob('mnk_space','<b> </b>')
    knob.setValue(" ")
    addToPreferences(knob)





    # pref knob: Launch Label #-----------------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_launch_label','<b>Launch</b>'))

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

    # pref knob: [Divider] empty label divider line #------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_divider3','<b> </b>'))




    # pref knob: [String] trigger shortcut #------------------------------
    knob = nuke.String_Knob('mnk_shortcut','Shortcut')
    knob.setValue('~')
    tooltip = ("The key that triggers the config window from the selected node. Nuke needs be restarted in order for the changes to take effect.")
    addToPreferences(knob, tooltip)

    global shortcut
    shortcut = preferences_node.knob('mnk_shortcut').value()

    # pref knob: [button] reset shortcut knob and update Edit/Node menu item
    knob = nuke.PyScript_Knob('mnk_reset_shortcut','set', 'MacAndKeys.resetMenuItems()')
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Apply new shortcut."
    addToPreferences(knob, tooltip)




    # pref knob: [combobox] panel mode #-------------------------------------
    knob = nuke.Enumeration_Knob('mnk_panel_mode', 'Open panel mode', ['Floating Panel','Properties Panel'])
    knob.setFlag(nuke.STARTLINE)
    tooltip = "The Mode in which the config panel opens when triggered"
    addToPreferences(knob, tooltip)

    # pref knob: [checkbox] save when closing #------------------------------
    knob = nuke.Boolean_Knob('mnk_save_on_closing','Save on Closing')
    knob.setValue(False)
    knob.clearFlag(nuke.STARTLINE)
    tooltip = "Autosave config on closing the node config window"
    addToPreferences(knob, tooltip)



    # pref knob: [Text] Exclusion Rules Label #-----------------------------------------------
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

    # pref knob: [Divider] empty label divider line #------------------------------------
    addToPreferences(nuke.Text_Knob('mnk_divider4','<b> </b>'))

    # pref knob: [button] reset preferences #----------------------------------
    # TODO function to reset the preferences Mac&Keys.resetPreferences()
    knob = nuke.PyScript_Knob('mnk_reset_preferences', ' reset preferences ', 'Mac&Keys.resetPreferences(True)')
    knob.setFlag(nuke.STARTLINE)
    tooltip = "Reset preferences to the default values"
    addToPreferences(knob, tooltip)



    # save all added preferences to the preference file in HOME folder
    #savePreferencesToFile() 
# end def

def savePreferencesToFile():
    """
    Purpose: Saves the current preferences from the Nuke Preferences Node in the .nuke folder
    in order to populate correctly the preferences node upon every launch.
    By default it will be saved to the app folder: ~/.nuke/MacNKeys/preferencesXX.Y.nk
    in which XX is the Major Nuke version number and Y the minor Nuke version number
    """
    
    preferences_file = getPreferencesFile() #str (path + .ext)   
# end def


def saveKeysPresetsToFile(nodeClass=None):
    """
    Purpose: 
    """
    pass
# end def


def saveUserProfileToFile():
    """
    Purpose: 
    """
    pass
# end def


def refreshUserProfilesFolder():
    """
    Purpose: 
    """
    pass
# end def

def refreshPyscriptFolder():
    """
    Purpose: 
    """
    pass
# end def




def getPreferencesFile():
    """
    Purpose: returns the full path of the preferences file in which
    is saved all the custom content from the Nuke's Preferences node.
    
    """
    nuke_folder_path = getNukeFolderPath()
    app_folder_path = nuke_folder_path + '/' + app_folder_name
    nuke_v_maj = nuke.NUKE_VERSION_MAJOR
    nuke_v_min = nuke.NUKE_VERSION_MINOR
    preferences_file_name = "preferences{}.{}.nk".format(nuke_v_maj, nuke_v_min)
    preferences_file = app_folder_path + '/' + preferences_file_name

    return preferences_file  
# end def

def getNukeFolderPath():
    """
    Purpose: returns the path of the .nuke folder (native or custom)
    """
    nuke_folder_path = os.path.expanduser('~') + '/.nuke'

    if os.getenv('NUKE_PATH') is not None:
        nuke_folder_path = os.getenv('NUKE_PATH')
    
    if nuke_folder_path.endswith(";"): nuke_folder_path = nuke_folder_path.replace(';', '')

    print("nuke_folder_path:{}".format(nuke_folder_path))
    return nuke_folder_path
# end def

def getHomeFolderPath():
    """
    Purpose: returns the path of the user Home folder
    """
    home_folder_path = os.path.expanduser('~') + '/.nuke'

    if os.getenv('HOME') is not None:
        home_folder_path = os.getenv('HOME')
    
    return home_folder_path   
# end def




# TODO
def showMnKeysPanel():
    """
    Purpose: 
    """
    pass
# end def
# TODO
def resetMnKeys():
    """
    Purpose: 
    """
    pass
# end def







def setAppFolder():
    """
    Purpose: makes sure the folders and sub folder structure exists or creates them within the user home folder (/.nuke)
    """
    #user_home_folder_path = os.getenv('HOME').replace('\\','/') + '/.nuke'
    #app_folder_name = "MacAndKeys"
    app_sub_folders = ['','profiles', 'pyscripts', 'presets', 'preferences']
    print(preferences_node.knob("mnk_app_directory_location").getValue())

    #preferences_node = nuke.toNode('preferences')
    pref_app_folder_path = preferences_node.knob("mnk_app_directory_full_path").getValue().replace('\\', '/')


    if not pref_app_folder_path:
        # app location knob is empty => assigning the default value
        pref_app_folder_path = user_home_folder_path + '/' + app_folder_name
        preferences_node.knob("mnk_app_directory_full_path").setValue(pref_app_folder_path)
    
    if pref_app_folder_path[-1] != '/': pref_app_folder_path += '/'

    for app_sub_folder in app_sub_folders:
        app_sub_folder_path = pref_app_folder_path + app_sub_folder

        # create a sub folder if inexistent
        if not os.path.isdir(app_sub_folder_path):
            os.mkdir(app_sub_folder_path)
        else:
            pass
    

    # Node Presets folder
    nuke_folder_path = getNukeFolderPath()
    node_presets_folder_path = nuke_folder_path + '/NodePresets'
    print("node_presets_folder_path:{}".format(node_presets_folder_path))
    if not os.path.isdir(node_presets_folder_path):
        os.mkdir(node_presets_folder_path)
    else:
        pass

# end def





# TODO
def addMenuItems():
    """
    Purpose: Add the contextual shortcut item in the Edit/Node menu in Nuke
    """
    edit_node_menu.addCommand('MacNKeys/Refresh All', '', '')
    # TODO refreshAll() function to re-scan all folder with content
    edit_node_menu.addCommand('MacNKeys/Open Contextual Shortcut Pane for...', showMnKeysPanel, shortcut)
    # TODO showMnKeysPanel() function
    
    edit_node_menu.addCommand('MacNKeys/Reset Contextual Shortcuts for...', resetMnKeys, '') 
    # TODO resetMnKeys() function
    edit_node_menu.addCommand('MacNKeys/-', '', '')
    edit_node_menu.addCommand('MacNKeys/Open in Explorer.../MacNKeys folder', '', '')
    edit_node_menu.addCommand('MacNKeys/Open in Explorer.../preferences folder', '', '')
    edit_node_menu.addCommand('MacNKeys/Open in Explorer.../profiles folder', '', '')
    edit_node_menu.addCommand('MacNKeys/Open in Explorer.../pyscripts folder', '', '')
    edit_node_menu.addCommand('MacNKeys/Open in Explorer.../presets folder', '', '')
    edit_node_menu.addCommand('MacNKeys/Delete .../All MnKeys', '', '')
    edit_node_menu.addCommand('MacNKeys/Delete .../All preferences', '', '')
    edit_node_menu.addCommand('MacNKeys/Delete .../All profiles', '', '')
    edit_node_menu.addCommand('MacNKeys/Delete .../All pyscripts', '', '')
    edit_node_menu.addCommand('MacNKeys/Delete .../All presets', '', '')
    # TODO Command for all the menu items above
# end def

def resetMenuItems():
    """
    Purpose: Update the menu items and shortcut with the latest from the preferences panel
    """
    global shortcut
    shortcut = preferences_node.knob('mnk_shortcut').value()

    if edit_node_menu.findItem('MacNKeys'):
        edit_node_menu.removeItem('MacNKeys')
    
    addMenuItems()
# end def

################################################################################

# -------------------------------------------------------
# EXECUTION / START
# -------------------------------------------------------

# Execute the .bat file to open nuke
#if __name__ == "__main__":
#    p = subprocess.Popen("nuke.bat", cwd=r"C:/Users/aheraud/Documents/TDAcademy/assignments/1_tools/nuke.bat")


# initiate the preferences variables at launch
preferences_node = nuke.toNode('preferences')
app_folder_name = "MacAndKeys"

# getting the .nuke home folder
user_home_folder_path = os.getenv('HOME').replace('\\', '/') + '/.nuke'
if os.getenv('SCRIPT_PATH') is not None:
    user_home_folder_path = os.getenv('SCRIPT_PATH').replace('\\', '/')


clearPreferences()
#shortcut = '~' # for test

# Populate the Preferences panel
#updatePreferences()
addPreferences()

# Set the folder and sub folders on disk
setAppFolder()






# Add the menu items
edit_node_menu = nuke.menu('Nuke').findItem('Edit/Node')
edit_node_menu.addCommand('-', '', '')
addMenuItems()

# Add the app folder to the python path repo for python execution
# TODO

# Add the menu items and shortcut commands in the menu.py
# TODO


