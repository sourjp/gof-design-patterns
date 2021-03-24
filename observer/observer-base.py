from __future__ import annotations
from abc import ABC, abstractmethod


class Observer(ABC):

    def __init__(self, subject: Subject):
        subject.register_observer(self)

    @abstractmethod
    def notify(self):
        pass


class ObserverA(Observer):

    def notify(self):
        print('observer_A')


class ObserverB(Observer):

    def notify(self):
        print('observer_B')


class Subject:

    def __init__(self):
        self.observers: list[Observer] = []

    def register_observer(self, observer: Observer):
        self.observers.append(observer)

    def unregister_observer(self, observer: Observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.notify()


if __name__ == '__main__':
    subject = Subject()
    ObserverA(subject)
    ObserverB(subject)

    subject.notify_observers()
    # observer_A
    # observer_B
