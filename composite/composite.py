#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from typing import List


class Entry(metaclass=ABCMeta):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry: "Entry"):
        raise FileTreatmentException

    def print_list(self):
        return self._print_list()

    @abstractmethod
    def _print_list(self, prefix: str):
        pass

    def to_string(self) -> str:
        return f"{self.get_name()} ({self.get_size()})"


class FileTreatmentException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "FileTreatmentException"


class File(Entry):
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def _print_list(self, prefix: str = ""):
        return f"{prefix}/{self.to_string()}\n"


class Directory(Entry):
    def __init__(self, name: str):
        self.name: str = name
        self.directory: List["Entry"] = []

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        size = 0
        for d in self.directory:
            size += d.get_size()
        return size

    def add(self, entry: "Entry"):
        self.directory.append(entry)

    def _print_list(self, prefix: str = ""):
        out = f"{prefix}/{self.to_string()}\n"
        for entry in self.directory:
            out += entry._print_list(f"{prefix}/{self.name}")
        return out
