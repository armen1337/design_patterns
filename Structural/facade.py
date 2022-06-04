from enum import Enum
from time import sleep, time


class Spinning:
    def __init__(self):
        self._rpm = None

    @property
    def rpm(self):
        return self._rpm

    @rpm.setter
    def rpm(self, rpm: int):
        self._rpm = rpm

    def spin(self) -> None:
        print(f"Spinning with the {self.rpm} revolutions per minute")
        print("Spinning...")
        start_time = time()
        sleep(10000/self.rpm)
        print(f"Spinning time: {time() - start_time:.2f}")


class WashingMode(Enum):
    BLACK = 0
    COLOR = 1


class Washing:
    def __init__(self):
        self._mode = None

    @property
    def mode(self):
        return self._mode

    @mode.setter
    def mode(self, mode: WashingMode):
        self._mode = mode

    def wash(self) -> None:
        print(f"Washing with the {self.mode.name.lower()} mode")


class WashingMachine:
    """ Facade """
    def __init__(self):
        self._washing = Washing()
        self._spinning = Spinning()

    def fast_washing(self) -> None:
        self._spinning.rpm = 3600
        self._washing.mode = WashingMode.BLACK
        self._washing.wash()
        self._spinning.spin()

    def thorough_washing(self):
        self._spinning.rpm = 2000
        self._washing.mode = WashingMode.COLOR
        self._washing.wash()
        self._spinning.spin()


if __name__ == '__main__':
    washing_machine = WashingMachine()

    print("Performing fast washing\n")
    washing_machine.fast_washing()

    print("\n\nPerforming thorough washing\n")
    washing_machine.thorough_washing()
