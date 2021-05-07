from abc import ABC, abstractmethod


class Button(ABC):

    @abstractmethod
    def paint(self):
        pass


class WinButton(Button):

    def paint(self):
        print("paint windows button")


class MacButton(Button):

    def paint(self):
        print("paint mac button")


class Checkbox(ABC):

    @abstractmethod
    def paint(self):
        pass


class WinCheckbox(Checkbox):

    def paint(self):
        print("paint windows checkbox")


class MacCheckbox(Checkbox):

    def paint(self):
        print("paint mac checkbox")


class GUIFactory(ABC):

    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass


class WinFactory(GUIFactory):

    def create_button(self) -> Button:
        return WinButton()

    def create_checkbox(self) -> Checkbox:
        return WinCheckbox()


class MacFactory(GUIFactory):

    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()


for factory in (WinFactory(), MacFactory()):
    button_a = factory.create_button()
    button_b = factory.create_button()
    button_a.paint()
    button_b.paint()
    checkbox_a = factory.create_checkbox()
    checkbox_b = factory.create_checkbox()
    checkbox_a.paint()
    checkbox_b.paint()



