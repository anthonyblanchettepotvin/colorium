import re as regex

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
    template = "{type}_{name}_"
    
    if assetData.hasVariant:
        template += "{variant:02d}_"
    
    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}-{shot:03d}_"
    elif assetData.hasScene:
        template += "{scene:03d}_"
    
    template += "v{version:03d}"
        
    return template.format(
        type=assetData.type.code,
        name=assetData.name,
        variant=assetData.variant,
        scene=assetData.scene,
        shot=assetData.shot,
        version=assetData.version
    ).replace("__", "_")

def generateFileNameForPublishedAsset(assetData):
    template = "{type}_{name}_"
    
    if assetData.hasVariant:
        template += "{variant:02d}_"
        
    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}-{shot:03d}_"
    elif assetData.hasScene:
        template += "{scene:03d}_"
        
    template += "publish"
        
    return template.format(
        type=assetData.type.code,
        name=assetData.name,
        variant=assetData.variant,
        scene=assetData.scene,
        shot=assetData.shot
    ).replace("__", "_")

def generateFileNameForExportedAsset(assetData):
    template = "{type}_{name}_"
    
    if assetData.hasVariant:
        template += "{variant:02d}_"
        
    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}-{shot:03d}_"
    elif assetData.hasScene:
        template += "{scene:03d}_"
        
    template += "export"

    return template.format(
        type=assetData.type.code,
        name=assetData.name,
        variant=assetData.variant,
        scene=assetData.scene,
        shot=assetData.shot
    ).replace("__", "_")

def generatePathForSavedAsset(assetData):
    template = "{saveDir}/"

    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}/{shot:03d}/"
    elif assetData.hasScene:
        template += "{scene:03d}/"
    
    template += "{name}/"
    
    if assetData.hasVariant:
        template += "{variant:02d}/"
        
    return template.format(
        saveDir=assetData.type.saveDir,
        type=assetData.type.code,
        scene=assetData.scene,
        shot=assetData.shot,
        name=assetData.name,
        variant=assetData.variant
    ).replace("//", "/")

def generatePathForPublishedAsset(assetData):
    template = "{publishDir}/"
    
    return template.format(
        publishDir=assetData.type.publishDir,
        type=assetData.type.code,
        scene=assetData.scene,
        shot=assetData.shot,
        name=assetData.name,
        variant=assetData.variant
    ).replace("//", "/")

def generatePathForExportedAsset(assetData):
    template = "{exportDir}/"

    if assetData.hasScene and assetData.hasShot:
        template += "{scene:03d}/{shot:03d}/"
    elif assetData.hasScene:
        template += "{scene:03d}/"
    
    template += "{name}/"
    
    if assetData.hasVariant:
        template += "{variant:02d}/"
    
    return template.format(
        exportDir=assetData.type.exportDir,
        type=assetData.type.code,
        scene=assetData.scene,
        shot=assetData.shot,
        name=assetData.name,
        variant=assetData.variant
    ).replace("//", "/")
