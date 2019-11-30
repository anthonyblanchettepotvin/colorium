"""Module containing all the commands used in Colorium's tools."""

from abc import ABCMeta, abstractmethod, abstractproperty
import os
import maya.cmds as cmds


class CCommand:
    """Abstract class for a command."""

    __metaclass__ = ABCMeta


    @abstractproperty
    def name(self):
        """The name of the command."""

        pass


    @abstractproperty
    def action(self):
        """The type of action the command does."""

        pass


    @abstractmethod
    def execute(self, config):
        """The execution of the command."""

        pass


class CConcreteCommand(CCommand):
    """Concrete implementation of the CCommand class."""

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
        """The function that contains the executing code."""

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


def __open_explorer(config):
    """Open the configuration path in the Explorer."""

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


def __open_scene(config):
    """Open the Maya scene based on the configuration."""

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


def __create_blank_maya_ascii(config):
    """Create a blank Maya Ascii scene based on the configuration."""

    if not os.path.exists(config.path):
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


def __save_maya_ascii(config):
    """Save the scene in Maya Ascii based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    cmds.file(rn=config.path + config.fileName)
    cmds.file(s=True, typ="mayaAscii")


def __save_maya_binary(config):
    """Save the scene in Maya Binary based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    cmds.file(rn=config.path + config.fileName)
    cmds.file(s=True, typ="mayaBinary")


def __publish_maya_ascii(config):
    """Publish the asset in Maya Ascii based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    selection = cmds.ls(sl=True)
    if not selection:
        cmds.confirmDialog(
            title="Cannot publish asset",
            message="The asset cannot be published. Please, select the objects you want to publish.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return

    cmds.file(config.path + config.fileName, es=True, typ="mayaAscii")


def __publish_maya_binary(config):
    """Publish the asset in Maya Binary based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    selection = cmds.ls(sl=True)
    if not selection:
        cmds.confirmDialog(
            title="Cannot publish asset",
            message="The asset cannot be published. Please, select the objects you want to publish.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return

    cmds.file(config.path + config.fileName, es=True, typ="mayaBinary")


def __publish_maya_geometry_cache(config):
    """Publish the asset in Maya Geometry Cache based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    selection = cmds.ls(sl=True)
    selected_shapes = cmds.listRelatives(selection, s=True)
    if not selected_shapes:
        cmds.confirmDialog(
            title="Cannot publish asset",
            message="The asset cannot be published. Please, select the geometry you want to publish.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return

    start_frame = cmds.playbackOptions(q=True, ast=True)
    end_frame = cmds.playbackOptions(q=True, aet=True)

    cmds.cacheFile(f=config.fileName, dir=config.path, pts=selected_shapes, st=start_frame, et=end_frame, r=True, ws=True, fm="OneFile", sch=True)


def __export_maya_ascii(config):
    """Export the asset in Maya Ascii based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    selection = cmds.ls(sl=True)
    if not selection:
        cmds.confirmDialog(
            title="Cannot export asset",
            message="The asset cannot be exported. Please, select the objects you want to export.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return

    cmds.file(config.path + config.fileName, es=True, typ="mayaAscii")


def __export_maya_binary(config):
    """Export the asset in Maya Binary based on the configuration."""

    if not os.path.exists(config.path):
        os.makedirs(config.path)

    selection = cmds.ls(sl=True)
    if not selection:
        cmds.confirmDialog(
            title="Cannot export asset",
            message="The asset cannot be exported. Please, select the objects you want to export.",
            button=["Ok"],
            defaultButton="Ok"
        )

        return

    cmds.file(config.path + config.fileName, es=True, typ="mayaBinary")


def __export_alembic(config):
    """Export the asset in Alembic based on the configuration."""

    pass


def __export_fbx(config):
    """Export the asset in FBX based on the configuration."""

    pass


def __export_obj(config):
    """Export the asset in OBJ based on the configuration."""

    pass


COMMANDS = []
COMMANDS.append(CConcreteCommand("open", "Explorer", __open_explorer))
COMMANDS.append(CConcreteCommand("open", "Scene", __open_scene))
COMMANDS.append(CConcreteCommand("create", "Blank Maya Ascii", __create_blank_maya_ascii))
COMMANDS.append(CConcreteCommand("save", "Maya Ascii", __save_maya_ascii))
COMMANDS.append(CConcreteCommand("save", "Maya Binary", __save_maya_binary))
COMMANDS.append(CConcreteCommand("publish", "Maya Ascii", __publish_maya_ascii))
COMMANDS.append(CConcreteCommand("publish", "Maya Binary", __publish_maya_binary))
COMMANDS.append(CConcreteCommand("publish", "Geometry Cache", __publish_maya_geometry_cache))
COMMANDS.append(CConcreteCommand("export", "Maya Ascii", __export_maya_ascii))
COMMANDS.append(CConcreteCommand("export", "Maya Binary", __export_maya_binary))
COMMANDS.append(CConcreteCommand("export", "FBX", __export_fbx))
COMMANDS.append(CConcreteCommand("export", "OBJ", __export_obj))
COMMANDS.append(CConcreteCommand("export", "Alembic", __export_alembic))


def get_commands_by_action(action):
    """Get commands by action."""

    commands_to_return = []

    for command in COMMANDS:
        if command.action == action:
            commands_to_return.append(command)

    return commands_to_return


def get_commands_by_name(name):
    """Get commands by name."""

    commands_to_return = []

    for command in COMMANDS:
        if command.name == name:
            commands_to_return.append(name)

    return commands_to_return


def get_command_names_by_action(action):
    """Get command names by action."""

    command_names_to_return = []

    for command in COMMANDS:
        if command.action == action:
            command_names_to_return.append(command.name)

    return command_names_to_return


def get_command(action, name):
    """Get the command by action and name."""

    for command in COMMANDS:
        if command.action == action and command.name == name:
            return command
