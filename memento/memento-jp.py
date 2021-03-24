"""I referred below sample.

https://ja.wikipedia.org/wiki/Memento_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from __future__ import annotations


class Memento:

    def __init__(self, state: str) -> None:
        self.state = state


class Originator:

    def __init__(self, state: str) -> None:
        self.state = state

    def save(self) -> Memento:
        return Memento(self.state)

    def restore(self, memento) -> None:
        if isinstance(memento, Memento):
            self.state = memento.state


class Caretaker:

    def __init__(self) -> None:
        self.mementos: list[Memento] = []

    def backup(self, memento: Memento) -> None:
        self.mementos.append(memento)

    def get_history(self, generation: int) -> Memento:
        return self.mementos[generation]


if __name__ == '__main__':
    caretaker = Caretaker()

    originator = Originator('state1')
    caretaker.backup(originator.save())
    originator.state = 'state2'
    caretaker.backup(originator.save())

    originator.state = 'state3'
    before_memento = originator.save()
    print(before_memento.state)  # state3

    old_memento = caretaker.get_history(1)
    originator.restore(old_memento)
    restore_memento = originator.save()
    print(old_memento.state, restore_memento.state)  # state2 state2
