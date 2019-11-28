import re as regex
import colorium.assetTypeDefinition as assetTypeDefinition


class NamingConvention:
    variantPattern = r"(?<=_)\d{2}(?=_)"
    scenePattern = r"(?<=_)\d{3}(?=-)"
    shotPattern = r"(?<=-)\d{3}(?=_)"
    versionPattern = r"(?<=_)v\d{3}(?=.)"
        
    def __init__(self, variantPattern="", scenePattern="", shotPattern="", versionPattern=""):
        if variantPattern != "":
            self.variantPattern = variantPattern
            
        if scenePattern != "":
            self.scenePattern = scenePattern
            
        if shotPattern != "":
            self.shotPattern = shotPattern
            
        if versionPattern != "":
            self.versionPattern = versionPattern
    
    def searchTypeInSceneName(self, sceneName):
        sceneName = sceneName.split("_", 2)
        
        if sceneName[0] != None:
            return sceneName[0]
        else:
            return None
    
    def searchNameInSceneName(self, sceneName):
        sceneName = sceneName.split("_", 2)
        
        if sceneName[1] != None:
            return sceneName[1]
        else:
            return None
    
    def searchVariantInSceneName(self, sceneName):
        result = regex.search(self.variantPattern, sceneName)
        
        if result != None:
            return result.group()
        else:
            return None

    def searchVersionInSceneName(self, sceneName):
        result = regex.search(self.versionPattern, sceneName)
        
        if result != None:
            return result.group()
        else:
            return None
        
    def searchSceneInSceneName(self, sceneName):
        result = regex.search(self.scenePattern, sceneName)
        
        if result != None:
            return result.group()
        else:
            return None
            
    def searchShotInSceneName(self, sceneName):
        result = regex.search(self.shotPattern, sceneName)
        
        if result != None:
            return result.group()
        else:
            return None

def generateFileNameForSavedAsset(assetData):
    asset_type_definition = assetTypeDefinition.getTypeByCode(assetData.type)

    if asset_type_definition == assetTypeDefinition.noneType:
        asset_type_definition = assetTypeDefinition.getTypeByName(assetData.type)

    template = "{type}_{name}_"
    
    if assetData.hasVariant:
        template += "{variant:02d}_"
    
    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}-{shot:03d}_"
    elif assetData.hasScene:
        template += "{scene:03d}_"
    
    template += "v{version:03d}"
        
    return template.format(
        type=asset_type_definition.code,
        name=assetData.name,
        variant=assetData.variant,
        scene=assetData.scene,
        shot=assetData.shot,
        version=assetData.version
    ).replace("__", "_")

def generateFileNameForPublishedAsset(assetData):
    asset_type_definition = assetTypeDefinition.getTypeByCode(assetData.type)

    if asset_type_definition == assetTypeDefinition.noneType:
        asset_type_definition = assetTypeDefinition.getTypeByName(assetData.type)

    template = "{type}_{name}_"
    
    if assetData.hasVariant:
        template += "{variant:02d}_"
        
    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}-{shot:03d}_"
    elif assetData.hasScene:
        template += "{scene:03d}_"
        
    template += "publish"
        
    return template.format(
        type=asset_type_definition.code,
        name=assetData.name,
        variant=assetData.variant,
        scene=assetData.scene,
        shot=assetData.shot
    ).replace("__", "_")

def generateFileNameForExportedAsset(assetData):
    asset_type_definition = assetTypeDefinition.getTypeByCode(assetData.type)

    if asset_type_definition == assetTypeDefinition.noneType:
        asset_type_definition = assetTypeDefinition.getTypeByName(assetData.type)

    template = "{type}_{name}_"
    
    if assetData.hasVariant:
        template += "{variant:02d}_"
        
    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}-{shot:03d}_"
    elif assetData.hasScene:
        template += "{scene:03d}_"
        
    template += "export"

    return template.format(
        type=asset_type_definition.code,
        name=assetData.name,
        variant=assetData.variant,
        scene=assetData.scene,
        shot=assetData.shot
    ).replace("__", "_")

def generatePathForSavedAsset(assetData):
    asset_type_definition = assetTypeDefinition.getTypeByCode(assetData.type)

    if asset_type_definition == assetTypeDefinition.noneType:
        asset_type_definition = assetTypeDefinition.getTypeByName(assetData.type)

    template = "{saveDir}/"

    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}/{shot:03d}/"
    elif assetData.hasScene:
        template += "{scene:03d}/"
    
    template += "{name}/"
    
    if assetData.hasVariant:
        template += "{variant:02d}/"
        
    return template.format(
        saveDir=asset_type_definition.saveDir,
        type=asset_type_definition.code,
        scene=assetData.scene,
        shot=assetData.shot,
        name=assetData.name,
        variant=assetData.variant
    ).replace("//", "/")

def generatePathForPublishedAsset(assetData):
    asset_type_definition = assetTypeDefinition.getTypeByCode(assetData.type)

    if asset_type_definition == assetTypeDefinition.noneType:
        asset_type_definition = assetTypeDefinition.getTypeByName(assetData.type)

    template = "{publishDir}/"
    
    return template.format(
        publishDir=asset_type_definition.publishDir,
        type=asset_type_definition.code,
        scene=assetData.scene,
        shot=assetData.shot,
        name=assetData.name,
        variant=assetData.variant
    ).replace("//", "/")

def generatePathForExportedAsset(assetData):
    asset_type_definition = assetTypeDefinition.getTypeByCode(assetData.type)

    if asset_type_definition == assetTypeDefinition.noneType:
        asset_type_definition = assetTypeDefinition.getTypeByName(assetData.type)

    template = "{exportDir}/"

    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}/{shot:03d}/"
    elif assetData.hasScene:
        template += "{scene:03d}/"
    
    template += "{name}/"
    
    if assetData.hasVariant:
        template += "{variant:02d}/"
    
    return template.format(
        exportDir=asset_type_definition.exportDir,
        type=asset_type_definition.code,
        scene=assetData.scene,
        shot=assetData.shot,
        name=assetData.name,
        variant=assetData.variant
    ).replace("//", "/")
