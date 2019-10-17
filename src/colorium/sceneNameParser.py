from assetData import AssetData
from namingConvention import NamingConvention

class SceneNameParser:
    namingConvention = None
    assetData = None
    
    def __init__(self):
        self.namingConvention = NamingConvention()
        self.assetData = AssetData()
    
    def parseSceneName(self, sceneName):
        self.parseTypeValueFromSceneName(sceneName)
        self.parseNameValueFromSceneName(sceneName)
        self.parseVariantValueFromSceneName(sceneName)
        self.parseSceneValueFromSceneName(sceneName)
        self.parseShotValueFromSceneName(sceneName)
        self.parseVersionValueFromSceneName(sceneName)
        
        return self.assetData
        
    def parseTypeValueFromSceneName(self, sceneName):
        type = self.namingConvention.searchTypeInSceneName(sceneName)
        
        if type != None:
            self.assetData.type = type
        
    def parseNameValueFromSceneName(self, sceneName):
        name = self.namingConvention.searchNameInSceneName(sceneName)
        
        if name != None:
            self.assetData.name = name

    def parseVariantValueFromSceneName(self, sceneName):
        variant = self.namingConvention.searchVariantInSceneName(sceneName)
        
        if variant != None:
            self.assetData.variant = int(variant)
            self.assetData.hasVariant = True
    
    def parseSceneValueFromSceneName(self, sceneName):
        scene = self.namingConvention.searchSceneInSceneName(sceneName)
        
        if scene != None:
            self.assetData.scene = int(scene)
            self.assetData.hasScene = True
    
    def parseShotValueFromSceneName(self, sceneName):
        shot = self.namingConvention.searchShotInSceneName(sceneName)
        
        if shot != None:
            self.assetData.shot = int(shot)
            self.assetData.hasShot = True
        
    def parseVersionValueFromSceneName(self, sceneName):
        version = self.namingConvention.searchVersionInSceneName(sceneName)
        
        if version != None:
            self.assetData.version = int(version.replace("v", ""))