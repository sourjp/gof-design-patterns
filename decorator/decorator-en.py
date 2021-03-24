"""I referred below sample.

https://en.wikipedia.org/wiki/Decorator_pattern
https://wiki.python.org/moin/DecoratorPattern

Demonstrated decorators in a world of a 10x10 grid of values 0-255.
"""

from abc import ABC, abstractmethod
import random


def s32_to_u16(x):
    if x < 0:
        sign = 0xF000
    else:
        sign = 0
    bottom = x & 0x00007FFF
    return bottom | sign


def seed_from_xy(x, y):
    return s32_to_u16(x) | (s32_to_u16(y) << 16)


class Square(ABC):
    """Component"""

    @abstractmethod
    def get(self, x, y):
        pass


class RandomSquare(Square):
    """ConcreteComponent"""

    def __init__(s, seed_modifier):
        s.seed_modifier = seed_modifier

    def get(s, x, y):
        seed = seed_from_xy(x, y) ^ s.seed_modifier
        random.seed(seed)
        return random.randint(0, 255)


class DataSquare(Square):
    """ConcreteComponent"""

    def __init__(s, initial_value=None):
        s.data = [initial_value] * 10 * 10

    def get(s, x, y):
        return s.data[(y * 10) + x]  # yes: these are all 10x10

    def set(s, x, y, u):
        s.data[(y * 10) + x] = u


class CacheDecorator(Square):
    """ConcreteDecorator"""

    def __init__(s, decorated):
        s.decorated = decorated
        s.cache = DataSquare()

    def get(s, x, y):
        if s.cache.get(x, y) is None:
            s.cache.set(x, y, s.decorated.get(x, y))
        return s.cache.get(x, y)


class MaxDecorator(Square):
    """ConcreteDecorator"""

    def __init__(s, decorated, max):
        s.decorated = decorated
        s.max = max

    def get(s, x, y):
        if s.decorated.get(x, y) > s.max:
            return s.max
        return s.decorated.get(x, y)


class MinDecorator(Square):
    """ConcreteDecorator"""

    def __init__(s, decorated, min):
        s.decorated = decorated
        s.min = min

    def get(s, x, y):
        if s.decorated.get(x, y) < s.min:
            return s.min
        return s.decorated.get(x, y)


class VisibilityDecorator(Square):
    """ConcreteDecorator"""

    def __init__(s, decorated):
        s.decorated = decorated

    def get(s, x, y):
        return s.decorated.get(x, y)

    def draw(s):
        for y in range(10):
            for x in range(10):
                print("%3d" % s.get(x, y), end=' ')
            print()


if __name__ == '__main__':
    # Now, build up a pipeline of decorators:

    random_square = RandomSquare(635)
    random_cache = CacheDecorator(random_square)
    max_filtered = MaxDecorator(random_cache, 200)
    min_filtered = MinDecorator(max_filtered, 100)
    final = VisibilityDecorator(min_filtered)

    final.draw()
