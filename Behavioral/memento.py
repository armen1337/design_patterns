from abc import ABC, abstractmethod
from datetime import datetime


class AbstractMemento(ABC):
    @abstractmethod
    def get_date(self) -> str:
        pass

    @abstractmethod
    def get_state(self) -> str:
        pass


class Memento(AbstractMemento):
    def __init__(self, state):
        self._state = state
        self._datetime = str(datetime.now())[:19]

    def get_date(self) -> str:
        return self._datetime

    def get_state(self) -> str:
        return self._state


class Originator:
    """ Objects of this class will be saved """

    def __init__(self, state: str):
        self._state = state

    @property
    def state(self) -> str:
        return self._state

    @state.setter
    def state(self, state):
        self._state = state

    def save(self) -> Memento:
        return Memento(self.state)

    def restore(self, memento: Memento) -> None:
        print("Restoring state to", memento.get_date())
        self._state = memento.get_state()


class Caretaker:
    """ Caretaker doesn't depend on the Memento class. """

    def __init__(self, originator: Originator):
        self._mementos: list[Memento] = []
        self._originator = originator

    def backup(self) -> None:
        self._mementos.append(self._originator.save())

    def undo(self) -> None:
        memento = self._mementos.pop()
        self._originator.restore(memento)

    def list_mementos(self) -> None:
        for memento in self._mementos:
            print(f"Date: {memento.get_date()}\nMemento with state: {memento.get_state()}")
            print("-"*20)


if __name__ == '__main__':
    originator = Originator("Initial state")
    caretaker = Caretaker(originator)
    caretaker.backup()

    originator.state = "Second state"
    caretaker.backup()

    originator.state = "Third state"

    caretaker.list_mementos()

    print("Originator state:", originator.state, end="\n\n")
    caretaker.undo()
    print("Originator state:", originator.state, end="\n\n")
    caretaker.undo()
    print("Originator state:", originator.state)
