# Copyright (c) 2017 Ultimaker B.V.
# This example is released under the terms of the AGPLv3 or higher.

import os.path #To find the QML files.
from PyQt5.QtCore import pyqtProperty, pyqtSignal, Qt, QUrl, QObject, QVariant #To define a shortcut key and to find the QML files, and to expose information to QML.
from PyQt5.QtQml import QQmlComponent, QQmlContext #To create a dialogue window.

from UM.Application import Application #To register the information dialogue.
from UM.Event import Event #To understand what events to react to.
from UM.PluginRegistry import PluginRegistry #To find the QML files in the plug-in folder.
from UM.Scene.Selection import Selection #To get the current selection and some information about it.
from UM.Tool import Tool #The PluginObject we're going to extend.

class ExampleTool(Tool): #The Tool class extends from PluginObject, and we have to be a PluginObject for the plug-in to load.
    ##  Creates an instance of this tool.
    #
    #   Here you can set some additional metadata.
    def __init__(self):
        super().__init__()

        self._shortcut_key = Qt.Key_X

        #This plug-in creates a window with information about the objects we've selected. That window is lazily-loaded.
        self.info_window = None

    ##  Called when something happens in the scene while our tool is active.
    #
    #   For instance, we can react to mouse clicks, mouse movements, and so on.
    def event(self, event):
        super().event(event) #The super event updates the selection if the user clicks on some object.

        if event.type == Event.MouseReleaseEvent and Selection.hasSelection(): #Only if something is selected.
            #As example for this tool, we'll spawn a message with some information.
            if self.info_window is None:
                self.info_window = self._createDialogue()
            self.info_window.show()

    ##  Creates a modal dialogue with information about the selection.
    def _createDialogue(self):
        #Create a QML component from the SelectionInfo.qml file.
        qml_file_path = os.path.join(PluginRegistry.getInstance().getPluginPath(self.getPluginId()), "SelectionInfo.qml")
        component = Application.getInstance().createQmlComponent(qml_file_path)

        return component