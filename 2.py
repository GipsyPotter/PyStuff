from __future__ import annotations
from abc import ABC, abstractmethod


class Context:
    """
    The Context defines the interface of interest to clients. It also maintains
    a reference to an instance of a State subclass, which represents the current
    state of the Context.
    """

    _state = None
    """
    A reference to the current state of the Context.
    """

    def __init__(self, state: State) -> None:
        self.transition_to(state)

    def transition_to(self, state: State):
        """
        The Context allows changing the State object at runtime.
        """

        print(f"Context: Transition to {type(state).__name__}")
        self._state = state
        self._state.context = self

    """
    The Context delegates part of its behavior to the current State object.
    """

    def nextState(self):
        self._state.nextState()


class State(ABC):
    """
    The base State class declares methods that all Concrete State should
    implement and also provides a backreference to the Context object,
    associated with the State. This backreference can be used by States to
    transition the Context to another State.
    """

    @property
    def context(self) -> Context:
        return self._context

    @context.setter
    def context(self, context: Context) -> None:
        self._context = context

    @abstractmethod
    def nextState(self) -> None:
        pass


"""
Concrete States implement various behaviors, associated with a state of the
Context.
"""


class Red(State):
    def nextState(self) -> None:
        print("Red wants to change the state of the context.")
        self.context.transition_to(Green())


class Green(State):
    def nextState(self) -> None:
        print("Green wants to change the state of the context.")
        self.context.transition_to(Yellow())


class Yellow(State):
    def nextState(self) -> None:
        print("Yellow wants to change the state of the context.")
        self.context.transition_to(Red())


if __name__ == "__main__":
    # The client code.

    context = Context(Red())
    context.nextState()
    context.nextState()
    context.nextState()
