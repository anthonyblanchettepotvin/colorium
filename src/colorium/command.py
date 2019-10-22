from abc import ABCMeta, abstractmethod, abstractproperty


# Module classes
class Command:
    __metaclass__ = ABCMeta

    @abstractproperty
    def name(self):
        pass

    @abstractmethod
    def execute(self, config):
        pass
