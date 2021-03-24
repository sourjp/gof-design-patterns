"""I referred below sample.

https://en.wikipedia.org/wiki/Prototype_pattern
"""

import copy


class Prototype:
    def clone(self) -> "Prototype":
        return copy.deepcopy(self)


if __name__ == '__main__':
    prototype1 = Prototype()
    prototype2 = prototype1.clone()

    assert id(prototype1) != id(prototype2)
