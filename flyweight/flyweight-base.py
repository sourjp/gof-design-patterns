class Flyweight:
    pass


class FlyweightFactory:

    __flyweights: dict[int, Flyweight] = {}

    # Use instance vars to protect within factories.
    # def __init__(self):
    #     self.__flyweights: dict[int, Flyweight] = {}

    @classmethod
    def get(cls, id: int) -> Flyweight:
        return cls.__flyweights.setdefault(id, Flyweight())


class FlyweightMixin:

    _instances: dict = {}

    @ classmethod
    def get_instance(cls, *args, **kwargs):
        """Share instances between inherited classes.

        Args:
            *args (Any): Be key to get instances(e.g. id=1)
            **kwargs (Any): Be args to create new instances(e.g. name=a).

        Returns:
            FlyweightMixin
        """
        instance_key = (cls, *args)
        if instance_key not in cls._instances:
            cls._instances[instance_key] = cls(**kwargs)
        return cls._instances[instance_key]


class ObjA(FlyweightMixin):

    def __init__(self, name: str) -> None:
        self.name = name


class ObjB(FlyweightMixin):

    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == '__main__':
    def test_normal() -> None:
        flyweight1 = FlyweightFactory.get(1)
        flyweight2 = FlyweightFactory.get(1)
        assert flyweight1 == flyweight2

    test_normal()

    def test_mixin() -> None:
        a1 = ObjA.get_instance(1, name='A')
        a2 = ObjA.get_instance(1)
        print(a1._instances)
        assert id(a1) == id(a2)

        b1 = ObjB.get_instance(1, name='B')
        b2 = ObjB.get_instance(1)
        print(b1._instances)
        assert id(b1) == id(b2)

    test_mixin()
