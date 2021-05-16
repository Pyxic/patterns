from abc import ABC, abstractmethod


class BaseStrategy(ABC):

    @abstractmethod
    def do_work(self, x, y):
        pass


class Adder(BaseStrategy):

    def do_work(self, x, y):
        return x + y


class Multiplicator(BaseStrategy):

    def do_work(self, x, y):
        return x * y


class Calculator:

    def set_strategy(self, strategy: BaseStrategy):
        self.strategy = strategy

    def calculate(self, x, y):
        print(f"Result is: {self.strategy.do_work(x, y)}")


calculator = Calculator()
calculator.set_strategy(Adder())
calculator.calculate(5, 4)

calculator.set_strategy(Multiplicator())
calculator.calculate(5, 4)
