from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any


class Builder(ABC):

    @property
    @abstractmethod
    def product(self) -> None:
        pass

    @abstractmethod
    def product_part_1(self) -> None:
        pass

    @abstractmethod
    def product_part_2(self) -> None:
        pass

    @abstractmethod
    def product_part_3(self) -> None:
        pass


class CityBuilder(Builder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._product = CityHouse()

    @property
    def product(self) -> None:
        product = self._product
        self.reset()
        return product

    def product_part_1(self) -> None:
        self._product.add("есть пентхаус")

    def product_part_2(self) -> None:
        self._product.add("есть лифт")

    def product_part_3(self) -> None:
        self._product.add("есть консьерж")


class CityHouse:
    def __init__(self) -> None:
        self.pats = []

    def add(self, part: Any) -> None:
        self.pats.append(part)

    def show_list(self) -> None:
        print(f"Параметры этого городского здания:{self.pats}")


class Director:

    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder):
        self._builder = builder

    def build_econom(self):
        self.builder.product_part_2()

    def build_comfort(self):
        self.builder.product_part_2()
        self.builder.product_part_3()

    def build_besness(self):
        self.builder.product_part_1()
        self.builder.product_part_2()
        self.builder.product_part_3()


if __name__ == "__main__":
    director = Director()
    builder = CityBuilder()
    director.builder = builder

    print("------------ ECONOM ---------------------")

    director.build_econom()
    builder.product.show_list()

    print("-----------------------------------------")

    print("------------ BUISNESS ---------------------")

    director.build_besness()
    builder.product.show_list()

    print("-----------------------------------------")