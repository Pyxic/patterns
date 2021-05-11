from abc import ABC, abstractmethod


class Text(ABC):

    @abstractmethod
    def show(self):
        pass


class TextEmpty(Text):

    def show(self):
        pass


class TextSpace(Text):

    def __init__(self, text: Text):
        self.object = text

    def show(self):
        print(' ', end='')
        self.object.show()


class TextHello(Text):

    def __init__(self, text: Text):
        self.object = text

    def show(self):
        print("hello", end='')
        self.object.show()


class TextWorld(Text):

    def __init__(self, text: Text):
        self.object = text

    def show(self):
        print("world", end='')
        self.object.show()


decorator = TextHello(TextSpace(TextWorld(TextEmpty())))
decorator.show()
