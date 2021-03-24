"""I referred below sample.

https://en.wikipedia.org/wiki/Factory_method_pattern
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Room(ABC):

    def __init__(self) -> None:
        self._connect_rooms: list[Room] = []

    @abstractmethod
    def connect(self, room: Room) -> None:
        pass


class MagicRoom(Room):

    def connect(self, room: Room) -> None:
        self._connect_rooms.append(room)

    def __str__(self):
        return f'MagicRoomID={id(self)}'


class OrdinaryRoom(Room):

    def connect(self, room: Room) -> None:
        self._connect_rooms.append(room)

    def __str__(self):
        return f'OrdinaryRoomID={id(self)}'


class MazeGame(ABC):

    def __init__(self) -> None:
        self.rooms: list[Room] = []
        self._setup_room()

    def _setup_room(self) -> None:
        room1 = self.make_room()
        room2 = self.make_room()
        room1.connect(room2)
        self.rooms.append(room1)
        self.rooms.append(room2)

    def play(self) -> None:
        for room in self.rooms:
            print(room)

    @abstractmethod
    def make_room(self) -> Room:
        pass


class MagicMazeGame(MazeGame):

    def make_room(self) -> Room:
        return MagicRoom()


class OrdinaryMazeGame(MazeGame):

    def make_room(self) -> Room:
        return OrdinaryRoom()


if __name__ == '__main__':
    magic_game = MagicMazeGame()
    print(vars(magic_game))
    magic_game.play()

    ordinary_game = OrdinaryMazeGame()
    print(vars(ordinary_game))
    ordinary_game.play()
