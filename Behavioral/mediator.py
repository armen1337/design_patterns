from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event: str) -> None:
        pass


class ConcreteMediator(Mediator):
    def __init__(self, component_a, component_b):
        self._component_a = component_a
        self._component_a.mediator = self
        self._component_b = component_b
        self._component_b.mediator = self

    def notify(self, sender, event: str) -> None:
        match event:
            case "A":
                print("Handling 'A' event")
                self._component_a.do_b()
            case "C":
                print("Handling 'C' event")
                self._component_b.do_d()
            case _:
                raise ValueError("Invalid event")


class BaseComponent(ABC):
    def __init__(self):
        self._mediator: Mediator = None

    @property
    def mediator(self) -> Mediator:
        return self._mediator

    @mediator.setter
    def mediator(self, mediator: Mediator) -> None:
        self._mediator = mediator


class ComponentA(BaseComponent):
    def do_a(self):
        print("Sending signal A")
        self.mediator.notify(self, "A")

    def do_b(self):
        print("Doing B")


class ComponentB(BaseComponent):
    def do_c(self):
        print("Sending signal C")
        self.mediator.notify(self, "C")

    def do_d(self):
        print("Doing D")


if __name__ == '__main__':
    component_a = ComponentA()
    component_b = ComponentB()
    mediator = ConcreteMediator(component_a, component_b)

    component_a.do_a()
    print()
    component_b.do_c()

