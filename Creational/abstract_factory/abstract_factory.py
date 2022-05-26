from abc import ABC, abstractmethod

from abstract_furniture import AbstractChair, AbstractSofa, AbstractTable


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self) -> AbstractChair:
        pass

    @abstractmethod
    def create_sofa(self) -> AbstractSofa:
        pass

    @abstractmethod
    def create_table(self) -> AbstractTable:
        pass
