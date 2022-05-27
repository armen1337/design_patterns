from abstract_builder import AbstractHouseBuilder
from house import House


class ModernHouseBuilder(AbstractHouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._house = House()

    def get_result(self) -> House:
        house = self._house
        self.reset()
        return house

    def build_pool(self) -> None:
        self._house.add_feature("Modern pool")

    def build_garden(self) -> None:
        self._house.add_feature("Modern garden")

    def build_backyard(self) -> None:
        self._house.add_feature("Modern backyard")


class EuropeanHouseBuilder(AbstractHouseBuilder):
    def __init__(self):
        self.reset()

    def reset(self) -> None:
        self._house = House()

    def get_result(self) -> House:
        house = self._house
        self.reset()
        return house

    def build_pool(self) -> None:
        self._house.add_feature("European pool")

    def build_garden(self) -> None:
        self._house.add_feature("European garden")

    def build_backyard(self) -> None:
        self._house.add_feature("European backyard")
