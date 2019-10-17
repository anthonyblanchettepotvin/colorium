from abc import ABCMeta, abstractmethod

class Subject():
    __metaclass__ = ABCMeta

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def attachAndNotify(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass

    @abstractmethod
    def notify(self, *args):
        pass

    @abstractmethod
    def clearObservers(self):
        pass


class Observer():
    __metaclass__ = ABCMeta

    @abstractmethod
    def update(self, *args):
        pass
