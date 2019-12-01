"""Module used to parse a string into a Colorium Asset using the Colorium Naming Convention."""

import maya.cmds as cmds
from colorium.asset import CAsset
from colorium.naming_convention import CNamingConvention


NAMING_CONVENTION = CNamingConvention()
ASSET = CAsset()


def parse_scene_name_to_asset():
    """Parse the scene name and return an instance of an asset containing the parsed values."""

    scene_name = cmds.file(q=True, sn=True, shn=True)

    return parse_string_to_asset(scene_name)


def parse_string_to_asset(string):
    """Parse a string and return an instance of an asset containing the parsed values."""

    string.encode("ascii", "ignore")
    if string:
        parse_type_from_string(string)
        parse_name_from_string(string)
        parse_variant_from_string(string)
        parse_scene_from_string(string)
        parse_shot_from_string(string)
        parse_version_from_string(string)

    return ASSET


def parse_type_from_string(string_to_parse):
    """Parse the type out of a string and assign it to the asset."""

    asset_type = NAMING_CONVENTION.search_type_in_name(string_to_parse)

    if asset_type != None:
        ASSET.type = asset_type


def parse_name_from_string(string_to_parse):
    """Parse the name out of a string and assign it to the asset."""

    name = NAMING_CONVENTION.search_name_in_name(string_to_parse)

    if name != None:
        ASSET.name = name


def parse_variant_from_string(string_to_parse):
    """Parse the variant out of a string and assign it to the asset."""

    variant = NAMING_CONVENTION.search_variant_in_name(string_to_parse)

    if variant != None:
        ASSET.variant = int(variant)
        ASSET.has_variant = True


def parse_scene_from_string(string_to_parse):
    """Parse the scene out of a string and assign it to the asset."""

    scene = NAMING_CONVENTION.search_scene_in_name(string_to_parse)

    if scene != None:
        ASSET.scene = int(scene)
        ASSET.has_scene = True


def parse_shot_from_string(string_to_parse):
    """Parse the shot out of a string and assign it to the asset."""

    shot = NAMING_CONVENTION.search_shot_in_name(string_to_parse)

    if shot != None:
        ASSET.shot = int(shot)
        ASSET.has_shot = True


def parse_version_from_string(string_to_parse):
    """Parse the version out of a string and assign it to the asset."""

    version = NAMING_CONVENTION.seach_version_in_name(string_to_parse)

    if version != None:
        ASSET.version = int(version.replace("v", ""))
