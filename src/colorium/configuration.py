from abc import ABCMeta, abstractmethod, abstractproperty
from patterns.observerPattern import Subject, Observer
from assetData import AssetData
from configurationParameter import ConfigurationParameter
import namingConvention


class Configuration(Subject, Observer):
    _metaclass_ = ABCMeta

    _observers = []

    _fileName = ""
    _fileExtension = ""
    _path = ""
    _parameters = None
    _command = None
    _assetData = None

    @property
    def fileName(self):
        return self._fileName

    @fileName.setter
    def fileName(self, value):
        self._fileName = value
        self.notify()

    @property
    def fileExtension(self):
        return self._fileExtension

    @fileExtension.setter
    def fileExtension(self, value):
        self._fileExtension = value
        self.notify()

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
        self.notify()

    @property
    def assetData(self):
        return self._assetData

    @assetData.setter
    def assetData(self, value):
        self._assetData = value
        self.notify()

    @property
    def command(self):
        return self._command

    @command.setter
    def command(self, value):
        self._command = value
        self.notify()
    
    def __init__(self, assetData):
        self._assetData = assetData

        self.updateFileName()
        self.updatePath()

        self._assetData.attach(self)

    def attach(self, observer):
        self._observers.append(observer)

    def attachAndNotify(self, observer):
        self.attach(observer)
        self.notify()

    def detach(self, observer):
        self._observers.remove(observer)

    @abstractmethod
    def notify(self, *args):
        pass

    def clearObservers(self):
        self._observers = []

    def update(self, *args):
        self.updateFileName()
        self.updatePath()

    def appendParameter(self, name, value):
        parameter = ConfigurationParameter(name, value)
        self._parameters.append(parameter)

    def removeParameter(self, name):
        for parameter in self._parameters:
            if parameter.name == name:
                self._parameters.remove(parameter)

    @abstractmethod
    def updateFileName(self):
        pass
    
    @abstractmethod
    def updatePath(self):
        pass

    def executeCommand(self):
        self._command.execute(self)


class SaveConfiguration(Configuration):
    def notify(self, *args):
        for observer in self._observers:
            observer.update("saveConfig")

    def updateFileName(self):
        self.fileName = namingConvention.generateFileNameForSavedAsset(self.assetData) + self.fileExtension

    def updatePath(self):
        self.path = namingConvention.generatePathForSavedAsset(self.assetData)


class PublishConfiguration(Configuration):
    def notify(self, *args):
        for observer in self._observers:
            observer.update("publishConfig")

    def updateFileName(self):
        self.fileName = namingConvention.generateFileNameForPublishedAsset(self.assetData) + self.fileExtension

    def updatePath(self):
        self.path = namingConvention.generatePathForPublishedAsset(self.assetData)


class ExportConfiguration(Configuration):
    def notify(self, *args):
        for observer in self._observers:
            observer.update("exportConfig")

    def updateFileName(self):
        self.fileName = namingConvention.generateFileNameForExportedAsset(self.assetData) + self.fileExtension

    def updatePath(self):
        self.path = namingConvention.generatePathForExportedAsset(self.assetData)