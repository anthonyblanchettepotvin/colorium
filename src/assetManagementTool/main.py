import imports

imports.dropCachedImports(
    "ui",
    "assetManagementToolUI",
    "functools",
    "patterns",
    "colorium"
)

# from assetManagementToolUI import ColoriumAssetManagementToolUI as UI

# ui = UI()

import ui

ui = ui.AssetManagementToolUI("Asset Management Tool", ui.AssetManagementToolController())
