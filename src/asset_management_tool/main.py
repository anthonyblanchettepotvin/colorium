"""Main module of Colorium's Asset Management Tool."""

import imports

# Maya caches the imported modules, so we need to drop them to avoid weird problems.
# The kinds of problems caused by this are :
# - Changes on a module doesn't apply in next execution in Maya;
# - Things breaks when you close and reopen the tool (can't say why).
imports.dropCachedImports(
    "asset_management_tool",
    "functools",
    "patterns",
    "colorium"
)

import asset_management_tool.ui as ui


ui.AssetManagementToolUI("Asset Management Tool", ui.AssetManagementToolController())

print "Colorium's Asset Management Tool loaded."
