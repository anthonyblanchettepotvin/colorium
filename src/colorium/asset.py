"""Module containing the CAsset class. The CAsset class contains the information used for saving, publishing, exporting, creating, opening and deleting an asset (Maya scene file)."""

from colorium.configuration import CConfiguration
import colorium.data_binding as data_binding
import colorium.command as command
import colorium.naming_convention as naming_convention
import colorium.settings as settings


class CAsset(object, data_binding.CBindable):
    """Information used for saving, publishing, exporting, creating, opening and deleting an asset (Maya scene file)."""

    @property
    def has_type(self):
        """Indicates if the asset has a type."""

        return self._has_type

    @has_type.setter
    def has_type(self, value):
        self._has_type = value
        self.notify_configurations()
        self.notify_property_changed("has_type", value)
        print('\'has_type\' property of CAsset set to \'{}\'').format(value)


    @property
    def type(self):
        """The type of the asset."""

        return self._type

    @type.setter
    def type(self, value):
        self._type = value
        self.notify_configurations()
        self.notify_property_changed("type", value)
        print('\'type\' property of CAsset set to \'{}\'').format(value)


    @property
    def has_name(self):
        """Indicates if the asset has a name."""

        return self._has_name

    @has_name.setter
    def has_name(self, value):
        self._has_name = value
        self.notify_configurations()
        self.notify_property_changed("has_name", value)
        print('\'has_name\' property of CAsset set to \'{}\'').format(value)


    @property
    def name(self):
        """The name of the asset."""

        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.notify_configurations()
        self.notify_property_changed("name", value)
        print('\'name\' property of CAsset set to \'{}\'').format(value)


    @property
    def has_variant(self):
        """Indicates if the asset has a variant."""

        return self._has_variant

    @has_variant.setter
    def has_variant(self, value):
        self._has_variant = value
        self.notify_configurations()
        self.notify_property_changed("has_variant", value)
        print('\'has_variant\' property of CAsset set to \'{}\'').format(value)


    @property
    def variant(self):
        """The variant of the asset."""
        return self._variant

    @variant.setter
    def variant(self, value):
        self._variant = value
        self.notify_configurations()
        self.notify_property_changed("variant", value)
        print('\'variant\' property of CAsset set to \'{}\'').format(value)


    @property
    def has_scene(self):
        """Indicates if the asset has a scene."""

        return self._has_scene

    @has_scene.setter
    def has_scene(self, value):
        self._has_scene = value
        self.notify_configurations()
        self.notify_property_changed("has_scene", value)
        print('\'has_scene\' property of CAsset set to \'{}\'').format(value)


    @property
    def scene(self):
        """The scene of the asset."""

        return self._scene

    @scene.setter
    def scene(self, value):
        self._scene = value
        self.notify_configurations()
        self.notify_property_changed("scene", value)
        print('\'scene\' property of CAsset set to \'{}\'').format(value)


    @property
    def has_shot(self):
        """Indicates if the asset has a shot."""

        return self._has_shot

    @has_shot.setter
    def has_shot(self, value):
        self._has_shot = value
        self.notify_configurations()
        self.notify_property_changed("has_shot", value)
        print('\'has_shot\' property of CAsset set to \'{}\'').format(value)


    @property
    def shot(self):
        """The shot of the asset."""

        return self._shot

    @shot.setter
    def shot(self, value):
        self._shot = value
        self.notify_configurations()
        self.notify_property_changed("shot", value)
        print('\'shot\' property of CAsset set to \'{}\'').format(value)


    @property
    def has_version(self):
        """Indicates if the asset has a version."""

        return self._has_version

    @has_version.setter
    def has_version(self, value):
        self._has_version = value
        self.notify_configurations()
        self.notify_property_changed("has_version", value)
        print('\'has_version\' property of CAsset set to \'{}\'').format(value)


    @property
    def version(self):
        """The version of the asset."""

        return self._version

    @version.setter
    def version(self, value):
        self._version = value
        self.notify_configurations()
        self.notify_property_changed("version", value)
        print('\'version\' property of CAsset set to \'{}\'').format(value)


    @property
    def save_config(self):
        """The save configuration of the asset."""

        return self._save_config

    @save_config.setter
    def save_config(self, value):
        self._save_config = value
        self.notify_configurations()
        self.notify_property_changed("save_config", value)
        print('\'save_config\' property of CAsset set to \'{}\'').format(value)


    @property
    def publish_config(self):
        """The publish configuration of the asset."""

        return self._publish_config

    @publish_config.setter
    def publish_config(self, value):
        self._publish_config = value
        self.notify_configurations()
        self.notify_property_changed("publish_config", value)
        print('\'publish_config\' property of CAsset set to \'{}\'').format(value)


    @property
    def export_config(self):
        """The export configuration of the asset."""

        return self._export_config

    @export_config.setter
    def export_config(self, value):
        self._export_config = value
        self.notify_configurations()
        self.notify_property_changed("export_config", value)
        print('\'export_config\' property of CAsset set to \'{}\'').format(value)


    def __init__(self, has_type=False, asset_type="non", has_name=False, name="unamed", has_variant=False, variant=1, has_scene=False, scene=10, has_shot=False, shot=10, has_version=False, version=1, save_config=None, publish_config=None, export_config=None):
        data_binding.CBindable.__init__(self)

        self._has_type = has_type
        self._type = asset_type
        self._has_name = has_name
        self._name = name
        self._has_variant = has_variant
        self._variant = variant
        self._has_scene = has_scene
        self._scene = scene
        self._has_shot = has_shot
        self._shot = shot
        self._has_version = has_version
        self._version = version

        if save_config:
            self._save_config = save_config
        else:
            self._save_config = CConfiguration("save", self,\
                file_name_generator_function=naming_convention.generate_file_name_for_saved_asset,\
                path_generator_function=naming_convention.generate_path_for_saved_asset,\
                default_command=command.get_command('save', settings.DEFAULT_FILE_FORMAT),\
                )

        if publish_config:
            self._publish_config = publish_config
        else:
            self._publish_config = CConfiguration("publish", self,\
                file_name_generator_function=naming_convention.generate_file_name_for_published_asset,\
                path_generator_function=naming_convention.generate_path_for_published_asset,\
                default_command=command.get_command('publish', settings.DEFAULT_FILE_FORMAT),\
                )

        if export_config:
            self._export_config = export_config
        else:
            self._export_config = CConfiguration("export", self,\
                file_name_generator_function=naming_convention.generate_file_name_for_exported_asset,\
                path_generator_function=naming_convention.generate_path_for_exported_asset,\
                default_command=command.get_command('export', settings.DEFAULT_FILE_FORMAT),\
                )


    def notify_configurations(self):
        """Method that asks the asset's configuration to update themselves."""

        self.save_config.update()
        self.publish_config.update()
        self.export_config.update()
