from abc import ABC, abstractmethod


class Component(ABC):

    @abstractmethod
    def get_price(self):
        pass


class Offer(Component):

    def __init__(self):
        self._children = []

    def add(self, component):
        self._children.append(component)

    def remove(self, component):
        self._children.remove(component)

    def get_price(self):
        result = 0
        for child in self._children:
            result += child.get_price()
        return result


class Product(Component):

    def __init__(self, name, price):
        self._name = name
        self._price = price

    def get_price(self):
        return self._price


hat = Product('hat', 450)
t_shirt = Product('t-shirt', 500)
knee_pads = Product('knee pads', 300)

offer = Offer()
offer.add(hat)
offer.add(t_shirt)
offer.add(knee_pads)

print(offer.get_price())
