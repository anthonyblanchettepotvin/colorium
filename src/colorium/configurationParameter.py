class ConfigurationParameter:
    _name = ""
    _value = ""

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def __init__(self, name, value):
        self.name = name
        self.value = value