

class AssetTypeDefinition(object):
    @property
    def code(self):
        return self._code

    @property
    def name(self):
        return self._name
        
    @property
    def saveDir(self):
        return self._saveDir

    @property
    def publishDir(self):
        return self._publishDir

    @property
    def exportDir(self):
        return self._exportDir

    def __init__(self, code="", name="", saveDir="", publishDir="", exportDir=""):
        self._code = code
        self._name = name
        self._saveDir = saveDir
        self._publishDir = publishDir
        self._exportDir = exportDir


SAVE_BASE_PATH = "Y:/project/maya_work/scenes"
PUBLISH_BASE_PATH = "Y:/project/maya_work/assets"
EXPORT_PATH = "Y:/project/exports/maya"

assetTypes = []

noneType = AssetTypeDefinition(
    code="non",
    name="None",
    saveDir=SAVE_BASE_PATH + "/nones",
    publishDir=PUBLISH_BASE_PATH + "/nones",
    exportDir=EXPORT_PATH + "/nones"
)
assetTypes.append(noneType)

modelType = AssetTypeDefinition(
    code="mdl",
    name="Model",
    saveDir=SAVE_BASE_PATH + "/models",
    publishDir=PUBLISH_BASE_PATH + "/models",
    exportDir=EXPORT_PATH + "/models"
)
assetTypes.append(modelType)

animationType = AssetTypeDefinition(
    code="anm",
    name="Animation",
    saveDir=SAVE_BASE_PATH + "/animations",
    publishDir=PUBLISH_BASE_PATH + "/animations",
    exportDir=EXPORT_PATH + "/animations"
)
assetTypes.append(animationType)

rigType = AssetTypeDefinition(
    code="rig",
    name="Rig",
    saveDir=SAVE_BASE_PATH + "/rigs",
    publishDir=PUBLISH_BASE_PATH + "/rigs",
    exportDir=EXPORT_PATH + "/rigs"
)
assetTypes.append(rigType)

layoutType = AssetTypeDefinition(
    code="lay",
    name="Layout",
    saveDir=SAVE_BASE_PATH + "/layouts",
    publishDir=PUBLISH_BASE_PATH + "/layouts",
    exportDir=EXPORT_PATH + "/layouts"
)
assetTypes.append(layoutType)

proxyType = AssetTypeDefinition(
    code="prx",
    name="Proxy",
    saveDir=SAVE_BASE_PATH + "/proxies",
    publishDir=PUBLISH_BASE_PATH + "/proxies",
    exportDir=EXPORT_PATH + "/proxies"
)
assetTypes.append(proxyType)

simulationType = AssetTypeDefinition(
    code="sim",
    name="Simulation",
    saveDir=SAVE_BASE_PATH + "/simulations",
    publishDir=PUBLISH_BASE_PATH + "/simulations",
    exportDir=EXPORT_PATH + "/simulations"
)
assetTypes.append(simulationType)

renderType = AssetTypeDefinition(
    code="rnd",
    name="Render",
    saveDir=SAVE_BASE_PATH + "/renders",
    publishDir=PUBLISH_BASE_PATH + "/renders",
    exportDir=EXPORT_PATH + "/renders"
)
assetTypes.append(renderType)

testType = AssetTypeDefinition(
    code="tst",
    name="Test",
    saveDir=SAVE_BASE_PATH + "/tests",
    publishDir=PUBLISH_BASE_PATH + "/tests",
    exportDir=EXPORT_PATH + "/tests"
)
assetTypes.append(testType)

kitType = AssetTypeDefinition(
    code="kit",
    name="Kit",
    saveDir=SAVE_BASE_PATH + "/kits",
    publishDir=PUBLISH_BASE_PATH + "/kits",
    exportDir=EXPORT_PATH + "/kits"
)
assetTypes.append(kitType)

cameraType = AssetTypeDefinition(
    code="cam",
    name="Camera",
    saveDir=SAVE_BASE_PATH + "/cameras",
    publishDir=PUBLISH_BASE_PATH + "/cameras",
    exportDir=EXPORT_PATH + "/cameras"
)
assetTypes.append(cameraType)

lightingType = AssetTypeDefinition(
    code="ltg",
    name="Lighting",
    saveDir=SAVE_BASE_PATH + "/lightings",
    publishDir=PUBLISH_BASE_PATH + "/lightings",
    exportDir=EXPORT_PATH + "/lightings"
)
assetTypes.append(lightingType)


def codes():
    codes = []

    for assetType in assetTypes:
        codes.append(assetType.code)

    return codes


def names():
    names = []

    for assetType in assetTypes:
        names.append(assetType.name)

    return names


def getTypeByName(name):
    for type in assetTypes:
        if type.name == name:
            return type

    return noneType


def getTypeByCode(code):
    for type in assetTypes:
        if type.code == code:
            return type

    return noneType
