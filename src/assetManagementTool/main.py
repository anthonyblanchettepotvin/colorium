import imports

imports.dropCachedImports(
    "ui",
    "assetManagementToolUI",
    "functools",
    "patterns",
    "colorium"
)

import ui

ui = ui.AssetManagementToolUI("Asset Management Tool", ui.AssetManagementToolController())
