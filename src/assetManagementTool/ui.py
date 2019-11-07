import colorium.CUI as CUI
import maya.cmds as cmds
from colorium.CAsset import CAsset
import colorium.assetTypeDefinition as assetTypeDefinition
import colorium.CSceneNameParser as CSceneNameParser


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

        type_input = CUI.CComboInput("type", "Asset's type", frm_asset_information,\
            enabled=True,\
            items=assetTypeDefinition.names(),\
            changed_command=self.controller.set_asset_type,\
            default_value=self.controller.asset.type.name,\
        )
        self.controller.asset.bind(type_input)
        self.add_control(type_input)
        
        name_input = CUI.CTextInput("name", "Asset's name", frm_asset_information,\
            enabled=True,\
            changed_command=self.controller.set_asset_name,\
            default_value=self.controller.asset.name,\
        )
        self.controller.asset.bind(name_input)
        self.add_control(name_input)
        
        variant_input = CUI.CIntInput("variant", "Asset's variant", frm_asset_information,\
            enabled=self.controller.asset.hasVariant,\
            min=1,\
            max=99,\
            changed_command=self.controller.set_asset_variant,\
            toggle=True,\
            toggle_command=self.controller.set_asset_hasVariant,\
            default_value=self.controller.asset.variant,\
        )
        self.controller.asset.bind(variant_input)
        self.add_control(variant_input)
        
        scene_input = CUI.CIntInput("scene", "Asset's scene", frm_asset_information,\
            enabled=self.controller.asset.hasScene,\
            min=0,\
            max=995,\
            changed_command=self.controller.set_asset_scene,\
            toggle=True,\
            toggle_command=self.controller.set_asset_hasScene,\
            default_value=self.controller.asset.scene,\
        )
        self.controller.asset.bind(scene_input)
        self.add_control(scene_input)
        
        shot_input = CUI.CIntInput("shot", "Asset's shot", frm_asset_information,\
            enabled=self.controller.asset.hasShot,\
            min=0,\
            max=995,\
            changed_command=self.controller.set_asset_shot,\
            toggle=True,\
            toggle_command=self.controller.set_asset_hasShot,\
            default_value=self.controller.asset.shot,\
        )
        self.controller.asset.bind(shot_input)
        self.add_control(shot_input)
        
        version_input = CUI.CIntInput("version", "Asset's version", frm_asset_information,\
            enabled=True,\
            min=1,\
            max=99,\
            changed_command=self.controller.set_asset_version,\
            default_value=self.controller.asset.version,\
        )
        self.controller.asset.bind(version_input)
        self.add_control(version_input)


    def build_save_options_section(self):
        """
        Builds the save options section.
        """
        
        frm_save_options = cmds.frameLayout("frm_save_options", l="Save Options", p=self.main_layout, mh=5, mw=5, cll=True)

        save_input = CUI.CComboInput("save_type", "Save type", frm_save_options,\
            enabled=False,\
            items=[],\
            toggle=True,\
        )
        self.add_control(save_input)


    def build_publish_options_section(self):
        """
        Builds the publish options section.
        """

        frm_publish_options = cmds.frameLayout("frm_publish_options", l="Publish Options", p=self.main_layout, mh=5, mw=5, cll=True)

        publish_input = CUI.CComboInput("publish_type", "Publish type", frm_publish_options,\
            enabled=False,\
            items=[],\
            toggle=True,\
        )
        self.add_control(publish_input)


    def build_export_options_section(self):
        """
        Builds the export options section.
        """

        frm_export_options = cmds.frameLayout("frm_export_options", l="Export Options", p=self.main_layout, mh=5, mw=5, cll=True)

        export_input = CUI.CComboInput("export_type", "Export type", frm_export_options,\
            enabled=False,\
            items=[],\
            toggle=True,\
        )
        self.add_control(export_input)

    
    def build_file_name_preview_section(self):
        """
        Builds the file name preview section.
        """

        frm_file_name_preview = cmds.frameLayout("frm_file_name_preview", l="File Name Preview", p=self.main_layout, mh=5, mw=5, cll=True)

        save_file_name_input = CUI.CTextInput("save_file_name", "Save file name", frm_file_name_preview,\
            enabled=False,\
            toggle=True,\
            toggle_command=self.controller.set_save_config_file_name_override,\
            default_value=self.controller.asset.save_config.fileName,\
        )
        self.controller.asset.save_config.bind(save_file_name_input)
        self.add_control(save_file_name_input)

        publish_file_name_input = CUI.CTextInput("publish_file_name", "Publish file name", frm_file_name_preview,\
            enabled=False,\
            toggle=True,\
            toggle_command=self.controller.set_publish_config_file_name_override,\
            default_value=self.controller.asset.publish_config.fileName,\
        )
        self.controller.asset.publish_config.bind(publish_file_name_input)
        self.add_control(publish_file_name_input)

        export_file_name_input = CUI.CTextInput("export_file_name", "Export file name", frm_file_name_preview,\
            enabled=False,\
            toggle=True,\
            toggle_command=self.controller.set_export_config_file_name_override,\
            default_value=self.controller.asset.export_config.fileName,\
        )
        self.controller.asset.export_config.bind(export_file_name_input)
        self.add_control(export_file_name_input)
    
    
    def build_path_preview_section(self):
        """
        Builds the path preview section.
        """

        frm_path_preview = cmds.frameLayout("frm_path_preview", l="Path Preview", p=self.main_layout, mh=5, mw=5, cll=True)

        save_path_input = CUI.CFilePathInput("save_path", "Save path", frm_path_preview,\
            enabled=False,\
            toggle=True,\
            toggle_command=self.controller.set_save_config_path_override,\
            default_value=self.controller.asset.save_config.path,\
        )
        self.controller.asset.save_config.bind(save_path_input)
        self.add_control(save_path_input)

        publish_path_input = CUI.CFilePathInput("publish_path", "Publish path", frm_path_preview,\
            enabled=False,\
            toggle=True,\
            toggle_command=self.controller.set_publish_config_path_override,\
            default_value=self.controller.asset.publish_config.path,\
        )
        self.controller.asset.publish_config.bind(publish_path_input)
        self.add_control(publish_path_input)

        export_path_input = CUI.CFilePathInput("export_path", "Export path", frm_path_preview,\
            enabled=False,\
            toggle=True,\
            toggle_command=self.controller.set_export_config_path_override,\
            default_value=self.controller.asset.export_config.path,\
        )
        self.controller.asset.export_config.bind(export_path_input)
        self.add_control(export_path_input)
    
    
    def build_actions_section(self):
        """
        Builds the actions section.
        """

        frm_actions = cmds.frameLayout("frm_actions", l="Actions", p=self.main_layout, mh=5, mw=5)

        lay_actions = CUI.CInlineLayout("actions", "Actions", frm_actions, [], "right")
        
        cancel_button = CUI.CButtonControl("cancel", "Cancel", lay_actions._name, self.controller.cancel)
        lay_actions.add_children(cancel_button)

        open_button = CUI.CButtonControl("open", "Open", lay_actions._name, self.controller.open)
        lay_actions.add_children(open_button)

        create_button = CUI.CButtonControl("create", "Create", lay_actions._name, self.controller.create)
        lay_actions.add_children(create_button)

        delete_button = CUI.CButtonControl("delete", "Delete", lay_actions._name, self.controller.delete)
        lay_actions.add_children(delete_button)

        commit_button = CUI.CButtonControl("commit", "Commit", lay_actions._name, self.controller.commit)
        lay_actions.add_children(commit_button)

        self.add_control(lay_actions)


class AssetManagementToolController(CUI.CController):
    @property
    def asset(self):
        return self._asset


    @asset.setter
    def asset(self, value):
        self._asset = value


    def __init__(self):
        super(AssetManagementToolController, self).__init__()

        self._asset = CSceneNameParser.parseSceneName()


    def display_ui_callback(self):
        NotImplemented


    def cancel(self, value):
        print("Cancel")

    
    def open(self, value):
        print("Open")


    def create(self, value):
        print("Create")


    def delete(self, value):
        print("Delete")


    def commit(self, value):
        print("Commit")


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


    def set_save_config_file_name_override(self, value):
        self.asset.save_config.fileNameOverridden = value
        print self.asset.save_config.fileNameOverridden

    
    def set_publish_config_file_name_override(self, value):
        self.asset.publish_config.fileNameOverridden = value
        print self.asset.publish_config.fileNameOverridden

    
    def set_export_config_file_name_override(self, value):
        self.asset.export_config.fileNameOverridden = value
        print self.asset.export_config.fileNameOverridden


    def set_save_config_path_override(self, value):
        self.asset.save_config.pathOverridden = value
        print self.asset.save_config.pathOverridden

    
    def set_publish_config_path_override(self, value):
        self.asset.publish_config.pathOverridden = value
        print self.asset.publish_config.pathOverridden

    
    def set_export_config_path_override(self, value):
        self.asset.export_config.pathOverridden = value
        print self.asset.export_config.pathOverridden
