"""I referred below sample.

https://en.wikipedia.org/wiki/Abstract_factory_pattern
https://ja.wikipedia.org/wiki/Abstract_Factory_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod
from sys import platform


class Button(ABC):

    @abstractmethod
    def paint(self) -> str:
        pass


class LinuxButton(Button):

    def paint(self) -> str:
        return 'Linux Style'


class WindowsButton(Button):

    def paint(self) -> str:
        return 'Windows Style'


class MacOSButton(Button):

    def paint(self) -> str:
        return 'MacOS Style'


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass


class LinuxFactory(GUIFactory):

    def create_button(self) -> Button:
        return LinuxButton()


class WindowsFactory(GUIFactory):

    def create_button(self) -> Button:
        return WindowsButton()


class MacOSFactory(GUIFactory):

    def create_button(self) -> Button:
        return MacOSButton()


if __name__ == '__main__':
    factory: GUIFactory
    if platform == 'linux':
        factory = LinuxFactory()
    elif platform == 'darwin':
        factory = MacOSFactory()
    elif platform == 'win32':
        factory = WindowsFactory()
    else:
        raise NotImplementedError(
            f'Not Implemented for your platform: {platform}')

    button = factory.create_button()
    print(button.paint())
