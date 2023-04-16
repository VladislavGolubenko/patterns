from abc import ABC, abstractmethod
from enum import Enum
from random import choice


class Technik(Enum):
    APPLE = 1
    HUAWEI = 2
    SAMSUNG = 3


class Order:
    order_id = 1

    def __init__(self, order_type: Technik):
        self.id = Order.order_id
        self.order_type = order_type
        Order.order_id += 1

    def __str__(self):
        return f"Заказ {self.order_id}, {self.order_type}"


class Observer(ABC):
    @abstractmethod
    def update(self, order_id):
        pass


class Sabject(ABC):
    def __init__(self):
        self._observers = []  # list(Observer)

    def attech(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detech(self, observer):
        self._observers.remove(observer)

    def notify(self, observer_id):
        for observer in self._observers:
            observer.update(observer_id)


class Personas(Sabject):
    def __init__(self):
        super().__init__()
        self.__orders = []
        self.__finish = []

    def take_order(self, order):
        print(f"Заказ {order} принят в обработку")
        self.__orders.append(order)

    def compliting_order(self, order_id):
        order = None
        for i in self.__finish:
            if i.id == order_id:
                order = i
                break
        self.__finish.remove(order)
        return order

    def get_process_order(self):
        if self.__orders:
            order = choice(self.__orders)
            self.__orders.remove(order)
            self.__finish.append(order)
            print(f"Прибыл заказ {order}")
            self.notify(order.id)
        else:
            print("Оюидаем новые заказы")


class Clients(Observer):
    def __init__(self, name, persona):
        self.__persona = persona
        self.__name = name
        self.order = None

    def update(self, order_id):
        if self.order is not None:
            if order_id == self.order.id:
                print(f"Клиент {self.__name} принял свой заказ")
                self.__persona.detech(self)

    def create_order(self):
        order_type = choice(
            [
                Technik.APPLE,
                Technik.HUAWEI,
                Technik.SAMSUNG,
            ]
        )
        self.order = Order(order_type)
        print(f"Был сделан заказ {self.__name}, {self.order}")
        self.__persona.attech(self)
        self.__persona.take_order(self.order)


if __name__ == "__main__":
    names = ['name1', 'name2', 'name3']
    persona = Personas()
    clients = [Clients(name, persona) for name in names]
    for client in clients:
        client.create_order()

    for a in range(3):
        persona.get_process_order()
