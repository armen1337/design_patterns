from abc import ABC, abstractmethod


class AbstractComponent(ABC):  # Class which will use decorators
    @abstractmethod
    def operation(self) -> str:
        pass


class Component(AbstractComponent):  # One implementation of AbstractComponent
    def operation(self) -> str:
        return "ComponentA"


class AbstractLogger(Component):  # Abstract Decorator
    def __init__(self, component: AbstractComponent):
        self._component = component

    @property
    def component(self):
        return self._component

    def operation(self) -> str:
        return self.component.operation()


class TextFileLogger(AbstractLogger):
    def operation(self) -> str:
        content = self.component.operation()
        print("Logging to .txt file")
        return content


class CSVFileLogger(AbstractLogger):
    def operation(self) -> str:
        content = self.component.operation()
        print("Logging to .csv file")
        return content


if __name__ == '__main__':
    component = Component()
    text_file_logger = TextFileLogger(component)
    csv_and_text_logger = CSVFileLogger(text_file_logger)

    print("Text file logger:")
    print(text_file_logger.operation())

    print("\nCSV and text file logger")
    print(csv_and_text_logger.operation())
