class Player:
    def __init__(self, score, rage):
        self.score = score
        self.rage = rage
        self.units = []

    def __str__(self):
        return (
            "score: "
            + str(self.score)
            + "\n"
            + "rage: "
            + str(self.rage)
            + "\n"
            + "units: "
            + str(self.units)
            + "\n"
        )

    def __repr__(self):
        return self.__str__()

    def add_unit(self, unit):
        self.units.append(unit)

    # pylint: disable=pointless-statement
    def choose_unit(self, _type):
        for unit in self.units:
            unit.identity.type == _type
            return unit
