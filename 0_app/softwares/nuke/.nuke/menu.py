##############################################################################################
##   1. IMPORT MODULES   -------------------------------------------------------------------## 
##############################################################################################

##  1.1 import modules: python modules  ---------------------##
import nuke
import os.path


##  1.2 import modules: third party modules  ----------------##
import KnobScripter
#import RandomPosition
#import pixelfudger
#import AOV_selector
#import cryptomatte_utilities
#cryptomatte_utilities.setup_cryptomatte_ui()


##  1.3 import modules: third party modules from TOOLS  -----##

## import module: nukeserversocket ############################
#  nukeserversocket - allow python script execution in nuke from outside nuke
# https://github.com/sisoe24/nukeserversocket
from nukeserversocket import nukeserversocket
nukeserversocket.install_nuke()


## import module: pythonEditor by Plasmax #####################
import PythonEditor
PythonEditor.nuke_menu_setup(nuke_menu=True, node_menu=True, pane_menu=True)
#END------------


## import module: Mac&Keys Module #############################
import MacAndKeys as mnk

## END OF IMPORT MODULE --------------------------------------------------------------------##





##############################################################################################
##   2. MENUS, TOOLBARS AND COMMANDS   -----------------------------------------------------## 
##############################################################################################

###--- 2.1 NUKE MENUS ---###
m=nuke.menu('Nuke')

##  nuke menus: Add New Menus  ##
r=m.addMenu('TDAcademy', icon='github.png')
r=m.addMenu('User',icon='nuke_icon.png')

# ------------------------------------------------------------------------------------------#

###--- 2.2 NUKE TOOLBARS ---###
toolbar = nuke.toolbar("Nodes")

##  nuke toolbars: Add New Toolbar  ##

# ------------------------------------------------------------------------------------------#

###--- 2.3 COMMANDS ---###
## 2.3.1 add command to menus ##

# menu: TDAcademy ---------------------##
r.addCommand('Nothing so far...', "nothingSoFar()", icon="github.png")

def nothingSoFar():
    nuke.message("Nothing So Far... like I said.")


# menu: User -------------------------##
#r.addCommand('Aweye les Nodes', "RandomPosition.setRandomPosition()", "Shift+p", icon="nuke_icon.png")



## 2.3.2 add command to toolbars ##
# WIP

## END OF MENUS/TOOLBARS/COMMANDS ----------------------------------------------------------##



##############################################################################################
##   DEFAULT NODES VALUES   ----------------------------------------------------------------## 
##############################################################################################

#BLUR NODE
nuke.knobDefault('Blur.size', '1.5')
nuke.knobDefault('Blur.label', '[value size]')

#COPY NODE

#MERGE NODE
nuke.knobDefault('Merge2.bbox', 'B')

#MULTIPLY NODE
nuke.knobDefault('Multiply.label', '[value value]')

## END OF DEFAULT NODES VALUES ------------------------------------------------------------##