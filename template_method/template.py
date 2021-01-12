#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class AbstractDisplay(metaclass=ABCMeta):
    """Abstract Dsiplayではdisplay()による振る舞いのみ定義し、実装は任せる"""

    @abstractmethod
    def open(self) -> str:
        pass

    @abstractmethod
    def print(self) -> str:
        pass

    @abstractmethod
    def close(self) -> str:
        pass

    def display(self) -> str:
        msg = self.open()
        for i in range(5):
            msg += self.print()
        msg += self.close()
        return msg


class CharDisplay(AbstractDisplay):
    """CharDisplayはCharの前後に`<< >>`をつける"""

    def __init__(self, ch):
        self._ch = ch

    def open(self) -> str:
        return "<<"

    def print(self) -> str:
        return self._ch

    def close(self) -> str:
        return ">>"


class StringDisplay(AbstractDisplay):
    """StringDisplayはStringの周りに囲いをつける"""

    def __init__(self, string):
        self._string = string

    def open(self) -> str:
        return self.print_line() + "\n"

    def print(self) -> str:
        return "|" + self._string + "|" + "\n"

    def close(self) -> str:
        return self.print_line()

    def print_line(self):
        return "+" + "-" * len(self._string) + "+"


