#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
import copy


class Manager(object):
    def __init__(self):
        self.showcase = {}

    def register(self, name: str, proto: 'Product'):
        self.showcase[name] = proto

    def create(self, protoname: str) -> 'Product':
        p = self.showcase.get(protoname)
        return p.create_clone()


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self, s) -> str:
        pass

    @abstractmethod
    def create_clone(self):
        """create_cloneでインスタンスをコピーすることでクラスから作成するコストを減らす"""
        pass


class MessageBox(Product):
    def __init__(self, decochar):
        self.decochar = decochar

    def use(self, s: str) -> str:
        msg = f"{self.decochar} {s} {self.decochar}"
        return "\n".join([self.print_line(s),
                          msg,
                          self.print_line(s)])

    def print_line(self, s: str) -> str:
        # 4 は端と前後のスペース
        return self.decochar * (len(s) + 4)

    def create_clone(self):
        return copy.deepcopy(self)


class UnderlinePen(Product):
    def __init__(self, ulchar):
        self.ulchar = ulchar

    def use(self, s: str) -> str:
        msg = f"\"{s}\""
        return "\n".join([msg,
                          self.print_underline(s)])

    def print_underline(self, s: str) -> str:
        return " " + self.ulchar * len(s) + " "

    def create_clone(self):
        return copy.deepcopy(self)
