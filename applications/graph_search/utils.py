from enum import Enum, auto

class Status(Enum):
    ON_PAUSE = auto()
    SHOULD_RESTART = auto()
    SHOULD_GO_BACK = auto()
    SHOULD_GO_NEXT = auto()

class Button:

    # TODO: Have reset button
    @staticmethod
    def back(status_dictionary):
        status_dictionary[Status.SHOULD_GO_BACK] = True

    @staticmethod
    def next(status_dictionary):
        status_dictionary[Status.SHOULD_GO_NEXT] = True

    @staticmethod
    def play(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = False

    @staticmethod
    def stop(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = True

    @staticmethod
    def restart(status_dictionary):
        status_dictionary[Status.SHOULD_RESTART] = True
