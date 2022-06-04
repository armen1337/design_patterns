from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def is_composite(self) -> bool:
        pass

    @abstractmethod
    def calculate(self) -> int:
        pass


class Box(Component):
    """
    Composites do not have a price.
    But they have the method 'calculate' which will calculate the price for children products.
    """
    def __init__(self):
        self._children: list[Component] = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def is_composite(self) -> bool:
        return True

    def calculate(self) -> int:
        return sum([component.calculate() for component in self._children])


class Product(Component):
    """
    Products are leaves of the tree, so they are the exit points in calculation recursion, as they have a price attribute.
    """
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    def is_composite(self) -> bool:
        return False

    def calculate(self) -> int:
        return self.price


if __name__ == '__main__':
    product = Product(20)
    intermediate_box = Box()
    for _ in range(5):
        intermediate_box.add(product)

    # intermediate_box - recursive price is 100
    print("Intermediate box price:", intermediate_box.calculate())

    parent_box = Box()
    for _ in range(5):
        parent_box.add(intermediate_box)

    # parent_box - recursive price is 500
    print("Parent box price:", parent_box.calculate())
