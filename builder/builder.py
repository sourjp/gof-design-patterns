from abc import ABCMeta, abstractmethod
from typing import List


class Builder(metaclass=ABCMeta):
    @abstractmethod
    def make_title(self, title: str):
        pass

    @abstractmethod
    def make_string(self, string: str):
        pass

    @abstractmethod
    def make_items(self, items: List[str]):
        pass

    @abstractmethod
    def close(self):
        pass


class Director(object):
    """Directoryに様々なBuilderを渡して共通処理ができる"""

    def __init__(self, builder: "Builder"):
        self.builder = builder

    def construct(self):
        self.builder.make_title("Greeting!")
        self.builder.make_string("朝から昼にかけて、")
        self.builder.make_items(["おはよう。", "こんにちは。"])
        self.builder.make_string("夜に、")
        self.builder.make_items(["こんばんは。", "おやすみ。", "さようなら。"])
        self.builder.close()


class TextBuilder(Builder):
    def __init__(self):
        self._buffer = ""

    def make_title(self, title: str):
        self._buffer += f"=====\n「{title}」\n\n"

    def make_string(self, string: str):
        self._buffer += f"*{string}\n\n"

    def make_items(self, items: List[str]):
        for item in items:
            self._buffer += f"・{item}\n"
        self._buffer += "\n"

    def close(self):
        self._buffer += "=====\n"

    def get_string(self) -> str:
        return self._buffer
