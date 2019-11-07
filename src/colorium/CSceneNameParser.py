from CAsset import CAsset
from namingConvention import NamingConvention
import assetTypeDefinition
import maya.cmds as cmds


_namingConvention = NamingConvention()
_assetData = CAsset()


def parseSceneName():
    sceneName = cmds.file(q=True, sn=True, shn=True)
    if sceneName:
        parseTypeValueFromSceneName(sceneName)
        parseNameValueFromSceneName(sceneName)
        parseVariantValueFromSceneName(sceneName)
        parseSceneValueFromSceneName(sceneName)
        parseShotValueFromSceneName(sceneName)
        parseVersionValueFromSceneName(sceneName)
    
    return _assetData
    

def parseTypeValueFromSceneName(sceneName):
    type = _namingConvention.searchTypeInSceneName(sceneName)
    
    if type != None:
        for assetType in assetTypeDefinition.assetTypes:
                if assetType.code == type:
                    _assetData.type = assetType


def parseNameValueFromSceneName(sceneName):
    name = _namingConvention.searchNameInSceneName(sceneName)
    
    if name != None:
        _assetData.name = name


def parseVariantValueFromSceneName(sceneName):
    variant = _namingConvention.searchVariantInSceneName(sceneName)
    
    if variant != None:
        _assetData.variant = int(variant)
        _assetData.hasVariant = True


def parseSceneValueFromSceneName(sceneName):
    scene = _namingConvention.searchSceneInSceneName(sceneName)
    
    if scene != None:
        _assetData.scene = int(scene)
        _assetData.hasScene = True


def parseShotValueFromSceneName(sceneName):
    shot = _namingConvention.searchShotInSceneName(sceneName)
    
    if shot != None:
        _assetData.shot = int(shot)
        _assetData.hasShot = True
    

def parseVersionValueFromSceneName(sceneName):
    version = _namingConvention.searchVersionInSceneName(sceneName)
    
    if version != None:
        _assetData.version = int(version.replace("v", ""))
