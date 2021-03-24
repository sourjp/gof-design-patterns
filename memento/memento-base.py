
class Memento:

    def __init__(self, state):
        self.state = state


class Originator:

    def __init__(self, state):
        self.state = state

    def create_memento(self):
        return Memento(self.state)

    def restore(self, memento: Memento):
        if isinstance(memento, Memento):
            self.state = memento.state


class Caretaker:

    def __init__(self):
        self.mementos: list[Memento] = []

    def save(self, memento: Memento):
        self.mementos.append(memento)

    def get_history(self, generation: int):
        return self.mementos[generation]
