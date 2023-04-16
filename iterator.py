from abc import abstractmethod, ABC
from typing import List


class CityShowplace:
    def __init__(self, place):
        self.place = place

    def __str__(self):
        return f"сейчас вы находитесь на {self.place}"


class Iterstor(ABC):
    @abstractmethod
    def next(self) -> CityShowplace:
        pass

    def has_next(self) -> bool:
        pass


class CityShowplaceIterator(Iterstor):
    def __init__(self, city: List[CityShowplace]):
        self._showplase_list = city
        self._index = 0

    def next(self) -> CityShowplace:
        showplace = self._showplase_list[self._index]
        print(f"сейчас вы находитесь на {self._showplase_list[self._index]} достопримечательности")
        self._index += 1
        return showplace

    def has_next(self) -> bool:
        return True if self._index < len(self._showplase_list) else False


if __name__ == "__main__":
    first = CityShowplace("Исакиевский собор")
    second = CityShowplace("Спас на крови")
    turystic_road = CityShowplaceIterator(city=[first, second])
    while turystic_road.has_next():
        turystic_road.next()


