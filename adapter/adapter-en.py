"""I referred below sample.

https://en.wikipedia.org/wiki/Adapter_pattern
"""

from abc import ABC, abstractmethod

NOT_IMPLEMENTED = "You should implement this."

RECHARGE = ["Recharge started.", "Recharge finished."]

POWER_ADAPTERS = {"Android": "MicroUSB", "iPhone": "Lightning"}

CONNECTED = "{} connected."
CONNECT_FIRST = "Connect {} first."


class RechargeTemplate(ABC):

    @abstractmethod
    def recharge(self) -> None:
        raise NotImplementedError(NOT_IMPLEMENTED)


class FormatIPhone(RechargeTemplate):
    """Target"""

    @abstractmethod
    def use_lightning(self) -> None:
        raise NotImplementedError(NOT_IMPLEMENTED)


class FormatAndroid(RechargeTemplate):
    """Target"""

    @abstractmethod
    def use_micro_usb(self) -> None:
        raise NotImplementedError(NOT_IMPLEMENTED)


class IPhone(FormatIPhone):
    """Adaptee"""

    __name__ = 'iPhone'

    def __init__(self) -> None:
        self.connector = False

    def use_lightning(self) -> None:
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self) -> None:
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))


class Android(FormatAndroid):
    """Adaptee"""
    __name__ = "Android"

    def __init__(self) -> None:
        self.connector = False

    def use_micro_usb(self) -> None:
        self.connector = True
        print(CONNECTED.format(POWER_ADAPTERS[self.__name__]))

    def recharge(self) -> None:
        if self.connector:
            for state in RECHARGE:
                print(state)
        else:
            print(CONNECT_FIRST.format(POWER_ADAPTERS[self.__name__]))


class IPhoneAdapter(FormatAndroid):
    """Adapter.

    To support micro usb cable to recharge power
    """

    def __init__(self, mobile):
        self.mobile = mobile

    def use_micro_usb(self) -> None:
        print(CONNECTED.format(POWER_ADAPTERS["Android"]))
        self.mobile.use_lightning()

    def recharge(self) -> None:
        self.mobile.recharge()


class AndroidRecharger:

    def __init__(self):
        self.phone = Android()
        self.phone.use_micro_usb()
        self.phone.recharge()


class IPhoneRecharger:

    def __init__(self):
        self.phone = IPhone()
        self.phone.use_lightning()
        self.phone.recharge()


class IPhoneMicroUSBRecharger:
    """Apply micro USB to iPhone"""

    def __init__(self):
        self.phone = IPhone()
        self.phone_adapter = IPhoneAdapter(self.phone)
        self.phone_adapter.use_micro_usb()
        self.phone_adapter.recharge()


if __name__ == '__main__':
    print('*** Android Recharger ***')
    AndroidRecharger()
    print('*** iPhone Recharger ***')
    IPhoneRecharger()
    print('*** iPhone/Micro Recharger ***')
    IPhoneMicroUSBRecharger()
