from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def do_algorithm(self, x: int, y: int) -> int:
        pass


class StrategyA(Strategy):
    def do_algorithm(self, x: int, y: int) -> int:
        """ Multiplication algorithm """
        return x * y


class StrategyB(Strategy):
    def do_algorithm(self, x: int, y: int) -> int:
        """ Addition algorithm """
        return x + y


class Context:
    def __init__(self, strategy: Strategy):
        self._strategy: Strategy = strategy

    @property
    def strategy(self) -> Strategy:
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        print(f"Changing strategy from '{self._strategy.__class__.__name__}' to '{strategy.__class__.__name__}'")
        self._strategy = strategy

    def operation(self, x: int, y: int) -> int:
        return self._strategy.do_algorithm(x, y)


if __name__ == '__main__':
    strategy_a = StrategyA()
    strategy_b = StrategyB()

    context = Context(strategy_a)

    print("Using multiplication algorithm:", context.operation(4, 5))

    context.strategy = strategy_b

    print("Using addition algorithm:", context.operation(4, 5))
