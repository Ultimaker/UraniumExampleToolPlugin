Example Tool
============

This is an example tool plug-in for Uranium. Uranium is the underlying framework used in Ultimaker Cura and NinjaKittens.

The tool type plug-in is meant to allow the user to manipulate the scene. Each tool gets its own button in the tool panel. The tool plug-in mainly works via an event that happens in the scene. The tool itself may decide what events it wants to act on, such as a keyboard event, a mouse release event, and so on. And then it does something with it.

Usually the tool acts upon the current selection. For instance, it may transform the selected scene nodes or modify some properties of it. This example shows how it displays the names of the currently selected items.

Packaging
---------

To package your plug-in, use the packaging script in Uranium: https://github.com/Ultimaker/Uranium/blob/master/create_plugin.py

Try the following command:

    python3 /path/to/Uranium/create_plugin.py /path/to/UraniumExampleExtensionPlugin

That should produce a .plugin file that can be added to any application based on Uranium.