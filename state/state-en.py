"""I referred below sample.

https://en.wikipedia.org/wiki/State_pattern
"""
from __future__ import annotations
from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def write_name(self, context: StateContext, name: str) -> None:
        pass


class LowerCaseState(State):

    def write_name(self, context: StateContext, name: str) -> None:
        print(name.lower())
        context.state = MultipleUpperCaseState()


class MultipleUpperCaseState(State):

    def __init__(self) -> None:
        self.count = 0

    def write_name(self, context: StateContext, name: str):
        print(name.upper())
        self.count += 1
        if self.count > 1:
            context.state = LowerCaseState()


class StateContext:

    def __init__(self):
        self.state = LowerCaseState()

    def write_name(self, name: str):
        self.state.write_name(self, name)


if __name__ == '__main__':
    context = StateContext()

    context.write_name("Monday")
    context.write_name("Tuesday")
    context.write_name("Wednesday")
    context.write_name("Thursday")
    context.write_name("Friday")
    context.write_name("Saturday")
    context.write_name("Sunday")
    # monday
    # TUESDAY
    # WEDNESDAY
    # thursday
    # FRIDAY
    # SATURDAY
    # sunday
