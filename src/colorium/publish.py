import os
import maya.cmds as cmds
from abc import ABCMeta, abstractmethod, abstractproperty
from command import Command
from CConfiguration import CConfiguration
import CSceneNameParser


# Module classes
class PublishCommand(Command):
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


class NonePublishCommand(PublishCommand):
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


class MayaAsciiPublishCommand(PublishCommand):
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

        selection = cmds.ls(sl=True)
        if len(selection) == 0:
            cmds.confirmDialog(
                title="Cannot publish asset",
                message="The asset cannot be published. Please, select the objects you want to publish.",
                button=["Ok"],
                defaultButton="Ok"
            )

            return

        cmds.file(config.path + config.fileName, es=True, typ="mayaAscii")


class GeometryCachePublishCommand(PublishCommand):
    _name = "Geometry Cache"
    _assetTypes = "*"

    @property
    def name(self):
        return self._name

    @property
    def assetTypes(self):
        return self._assetTypes

    def execute(self, config):
        NotImplemented


# Module functionnalities
commands = []

nonePublishCommand = NonePublishCommand()
commands.append(nonePublishCommand)

mayaAsciiPublishCommand = MayaAsciiPublishCommand()
commands.append(mayaAsciiPublishCommand)

geometryCachePublishCommand = GeometryCachePublishCommand()
commands.append(geometryCachePublishCommand)

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
