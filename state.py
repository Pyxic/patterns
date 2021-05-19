from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def find_food(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def dream(self):
        pass


class SleepState(State):

    def find_food(self):
        return "search food in his dreams"

    def eat(self):
        return 'can`t eat while sleep'

    def move(self):
        return 'ca`t move while sleep'

    def dream(self):
        return 'sleep and watch dream'


class OnGroundState(State):

    def eat(self):
        return 'eat of clams'

    def find_food(self):
        return 'find food of other'

    def move(self):
        return 'crawling awkwardly along the coastline'

    def dream(self):
        return 'stops for a moment, daydreaming about one familiar female'


class InWaterState(State):

    def eat(self):
        return 'can`t eat in water'

    def find_food(self):
        return 'plows the seabed with tusks, catching mollusks'

    def move(self):
        return 'gracefully cuts the waves of the world ocean'

    def dream(self):
        return 'don`t sleep in water'


class Walrus:

    def __init__(self, state: State):
        self._state = state

    def change_state(self, state: State):
        self._state = state

    def eat(self):
        self._execute('eat')

    def find_food(self):
        self._execute('find_food')

    def move(self):
        self._execute('move')

    def dream(self):
        self._execute('dream')

    def _execute(self, operation: str):
        try:
            func = getattr(self._state, operation)
            print('Walrus {}.'.format(func()))
        except AttributeError:
            print('Walrus can`t do this')


sleep = SleepState()
on_ground = OnGroundState()
in_water = InWaterState()
walrus = Walrus(on_ground)
print('OUTPUT:')
walrus.change_state(in_water)
walrus.move()
walrus.find_food()
walrus.change_state(on_ground)
walrus.eat()
walrus.move()
walrus.dream()
walrus.change_state(sleep)
walrus.dream()
