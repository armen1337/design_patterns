from abc import ABC, abstractmethod


class Subject(ABC):
    """ Interface for holding the subscribers and sending notifications """
    @property
    @abstractmethod
    def state(self) -> int:
        pass

    @abstractmethod
    def attach(self, subscriber) -> None:
        pass

    @abstractmethod
    def detach(self, subscriber) -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject: Subject) -> None:
        pass


class Newspaper(Subject):
    _state: int = None
    _observers: list[Observer] = []

    @property
    def state(self) -> int:
        return self._state

    @state.setter
    def state(self, state: int):
        self._state = state

    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)

    def detach(self, observer) -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        """ Sending notifications """
        for observer in self._observers:
            observer.update(self)


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state == 0 or subject.state > 3:
            print(f"NOTIFICATION FOR '{self.__class__.__name__}': '{subject.__class__.__name__}' state is {subject.state}")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject.state > 2:
            print(f"NOTIFICATION FOR '{self.__class__.__name__}': '{subject.__class__.__name__}' state is {subject.state}")


if __name__ == '__main__':
    newspaper = Newspaper()

    subscriber1 = ConcreteObserverA()
    subscriber2 = ConcreteObserverB()

    newspaper.attach(subscriber1)
    newspaper.attach(subscriber2)

    newspaper.state = 4
    newspaper.notify()

    print()

    newspaper.state = 0
    newspaper.notify()
