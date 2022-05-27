from abc import ABC, abstractmethod

from house import House


class AbstractHouseBuilder(ABC):
    @abstractmethod
    def get_result(self) -> House:
        pass

    @abstractmethod
    def build_pool(self) -> None:
        pass

    @abstractmethod
    def build_garden(self) -> None:
        pass

    @abstractmethod
    def build_backyard(self) -> None:
        pass

    @abstractmethod
    def reset(self) -> None:
        pass
