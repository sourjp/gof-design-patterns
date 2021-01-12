#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod


class Product(metaclass=ABCMeta):
    @abstractmethod
    def use(self) -> str:
        pass


class Factory(metaclass=ABCMeta):
    @abstractmethod
    def _create_product(self, owner: str) -> Product:
        pass

    @abstractmethod
    def _register_product(self, product: str):
        pass

    def create(self, owner: str) -> Product:
        p = self._create_product(owner)
        self._register_product(p)
        return p


class IDCard(Product):
    def __init__(self, owner: str):
        self._owner = owner

    def use(self) -> str:
        return self._owner


class IDCardFactory(Factory):
    def __init__(self):
        self._owners = []

    def _create_product(self, owner: str) -> Product:
        return IDCard(owner)

    def _register_product(self, product: str):
        self._owners.append(product)
