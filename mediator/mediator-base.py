from abc import ABC, abstractmethod


class Mediator(ABC):

    @abstractmethod
    def colleague_changed(self):
        pass


class Colleague(ABC):

    def __init__(self, mediator: Mediator):
        self.mediator = mediator

    @abstractmethod
    def control_colleague(self):
        pass


class ConcreteColleague1(Colleague):

    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def control_colleague(self):
        pass


class ConcreteColleague2(Colleague):

    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def control_colleague(self):
        pass


class ConcreteColleague3(Colleague):

    def __init__(self, mediator: Mediator):
        super().__init__(mediator)

    def control_colleague(self):
        pass


class ConcreteMediator(Mediator):

    def set_mediator(self,
                     colleague1: Colleague,
                     colleague2: Colleague,
                     colleague3: Colleague):
        self.colleague1 = colleague1
        self.colleague2 = colleague2
        self.colleague3 = colleague3

    def colleague_changed(self):
        pass
