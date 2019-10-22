import os
import maya.cmds as cmds
from abc import ABCMeta, abstractmethod, abstractproperty
from command import Command
from configuration import Configuration


# Module classes
class SaveCommand(Command):
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def assetTypes(self):
        pass

    @abstractmethod
    def execute(self, config):
        pass


class NoneSaveCommand(SaveCommand):
    _name = "None"
    _assetTypes = "*"

    @property
    def name(self):
        return self._name

    @property
    def assetTypes(self):
        return self._assetTypes

    def execute(self, config):
        NotImplemented


class MayaAsciiSaveCommand(SaveCommand):
    _name = "MA"
    _assetTypes = "*"

    @property
    def name(self):
        return self._name

    @property
    def assetTypes(self):
        return self._assetTypes

    def execute(self, config):
        if not os.path.exists(config.path):
            os.makedirs(config.path)

        cmds.file(rn=config.path + config.fileName + config.fileExtension)
        cmds.file(s=True, typ="mayaAscii")


class MayaBinarySaveCommand(SaveCommand):
    _name = "MB"
    _assetTypes = "*"

    @property
    def name(self):
        return self._name

    @property
    def assetTypes(self):
        return self._assetTypes

    def execute(self, config):
        if not os.path.exists(config.path):
            os.makedirs(config.path)

        cmds.file(rn=config.path + config.fileName + config.fileExtension)
        cmds.file(s=True, typ="mayaBinary")


# Module functionnalities
commands = []

noneSaveCommand = NoneSaveCommand()
commands.append(noneSaveCommand)

mayaAsciiSaveCommand = MayaAsciiSaveCommand()
commands.append(mayaAsciiSaveCommand)

# mayaBinarySaveCommand = MayaBinarySaveCommand()
# commands.append(mayaBinarySaveCommand)

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
            
