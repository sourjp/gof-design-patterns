"""I referred below sample.

https://ja.wikipedia.org/wiki/Chain_of_Responsibility_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum
from typing import Optional


class Severity(Enum):

    ERROR = 3
    NOTICE = 5
    DEBUG = 7


class Logger(ABC):

    def __init__(self, mask: Severity) -> None:
        self.mask = mask.value
        self.next: Optional[Logger] = None

    def set_next(self, logger: Logger) -> Logger:
        self.next = logger
        return self

    def message(self, msg: str, priority: Severity) -> None:
        if priority.value <= self.mask:
            self.write_message(msg)
            if self.next is not None:
                self.next.message(msg, priority)

    @ abstractmethod
    def write_message(self, msg: str) -> None:
        pass


class StdoutLogger(Logger):

    def write_message(self, msg: str) -> None:
        print(f'Writing to stdout: {msg}')


class StderrLogger(Logger):

    def write_message(self, msg: str) -> None:
        print(f'Sending to stderr: {msg}')


class EmailLogger(Logger):

    def write_message(self, msg: str) -> None:
        print(f'Sending via email: {msg}')


if __name__ == '__main__':
    logger = StdoutLogger(Severity.DEBUG).set_next(
        EmailLogger(Severity.NOTICE).set_next(
            StderrLogger(Severity.ERROR)
        )
    )

    logger.message('Entering function y.', Severity.DEBUG)
    logger.message('Step1 completed.', Severity.NOTICE)
    logger.message('An error has occurred.', Severity.ERROR)
