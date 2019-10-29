import colorium.CUI as CUI
import maya.cmds as cmds
from colorium.assetData import AssetData
import colorium.assetTypeDefinition as assetTypeDefinition


class AssetManagementToolUI(CUI.CUI):
    def build_ui(self):
        self.build_asset_information_section()
        self.build_save_options_section()
        self.build_publish_options_section()
        self.build_export_options_section()
        self.build_file_name_preview_section()
        self.build_path_preview_section()
        self.build_actions_section()


    def build_asset_information_section(self):
        """
        Builds the asset information section.
        """

        frm_asset_information = cmds.frameLayout("frm_asset_information", l="Asset Information", p=self.main_layout, mh=5, mw=5)

        CUI.CComboInput("type", frm_asset_information, True, assetTypeDefinition.names(), self.controller.set_asset_type, self.controller.set_asset_hasType, True)
        CUI.CTextInput("name", frm_asset_information, True, self.controller.set_asset_name, self.controller.set_asset_hasName, True)
        CUI.CIntInput("variant", frm_asset_information, self.controller.asset.hasVariant, 1, 99, self.controller.set_asset_variant, self.controller.set_asset_hasVariant, True)
        CUI.CIntInput("scene", frm_asset_information, self.controller.asset.hasScene, 0, 995, self.controller.set_asset_scene, self.controller.set_asset_hasScene, True)
        CUI.CIntInput("shot", frm_asset_information, self.controller.asset.hasShot, 0, 995, self.controller.set_asset_shot, self.controller.set_asset_hasShot, True)
        CUI.CIntInput("version", frm_asset_information, True, 1, 99, self.controller.set_asset_version, self.controller.set_asset_hasVersion, True)
        

    def build_save_options_section(self):
        """
        Builds the save options section.
        """

        frm_save_options = cmds.frameLayout("frm_save_options", l="Save Options", p=self.main_layout, mh=5, mw=5)


    def build_publish_options_section(self):
        """
        Builds the publish options section.
        """

        frm_publish_options = cmds.frameLayout("frm_publish_options", l="Publish Options", p=self.main_layout, mh=5, mw=5)


    def build_export_options_section(self):
        """
        Builds the export options section.
        """

        frm_export_options = cmds.frameLayout("frm_export_options", l="Export Options", p=self.main_layout, mh=5, mw=5)

    
    def build_file_name_preview_section(self):
        """
        Builds the file name preview section.
        """

        frm_file_name_preview = cmds.frameLayout("frm_file_name_preview", l="File Name Preview", p=self.main_layout, mh=5, mw=5)

    
    def build_path_preview_section(self):
        """
        Builds the path preview section.
        """

        frm_path_preview = cmds.frameLayout("frm_path_preview", l="Path Preview", p=self.main_layout, mh=5, mw=5)
    
    
    def build_actions_section(self):
        """
        Builds the actions section.
        """

        frm_actions = cmds.frameLayout("frm_actions", l="Actions", p=self.main_layout, mh=5, mw=5)
        

class AssetManagementToolController(CUI.CController):
    @property
    def asset(self):
        return self._asset


    @asset.setter
    def asset(self, value):
        self._asset = value


    def __init__(self):
        super(AssetManagementToolController, self).__init__()
        
        self._asset = AssetData()


    def display_ui_callback(self):
        print "UI displayed !"


    def set_asset_type(self, value):
        self.asset.type = value
        print self.asset.type


    def set_asset_hasType(self, value):
        # self.asset.hasType = value
        # print self.asset.hasType
        pass


    def set_asset_name(self, value):
        self.asset.name = value
        print self.asset.name


    def set_asset_hasName(self, value):
        # self.asset.hasName = value
        # print self.asset.hasName
        pass


    def set_asset_variant(self, value):
        self.asset.variant = value
        print self.asset.variant


    def set_asset_hasVariant(self, value):
        self.asset.hasVariant = value
        print self.asset.hasVariant


    def set_asset_scene(self, value):
        self.asset.scene = value
        print self.asset.scene


    def set_asset_hasScene(self, value):
        self.asset.hasScene = value
        print self.asset.hasScene


    def set_asset_shot(self, value):
        self.asset.shot = value
        print self.asset.shot


    def set_asset_hasShot(self, value):
        self.asset.hasShot = value
        print self.asset.hasShot


    def set_asset_version(self, value):
        self.asset.version = value
        print self.asset.version


    def set_asset_hasVersion(self, value):
        # self.asset.hasVersion = value
        # print self.asset.hasVersion
        pass
