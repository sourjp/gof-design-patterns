"""I referred below sample.

https://en.wikipedia.org/wiki/Singleton_pattern
https://ja.wikipedia.org/wiki/Singleton_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from typing import Optional


class DataBase:

    __instance: Optional["DataBase"] = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            if args or kwargs:
                cls.__instance.__setup(*args, **kwargs)
            else:
                raise ValueError()
        return cls.__instance

    def __setup(self, database_url: str) -> None:
        self.__database_url = database_url

    @property
    def database_url(self) -> str:
        return self.__database_url

    def connect(self) -> None:
        pass


if __name__ == '__main__':
    db = DataBase(database_url='localhost:5432')
    assert db.database_url == 'localhost:5432'
    db.connect()
