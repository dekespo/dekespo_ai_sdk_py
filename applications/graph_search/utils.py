from enum import Enum, auto

class Status(Enum):
    ON_PAUSE = auto()

class Button:

    @staticmethod
    def back(status_dictionary):
        print("Pressed back", status_dictionary)

    @staticmethod
    def play(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = False

    @staticmethod
    def stop(status_dictionary):
        status_dictionary[Status.ON_PAUSE] = True

    @staticmethod
    def restart(status_dictionary):
        print("Pressed restart", status_dictionary)
