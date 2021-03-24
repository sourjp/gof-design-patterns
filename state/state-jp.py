from abc import ABC, abstractmethod
from datetime import datetime


class State(ABC):

    @abstractmethod
    def greeting(self) -> None:
        pass


class DayState(ABC):

    def greeting(self) -> None:
        print('Hello')


class NightState(ABC):

    def greeting(self) -> None:
        print('Good evening')


class Context:

    def __init__(self):
        self.state = DayState()

    def change_state(self) -> None:
        now = datetime.now()
        if 6 < now.hour < 17:
            self.state = DayState()
        else:
            self.state = NightState()

    def greeting(self) -> None:
        self.change_state()
        self.state.greeting()


if __name__ == '__main__':
    context = Context()
    context.greeting()
