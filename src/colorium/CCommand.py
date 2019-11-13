from abc import ABCMeta, abstractmethod, abstractproperty
import os
import maya.cmds as cmds


class CCommand:
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

    @abstractproperty
    def action(self):
        pass

    @abstractmethod
    def execute(self, config):
        pass
    

class CConcreteCommand(CCommand):
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value


    @property
    def action(self):
        return self._action

    @action.setter
    def action(self, value):
        self._action = value


    @property
    def function(self):
        return self._function

    @function.setter
    def function(self, value):
        self._function = value


    def __init__(self, action, name, function):
        self._action = action
        self._name = name
        self._function = function

    
    def execute(self, config):
        self._function(config)


def __openExplorer(config):
    if not os.path.exists(config.path):
        cmds.confirmDialog(
            title="Cannot open in Explorer",
            message="The asset's folder cannot be opened in Explorer. Please, make sure the asset information is correct.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return
        
    path = os.path.realpath(config.path)

    os.startfile(path)


def __openScene(config):
    if not os.path.exists(config.path + config.fileName + ".ma"):
        cmds.confirmDialog(
            title="Cannot open asset",
            message="The asset cannot be opened. Please, make sure the asset information is correct.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return
    
    current_scene_name = cmds.file(q=True, sn=True)
    if current_scene_name:
        cmds.file(s=True)
        cmds.file(new=True)

    cmds.file(config.path + config.fileName + ".ma", f=True, o=True, iv=True)


def __createBlankMayaAscii(config):
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
    
    current_scene_name = cmds.file(q=True, sn=True)
    if current_scene_name:
        cmds.file(s=True)
        cmds.file(new=True)

    cmds.file(rn=config.path + config.fileName)
    cmds.file(s=True, typ="mayaAscii")


def __publishMayaAscii(config):
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


def __publishMayaBinary(config):
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

    cmds.file(config.path + config.fileName, es=True, typ="mayaBinary")


def __exportMayaAscii(config):
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

    cmds.file(config.path + config.fileName, es=True, typ="mayaAscii")


def __exportMayaBinary(config):
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

    cmds.file(config.path + config.fileName, es=True, typ="mayaBinary")


commands = []
commands.append(CConcreteCommand("open", "Explorer", __openExplorer))
commands.append(CConcreteCommand("open", "Scene", __openScene))
commands.append(CConcreteCommand("create", "Blank Maya Ascii", __createBlankMayaAscii))
commands.append(CConcreteCommand("publish", "Maya Ascii", __publishMayaAscii))
commands.append(CConcreteCommand("publish", "Maya Binary", __publishMayaBinary))


def getCommandsByAction(action):
    commands_to_return = []

    for command in commands:
        if command.action == action:
            commands_to_return.append(command)

    return commands_to_return


def getCommandsByName(name):
    commands_to_return = []

    for command in commands:
        if command.name == name:
            commands_to_return.append(name)

    return commands_to_return


def getCommand(action, name):
    for command in commands:
        if command.action == action and command.name == name:
            return command
