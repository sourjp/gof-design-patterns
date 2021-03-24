"""I referred below sample.

https://ja.wikipedia.org/wiki/Observer_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""
from __future__ import annotations


class Listener:
    """Observer"""

    def __init__(self, name: str, subject: Subject) -> None:
        self.name = name
        subject.register(self)

    def update(self, event: str) -> None:
        print(f'{self.name} received event {event}')


class Subject:

    def __init__(self) -> None:
        self.listeners: list[Listener] = []

    def register(self, listener: Listener) -> None:
        self.listeners.append(listener)

    def unregister(self, listener: Listener) -> None:
        self.listeners.remove(listener)

    def notify_listeners(self, event: str) -> None:
        for listener in self.listeners:
            listener.update(event)


if __name__ == '__main__':
    subject = Subject()
    Listener("<listener A>", subject)
    Listener("<listener B>", subject)

    subject.notify_listeners("<event 1>")
    # <listener A> received event <event 1>
    # <listener B> received event <event 1>
