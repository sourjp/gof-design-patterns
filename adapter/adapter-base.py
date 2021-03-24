from abc import ABC, abstractmethod


class Target(ABC):
    """Interface for Client to use Adapter"""

    @abstractmethod
    def require_method(self):
        pass


class Adaptee:
    """This is product which have old method"""

    def old_method(self):
        pass


class Adapter(Target):
    """This is implements pattern pattern.

    Some programming languages ​​also have an extends pattern.
    """

    def __init__(self, adaptee: Adaptee):
        self._adaptee = adaptee

    # def __init__(self):
    #     self._adaptee = Adaptee()

    def require_method(self):
        return self.adaptee.old_method()
