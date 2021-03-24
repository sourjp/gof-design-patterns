"""I referred below sample.

https://en.wikipedia.org/wiki/Chain-of-responsibility_pattern
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from enum import Enum, auto


class LogLevel(Enum):

    NONE = auto()
    INFO = auto()
    DEBUG = auto()
    WARNING = auto()
    ERROR = auto()
    FUNCTIONAL_MESSAGE = auto()
    FUNCTIONAL_ERROR = auto()
    ALL = auto()


class Logger(ABC):

    next = None

    def __init__(self, levels: list[LogLevel]) -> None:
        self.log_levels = []
        for level in levels:
            self.log_levels.append(level)

    def set_next(self, next_logger: Logger) -> Logger:
        self.next = next_logger
        return self.next

    def message(self, msg: str, severity: LogLevel) -> None:
        if LogLevel.ALL in self.log_levels or severity in self.log_levels:
            self.write_message(msg)
        if self.next is not None:
            self.next.message(msg, severity)

    @abstractmethod
    def write_message(self, msg: str) -> None:
        raise NotImplementedError('You should implement this method')


class ConsoleLogger(Logger):

    def write_message(self, msg: str) -> None:
        print(f'Writing to console: {msg}')


class EmailLogger(Logger):

    def write_message(self, msg: str) -> None:
        print(f'Sending via email: {msg}')


class FileLogger(Logger):

    def write_message(self, msg: str) -> None:
        print(f'Writing to log file: {msg}')


if __name__ == '__main__':
    # Set logger chain
    # ConsoleLogger -> EmailLogger -> FileLogger
    logger = ConsoleLogger([LogLevel.ALL])
    email_logger = logger.set_next(
        EmailLogger([LogLevel.FUNCTIONAL_MESSAGE, LogLevel.FUNCTIONAL_ERROR])
    )
    email_logger.set_next(FileLogger([LogLevel.WARNING, LogLevel.ERROR]))

    logger.message("debug log.", LogLevel.DEBUG)
    logger.message("info log.", LogLevel.INFO)
    logger.message("warning log.", LogLevel.WARNING)
    logger.message("error log.", LogLevel.ERROR)
    logger.message("functional_error log.", LogLevel.FUNCTIONAL_ERROR)
    logger.message("functional_message log.", LogLevel.FUNCTIONAL_MESSAGE)
