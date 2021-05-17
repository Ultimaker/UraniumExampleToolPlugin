Example Tool
============

This is an example tool plug-in for Uranium. Uranium is the underlying framework used in Ultimaker Cura and NinjaKittens.

The tool type plug-in is meant to allow the user to manipulate the scene. Each tool gets its own button in the tool panel. The tool plug-in mainly works via an event that happens in the scene. The tool itself may decide what events it wants to act on, such as a keyboard event, a mouse release event, and so on. And then it does something with it.

Usually the tool acts upon the current selection. For instance, it may transform the selected scene nodes or modify some properties of it. This example shows how it displays the names of the currently selected items.

Packaging
---------

To package your plug-in, compress your plug-in folder in a .zip archive and rename that archive to get the `.plugin` extension. These .plugin files can be dropped into any Uranium application to be installed.
