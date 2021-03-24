"""I referred below sample.

https://en.wikipedia.org/wiki/Mediator_pattern
https://ja.wikipedia.org/wiki/Mediator_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def notify(self, sender: str, action: str) -> None:
        pass


class Window(ABC):

    def __init__(self, mediator: Mediator) -> None:
        self.mediator = mediator
        self.is_open = False

    @abstractmethod
    def open(self) -> None:
        pass

    @abstractmethod
    def close(self) -> None:
        pass

    def __str__(self) -> str:
        return f'{self.is_open=}'


class WindowA(Window):

    def open(self) -> None:
        self.mediator.notify('A', 'open')
        self.is_open = True

    def close(self) -> None:
        self.is_open = False


class WindowB(Window):

    def open(self) -> None:
        self.mediator.notify('B', 'open')
        self.is_open = True

    def close(self) -> None:
        self.is_open = False


class WindowC(Window):

    def open(self):
        self.is_open = True

    def close(self) -> None:
        self.mediator.notify('C', 'close')
        self.is_open = False


class WindowMediator(Mediator):

    def set_mediator(self,
                     window_a: Window,
                     window_b: Window,
                     window_c: Window) -> None:
        self.window_a = window_a
        self.window_b = window_b
        self.window_c = window_c

    def notify(self, sender: str, action: str) -> None:
        if sender == 'A' and action == 'open':
            self.window_b.close()
        if sender == 'B' and action == 'open':
            self.window_a.close()
        if sender == 'C' and action == 'close':
            self.window_a.close()
            self.window_b.close()

    @property
    def values(self) -> str:
        return f'A={self.window_a}, B={self.window_b}, C={self.window_c}'


if __name__ == '__main__':
    window_mediator = WindowMediator()
    window_a = WindowA(window_mediator)
    window_b = WindowB(window_mediator)
    window_c = WindowC(window_mediator)
    window_mediator.set_mediator(window_a, window_b, window_c)
    print(window_mediator.values)
    # A=self.is_open=False, B=self.is_open=False, C=self.is_open=False

    window_c.open()
    print(window_mediator.values)
    # A=self.is_open=False, B=self.is_open=False, C=self.is_open=True

    window_a.open()
    print(window_mediator.values)
    # A=self.is_open=True, B=self.is_open=False, C=self.is_open=True

    window_b.open()
    print(window_mediator.values)
    # A=self.is_open=False, B=self.is_open=True, C=self.is_open=True

    window_c.close()
    print(window_mediator.values)
    # A=self.is_open=False, B=self.is_open=False, C=self.is_open=False
