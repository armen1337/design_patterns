from abc import ABC, abstractmethod


class Engine:  # Implementation
    def __init__(self, hp: int):
        self._hp = hp

    @abstractmethod
    def start_engine(self) -> None:
        pass


class EngineV6(Engine):
    def __init__(self):
        super().__init__(200)

    def start_engine(self) -> None:
        print("Started V6 Engine")


class EngineV8(Engine):
    def __init__(self):
        super().__init__(250)

    def start_engine(self) -> None:
        print("Started V8 Engine")


class Car:  # Abstraction
    def __init__(self, engine: Engine):
        self._engine = engine

    def start_car(self):
        self._engine.start_engine()

    def change_engine(self, engine: Engine):
        self._engine = engine


if __name__ == '__main__':
    engineV6 = EngineV6()
    engineV8 = EngineV8()

    car = Car(engineV6)
    car.start_car()

    car.change_engine(engineV8)
    car.start_car()
