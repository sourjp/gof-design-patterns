from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):

    def handle(self):
        pass


class ConcreteStateB(State):

    def handle(self):
        pass


class Context:

    def __init__(self):
        self.state = ConcreteStateA()

    def request(self):
        self.state.handle()
