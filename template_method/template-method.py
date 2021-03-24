"""I referred below sample.

https://en.wikipedia.org/wiki/Template_method_pattern
https://ja.wikipedia.org/wiki/Template_Method_%E3%83%91%E3%82%BF%E3%83%BC%E3%83%B3
"""

from abc import ABC, abstractmethod


class StringLister(ABC):

    def display(self, items: list[str]) -> str:
        result = self.format_header()
        for item in items:
            result += self.format_item(item)
        result += self.format_footer()
        return result

    @abstractmethod
    def format_header(self) -> str:
        pass

    @abstractmethod
    def format_item(self, item: str) -> str:
        pass

    @abstractmethod
    def format_footer(self) -> str:
        pass


class PlainTextStringLister(StringLister):

    def format_header(self) -> str:
        return ''

    def format_item(self, item: str) -> str:
        return ' - ' + item + '\r\n'

    def format_footer(self) -> str:
        return ''


class HtmlStringLister(StringLister):

    def format_header(self) -> str:
        return '<ul>\r\n'

    def format_item(self, item: str) -> str:
        return '  <li>' + item + '</li>\r\n'

    def format_footer(self) -> str:
        return '</ul>\r\n'


if __name__ == '__main__':
    items = ['First', 'Second', 'Third']
    l1 = PlainTextStringLister()
    l2 = HtmlStringLister()

    print(l1.display(items))
    #  - First
    #  - Second
    #  - Third

    print(l2.display(items))
    # <ul>
    #   <li>First</li>
    #   <li>Second</li>
    #   <li>Third</li>
    # </ul>
