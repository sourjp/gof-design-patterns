"""I referred below sample.

https://en.wikipedia.org/wiki/Memento_pattern
"""


class Memento:
    def __init__(self, state: str) -> None:
        self._state = state

    def get_saved_state(self) -> str:
        return self._state


class Originator:

    def set(self, state: str) -> None:
        print("Originator: Setting state to", state)
        self._state = state

    def save_to_memento(self) -> Memento:
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento: Memento) -> None:
        self._state = memento.get_saved_state()
        print("Originator: State after restoring from Memento:", self._state)


if __name__ == '__main__':
    saved_states = []
    originator = Originator()
    originator.set("State1")
    originator.set("State2")
    saved_states.append(originator.save_to_memento())

    originator.set("State3")
    saved_states.append(originator.save_to_memento())

    originator.set("State4")

    originator.restore_from_memento(saved_states[1])

    # Originator: Setting state to State1
    # Originator: Setting state to State2
    # Originator: Saving to Memento.
    # Originator: Setting state to State3
    # Originator: Saving to Memento.
    # Originator: Setting state to State4
    # Originator: State after restoring from Memento: State3
