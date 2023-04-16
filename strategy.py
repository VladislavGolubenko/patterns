from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def calculate_marshrut(self, road: list) -> None:
        pass


class CarStrategy(Strategy):
    def calculate_marshrut(self, road: list) -> list:
        road.reverse()
        return road


class WalkStrategy(Strategy):
    def calculate_marshrut(self, road: list) -> list:
        return road


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    @property
    def strategy(self):
        return self._strategy

    @strategy.setter
    def strategy(self, strategy: Strategy):
        self._strategy = strategy

    def do_something(self, list):
        result = self._strategy.calculate_marshrut(list)
        print("".join(result))


if __name__ == "__main__":
    points = ['1', '2', '4', '6']
    context = Context(CarStrategy())
    context.do_something(list=points)
