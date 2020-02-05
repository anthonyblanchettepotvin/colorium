"""Module containing the CConfiguration class. The CConfiguration class uses an asset information to generate a path and file name for saving, publishing, exporting, creating and deleting the asset using a specific command."""

import colorium.data_binding as data_binding


class CConfiguration(object, data_binding.CBindable):
    """Uses an asset information to generate a path and file name for saving, publishing, exporting, creating and deleting the asset using a specific command."""

    @property
    def name(self):
        """The name of the configuration."""

        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.notify_property_changed('name', value)
        print('\'name\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def file_name_overridden(self):
        """Indicates if the file name is overridden."""

        return self.__file_name_overridden

    @file_name_overridden.setter
    def file_name_overridden(self, value):
        self.__file_name_overridden = value
        self.notify_property_changed('file_name_overridden', value)
        print('\'file_name_overridden\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def file_name(self):
        """The file name."""

        return self.__file_name

    @file_name.setter
    def file_name(self, value):
        self.__file_name = value
        self.notify_property_changed('file_name', value)
        print('\'file_name\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def path_overridden(self):
        """Indicates if the file path is overridden."""

        return self.__path_overridden

    @path_overridden.setter
    def path_overridden(self, value):
        self.__path_overridden = value
        self.notify_property_changed('path_overridden', value)
        print('\'path_overridden\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def path(self):
        """The file path."""

        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value
        self.notify_property_changed('path', value)
        print('\'path\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def asset(self):
        """The asset associated with the configuration."""

        return self.__asset

    @asset.setter
    def asset(self, value):
        self.__asset = value
        self.notify_property_changed('asset', value)
        print('\'asset\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def command(self):
        """The command associated with the configuration."""

        return self.__command

    @command.setter
    def command(self, value):
        self.__command = value
        self.notify_property_changed('command', value)
        print('\'command\' property of CConfiguration set to \'{}\'').format(value)


    def __init__(self, name, asset_data, file_name_generator_function, path_generator_function, default_command):
        data_binding.CBindable.__init__(self)

        self.__name = name
        self.__file_name_overridden = False
        self.__file_name = ""
        self.__path_overridden = False
        self.__path = ""
        self.__asset = asset_data
        self.__file_name_generator_function = file_name_generator_function
        self.__path_generator_function = path_generator_function
        self.__command = default_command

        self.update_file_name()
        self.update_path()


    def update(self):
        """Update the configuration based on the asset information."""

        self.update_file_name()
        self.update_path()


    def update_file_name(self):
        """Update the file name based on the asset configuration using the file name generator function passed on instanciation."""

        self.file_name = self.__file_name_generator_function(self.__asset)


    def update_path(self):
        """Update the file paht based on the asset configuration using the file path generator function passed on instanciation."""

        self.path = self.__path_generator_function(self.__asset)


    def execute_command(self):
        """Execute the command associated to the configuration."""

        self.__command.execute(self)
