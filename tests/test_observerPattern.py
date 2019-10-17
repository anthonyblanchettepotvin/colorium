import pytest
from patterns.observerPattern import Subject
from patterns.observerPattern import Observer


class ConcreteSubject(Subject):
    _observers = []

    _value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
        self.notify()

    def attach(self, observer):
        self._observers.append(observer)

    def attachAndNotify(self, observer):
        self.attach(observer)
        self.notify()

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self, *args):
        for observer in self._observers:
            observer.update(self._value)

    def clearObservers(self):
        self._observers = []


class ConcreteObserver(Observer):
    _value = 0

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value

    def update(self, *args):
        self._value = args[0]


subject = ConcreteSubject()
observer = ConcreteObserver()

def test_subjectGetterSetter():
    subject.value = 10

    assert subject.value == 10

def test_observerGetterSetter():
    subject.value = 10

    assert subject.value == 10

def test_attach():
    subject.attach(observer)
    subject.value = 10

    assert observer.value == subject.value

def test_detach():
    subject.detach(observer)
    subject.value = 20

    assert observer.value != subject.value
