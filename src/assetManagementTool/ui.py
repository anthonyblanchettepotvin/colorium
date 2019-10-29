import colorium.CUI as CUI
from patterns.observerPattern import Observer
import maya.cmds as cmds
from colorium.CAsset import CAsset
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

        type_input = CUI.CComboInput("type", frm_asset_information, True, assetTypeDefinition.names(), self.controller.set_asset_type)
        self.controller.asset.bind(type_input)
        self.add_control(type_input)
        
        name_input = CUI.CTextInput("name", frm_asset_information, True, self.controller.set_asset_name)
        self.controller.asset.bind(name_input)
        self.add_control(name_input)
        
        variant_input = CUI.CIntInput("variant", frm_asset_information, self.controller.asset.hasVariant, 1, 99, self.controller.set_asset_variant, self.controller.set_asset_hasVariant, True)
        self.controller.asset.bind(variant_input)
        self.add_control(variant_input)
        
        scene_input = CUI.CIntInput("scene", frm_asset_information, self.controller.asset.hasScene, 0, 995, self.controller.set_asset_scene, self.controller.set_asset_hasScene, True)
        self.controller.asset.bind(scene_input)
        self.add_control(scene_input)
        
        shot_input = CUI.CIntInput("shot", frm_asset_information, self.controller.asset.hasShot, 0, 995, self.controller.set_asset_shot, self.controller.set_asset_hasShot, True)
        self.controller.asset.bind(shot_input)
        self.add_control(shot_input)
        
        version_input = CUI.CIntInput("version", frm_asset_information, True, 1, 99, self.controller.set_asset_version)
        self.controller.asset.bind(version_input)
        self.add_control(version_input)


    def build_save_options_section(self):
        """
        Builds the save options section.
        """
        
        frm_save_options = cmds.frameLayout("frm_save_options", l="Save Options", p=self.main_layout, mh=5, mw=5)

        save_input = CUI.CComboInput("savet", frm_save_options, False, [], None, None, True)
        self.add_control(save_input)


    def build_publish_options_section(self):
        """
        Builds the publish options section.
        """

        frm_publish_options = cmds.frameLayout("frm_publish_options", l="Publish Options", p=self.main_layout, mh=5, mw=5)

        publish_input = CUI.CComboInput("publisht", frm_publish_options, False, [], None, None, True)
        self.add_control(publish_input)


    def build_export_options_section(self):
        """
        Builds the export options section.
        """

        frm_export_options = cmds.frameLayout("frm_export_options", l="Export Options", p=self.main_layout, mh=5, mw=5)

        export_input = CUI.CComboInput("exportt", frm_export_options, False, [], None, None, True)
        self.add_control(export_input)

    
    def build_file_name_preview_section(self):
        """
        Builds the file name preview section.
        """

        frm_file_name_preview = cmds.frameLayout("frm_file_name_preview", l="File Name Preview", p=self.main_layout, mh=5, mw=5)

        save_file_name_input = CUI.CTextInput("savefn", frm_file_name_preview, False, None, None, True)
        self.add_control(save_file_name_input)

        publish_file_name_input = CUI.CTextInput("publishfn", frm_file_name_preview, False, None, None, True)
        self.add_control(publish_file_name_input)

        export_file_name_input = CUI.CTextInput("exportfn", frm_file_name_preview, False, None, None, True)
        self.add_control(export_file_name_input)
    
    
    def build_path_preview_section(self):
        """
        Builds the path preview section.
        """

        frm_path_preview = cmds.frameLayout("frm_path_preview", l="Path Preview", p=self.main_layout, mh=5, mw=5)

        save_path_input = CUI.CFilePathInput("savep", frm_path_preview, False, None, None, True)
        self.add_control(save_path_input)

        publish_path_input = CUI.CFilePathInput("publishp", frm_path_preview, False, None, None, True)
        self.add_control(publish_path_input)

        export_path_input = CUI.CFilePathInput("exportp", frm_path_preview, False, None, None, True)
        self.add_control(export_path_input)
    
    
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
        
        self._asset = CAsset()


    def display_ui_callback(self):
        NotImplemented


    def set_asset_type(self, value):
        self.asset.type = value
        print self.asset.type


    def set_asset_hasType(self, value):
        self.asset.hasType = value
        print self.asset.hasType


    def set_asset_name(self, value):
        self.asset.name = value
        print self.asset.name


    def set_asset_hasName(self, value):
        self.asset.hasName = value
        print self.asset.hasName


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
        self.asset.hasVersion = value
        print self.asset.hasVersion
