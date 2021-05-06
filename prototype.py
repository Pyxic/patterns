import copy
from abc import ABC, abstractmethod


class Prototype(ABC):

    @abstractmethod
    def clone(self):
        pass


class ConcreteClass1(Prototype):

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy())

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


class ConcreteClass2(Prototype):

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d))

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


obj1 = ConcreteClass2(1, "object1", [[1, 2, 3], 2, 1], {'a': 1, 'b': 2, 'c': 3})
print(obj1)
obj2 = obj1.clone()
obj2.l[0][0] = 10
print(obj2)
print(obj1)

