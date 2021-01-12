#!/usr/bin/env python3

class Singleton(object):
    """Singletonパターンを作るためにinstanceを返す

    classmethodにすることで、インスタンス化せずに直接アクセス可能にする
    instanceが生成されている場合は、'_instance'が生成されるのでそれを確認する
    >>> dir(cls)
    >>> ['__class__', ..., '_instance', 'get_instance']
    """

    def __init__(self, input: str):
        self.input = input

    @classmethod
    def get_instance(cls, input: str) -> 'Singleton':
       if not hasattr(cls, "_instance"):
            cls._instance = cls(input)
        else:
            cls._instance.input = input
        return cls._instance
