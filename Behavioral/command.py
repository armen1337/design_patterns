from abc import ABC, abstractmethod


class Command(ABC):
    """ Abstract Command class with its single method """
    @abstractmethod
    def execute(self) -> None:
        pass


class PrintCommand(Command):
    """ In this case, Command implementation receives only one argument in the constructor """
    def __init__(self, text):
        self._text = text

    def execute(self) -> None:
        print("LOG:", self._text)


class SendEmailCommand(Command):
    """ In this case, Command implementation receives three arguments in the constructor """
    def __init__(self, sender, receiver, contents):
        self._sender = sender
        self._receiver = receiver
        self._contents = contents

    def execute(self) -> None:
        print(f"'{self._sender}' sent email '{self._contents}' to the person '{self._receiver}'")


class Invoker:
    def __init__(self):
        self._on_start: Command = None
        self._on_finish: Command = None

    def set_on_start(self, command: Command) -> None:
        self._on_start = command

    def set_on_finish(self, command: Command) -> None:
        self._on_finish = command

    def operation(self):
        if self._on_start is not None:
            self._on_start.execute()

        print("Performing operation!")

        if self._on_finish is not None:
            self._on_finish.execute()


if __name__ == '__main__':
    print_command = PrintCommand("Text to print")
    send_email_command = SendEmailCommand("sender@gmail.com", "receiver@gmail.com", "hello")

    invoker = Invoker()
    invoker.set_on_start(print_command)
    invoker.set_on_finish(send_email_command)

    invoker.operation()
