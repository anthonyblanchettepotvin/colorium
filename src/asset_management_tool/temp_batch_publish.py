"""Temporary module used to test a potential batch publish functionnality."""

import imports

# Maya caches the imported modules, so we need to drop them to avoid weird problems.
# The kinds of problems caused by this are :
# - Changes on a module doesn't apply in next execution in Maya;
# - Things breaks when you close and reopen the tool (can't say why).
imports.dropCachedImports(
    "maya",
    "colorium",
)

import maya.cmds as cmds
import colorium.command as command
import colorium.scene_name_parser as scene_name_parser


def batch_publish_maya_ascii():
    """Publish all selected objects using Maya Ascii publish command."""

    selection = cmds.ls(sl=True)

    for element in selection:
        asset = scene_name_parser.parse_string_to_asset(element)

        cmds.select(cl=True)
        cmds.select(element, add=True)

        asset.publish_config.command = command.get_command('publish', 'Maya Ascii')
        asset.publish_config.executeCommand()
