from __future__ import annotations
from typing import Any


class SingletonNew:
    """SingletonNew may be pythonic style.

    Easy to use. But be careful to use with initialise args. __init__() is
    called in each times which means initialize args are override. Moreover
    User should remember same value thou. So may be good to use in case of
    without initialize args.

    >>> s1 = SingletonNew(val1=1)
    >>> s2 = SingletonNew(val1=2)

    This method will override val1=1 to val1=2 even same object.
    >>> assert s1.val1 == 2
    >>> assert s2.val1 == 2
    >>> assert id(s1) == id(s2)
    """

    __instance = None

    def __new__(cls, *args, **kwargs) -> SingletonNew:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, val1: Any) -> None:
        self.val1 = val1


class SingletonNewUpgrade:
    """SingletonNewUpgrade easier to use before.

    >>> s1 = SingletonNewUpgrade(val1=1)
    >>> s2 = SingletonNewUpgrade(val1=2)
    >>> assert s1.val1 == 1
    >>> assert s2.val1 == 1
    >>> assert id(s1) == id(s2)
    """

    __instance = None

    def __new__(cls, *args, **kwargs) -> SingletonNewUpgrade:
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            if args or kwargs:
                cls.__instance.__setup(*args, **kwargs)
        return cls.__instance

    def __setup(self, val1: Any) -> None:
        if val1:
            self.__val1 = val1

    @property
    def val1(self) -> Any:
        return self.__val1


class SingletonGet:
    """SingletonGet may be common style.

    Little complicate to use. But SingletonGet can avoid to override initialize
    args. However user might use as wrong way because user can call
    SingletongGet(). Moreover user can directly access to each args.

    >>> s1 = SingletonGet.get_instance(val1=1)
    >>> s2 = SingletonGet.get_instance(val1=2)
    >>> assert s1.val1 == 1
    >>> assert s2.val1 == 1
    >>> assert id(s1) == id(s2)
    """

    __instance = None

    def __init__(self, val1: Any) -> None:
        self.val1 = val1

    @classmethod
    def get_instance(cls, *args, **kwargs) -> SingletonGet:
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance


class SingletonGetUpgrade:
    """SingletonGetUpgrade easier to use before.

    >>> s1 = SingletonGetUpgrade()
    Traceback (most recent call last):
    ...
    RuntimeError: You can not call __init__(). Use get_instance()

    >>> s1 = SingletonGetUpgrade.get_instance(val1=1)
    >>> s2 = SingletonGetUpgrade.get_instance(val1=2)
    >>> assert s1.val1 == 1
    >>> assert s2.val1 == 1
    >>> assert id(s1) == id(s2)
    """

    __instance = None

    def __init__(self) -> None:
        raise RuntimeError('You can not call __init__(). Use get_instance()')

    @classmethod
    def get_instance(cls, *args, **kwargs) -> SingletonGetUpgrade:
        if cls.__instance is None:
            cls.__instance = cls.__new__(cls)
            if args or kwargs:
                cls.__instance.__setup(*args, **kwargs)
        return cls.__instance

    def __setup(self, val1: Any) -> None:
        if val1:
            self.__val1 = val1

    @property
    def val1(self) -> Any:
        return self.__val1


if __name__ == '__main__':
    import doctest
    doctest.testmod()
