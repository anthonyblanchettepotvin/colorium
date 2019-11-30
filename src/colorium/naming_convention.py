"""Module used to validates the name of a file based on Colorium's naming convention."""

import re as regex
import colorium.asset_type_definition as asset_type_definition


class CNamingConvention:
    """Validates the name of a file based on a naming convention's rules."""

    variant_pattern = r"(?<=_)\d{2}(?=_)"
    scene_pattern = r"(?<=_)\d{3}(?=-)"
    shot_pattern = r"(?<=-)\d{3}(?=_)"
    version_pattern = r"(?<=_)v\d{3}(?=.)"


    def __init__(self, variant_pattern="", scene_pattern="", shot_pattern="", version_pattern=""):
        if variant_pattern != "":
            self.variant_pattern = variant_pattern

        if scene_pattern != "":
            self.scene_pattern = scene_pattern

        if shot_pattern != "":
            self.shot_pattern = shot_pattern

        if version_pattern != "":
            self.version_pattern = version_pattern


    def search_type_in_name(self, name):
        """Search the name for the type variable."""

        name = name.split("_", 2)

        if name[0] != None:
            return name[0]

        return None


    def search_name_in_name(self, name):
        """Search the name for the name variable."""

        name = name.split("_", 2)

        if name[1] != None:
            return name[1]

        return None


    def search_variant_in_name(self, name):
        """Search the name for the variant variable."""

        result = regex.search(self.variant_pattern, name)

        if result != None:
            return result.group()

        return None


    def seach_version_in_name(self, name):
        """Search the name for the version variable."""

        result = regex.search(self.version_pattern, name)

        if result != None:
            return result.group()

        return None


    def search_scene_in_name(self, name):
        """Search the name for the scene variable."""

        result = regex.search(self.scene_pattern, name)

        if result != None:
            return result.group()

        return None


    def search_shot_in_name(self, name):
        """Search the name for the shot variable."""

        result = regex.search(self.shot_pattern, name)

        if result != None:
            return result.group()

        return None


def generate_file_name_for_saved_asset(asset_data):
    """Generate the file name of an asset that's going to be saved."""

    asset_type = asset_type_definition.get_type_by_code(asset_data.type)

    if asset_type == asset_type_definition.NONE_TYPE:
        asset_type = asset_type_definition.get_type_by_name(asset_data.type)

    template = "{type}_{name}_"

    if asset_data.has_variant:
        template += "{variant:02d}_"

    if asset_data.has_scene and asset_data.has_shot:
        template += "{scene:03d}-{shot:03d}_"
    elif asset_data.has_scene:
        template += "{scene:03d}_"

    template += "v{version:03d}"

    return template.format(
        type=asset_type.code,
        name=asset_data.name,
        variant=asset_data.variant,
        scene=asset_data.scene,
        shot=asset_data.shot,
        version=asset_data.version
    ).replace("__", "_")


def generate_file_name_for_published_asset(asset_data):
    """Generate the file name of an asset that's going to be published."""

    asset_type = asset_type_definition.get_type_by_code(asset_data.type)

    if asset_type == asset_type_definition.NONE_TYPE:
        asset_type = asset_type_definition.get_type_by_name(asset_data.type)

    template = "{type}_{name}_"

    if asset_data.has_variant:
        template += "{variant:02d}_"

    if asset_data.has_scene and asset_data.has_shot:
        template += "{scene:03d}-{shot:03d}_"
    elif asset_data.has_scene:
        template += "{scene:03d}_"

    template += "publish"

    return template.format(
        type=asset_type.code,
        name=asset_data.name,
        variant=asset_data.variant,
        scene=asset_data.scene,
        shot=asset_data.shot
    ).replace("__", "_")


def generate_file_name_for_exported_asset(asset_data):
    """Generate the file name of an asset that's going to be exported."""

    asset_type = asset_type_definition.get_type_by_code(asset_data.type)

    if asset_type == asset_type_definition.NONE_TYPE:
        asset_type = asset_type_definition.get_type_by_name(asset_data.type)

    template = "{type}_{name}_"

    if asset_data.has_variant:
        template += "{variant:02d}_"

    if asset_data.has_scene and asset_data.has_shot:
        template += "{scene:03d}-{shot:03d}_"
    elif asset_data.has_scene:
        template += "{scene:03d}_"

    template += "export"

    return template.format(
        type=asset_type.code,
        name=asset_data.name,
        variant=asset_data.variant,
        scene=asset_data.scene,
        shot=asset_data.shot
    ).replace("__", "_")


def generate_path_for_saved_asset(asset_data):
    """Generate the file path of an asset that's going to be saved."""

    asset_type = asset_type_definition.get_type_by_code(asset_data.type)

    if asset_type == asset_type_definition.NONE_TYPE:
        asset_type = asset_type_definition.get_type_by_name(asset_data.type)

    template = "{saveDir}/"

    if asset_data.has_scene and asset_data.has_shot:
        template += "{scene:03d}/{shot:03d}/"
    elif asset_data.has_scene:
        template += "{scene:03d}/"

    template += "{name}/"

    if asset_data.has_variant:
        template += "{variant:02d}/"

    return template.format(
        saveDir=asset_type.save_dir,
        type=asset_type.code,
        scene=asset_data.scene,
        shot=asset_data.shot,
        name=asset_data.name,
        variant=asset_data.variant
    ).replace("//", "/")


def generate_path_for_published_asset(asset_data):
    """Generate the file path of an asset that's going to be published."""

    asset_type = asset_type_definition.get_type_by_code(asset_data.type)

    if asset_type == asset_type_definition.NONE_TYPE:
        asset_type = asset_type_definition.get_type_by_name(asset_data.type)

    template = "{publishDir}/"

    return template.format(
        publishDir=asset_type.publish_dir,
        type=asset_type.code,
        scene=asset_data.scene,
        shot=asset_data.shot,
        name=asset_data.name,
        variant=asset_data.variant
    ).replace("//", "/")


def generate_path_for_exported_asset(asset_data):
    """Generate the file path of an asset that's going to be exported."""

    asset_type = asset_type_definition.get_type_by_code(asset_data.type)

    if asset_type == asset_type_definition.NONE_TYPE:
        asset_type = asset_type_definition.get_type_by_name(asset_data.type)

    template = "{exportDir}/"

    if asset_data.has_scene and asset_data.has_shot:
        template += "{scene:03d}/{shot:03d}/"
    elif asset_data.has_scene:
        template += "{scene:03d}/"

    template += "{name}/"

    if asset_data.has_variant:
        template += "{variant:02d}/"

    return template.format(
        exportDir=asset_type.export_dir,
        type=asset_type.code,
        scene=asset_data.scene,
        shot=asset_data.shot,
        name=asset_data.name,
        variant=asset_data.variant
    ).replace("//", "/")
