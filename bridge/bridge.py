#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class Display(object):
    """機能のスーパークラス"""

    def __init__(self, impl: "DisplayImpl"):
        self.impl = impl

    def open(self) -> str:
        return self.impl.raw_open()

    def print(self) -> str:
        return self.impl.raw_print()

    def close(self) -> str:
        return self.impl.raw_close()

    def display(self) -> str:
        return self.open() + self.print() + self.close()


class CountDisplay(Display):
    """機能のサブクラス"""

    def __init__(self, impl: "DisplayImpl"):
        super().__init__(impl)

    def multi_display(self, times: int) -> str:
        out = self.open()
        for time in range(times):
            out += self.print()
        out += self.close()
        return out


class DisplayImpl(metaclass=ABCMeta):
    """実装のスーパークラス"""
    @abstractmethod
    def raw_open(self) -> str:
        pass

    @abstractmethod
    def raw_print(self) -> str:
        pass

    @abstractmethod
    def raw_close(self) -> str:
        pass


class StringDisplayImpl(DisplayImpl):
    """実装のサブクラス"""

    def __init__(self, string: str):
        self.string = string
        self.width = len(string)

    def raw_open(self) -> str:
        return self.print_line()

    def raw_print(self) -> str:
        return f"|{self.string}|"

    def raw_close(self) -> str:
        return self.print_line()

    def print_line(self) -> str:
        return "+" + "-" * self.width + "+"


class CharDisplayImpl(DisplayImpl):
    def __init__(self, head: str, char: str, bottom: str):
        self.head = head
        self.char = char
        self.bottom = bottom
        self.num = 0

    def raw_open(self) -> str:
        return self.head

    def raw_print(self) -> str:
        out = self.char * self.num
        self.num += 1
        return out

    def raw_close(self) -> str:
        return self.bottom
