from abstract_builder import AbstractHouseBuilder


class Director:
    def __init__(self, builder: AbstractHouseBuilder):
        self._builder = builder

    @property
    def builder(self) -> AbstractHouseBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: AbstractHouseBuilder):
        self._builder = builder

    def build_minimum_featured_house(self):
        self._builder.build_garden()

    def build_full_featured_house(self):
        self._builder.build_garden()
        self._builder.build_pool()
        self._builder.build_backyard()
