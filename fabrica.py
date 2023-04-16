from __future__ import annotations
from abc import ABC, abstractmethod


class Fabrica(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Мы производим {product}"


class LaptopFabrica(Fabrica):
    def factory_method(self) -> Product:
        return LaptopProduct().main_process()


class SmartphoneFabrica(Fabrica):
    def factory_method(self) -> Product:
        return SmartphoneProduct().main_process()


class Product(ABC):

    @abstractmethod
    def main_process(self) -> str:
        pass


class SmartphoneProduct(Product):

    def main_process(self) -> str:
        return "Гаджет который умеет звонить"


class LaptopProduct(Product):

    def main_process(self) -> str:
        return "Складывающийся гаджет для работы"


def client_code(fabrica: Fabrica) -> None:
    print(f"Я купил какой-то гаджет у компании. Они мне сказали при продаже: {fabrica.some_operation()}")


if __name__ == "__main__":
    print("день 1, мне что-то продали")
    client_code(LaptopFabrica())
    print("день 2, мне что-то продали")
    client_code(SmartphoneFabrica())
