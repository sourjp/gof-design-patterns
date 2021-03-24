"""I referred below sample.

https://ja.wikipedia.org/wiki/Proxy_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod


class Client(ABC):
    """Subject"""

    @property
    @abstractmethod
    def account_no(self):
        pass


class RealClient(Client):
    """RealSubject"""

    def __init__(self, account_no: str = '12345') -> None:
        print('RealClient: Initialized')
        self._account_no = account_no

    @property
    def account_no(self) -> str:
        print(f"RealClient's AccountNo: {self._account_no}")
        return self._account_no


class ProtectionProxy(Client):
    """Proxy provids auth function"""

    def __init__(self, pwd: str) -> None:
        print('ProtectionProxy: Initialized')
        self.__password = pwd
        self._client = RealClient()

    @property
    def account_no(self) -> str:
        pwd: str = input('Password: ')

        if pwd == self.__password:
            return self._client.account_no
        else:
            return 'ProtectionProxy: Illegal password!'


if __name__ == '__main__':
    client = ProtectionProxy('pwd')
    print(client.account_no)

    """
    ProtectionProxy: Initialized
    RealClient: Initialized
    Password: pwd
    RealClient's AccountNo: 12345
    12345
    """
