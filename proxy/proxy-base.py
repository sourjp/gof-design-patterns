from abc import ABC


class Subject(ABC):

    def action(self):
        pass


class RealSubject(Subject):

    def action(self):
        pass


class Proxy(Subject):

    def __init__(self):
        self.real_subject = RealSubject()

    def action(self):
        self.real_subject.action()

    # Easy to add helper function before do action()
    #
    # def __write_someting(self):
    #     pass
    #
    # def __check_something(self):
    #     pass
