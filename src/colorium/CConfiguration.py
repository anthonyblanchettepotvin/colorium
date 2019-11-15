from abc import ABCMeta, abstractmethod, abstractproperty
from patterns.observerPattern import Subject, Observer
from colorium.CUI import CBindable
import namingConvention


class CConfiguration(object, CBindable):
    _metaclass_ = ABCMeta


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.notify("{}_name".format(self.name), value)


    @property
    def fileNameOverridden(self):
        return self._fileNameOverridden

    @fileNameOverridden.setter
    def fileNameOverridden(self, value):
        self._fileNameOverridden = value
        self.notify("{}_file_name_overridden".format(self.name), value)


    @property
    def fileName(self):
        return self._fileName

    @fileName.setter
    def fileName(self, value):
        self._fileName = value
        self.notify("{}_file_name".format(self.name), value)


    @property
    def pathOverridden(self):
        return self._pathOverridden

    @pathOverridden.setter
    def pathOverridden(self, value):
        self._pathOverridden = value
        self.notify("{}_path_overridden".format(self.name), value)


    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        self.notify("{}_path".format(self.name), value)


    @property
    def assetData(self):
        return self._assetData

    @assetData.setter
    def assetData(self, value):
        self._assetData = value
        self.notify("{}_asset_data".format(self.name), value)


    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
        self.notify("{}_command".format(self.name), value)
    

    def __init__(self, name, asset_data):
        self._bindings = []
        self._notified_bindings = []

        self._name = name
        self._fileNameOverridden = False
        self._fileName = ""
        self._pathOverridden = False
        self._path = ""
        self._assetData = asset_data
        self._command = None

        self.update_file_name()
        self.update_path()


    def bind(self, bindable):
        if bindable not in self._bindings:
            self._bindings.append(bindable)

        
    def unbind(self, bindable):
        if bindable in self._bindings:
            self._bindings.remove(bindable)


    def notify(self, topic, value):
        for bindable in self._bindings:
            if bindable not in self._notified_bindings:
                bindable.update(topic, value)
                self._notified_bindings.append(bindable)

        self._notified_bindings = []


    def update(self, topic, value):
        if topic == "{}_file_name".format(self.name):
            self.update_file_name()
        elif topic == "{}_path".format(self.name):
            self.update_path()


    @abstractmethod
    def update_file_name(self):
        pass
    

    @abstractmethod
    def update_path(self):
        pass
    

    def executeCommand(self):
        self._command.execute(self)


class SaveConfiguration(CConfiguration):
    def update_file_name(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData)

    def update_path(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForSavedAsset(self.assetData)


class PublishConfiguration(CConfiguration):
    def update_file_name(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForPublishedAsset(self.assetData)

    def update_path(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForPublishedAsset(self.assetData)


class ExportConfiguration(CConfiguration):
    def update_file_name(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForExportedAsset(self.assetData)

    def update_path(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForExportedAsset(self.assetData)


class OpenConfiguration(CConfiguration):
    def update_file_name(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData)

    def update_path(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForSavedAsset(self.assetData)


class CreateConfiguration(CConfiguration):
    def update_file_name(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData)

    def update_path(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForSavedAsset(self.assetData)
