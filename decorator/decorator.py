#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class Display(metaclass=ABCMeta):
    @abstractmethod
    def get_columns(self) -> int:
        pass

    @abstractmethod
    def get_rows(self) -> int:
        pass

    @abstractmethod
    def get_rowtext(self, row: int) -> str:
        pass

    def show(self) -> str:
        out = ""
        for i in range(self.get_rows()):
            out += self.get_rowtext(i)
        return out


class StringDisplay(Display):
    def __init__(self, string: str):
        self.string: str = string

    def get_columns(self) -> int:
        return len(self.string)

    def get_rows(self) -> int:
        return 1

    def get_rowtext(self, row: int) -> str:
        if row == 0:
            return self.string
        else:
            return ""


class Border(Display):
    def __init__(self, display: "Display"):
        self.display: "Display" = display


class SideBorder(Border):
    def __init__(self, display: "Display", char: str):
        super().__init__(display)
        self.border_char: str = char

    def get_columns(self) -> int:
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        return self.display.get_rows()

    def get_rowtext(self, row: int) -> str:
        return self.border_char + \
            self.display.get_rowtext(row) + self.border_char


class FullBorder(Border):

    def __init__(self, display: "Display"):
        super().__init__(display)

    def get_columns(self) -> int:
        return 1 + self.display.get_columns() + 1

    def get_rows(self) -> int:
        return 1 + self.display.get_rows() + 1

    def get_rowtext(self, row: int) -> str:
        if row == 0:
            return "+" + self.make_line("-", self.display.get_columns()) + "+"
        elif row == self.display.get_rows() + 1:
            return "+" + self.make_line("-", self.display.get_columns()) + "+"
        else:
            return "|" + self.display.get_rowtext(row - 1) + "|"

    def make_line(self, char: str, count: int) -> str:
        return char * count
