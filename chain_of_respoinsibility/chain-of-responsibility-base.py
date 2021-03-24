from __future__ import annotations
from abc import ABC, abstractmethod


class Handler(ABC):

    def __init__(self):
        self.next = None

    def set_next(self, receiver: Handler):
        self.next = receiver
        return self

    def execute(self):
        self.request()
        if self.next:
            self.next.execute()

    @abstractmethod
    def request(self):
        pass


class ReceiverA(Handler):

    def request(self):
        print('A')


class ReceiverB(Handler):

    def request(self):
        print('B')


if __name__ == '__main__':
    handler = ReceiverA().set_next(ReceiverB())
    handler.execute()
