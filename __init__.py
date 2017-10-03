# Copyright (c) 2017 Ultimaker B.V.
# This example is released under the terms of the AGPLv3 or higher.

from . import ExampleTool

##  Defines additional metadata for the plug-in.
#
#   Tool plug-ins can have a button in the interface. This has some metadata
#   that describes the tool and provides an image.
def getMetaData():
    return {
        "tool": {
            "name": "Example Tool",
            "description": "This is an example tool to illustrate to plug-in developers how tool plug-ins are created.", #Typically displayed when hovering over the tool icon.
            "icon": "magnifying_glass.svg" #Displayed on the button.
        }
    }

##  Lets Uranium know that this plug-in exists.
#
#   This is called when starting the application to find out which plug-ins
#   exist and what their types are. We need to return a dictionary mapping from
#   strings representing plug-in types (in this case "tool") to objects that
#   inherit from PluginObject.
#
#   \param app The application that the plug-in needs to register with.
def register(app):
    return {"tool": ExampleTool.ExampleTool()}
