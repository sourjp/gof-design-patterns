from abc import ABC, abstractmethod


class Template(ABC):

    def template_method(self):
        self.method1()
        self.method2()

    @abstractmethod
    def method1(self):
        pass

    @abstractmethod
    def method2(self):
        pass


class ConcreteTemplate(Template):

    def method1(self):
        pass

    def method2(self):
        pass


if __name__ == '__main__':
    template = ConcreteTemplate()
    template.template_method()
