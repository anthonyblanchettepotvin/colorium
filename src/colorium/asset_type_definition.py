"""Module where all the Colorium Asset Type Definitions are centralized."""

import colorium.settings as settings


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


ASSET_TYPES = []

NONE_TYPE = CAssetTypeDefinition(
    code="non",
    name="None",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/nones",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/nones",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/nones"
)
ASSET_TYPES.append(NONE_TYPE)

MODEL_TYPE = CAssetTypeDefinition(
    code="mdl",
    name="Model",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/models",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/models",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/models"
)
ASSET_TYPES.append(MODEL_TYPE)

ANIMATION_TYPE = CAssetTypeDefinition(
    code="anm",
    name="Animation",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/animations",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/animations",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/animations"
)
ASSET_TYPES.append(ANIMATION_TYPE)

RIG_TYPE = CAssetTypeDefinition(
    code="rig",
    name="Rig",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/rigs",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/rigs",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/rigs"
)
ASSET_TYPES.append(RIG_TYPE)

LAYOUT_TYPE = CAssetTypeDefinition(
    code="lay",
    name="Layout",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/layouts",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/layouts",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/layouts"
)
ASSET_TYPES.append(LAYOUT_TYPE)

PROXY_TYPE = CAssetTypeDefinition(
    code="prx",
    name="Proxy",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/proxies",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/proxies",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/proxies"
)
ASSET_TYPES.append(PROXY_TYPE)

SIMULATION_TYPE = CAssetTypeDefinition(
    code="sim",
    name="Simulation",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/simulations",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/simulations",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/simulations"
)
ASSET_TYPES.append(SIMULATION_TYPE)

RENDER_TYPE = CAssetTypeDefinition(
    code="rnd",
    name="Render",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/renders",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/renders",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/renders"
)
ASSET_TYPES.append(RENDER_TYPE)

TEST_TYPE = CAssetTypeDefinition(
    code="tst",
    name="Test",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/tests",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/tests",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/tests"
)
ASSET_TYPES.append(TEST_TYPE)

KIT_TYPE = CAssetTypeDefinition(
    code="kit",
    name="Kit",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/kits",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/kits",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/kits"
)
ASSET_TYPES.append(KIT_TYPE)

CAMERA_TYPE = CAssetTypeDefinition(
    code="cam",
    name="Camera",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/cameras",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/cameras",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/cameras"
)
ASSET_TYPES.append(CAMERA_TYPE)

LIGHTING_TYPE = CAssetTypeDefinition(
    code="ltg",
    name="Lighting",
    save_dir=settings.ASSET_SAVE_BASE_FOLDER + "/lightings",
    publish_dir=settings.ASSET_PUBLISH_BASE_FOLDER + "/lightings",
    export_dir=settings.ASSET_EXPORT_BASE_FOLDER + "/lightings"
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
