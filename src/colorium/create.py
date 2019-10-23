import os
import maya.cmds as cmds
from abc import ABCMeta, abstractmethod, abstractproperty
from command import Command
from configuration import Configuration


# Module classes
class CreateCommand(Command):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def execute(self, config):
        pass


class MayaAsciiCreateCommand(CreateCommand):
    _name = "MA"

    @property
    def name(self):
        return self._name

    def execute(self, config):
        if not os.path.exists(config.path + config.fileName + ".ma"):
            os.makedirs(config.path)
        else:
            cmds.confirmDialog(
                title="Cannot create asset",
                message="The asset cannot be created, because an asset already exists for this configuration. Please, delete the original or change the configuration.",
                button=["Ok"],
                defaultButton="Ok"
            )

            return
        
        currentSceneName = cmds.file(q=True, sn=True)
        if currentSceneName:
            cmds.file(s=True)
            cmds.file(new=True)

        cmds.file(rn=config.path + config.fileName + config.fileExtension)
        cmds.file(s=True, typ="mayaAscii")


# Module functionnalities
commands = []

mayaAsciiCreateCommand = MayaAsciiCreateCommand()
commands.append(mayaAsciiCreateCommand)

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
        