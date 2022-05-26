from abc import ABC, abstractmethod


class AbstractChair(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    @abstractmethod
    def sit_on(self, person: str) -> None:
        pass


class AbstractSofa(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    @abstractmethod
    def sit_on(self, person: str) -> None:
        pass

    @abstractmethod
    def lay_on(self, person: str) -> None:
        pass


class AbstractTable(ABC):
    @abstractmethod
    def has_legs(self) -> bool:
        pass

    @abstractmethod
    def place_item(self, item: str) -> None:
        pass
