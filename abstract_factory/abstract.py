#!/usr/bin/env python3

from abc import ABCMeta, abstractmethod
from typing import List


class Item(metaclass=ABCMeta):
    def __init__(self, caption: str):
        self.caption = caption

    @abstractmethod
    def make_html(self):
        pass


class Link(Item):
    def __init__(self, caption: str, url: str):
        super().__init__(caption)
        self.url = url


class Tray(Item):
    def __init__(self, caption: str):
        super().__init__(caption)
        self.trays: List["Item"] = []

    def add(self, item: "Item"):
        self.trays.append(item)


class Page(metaclass=ABCMeta):
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.contents: List["Item"] = []

    def add(self, item: "Item"):
        self.contents.append(item)

    def output(self):
        filename = self.title + ".html"
        with open("py.html", "w") as f:
            f.write(self.make_html())

    @abstractmethod
    def make_html(self):
        pass


class Factory(metaclass=ABCMeta):

    # @classmethod
    # def get_factory(cls, classname: str):
    #     module, kls = classname.split(".")
    #     return getattr(__import__(module), kls)

    @abstractmethod
    def create_link(self, caption: str, url: str):
        pass

    @abstractmethod
    def create_tray(self, caption: str):
        pass

    @abstractmethod
    def create_page(self, title: str, author: str):
        pass


class ListFactory(Factory):
    def create_link(self, caption: str, url: str) -> "ListLink":
        return ListLink(caption, url)

    def create_tray(self, caption: str) -> "ListTray":
        return ListTray(caption)

    def create_page(self, title: str, author: str) -> "ListPage":
        return ListPage(title, author)


class ListLink(Link):
    def __init__(self, caption: str, url: str):
        super().__init__(caption, url)

    def make_html(self) -> str:
        return f'<li><a href="{self.url}">"{self.caption}"</a></li>\n'


class ListTray(Tray):
    def __init__(self, caption: str):
        super().__init__(caption)

    def make_html(self) -> str:
        out = "<li>\n" \
            + f"{self.caption}\n" \
            + "<ul>\n"
        for tray in self.trays:
            out += tray.make_html()
        out += "</ul>\n" \
            + "</li>\n"
        return out


class ListPage(Page):
    def __init__(self, title: str, author: str):
        super().__init__(title, author)

    def make_html(self) -> str:
        out = f"<html><head><title>{self.title}</title></head>\n" \
            + "<body>\n" \
            + f"<h1>{self.title}</h1>\n" \
            + "<ul>\n"
        for content in self.contents:
            out += content.make_html()
        out += "</ul>\n" \
            + f"<hr><address>{self.author}</address></body></html>\n"
        return out


if __name__ == "__main__":
    factory = ListFactory()
    link_google = factory.create_link("Google", "https://google.com")
    link_yahoo = factory.create_link("Yahoo!", "https://yahoo.com")

    tray = factory.create_tray("Search Engine")
    tray.add(link_google)
    tray.add(link_yahoo)

    page = factory.create_page("Title", "Author")
    page.add(tray)

    page.output()
