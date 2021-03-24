"""I referred below sample.

https://ja.wikipedia.org/wiki/Facade_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3#:~:text=Facade%20%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%81%82%E3%82%8B%E3%81%84%E3%81%AF%20Fa%C3%A7ade%20%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3,%E3%81%AE%E6%AD%A3%E9%9D%A2%E3%80%8D%E3%82%92%E6%84%8F%E5%91%B3%E3%81%99%E3%82%8B%E3%80%82
"""


class Car:
    """Module"""

    def __init__(self) -> None:
        self.speed: int = 0
        self.__distance: int = 0

    @property
    def distance(self) -> int:
        return self.__distance

    @distance.setter
    def distance(self, minutes: int) -> None:
        self.__distance += self.speed * minutes


class Driver:
    """Facade"""

    def __init__(self, car: Car) -> None:
        self.car = car

    def push_pedal(self, speed: int) -> None:
        self.car.speed = speed

    def drive(self, minutes: int) -> None:
        self.car.distance = minutes


if __name__ == '__main__':
    car = Car()
    driver = Driver(car)
    driver.push_pedal(speed=30)
    driver.drive(minutes=10)
    print(car.distance)  # 300

    driver.push_pedal(speed=100)
    driver.drive(minutes=20)
    print(car.distance)  # 2300
