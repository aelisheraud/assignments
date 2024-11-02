# *Mac&Keys (Application) - WIP*

## *Documentation - WIP*

### **Description**

This tool is a ***multi node contextual shortcut tool*** allowing Nuke users to perform more than one action using the same hotkey, depending on the node currently selected. It combines the *shortcut allocations system* with the *cycle-through mechanism* in one hotkey by mixing 2 current concepts together
: *"1 shortcut = 1 different action"* per Nuke panels (Viewer, Node Graph, 3D Space, etc...) and *"1 node = 1 shortcut"* per action (set knob values for instance) and applies the first on the second one to allow the user to have 1 shortcut = 1 different action per Node. This tool uses the 12 functions keys (F1 to F12) as well as the 4 pairs of Navigation keys (Arrows Up/Down, Arrows Left/Right, PageUp/PageDown, Home/End).

It helps in three different area of needs when extensively use of the same nodes in big scripts is concerned:
- Removing annoying repetitive task on node configuration 
- Allowing a very large amount of different node configurations available fast
- Reducing the amount of shortcut to use or remember

Conditioning one hotkey behavior (for instance F1) to the current selected node will exponentially increase the *'hotkey/node = action"* combinations available to the user. For example, it would mean that:

*"F1 + Merge Node"* will have a different result than *"F1 + Grade Node"*, which will also have a different result than *"F1 + Shuffle Node"*, etc...

Associated with the *cycle-through mechanism*, using F1 more than once on the same node will also have different results as well, sowhich could translate in *"F1 (hit once) + Merge Node"* will have a different result than *"F1 (hit twice) + Merge Node"*, which in turn will have a different result then *"F1 (hit three times) + Merge Node"*, etc...

In essence, this tool allow user to have more options to configure their most commonly used node, only using the same few hotkeys, in a faster way.



### **CYCLE-THROUGH MECHANISMS**

- **Toggle Value Mode:** List of 2 values for 1 knob
- **Toggle Preset Mode:** List of 2 user presets for 1 node
- **Full Value Cycle:** List of more than 2 user presets for 1 node
- **Full Preset Cycle:** List of more than 2 values for 1 knob
- **Macros:** List of a unique macros python script to execute


### **KEYS**

**1.Function Keys** (*a.k.a F.keys*), from F1 to F12 : For Toggle, Full Cycle and Macros mechanisms.
**2.Navigation Keys** (*a.k.a Nav.keys*) in the form of 4 pairs : For Full Cycle mechanisms.


### **FEATURES**
- Ability to ban one or more F.keys (usually used company wide for custom pipeline shortcut like Rendering or publishing)
- Ability to save all the keys/nodes configuration in a profile to export and import.
- ... *(to be continued - WIP)*

### **SETTINGS**

Settings will be apply from 2 types of locations:

- The Nuke native Preferences Panel: User will find all the general settings from the tool, like the local path for the macros python file, the exception/banning rules/nodes/keys, the import/export user profile, all the different settings affecting each shortcut the same way, the documentation and a summary of all the command/shortcut/nodes already assigned.

- The contextual Node Settings panel : a small floating panel accessible from the node graph using one specific hotkey (the tilde for instance) in which the user will be able to set all the different behavior of the alloted Fkeys and NavKeys for the current selected node.

*(WIP)*


### **POTENTIAL FUTURE FEATURES**
- *(WIP)*