import os
import maya.cmds as cmds
from abc import ABCMeta, abstractmethod, abstractproperty
from command import Command
from configuration import Configuration


# Module classes
class OpenCommand(Command):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def execute(self, config):
        pass


class GenericOpenCommand(Command):
    _name = "Generic"

    @property
    def name(self):
        return self._name

    def execute(self, config):
        if not os.path.exists(config.path + config.fileName + ".ma"):
            cmds.confirmDialog(
                title="Cannot open asset",
                message="The asset cannot be opened. Please, make sure the asset information is correct.",
                button=["Ok"],
                defaultButton="Ok"
            )

            return
        
        currentSceneName = cmds.file(q=True, sn=True)
        if currentSceneName:
            cmds.file(s=True)
            cmds.file(new=True)

        cmds.file(config.path + config.fileName + ".ma", f=True, o=True, iv=True)


# Module functionnalities
commands = []

genericOpenCommand = GenericOpenCommand()
commands.append(genericOpenCommand)

def getNames():
    names = []

    for command in commands:
        names.append(command.name)

    return names

def getNamesForAssetType(assetType):
    names = []

    for command in commands:
        if command._assetTypes == "*":
            names.append(command.name)
        elif assetType in command.assetTypes:
            names.append(command.name)

    return names

def getCommandByName(name):
    for command in commands:
        if command.name == name:
            return command
        