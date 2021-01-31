#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from typing import List


class Visitor(metaclass=ABCMeta):
    @abstractmethod
    def visit(self):
        pass


class ListVisitor(Visitor):
    def __init__(self):
        self.currentdir = ""

    def visit(self, directory: "Directory"):
        print(f"{self.currentdir}/{directory}")
        if isinstance(directory, Directory):
            savedir = self.currentdir
            self.currentdir = self.currentdir + "/" + directory.get_name()
            for f in directory:
                f.accept(self)
            self.currentdir = savedir


class Element(metaclass=ABCMeta):
    @abstractmethod
    def accept(self, v: "Visitor"):
        pass


class Entry(Element):
    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_size(self):
        pass

    def add(self, entry: "Entry"):
        raise FileTreatmentException

    def __str__(self):
        return f"{self.get_name()}({self.get_size()})"


class File(Entry):
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        return self.size

    def accept(self, v: "Visitor"):
        v.visit(self)


class Directory(Entry):
    def __init__(self, name: str):
        self.name: str = name
        self.dir: List["Directory"] = []

    def get_name(self) -> str:
        return self.name

    def get_size(self) -> int:
        size: int = 0
        for f in self.dir:
            size += f.get_size()
        return size

    def add(self, entry: "Entry") -> "Entry":
        self.dir.append(entry)
        return self

    def accept(self, v: "Visitor"):
        v.visit(self)

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.dir):
            raise StopIteration()
        dir = self.dir[self.index]
        self.index += 1
        return dir


class FileTreatmentException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "FileTreatmentException"


def main():
    print("Making root entries...")

    rootdir = Directory("root")
    bindir = Directory("bin")
    tmpdir = Directory("tmp")
    usrdir = Directory("usr")

    rootdir.add(bindir)
    rootdir.add(tmpdir)
    rootdir.add(usrdir)
    bindir.add(File("vi", 1000))
    bindir.add(File("latex", 20000))
    rootdir.accept(ListVisitor())


if __name__ == "__main__":
    main()
