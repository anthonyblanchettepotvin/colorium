"""UI module of Colorium's Asset Management Tool. This module creates the UI using Colorium's CUI module."""

import maya.cmds as cmds
import colorium.ui as ui
import colorium.asset_type_definition as asset_type_definition
import colorium.scene_name_parser as scene_name_parser
import colorium.command as command
import colorium.data_binding as data_binding
import colorium.settings as settings


class AssetManagementToolUI(ui.CUI):
    """This class manages the creation process of the Colorium's Asset Management Tool UI from the layout to the data binding."""

    def build_ui(self):
        self.build_asset_information_section()
        self.build_save_options_section()
        self.build_publish_options_section()
        self.build_export_options_section()
        self.build_file_name_preview_section()
        self.build_path_preview_section()
        self.build_actions_section()


    def build_asset_information_section(self):
        """Builds the asset information section."""

        frm_asset_information = cmds.frameLayout("frm_asset_information", l="Asset Information", p=self.main_layout, mh=5, mw=5)

        type_input = ui.CComboInput("type", "Asset's type", frm_asset_information,\
            enabled=True,\
            items=asset_type_definition.names(),\
            default_value=asset_type_definition.get_type_by_code(self.controller.asset.type).name,\
        )
        data_binding.bind(type_input, "enabled", self.controller.asset, "has_type")
        data_binding.bind(type_input, "value", self.controller.asset, "type")
        self.add_control(type_input)

        name_input = ui.CTextInput("name", "Asset's name", frm_asset_information,\
            enabled=True,\
            default_value=self.controller.asset.name,\
        )
        data_binding.bind(name_input, "enabled", self.controller.asset, "has_name")
        data_binding.bind(name_input, "text", self.controller.asset, "name")
        self.add_control(name_input)

        variant_input = ui.CIntInput("variant", "Asset's variant", frm_asset_information,\
            enabled=self.controller.asset.has_variant,\
            toggleable=True,\
            min_value=1,\
            max_value=99,\
            default_value=self.controller.asset.variant,\
        )
        data_binding.bind(variant_input, "enabled", self.controller.asset, "has_variant")
        data_binding.bind(variant_input, "value", self.controller.asset, "variant")
        self.add_control(variant_input)

        scene_input = ui.CIntInput("scene", "Asset's scene", frm_asset_information,\
            enabled=self.controller.asset.has_scene,\
            toggleable=True,\
            min_value=0,\
            max_value=995,\
            default_value=self.controller.asset.scene,\
        )
        data_binding.bind(scene_input, "enabled", self.controller.asset, "has_scene")
        data_binding.bind(scene_input, "value", self.controller.asset, "scene")
        self.add_control(scene_input)

        shot_input = ui.CIntInput("shot", "Asset's shot", frm_asset_information,\
            enabled=self.controller.asset.has_shot,\
            toggleable=True,\
            min_value=0,\
            max_value=995,\
            default_value=self.controller.asset.shot,\
        )
        data_binding.bind(shot_input, "enabled", self.controller.asset, "has_shot")
        data_binding.bind(shot_input, "value", self.controller.asset, "shot")
        self.add_control(shot_input)

        version_input = ui.CIntInput("version", "Asset's version", frm_asset_information,\
            enabled=True,\
            min_value=1,\
            max_value=99,\
            default_value=self.controller.asset.version,\
        )
        data_binding.bind(version_input, "value", self.controller.asset, "version")
        self.add_control(version_input)


    def build_save_options_section(self):
        """Builds the save options section."""

        frm_save_options = cmds.frameLayout("frm_save_options", l="Save Options", p=self.main_layout, mh=5, mw=5, cll=True)

        save_input = ui.CComboInput("save_type", "Save type", frm_save_options,\
            enabled=False,\
            toggleable=True,\
            items=command.get_command_names_by_action("save"),\
            changed_command=self.controller.set_save_config_command,\
            default_value=self.controller.asset.save_config.command.name,\
        )
        self.add_control(save_input)

        increment_option = ui.CCheckControl("increment_on_save", "Increment on save", frm_save_options,\
            default_value=False,\
        )
        self.add_control(increment_option)


    def build_publish_options_section(self):
        """Builds the publish options section."""

        frm_publish_options = cmds.frameLayout("frm_publish_options", l="Publish Options", p=self.main_layout, mh=5, mw=5, cll=True)

        publish_input = ui.CComboInput("publish_type", "Publish type", frm_publish_options,\
            enabled=False,\
            toggleable=True,\
            items=command.get_command_names_by_action("publish"),\
            changed_command=self.controller.set_publish_config_command,\
            default_value=self.controller.asset.publish_config.command.name,\
        )
        self.add_control(publish_input)


    def build_export_options_section(self):
        """Builds the export options section."""

        frm_export_options = cmds.frameLayout("frm_export_options", l="Export Options", p=self.main_layout, mh=5, mw=5, cll=True)

        export_input = ui.CComboInput("export_type", "Export type", frm_export_options,\
            enabled=False,\
            toggleable=True,\
            items=command.get_command_names_by_action("export"),\
            changed_command=self.controller.set_export_config_command,\
            default_value=self.controller.asset.export_config.command.name,\
        )
        self.add_control(export_input)


    def build_file_name_preview_section(self):
        """Builds the file name preview section."""

        frm_file_name_preview = cmds.frameLayout("frm_file_name_preview", l="File Name Preview", p=self.main_layout, mh=5, mw=5, cll=True)

        save_file_name_input = ui.CTextInput("save_file_name", "Save file name", frm_file_name_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.save_config.file_name,\
        )
        data_binding.bind(save_file_name_input, "enabled", self.controller.asset.save_config, "file_name_overridden")
        data_binding.bind(save_file_name_input, "text", self.controller.asset.save_config, "file_name")
        self.add_control(save_file_name_input)

        publish_file_name_input = ui.CTextInput("publish_file_name", "Publish file name", frm_file_name_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.publish_config.file_name,\
        )
        data_binding.bind(publish_file_name_input, "enabled", self.controller.asset.publish_config, "file_name_overridden")
        data_binding.bind(publish_file_name_input, "text", self.controller.asset.publish_config, "file_name")
        self.add_control(publish_file_name_input)

        export_file_name_input = ui.CTextInput("export_file_name", "Export file name", frm_file_name_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.export_config.file_name,\
        )
        data_binding.bind(export_file_name_input, "enabled", self.controller.asset.export_config, "file_name_overridden")
        data_binding.bind(export_file_name_input, "text", self.controller.asset.export_config, "file_name")
        self.add_control(export_file_name_input)


    def build_path_preview_section(self):
        """Builds the path preview section."""

        frm_path_preview = cmds.frameLayout("frm_path_preview", l="Path Preview", p=self.main_layout, mh=5, mw=5, cll=True)

        save_path_input = ui.CFilePathInput("save_path", "Save path", frm_path_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.save_config.path,\
            open_command=self.controller.open_save_path_explorer,\
        )
        data_binding.bind(save_path_input, "enabled", self.controller.asset.save_config, "path_overridden")
        data_binding.bind(save_path_input, "text", self.controller.asset.save_config, "path")
        self.add_control(save_path_input)

        publish_path_input = ui.CFilePathInput("publish_path", "Publish path", frm_path_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.publish_config.path,\
            open_command=self.controller.open_publish_path_explorer,\
        )
        data_binding.bind(publish_path_input, "enabled", self.controller.asset.publish_config, "path_overridden")
        data_binding.bind(publish_path_input, "text", self.controller.asset.publish_config, "path")
        self.add_control(publish_path_input)

        export_path_input = ui.CFilePathInput("export_path", "Export path", frm_path_preview,\
            enabled=False,\
            toggleable=True,\
            default_value=self.controller.asset.export_config.path,\
            open_command=self.controller.open_export_path_explorer,\
        )
        data_binding.bind(export_path_input, "enabled", self.controller.asset.export_config, "path_overridden")
        data_binding.bind(export_path_input, "text", self.controller.asset.export_config, "path")
        self.add_control(export_path_input)


    def build_actions_section(self):
        """Builds the actions section."""

        frm_actions = cmds.frameLayout("frm_actions", l="Actions", p=self.main_layout, mh=5, mw=5)

        lay_actions = ui.CInlineLayout("actions", "Actions", frm_actions, [], "right")

        cancel_button = ui.CButtonControl("cancel", "Cancel", lay_actions.name, self.controller.cancel)
        lay_actions.add_children(cancel_button)

        open_button = ui.CButtonControl("open", "Open", lay_actions.name, self.controller.open)
        lay_actions.add_children(open_button)

        create_button = ui.CButtonControl("create", "Create", lay_actions.name, self.controller.create)
        lay_actions.add_children(create_button)

        delete_button = ui.CButtonControl("delete", "Delete", lay_actions.name, self.controller.delete)
        lay_actions.add_children(delete_button)

        commit_button = ui.CButtonControl("commit", "Commit", lay_actions.name, self.controller.commit)
        lay_actions.add_children(commit_button)

        self.add_control(lay_actions)


class AssetManagementToolController(ui.CController):
    """This class controls the interactions between Colorium's Asset Management Tool UI and the business layer."""

    @property
    def asset(self):
        """The asset manipulated from the UI."""
        return self._asset


    @asset.setter
    def asset(self, value):
        self._asset = value


    def __init__(self):
        super(AssetManagementToolController, self).__init__()

        self._asset = scene_name_parser.parse_scene_name_to_asset()


    def display_ui_callback(self):
        pass


    def cancel(self, value):
        """Command used to close the tool."""

        cmds.deleteUI(self.ui.main_window, wnd=True)


    def open(self, value):
        """Command used to open a maya scene based on the asset data."""

        if settings.DEFAULT_FILE_FORMAT == 'Maya Ascii':
            self.asset.save_config.command = command.get_command('open', 'Maya Ascii')
        elif settings.DEFAULT_FILE_FORMAT == 'Maya Binary':
            self.asset.save_config.command = command.get_command('open', 'Maya Binary')

        self.asset.save_config.execute_command()


    def create(self, value):
        """Command used to create a maya scene based on the asset data."""

        if settings.DEFAULT_FILE_FORMAT == 'Maya Ascii':
            self.asset.save_config.command = command.get_command("create", "Blank Maya Ascii")
        elif settings.DEFAULT_FILE_FORMAT == 'Maya Binary':
            self.asset.save_config.command = command.get_command('create', 'Blank Maya Binary')

        self.asset.save_config.execute_command()


    def delete(self, value):
        """Command used to delete a maya scene based on the asset data."""

        if settings.DEFAULT_FILE_FORMAT == 'Maya Ascii':
            self.asset.save_config.command = command.get_command("delete", "Maya Ascii")
        elif settings.DEFAULT_FILE_FORMAT == 'Maya Binary':
            self.asset.save_config.command = command.get_command('delete', 'Maya Binary')

        self.asset.save_config.execute_command()


    def commit(self, value):
        """Command used to commit (save, publish and/or export) the scene based on the asset data."""

        save_enabled = self.ui.get_control_by_name("save_type").enabled
        publish_enabled = self.ui.get_control_by_name("publish_type").enabled
        export_enabled = self.ui.get_control_by_name("export_type").enabled

        if save_enabled:
            increment_on_save = self.ui.get_control_by_name('increment_on_save').value

            if increment_on_save:
                self.asset.version += 1

            self.asset.save_config.execute_command()

        if publish_enabled:
            self.asset.publish_config.execute_command()

        if export_enabled:
            self.asset.export_config.execute_command()


    def set_save_config_command(self, value):
        """Command used to set the asset's save configuration command based on a given value."""

        self.asset.save_config.command = command.get_command("save", value)
        print self.asset.save_config.command.name


    def set_publish_config_command(self, value):
        """Command used to set the asset's publish configuration command based on a given value."""

        self.asset.publish_config.command = command.get_command("publish", value)
        print self.asset.publish_config.command.name


    def set_export_config_command(self, value):
        """Command used to set the asset's export configuration command based on a given value."""

        self.asset.export_config.command = command.get_command("export", value)
        print self.asset.export_config.command.name


    def open_save_path_explorer(self, value):
        """Command used to open the asset's save configuration path in the Explorer."""

        self.asset.save_config.command = command.get_command("open", "Explorer")
        self.asset.save_config.execute_command()


    def open_publish_path_explorer(self, value):
        """Command used to open the asset's publish configuration path in the Explorer."""

        self.asset.publish_config.command = command.get_command("open", "Explorer")
        self.asset.publish_config.execute_command()


    def open_export_path_explorer(self, value):
        """Command used to open the asset's export configuration path in the Explorer."""

        self.asset.export_config.command = command.get_command("open", "Explorer")
        self.asset.export_config.execute_command()
