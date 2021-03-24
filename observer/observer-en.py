"""I referred below sample.

https://en.wikipedia.org/wiki/Observer_pattern
"""
from __future__ import annotations


class Observable:
    """Subject"""

    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def register_observer(self, observer: Observer) -> None:
        self._observers.append(observer)

    def notify_observers(self, *args, **kwargs) -> None:
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


class Observer:

    def __init__(self, observable: Observable) -> None:
        observable.register_observer(self)

    def notify(self, observable, *args, **kwargs) -> None:
        print('Got', args, kwargs, 'From', observable)


if __name__ == '__main__':
    subject = Observable()
    Observer(subject)

    subject.notify_observers('test')
    # Got ('test',) {} From <__main__.Observable object at 0x7fe9981e9fd0>
