#!/usr/bin/env python3

class Banner(object):
    def __init__(self, msg: str):
        self._message = msg

    def show_with_paren(self) -> str:
        return "(" + self._message + ")"

    def show_with_astr(self) -> str:
        return "*" + self._message + "*"


class PrintBanner(Banner):
    """PrintBannerを継承で作成、外部から継承元にアクセスできる"""

    def __init__(self, msg: str):
        super().__init__(msg)

    def print_weak(self) -> str:
        return self.show_with_paren()

    def print_strong(self) -> str:
        return self.show_with_astr()


class PrintBanner2(object):
    """PrintBanner2を移譲で作成、外部から移譲元にアクセスできない"""

    def __init__(self, msg: str) -> str:
        self._banner = Banner(msg)

    def print_weak(self) -> str:
        return self._banner.show_with_paren()

    def print_strong(self) -> str:
        return self._banner.show_with_astr()
