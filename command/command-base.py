from abc import ABC, abstractmethod


class Receiver(ABC):

    @abstractmethod
    def call_a(self):
        pass

    @abstractmethod
    def call_b(self):
        pass


class Caller(Receiver):

    def call_a(self):
        print('A has called')

    def call_b(self):
        print('B has called')


class Command(ABC):

    @abstractmethod
    def execute(self):
        pass


class CommandTypeA(Command):

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.call_a()


class CommandTypeB(Command):

    def __init__(self, receiver: Receiver):
        self.receiver = receiver

    def execute(self):
        self.receiver.call_b()


class Invoker:

    def __init__(self, cmd_a: Command, cmd_b: Command):
        self.cmd_a = cmd_a
        self.cmd_b = cmd_b

    def press_a(self):
        self.cmd_a.execute()

    def press_b(self):
        self.cmd_b.execute()


if __name__ == '__main__':
    caller = Caller()
    cmd_a = CommandTypeA(caller)
    cmd_b = CommandTypeB(caller)

    command = Invoker(cmd_a, cmd_b)
    command.press_a()
    command.press_b()
