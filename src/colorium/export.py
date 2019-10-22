import os
import maya.cmds as cmds
from abc import ABCMeta, abstractmethod, abstractproperty
from command import Command
from configuration import Configuration


# Module classes
class ExportCommand(Command):
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


class NoneExportCommand(ExportCommand):
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


class MayaAsciiExportCommand(ExportCommand):
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
                title="Cannot export asset",
                message="The asset cannot be exported. Please, select the objects you want to export.",
                button=["Ok"],
                defaultButton="Ok"
            )

            return

        cmds.file(config.path + config.fileName + config.fileExtension, es=True, typ="mayaAscii")


class MayaBinaryExportCommand(ExportCommand):
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

        selection = cmds.ls(sl=True)
        if len(selection) == 0:
            cmds.confirmDialog(
                title="Cannot export asset",
                message="The asset cannot be exported. Please, select the objects you want to export.",
                button=["Ok"],
                defaultButton="Ok"
            )

            return

        cmds.file(config.path + config.fileName + config.fileExtension, es=True, typ="mayaBinary")


class AlembicExportCommand(ExportCommand):
    _name = "Alembic"
    _assetTypes = "*"

    @property
    def name(self):
        return self._name

    @property
    def assetTypes(self):
        return self._assetTypes

    def execute(self, config):
        NotImplemented


class FBXExportCommand(ExportCommand):
    _name = "FBX"
    _assetTypes = "*"

    @property
    def name(self):
        return self._name

    @property
    def assetTypes(self):
        return self._assetTypes

    def execute(self, config):
        NotImplemented


class OBJExportCommand(ExportCommand):
    _name = "OBJ"
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

noneExportCommand = NoneExportCommand()
commands.append(noneExportCommand)

mayaAsciiExportCommand = MayaAsciiExportCommand()
commands.append(mayaAsciiExportCommand)

# mayaBinaryExportCommand = MayaBinaryExportCommand()
# commands.append(mayaBinaryExportCommand)

alembicExportCommand = AlembicExportCommand()
commands.append(alembicExportCommand)

fbxExportCommand = FBXExportCommand()
commands.append(fbxExportCommand)

objExportCommand = OBJExportCommand()
commands.append(objExportCommand)

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
