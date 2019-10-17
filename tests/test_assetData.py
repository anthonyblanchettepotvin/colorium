import pytest
from colorium.assetData import AssetData


assetData = AssetData()

def test_typeProperties():
    assetData.type = "test"
    assert assetData.type == "test"

def test_nameProperties():
    assetData.name = "test"
    assert assetData.name == "test"

def test_hasVariantProperty():
    assetData.hasVariant = True
    assert assetData.hasVariant == True

def test_variantProperty():
    assetData.variant = 10
    assert assetData.variant == 10

def test_hasSceneProperty():
    assetData.hasScene = True
    assert assetData.hasScene == True

def test_sceneProperty():
    assetData.scene = 100
    assert assetData.scene == 100

def test_hasShotProperty():
    assetData.hasShot = True
    assert assetData.hasShot == True

def test_shotProperty():
    assetData.shot = 100
    assert assetData.shot == 100

def test_versionProperty():
    assetData.version = 10
    assert assetData.version == 10