from abc import ABC, abstractmethod


class Context:
    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.context = self

    def lock_button(self):
        self._state.lock_button()


class State(ABC):
    @property
    def context(self):
        return self._context

    @context.setter
    def context(self, context: Context):
        self._context = context

    @abstractmethod
    def lock_button(self):
        pass


class DisabledScreen(State):
    def lock_button(self):
        print("Enabling the screen")
        self.context.transition_to(EnabledScreen())


class EnabledScreen(State):
    def lock_button(self):
        print("Disabling the screen")
        self.context.transition_to(DisabledScreen())


if __name__ == '__main__':
    print("Starting with disabled screen")
    context = Context(DisabledScreen())
    context.lock_button()  # Enable
    context.lock_button()  # Disable again
