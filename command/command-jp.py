"""I referred below sample.

https://ja.wikipedia.org/wiki/Command_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3#:~:text=Command%20%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%EF%BC%88%E8%8B%B1%3A%20command%20pattern,%E5%AE%9F%E8%A1%8C%EF%BC%89%E3%81%99%E3%82%8B%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3%E3%81%A7%E3%81%82%E3%82%8B%E3%80%82
"""

from abc import ABC, abstractmethod
from enum import auto, Enum


class RoomNumber(Enum):

    ROOM_A = 0
    ROOM_B = auto()
    ROOM_C = auto()


class Switchable(ABC):

    @abstractmethod
    def turn_on(self) -> None:
        pass

    @abstractmethod
    def turn_off(self) -> None:
        pass


class Light(Switchable):

    def turn_on(self) -> None:
        print('Turn on Light')

    def turn_off(self) -> None:
        print('Turn off Light')


class Command(ABC):

    @abstractmethod
    def execute(self) -> None:
        pass

    @abstractmethod
    def undo(self) -> None:
        pass


class NoCommand(Command):

    def execute(self) -> None:
        pass

    def undo(self) -> None:
        pass


class LightOnCommand(Command):

    def __init__(self, light: Switchable) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.turn_on()

    def undo(self) -> None:
        self.light.turn_off()


class LightOffCommand(Command):

    def __init__(self, light: Switchable) -> None:
        self.light = light

    def execute(self) -> None:
        self.light.turn_off()

    def undo(self) -> None:
        self.light.turn_on()


class NoMemorizedCommand(BaseException):
    pass


class LightController:

    def __init__(self) -> None:
        self.on_commands: list[Command] = [NoCommand()] * len(RoomNumber)
        self.off_commands: list[Command] = [NoCommand()] * len(RoomNumber)
        self.undo_command: Command = NoCommand()

    def set_cmd(
            self,
            number: RoomNumber,
            on_cmd: Command,
            off_cmd: Command) -> None:
        self.on_commands[number.value] = on_cmd
        self.off_commands[number.value] = off_cmd

    def on_cmd(self, number: RoomNumber) -> None:
        print(f'{number.name} has executed:')
        cmd: Command = self.on_commands[number.value]
        cmd.execute()
        self.undo_command = cmd

    def off_cmd(self, number: RoomNumber) -> None:
        print(f'{number.name} has executed:')
        cmd = self.off_commands[number.value]
        cmd.execute()
        self.undo_command = cmd

    def undo_cmd(self) -> None:
        try:
            self.undo_command.undo()
            self.undo_command = NoCommand()
        except AttributeError:
            raise NoMemorizedCommand


if __name__ == '__main__':

    light = Light()
    controller = LightController()
    controller.set_cmd(
        number=RoomNumber.ROOM_A,
        on_cmd=LightOnCommand(light),
        off_cmd=LightOffCommand(light))
    controller.set_cmd(
        number=RoomNumber.ROOM_B,
        on_cmd=LightOnCommand(light),
        off_cmd=LightOffCommand(light))
    controller.set_cmd(
        number=RoomNumber.ROOM_C,
        on_cmd=LightOnCommand(light),
        off_cmd=LightOffCommand(light))

    controller.on_cmd(RoomNumber.ROOM_A)
    # ROOM_A has executed:
    # Turn on Light

    controller.off_cmd(RoomNumber.ROOM_A)
    # ROOM_A has executed:
    # Turn off Light

    controller.on_cmd(RoomNumber.ROOM_B)
    # ROOM_B has executed:
    # Turn on Light

    controller.undo_cmd()
    # Turn off Light
