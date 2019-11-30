"""Module where all the Colorium Asset Type Definitions are centralized."""

class CAssetTypeDefinition(object):
    """Defines important variables of an asset's naming convention and its various save/export locations."""

    @property
    def code(self):
        """The code of the type."""

        return self._code


    @property
    def name(self):
        """The display name of the type."""

        return self._name


    @property
    def save_dir(self):
        """The save directory specific to the type."""

        return self._save_dir


    @property
    def publish_dir(self):
        """The publish directory specific to the type."""

        return self._publish_dir


    @property
    def export_dir(self):
        """The export directory specific to the type."""

        return self._export_dir


    def __init__(self, code="", name="", save_dir="", publish_dir="", export_dir=""):
        self._code = code
        self._name = name
        self._save_dir = save_dir
        self._publish_dir = publish_dir
        self._export_dir = export_dir


SAVE_BASE_PATH = "Y:/project/maya_work/scenes"
PUBLISH_BASE_PATH = "Y:/project/maya_work/assets"
EXPORT_PATH = "Y:/project/exports/maya"

ASSET_TYPES = []

NONE_TYPE = CAssetTypeDefinition(
    code="non",
    name="None",
    save_dir=SAVE_BASE_PATH + "/nones",
    publish_dir=PUBLISH_BASE_PATH + "/nones",
    export_dir=EXPORT_PATH + "/nones"
)
ASSET_TYPES.append(NONE_TYPE)

MODEL_TYPE = CAssetTypeDefinition(
    code="mdl",
    name="Model",
    save_dir=SAVE_BASE_PATH + "/models",
    publish_dir=PUBLISH_BASE_PATH + "/models",
    export_dir=EXPORT_PATH + "/models"
)
ASSET_TYPES.append(MODEL_TYPE)

ANIMATION_TYPE = CAssetTypeDefinition(
    code="anm",
    name="Animation",
    save_dir=SAVE_BASE_PATH + "/animations",
    publish_dir=PUBLISH_BASE_PATH + "/animations",
    export_dir=EXPORT_PATH + "/animations"
)
ASSET_TYPES.append(ANIMATION_TYPE)

RIG_TYPE = CAssetTypeDefinition(
    code="rig",
    name="Rig",
    save_dir=SAVE_BASE_PATH + "/rigs",
    publish_dir=PUBLISH_BASE_PATH + "/rigs",
    export_dir=EXPORT_PATH + "/rigs"
)
ASSET_TYPES.append(RIG_TYPE)

LAYOUT_TYPE = CAssetTypeDefinition(
    code="lay",
    name="Layout",
    save_dir=SAVE_BASE_PATH + "/layouts",
    publish_dir=PUBLISH_BASE_PATH + "/layouts",
    export_dir=EXPORT_PATH + "/layouts"
)
ASSET_TYPES.append(LAYOUT_TYPE)

PROXY_TYPE = CAssetTypeDefinition(
    code="prx",
    name="Proxy",
    save_dir=SAVE_BASE_PATH + "/proxies",
    publish_dir=PUBLISH_BASE_PATH + "/proxies",
    export_dir=EXPORT_PATH + "/proxies"
)
ASSET_TYPES.append(PROXY_TYPE)

SIMULATION_TYPE = CAssetTypeDefinition(
    code="sim",
    name="Simulation",
    save_dir=SAVE_BASE_PATH + "/simulations",
    publish_dir=PUBLISH_BASE_PATH + "/simulations",
    export_dir=EXPORT_PATH + "/simulations"
)
ASSET_TYPES.append(SIMULATION_TYPE)

RENDER_TYPE = CAssetTypeDefinition(
    code="rnd",
    name="Render",
    save_dir=SAVE_BASE_PATH + "/renders",
    publish_dir=PUBLISH_BASE_PATH + "/renders",
    export_dir=EXPORT_PATH + "/renders"
)
ASSET_TYPES.append(RENDER_TYPE)

TEST_TYPE = CAssetTypeDefinition(
    code="tst",
    name="Test",
    save_dir=SAVE_BASE_PATH + "/tests",
    publish_dir=PUBLISH_BASE_PATH + "/tests",
    export_dir=EXPORT_PATH + "/tests"
)
ASSET_TYPES.append(TEST_TYPE)

KIT_TYPE = CAssetTypeDefinition(
    code="kit",
    name="Kit",
    save_dir=SAVE_BASE_PATH + "/kits",
    publish_dir=PUBLISH_BASE_PATH + "/kits",
    export_dir=EXPORT_PATH + "/kits"
)
ASSET_TYPES.append(KIT_TYPE)

CAMERA_TYPE = CAssetTypeDefinition(
    code="cam",
    name="Camera",
    save_dir=SAVE_BASE_PATH + "/cameras",
    publish_dir=PUBLISH_BASE_PATH + "/cameras",
    export_dir=EXPORT_PATH + "/cameras"
)
ASSET_TYPES.append(CAMERA_TYPE)

LIGHTING_TYPE = CAssetTypeDefinition(
    code="ltg",
    name="Lighting",
    save_dir=SAVE_BASE_PATH + "/lightings",
    publish_dir=PUBLISH_BASE_PATH + "/lightings",
    export_dir=EXPORT_PATH + "/lightings"
)
ASSET_TYPES.append(LIGHTING_TYPE)


def codes():
    """Return a list of every asset type's code from the list of asset type definitions."""

    result = []

    for asset_type in ASSET_TYPES:
        result.append(asset_type.code)

    return result


def names():
    """Return a list of every asset type's name from the list of asset type definitions."""

    result = []

    for asset_type in ASSET_TYPES:
        result.append(asset_type.name)

    return result


def get_type_by_name(name):
    """Return an asset type definition by name."""

    for asset_type in ASSET_TYPES:
        if asset_type.name == name:
            return asset_type

    return NONE_TYPE


def get_type_by_code(code):
    """Return an asset type definition by code."""

    for asset_type in ASSET_TYPES:
        if asset_type.code == code:
            return asset_type

    return NONE_TYPE
