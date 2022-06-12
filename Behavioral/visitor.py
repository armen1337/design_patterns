from abc import ABC, abstractmethod


class Visitor(ABC):
    """ Visitors have methods to work with each concrete component class """
    @abstractmethod
    def visit_concrete_component_a(self, component):
        pass

    @abstractmethod
    def visit_concrete_component_b(self, component):
        pass


class Component(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class ConcreteComponentA(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_a(self)

    def component_a_method(self):
        return "A"


class ConcreteComponentB(Component):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_component_b(self)

    def component_b_method(self):
        return "B"


class ConcreteVisitorA(Visitor):
    def visit_concrete_component_a(self, component: ConcreteComponentA):
        print(f"{component.component_a_method()} + ConcreteVisitorA")

    def visit_concrete_component_b(self, component: ConcreteComponentB):
        print(f"{component.component_b_method()} + ConcreteVisitorA")


class ConcreteVisitorB(Visitor):
    def visit_concrete_component_a(self, component: ConcreteComponentA):
        print(f"{component.component_a_method()} + ConcreteVisitorB")

    def visit_concrete_component_b(self, component: ConcreteComponentB):
        print(f"{component.component_b_method()} + ConcreteVisitorB")


if __name__ == '__main__':
    visitor_a = ConcreteVisitorA()
    visitor_b = ConcreteVisitorB()

    component_a = ConcreteComponentA()
    component_b = ConcreteComponentB()

    component_a.accept(visitor_a)
    component_a.accept(visitor_b)

    component_b.accept(visitor_a)
    component_b.accept(visitor_b)
