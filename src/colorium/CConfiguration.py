import namingConvention
import colorium.CDataBinding as CDataBinding


class CConfiguration(object, CDataBinding.CBindable):

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        self.notify_property_changed('name', value)
        print('\'name\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def fileNameOverridden(self):
        return self.__fileNameOverridden

    @fileNameOverridden.setter
    def fileNameOverridden(self, value):
        self.__fileNameOverridden = value
        self.notify_property_changed('fileNameOverridden', value)
        print('\'fileNameOverridden\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def fileName(self):
        return self.__fileName

    @fileName.setter
    def fileName(self, value):
        self.__fileName = value
        self.notify_property_changed('fileName', value)
        print('\'fileName\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def pathOverridden(self):
        return self.__pathOverridden

    @pathOverridden.setter
    def pathOverridden(self, value):
        self.__pathOverridden = value
        self.notify_property_changed('pathOverridden', value)
        print('\'pathOverridden\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, value):
        self.__path = value
        self.notify_property_changed('path', value)
        print('\'path\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def assetData(self):
        return self.__assetData

    @assetData.setter
    def assetData(self, value):
        self.__assetData = value
        self.notify_property_changed('assetData', value)
        print('\'assetData\' property of CConfiguration set to \'{}\'').format(value)


    @property
    def command(self):
        return self.__command

    @command.setter
    def command(self, value):
        self.__command = value
        self.notify_property_changed('command', value)
        print('\'command\' property of CConfiguration set to \'{}\'').format(value)
    

    def __init__(self, name, asset_data, file_name_generator_function, path_generator_function, default_command):
        CDataBinding.CBindable.__init__(self)

        self.__name = name
        self.__fileNameOverridden = False
        self.__fileName = ""
        self.__pathOverridden = False
        self.__path = ""
        self.__assetData = asset_data
        self.__file_name_generator_function = file_name_generator_function
        self.__path_generator_function = path_generator_function
        self.__command = default_command

        self.update_file_name()
        self.update_path()


    def update(self):
        self.update_file_name()
        self.update_path()


    def update_file_name(self):
        self.fileName = self.__file_name_generator_function(self.__assetData)
    

    def update_path(self):
        self.path = self.__path_generator_function(self.__assetData)
    

    def executeCommand(self):
        self.__command.execute(self)
