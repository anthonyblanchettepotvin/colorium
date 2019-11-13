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

        self._name = name
        self._fileNameOverridden = False
        self._fileName = ""
        self._pathOverridden = False
        self._path = ""
        self._assetData = asset_data
        self._command = None

        self.updateFileName()
        self.updatePath()


    def bind(self, bindable):
        if bindable not in self._bindings:
            self._bindings.append(bindable)

        
    def unbind(self, bindable):
        if bindable in self._bindings:
            self._bindings.remove(bindable)


    def notify(self, topic, value):
        for bindable in self._bindings:
            bindable.update(topic, value)


    def update(self, topic, value):
        self.updateFileName()
        self.updatePath()


    @abstractmethod
    def updateFileName(self):
        pass
    

    @abstractmethod
    def updatePath(self):
        pass
    

    def executeCommand(self):
        self._command.execute(self)


class SaveConfiguration(CConfiguration):
    def updateFileName(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData)

    def updatePath(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForSavedAsset(self.assetData)


class PublishConfiguration(CConfiguration):
    def updateFileName(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForPublishedAsset(self.assetData)

    def updatePath(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForPublishedAsset(self.assetData)


class ExportConfiguration(CConfiguration):
    def updateFileName(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForExportedAsset(self.assetData)

    def updatePath(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForExportedAsset(self.assetData)


class OpenConfiguration(CConfiguration):
    def updateFileName(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData)

    def updatePath(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForSavedAsset(self.assetData)


class CreateConfiguration(CConfiguration):
    def updateFileName(self):
        if not self.fileNameOverridden:
            self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData)

    def updatePath(self):
        if not self.pathOverridden:
            self.path = namingConvention.generatePathForSavedAsset(self.assetData)
