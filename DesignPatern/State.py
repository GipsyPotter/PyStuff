#Phone button
from __future__ import annotations
from abc import ABC, abstractmethod


class Elevator:
    _state = None

    def __init__(self, state: State):
        self.setElevator(state)

    def setElevator(self, state: State):
        self._state = state
        self._state.elevator = self

    def presentState(self):
        print(f"Elevator is in {type(self._state).__name__}")

    def pushDownBtn(self):
        self._state.pushDownBtn()

    def pushUpBtn(self):
        self._state.pushUpBtn()

    def pushUpAndDownBtns(self):
        print("Oops.. you should press one button at a time")

    def noBtnPushed(self):
        print("Press any button. Up or Down")


class State(ABC):
    def elevator(self) -> Elevator:
        return self._elevator



    def pushDownBtn(self) -> None:
        pass

    def pushUpBtn(self) -> None:
        pass


class firstFloor(State):

    def pushDownBtn(self) -> None:
        print("Already in the bottom floor")

    def pushUpBtn(self) -> None:
        print("Elevator moving upward one floor.")
        self.elevator.setElevator(secondFloor())


class secondFloor(State):

    def pushDownBtn(self) -> None:
        print("Elevator moving down a floor...")
        self.elevator.setElevator(firstFloor())

    def pushUpBtn(self) -> None:
        print("Already in the top floor")


if __name__ == "__main__":
    myElevator = Elevator(firstFloor())
    myElevator.presentState()

    myElevator.pushUpBtn()

    myElevator.presentState()
