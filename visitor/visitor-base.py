from __future__ import annotations
from abc import ABC, abstractmethod


class Element(ABC):

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class ElementA(Element):

    def accept(self, visitor: Visitor):
        visitor.visit_element_a(self)

    def operationA(self):
        print('A called')


class ElementB(Element):

    def accept(self, visitor: Visitor):
        visitor.visit_element_b(self)

    def operationB(self):
        print('B called')


class Visitor(ABC):

    @abstractmethod
    def visit_element_a(self, a: ElementA):
        pass

    @abstractmethod
    def visit_element_b(self, b: ElementB):
        pass


class VisitorAB(Visitor):

    def visit_element_a(self, a: ElementA):
        a.operationA()

    def visit_element_b(self, b: ElementB):
        b.operationB()


if __name__ == '__main__':
    elements = [ElementA(), ElementB()]
    for element in elements:
        element.accept(VisitorAB())
