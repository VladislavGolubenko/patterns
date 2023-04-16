from __future__ import annotations
from abc import abstractmethod, ABC


class Context:
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state: State):
        print(f"Текущее состояние: {type(state).__name__}")
        self._state = state
        self._state.context = self

    def request1(self):
        return self._state.metod1()

    def request2(self):
        return self._state.metod2()


class State(ABC):

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def metod1(self) -> None:
        pass

    @abstractmethod
    def metod2(self) -> None:
        pass


class ConcreateState1(State):
    def metod1(self) -> None:
        print("выолняется первый метод первого состояния")
        self.context.transition_to(ConcreateState2())

    def metod2(self) -> None:
        print("Выполняется второй метод первого состояния")


class ConcreateState2(State):
    def metod1(self) -> None:
        print("Выполняется первый метод второго состояния")

    def metod2(self) -> None:
        print("Выполняется второй метод второго состояния")
        self.context.transition_to(ConcreateState1())


if __name__ == "__main__":
    context = Context(ConcreateState1())
    context.request1()
    context.request2()
