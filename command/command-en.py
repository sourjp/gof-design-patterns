"""I referred below sample.

https://en.wikipedia.org/wiki/Command_pattern
"""

from abc import ABC, abstractmethod


class Switchable(ABC):
    """Receiver"""

    @abstractmethod
    def power_on(self) -> None:
        pass

    @abstractmethod
    def power_off(self) -> None:
        pass


class Light(Switchable):
    """ConcreteReceiver"""

    def power_on(self) -> None:
        print('The light is on')

    def power_off(self) -> None:
        print('The light is off')


class Command(ABC):
    """Command"""

    @abstractmethod
    def execute(self) -> None:
        pass


class OpenSwitchCommand(Command):
    """ConcreteCommand"""

    def __init__(self, switchable: Switchable) -> None:
        self.switchable = switchable

    def execute(self) -> None:
        self.switchable.power_on()


class CloseSwitchCommand(Command):
    """ConcreteCommand"""

    def __init__(self, switchable: Switchable) -> None:
        self.switchable = switchable

    def execute(self) -> None:
        self.switchable.power_off()


class Switch:
    """Invoker"""

    def __init__(self, close_cmd: Command, open_cmd: Command) -> None:
        self.close_cmd = close_cmd
        self.open_cmd = open_cmd

    def close(self) -> None:
        self.close_cmd.execute()

    def open(self) -> None:
        self.open_cmd.execute()


if __name__ == '__main__':
    lamp = Light()
    close_switch = CloseSwitchCommand(lamp)
    open_switch = OpenSwitchCommand(lamp)

    switch = Switch(close_switch, open_switch)
    switch.open()
    switch.close()
