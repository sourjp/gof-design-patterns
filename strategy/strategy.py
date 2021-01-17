#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
import random
from typing import List


class Hand(object):
    HANDVALUE_GUU: int = 0
    HANDVALUE_CHO: int = 1
    HANDVALUE_PAA: int = 2
    hands: List["Hand"] = []

    def __init__(self, handvalue):
        self.handvalue = handvalue

    @classmethod
    def get_hand(cls, handvalue: int) -> "Hand":
        return cls.hands[handvalue]

    def is_stronger_than(self, h: "Hand") -> bool:
        return self._fight(h) == 1

    def is_weaker_than(self, h: "Hand") -> bool:
        return self._fight(h) == -1

    def _fight(self, h: "Hand") -> int:
        if self == h:
            return 0
        elif (self.handvalue + 1) % 3 == h.handvalue:
            return 1
        else:
            return -1


Hand.hands.append(Hand(Hand.HANDVALUE_GUU))
Hand.hands.append(Hand(Hand.HANDVALUE_CHO))
Hand.hands.append(Hand(Hand.HANDVALUE_PAA))


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def next_hand(self) -> "Hand":
        pass

    @abstractmethod
    def study(self, win: bool):
        pass


class WinningStrategy(Strategy):
    def __init__(self):
        self.won = False
        self.prev_hand: "Hand"

    def next_hand(self) -> "Hand":
        if not self.won:
            self.prev_hand = Hand.get_hand(random.randint(0, 2))
        return self.prev_hand

    def study(self, win: bool):
        self.won = win


class Player(object):

    def __init__(self, name: str, strategy: "Strategy"):
        self.name: str = name
        self.strategy: "Strategy" = strategy
        self.wincount: int = 0
        self.losecount: int = 0
        self.gamecount: int = 0

    def next_hand(self) -> "Hand":
        return self.strategy.next_hand()

    def win(self):
        self.strategy.study(True)
        self.wincount += 1
        self.gamecount += 1

    def lose(self):
        self.strategy.study(False)
        self.losecount += 1
        self.gamecount += 1

    def even(self):
        self.gamecount += 1

    def to_string(self) -> str:
        return f"[{self.name}:{self.gamecount} games, " \
            + f"{self.wincount} win, {self.losecount} lose]"

    def __str__(self):
        return self.name


if __name__ == "__main__":
    p1 = Player("player1", WinningStrategy())
    p2 = Player("player2", WinningStrategy())

    for i in range(10):
        nh1 = p1.next_hand()
        nh2 = p2.next_hand()

        if nh1.is_stronger_than(nh2):
            print(f"win: {p1}")
            p1.win()
            p2.lose()
        elif nh1.is_weaker_than(nh2):
            print(f"win: {p2}")
            p1.lose()
            p2.win()
        else:
            print("even...")
            p1.even()
            p2.even()

    print(p1.to_string())
    print(p2.to_string())
