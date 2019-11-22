import maya.cmds as cmds
import colorium.CUI as CUI
import colorium.assetTypeDefinition as assetTypeDefinition
import colorium.CSceneNameParser as CSceneNameParser
import colorium.CCommand as CCommand
import colorium.CDataBinding as CDataBinding

from colorium.CAsset import CAsset


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
            default_value=assetTypeDefinition.getTypeByCode(self.controller.asset.type).name,\
        )
        CDataBinding.bind(type_input, "enabled", self.controller.asset, "hasType")
        CDataBinding.bind(type_input, "value", self.controller.asset, "type")
        self.add_control(type_input)
        
        name_input = CUI.CTextInput("name", "Asset's name", frm_asset_information,\
            enabled=True,\
            default_value=self.controller.asset.name,\
        )
        CDataBinding.bind(name_input, "enabled", self.controller.asset, "hasName")
        CDataBinding.bind(name_input, "text", self.controller.asset, "name")
        self.add_control(name_input)
        
        variant_input = CUI.CIntInput("variant", "Asset's variant", frm_asset_information,\
            enabled=self.controller.asset.hasVariant,\
            toggleable=True,\
            min=1,\
            max=99,\
            default_value=self.controller.asset.variant,\
        )
        CDataBinding.bind(variant_input, "enabled", self.controller.asset, "hasVariant")
        CDataBinding.bind(variant_input, "value", self.controller.asset, "variant")
        self.add_control(variant_input)
        
        scene_input = CUI.CIntInput("scene", "Asset's scene", frm_asset_information,\
            enabled=self.controller.asset.hasScene,\
            toggleable=True,\
            min=0,\
            max=995,\
            default_value=self.controller.asset.scene,\
        )
        CDataBinding.bind(scene_input, "enabled", self.controller.asset, "hasScene")
        CDataBinding.bind(scene_input, "value", self.controller.asset, "scene")
        self.add_control(scene_input)
        
        shot_input = CUI.CIntInput("shot", "Asset's shot", frm_asset_information,\
            enabled=self.controller.asset.hasShot,\
            toggleable=True,\
            min=0,\
            max=995,\
            default_value=self.controller.asset.shot,\
        )
        CDataBinding.bind(shot_input, "enabled", self.controller.asset, "hasShot")
        CDataBinding.bind(shot_input, "value", self.controller.asset, "shot")
        self.add_control(shot_input)
        
        version_input = CUI.CIntInput("version", "Asset's version", frm_asset_information,\
            enabled=True,\
            min=1,\
            max=99,\
            default_value=self.controller.asset.version,\
        )
        CDataBinding.bind(version_input, "value", self.controller.asset, "version")
        self.add_control(version_input)


    def build_save_options_section(self):
        """
        Builds the save options section.
        """
        
        frm_save_options = cmds.frameLayout("frm_save_options", l="Save Options", p=self.main_layout, mh=5, mw=5, cll=True)

        save_input = CUI.CComboInput("save_type", "Save type", frm_save_options,\
            enabled=False,\
            toggleable=True,\
            items=CCommand.getCommandNamesByAction("save"),\
            changed_command=self.controller.set_save_config_command,\
            default_value=self.controller.asset.save_config.command.name,\
        )
        self.add_control(save_input)


    def build_publish_options_section(self):
        """
        Builds the publish options section.
        """

        frm_publish_options = cmds.frameLayout("frm_publish_options", l="Publish Options", p=self.main_layout, mh=5, mw=5, cll=True)

        publish_input = CUI.CComboInput("publish_type", "Publish type", frm_publish_options,\
            enabled=False,\
            toggleable=True,\
            items=CCommand.getCommandNamesByAction("publish"),\
            changed_command=self.controller.set_publish_config_command,\
            default_value=self.controller.asset.publish_config.command.name,\
        )
        self.add_control(publish_input)


    def build_export_options_section(self):
        """
        Builds the export options section.
        """

        frm_export_options = cmds.frameLayout("frm_export_options", l="Export Options", p=self.main_layout, mh=5, mw=5, cll=True)

        export_input = CUI.CComboInput("export_type", "Export type", frm_export_options,\
            enabled=False,\
            toggleable=True,\
            items=CCommand.getCommandNamesByAction("export"),\
            changed_command=self.controller.set_export_config_command,\
            default_value=self.controller.asset.export_config.command.name,\
        )
        self.add_control(export_input)

    
    def build_file_name_preview_section(self):
        """
        Builds the file name preview section.
        """

        frm_file_name_preview = cmds.frameLayout("frm_file_name_preview", l="File Name Preview", p=self.main_layout, mh=5, mw=5, cll=True)

        save_file_name_input = CUI.CTextInput("save_file_name", "Save file name", frm_file_name_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.save_config.fileName,\
        )
        CDataBinding.bind(save_file_name_input, "enabled", self.controller.asset.save_config, "fileNameOverridden")
        CDataBinding.bind(save_file_name_input, "text", self.controller.asset.save_config, "fileName")
        self.add_control(save_file_name_input)

        publish_file_name_input = CUI.CTextInput("publish_file_name", "Publish file name", frm_file_name_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.publish_config.fileName,\
        )
        CDataBinding.bind(publish_file_name_input, "enabled", self.controller.asset.publish_config, "fileNameOverridden")
        CDataBinding.bind(publish_file_name_input, "text", self.controller.asset.publish_config, "fileName")
        self.add_control(publish_file_name_input)

        export_file_name_input = CUI.CTextInput("export_file_name", "Export file name", frm_file_name_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.export_config.fileName,\
        )
        CDataBinding.bind(export_file_name_input, "enabled", self.controller.asset.export_config, "fileNameOverridden")
        CDataBinding.bind(export_file_name_input, "text", self.controller.asset.export_config, "fileName")
        self.add_control(export_file_name_input)
    
    
    def build_path_preview_section(self):
        """
        Builds the path preview section.
        """

        frm_path_preview = cmds.frameLayout("frm_path_preview", l="Path Preview", p=self.main_layout, mh=5, mw=5, cll=True)

        save_path_input = CUI.CFilePathInput("save_path", "Save path", frm_path_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.save_config.path,\
            open_command=self.controller.open_save_path_explorer,\
        )
        CDataBinding.bind(save_path_input, "enabled", self.controller.asset.save_config, "pathOverridden")
        CDataBinding.bind(save_path_input, "text", self.controller.asset.save_config, "path")
        self.add_control(save_path_input)

        publish_path_input = CUI.CFilePathInput("publish_path", "Publish path", frm_path_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.publish_config.path,\
            open_command=self.controller.open_publish_path_explorer,\
        )
        CDataBinding.bind(publish_path_input, "enabled", self.controller.asset.publish_config, "pathOverridden")
        CDataBinding.bind(publish_path_input, "text", self.controller.asset.publish_config, "path")
        self.add_control(publish_path_input)

        export_path_input = CUI.CFilePathInput("export_path", "Export path", frm_path_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.export_config.path,\
            open_command=self.controller.open_export_path_explorer,\
        )
        CDataBinding.bind(export_path_input, "enabled", self.controller.asset.export_config, "pathOverridden")
        CDataBinding.bind(export_path_input, "text", self.controller.asset.export_config, "path")
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
        self.asset.save_config.command = CCommand.getCommand("open", "Scene")
        self.asset.save_config.executeCommand()


    def create(self, value):
        self.asset.save_config.command = CCommand.getCommand("create", "Blank Maya Ascii")
        self.asset.save_config.executeCommand()


    def delete(self, value):
        print("Delete")


    def commit(self, value):
        save_enabled = self.ui.get_control_by_name("save_type").enabled
        publish_enabled = self.ui.get_control_by_name("publish_type").enabled
        export_enabled = self.ui.get_control_by_name("export_type").enabled

        if save_enabled:
            self.asset.save_config.executeCommand()

        if publish_enabled:
            self.asset.publish_config.executeCommand()

        if export_enabled:
            self.asset.export_config.executeCommand()


    def set_save_config_command(self, value):
        self.asset.save_config.command = CCommand.getCommand("save", value)
        print self.asset.save_config.command.name


    def set_publish_config_command(self, value):
        self.asset.publish_config.command = CCommand.getCommand("publish", value)
        print self.asset.publish_config.command.name


    def set_export_config_command(self, value):
        self.asset.export_config.command = CCommand.getCommand("export", value)
        print self.asset.export_config.command.name


    def open_save_path_explorer(self, value):
        self.asset.save_config.command = CCommand.getCommand("open", "Explorer")
        self.asset.save_config.executeCommand()

    
    def open_publish_path_explorer(self, value):
        self.asset.publish_config.command = CCommand.getCommand("open", "Explorer")
        self.asset.publish_config.executeCommand()


    def open_export_path_explorer(self, value):
        self.asset.export_config.command = CCommand.getCommand("open", "Explorer")
        self.asset.export_config.executeCommand()
