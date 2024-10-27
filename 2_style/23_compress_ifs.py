# STYLE ***************************************************************************
# content = assignment (Python Advanced)
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#**********************************************************************************

# student: Aélis Héraud
# cohort: October 2024


# SET COLOR FUNCTION --------------------------------------------------
# Not optimal
def set_color(ctrlList=None, color=None):

    # Color dictionary
    colors = {"0" : 1,
              "1" : 4,
              "2" : 13,
              "3" : 25,
              "4" : 17,
              "5" : 17,
              "6" : 15,
              "7" : 6,
              "8" : 16,
    }

    for ctrlName in ctrlList:

        #default color set if None
        if color is None or color not in range(len(colors)): color = 0
        else: pass #for future action needed
        
        #set color
        mc.setAttr(ctrlName + 'Shape.overrideEnabled', colors[str(color)])

# EXAMPLE
# set_color(['circle','circle1'], 8)

# TEST
#set_color(['circle','circle1'], 9)
#set_color(['circle','circle1'], -5)
#set_color(['circle','circle1'], 0)
#set_color(['circle','circle1'], None)
#set_color(['circle','circle1'], 3)