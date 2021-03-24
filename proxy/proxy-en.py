"""I referred below sample.

https://en.wikipedia.org/wiki/Proxy_pattern
"""

from abc import ABC, abstractmethod

NOT_IMPLEMENTED = 'You should implement this.'


class AbstractCar(ABC):
    """Subject"""

    @abstractmethod
    def drive(self):
        raise NotImplementedError(NOT_IMPLEMENTED)


class Driver:

    def __init__(self, age: int) -> None:
        self.age = age


class Car(AbstractCar):
    """RealSubject"""

    def drive(self) -> None:
        print('Car has been driven!')


class ProxyCar(AbstractCar):
    """Proxy"""

    def __init__(self, driver: Driver) -> None:
        self.car = Car()
        self.driver = driver

    def drive(self) -> None:
        if self.driver.age <= 16:
            print('Sorry, the driver is too young to drive.')
        else:
            self.car.drive()


if __name__ == '__main__':
    kid_car = ProxyCar(Driver(age=16))
    kid_car.drive()

    adult_car = ProxyCar(Driver(age=26))
    adult_car.drive()
