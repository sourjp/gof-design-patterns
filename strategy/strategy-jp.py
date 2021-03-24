"""I referred below sample.

https://en.wikipedia.org/wiki/Strategy_pattern
"""
from collections.abc import Callable


class Button:

    def __init__(self, submit_func: Callable):
        self.on_submit = submit_func


if __name__ == '__main__':
    button1 = Button(sum)
    button2 = Button(lambda numbers: " ".join(map(str, numbers)))

    numbers = range(1, 10)
    print(button1.on_submit(numbers))  # 45
    print(button2.on_submit(numbers))  # 1 2 3 4 5 6 7 8 9
