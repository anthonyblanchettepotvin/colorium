import imports

imports.dropCachedImports(
    "colorium"
)

import maya.cmds as cmds
import colorium.publish as publish
import colorium.CAsset as CAsset
import colorium.CSceneNameParser as CSceneNameParser

selection = cmds.ls(sl=True)

for element in selection:
    asset = CSceneNameParser.parseStringToAssetData(element)

    cmds.select(cl=True)
    cmds.select(element, add=True)

    asset.publish_config.command = publish.getCommandByName("MA")
    asset.publish_config.executeCommand()