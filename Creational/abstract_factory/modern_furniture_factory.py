from abc import ABC, abstractmethod

from abstract_factory import AbstractFactory
from abstract_furniture import AbstractChair, AbstractSofa, AbstractTable


# All the classes below need to be present in every case of AbstractFactory implementation
class ModernFurnitureFactory(AbstractFactory):
    """ The implementation of the AbstractFactory """
    def create_chair(self) -> AbstractChair:
        return ModernChair()

    def create_sofa(self) -> AbstractSofa:
        return ModernSofa()

    def create_table(self) -> AbstractTable:
        return ModernTable()


class AbstractModernFurniture(ABC):
    """ AbstractModernFurniture defines the style for the modern furniture """
    @abstractmethod
    def has_modern_style(self) -> bool:
        pass


# Below are the implementations for the abstract furniture
class ModernChair(AbstractChair, AbstractModernFurniture):
    def has_legs(self) -> bool:
        return True

    def sit_on(self, person: str) -> None:
        print(f"Person {person} sat on the modern chair")

    def has_modern_style(self) -> bool:
        return True


class ModernSofa(AbstractSofa, AbstractModernFurniture):
    def has_legs(self) -> bool:
        return False

    def sit_on(self, person: str) -> None:
        print(f"Person {person} sat on the modern sofa")

    def lay_on(self, person: str) -> None:
        print(f"Person {person} laid on the modern sofa")

    def has_modern_style(self) -> bool:
        return True


class ModernTable(AbstractTable, AbstractModernFurniture):
    def has_legs(self) -> bool:
        return True

    def place_item(self, item: str) -> None:
        print(f"Placed item {item} on the modern table")

    def has_modern_style(self) -> bool:
        return True
