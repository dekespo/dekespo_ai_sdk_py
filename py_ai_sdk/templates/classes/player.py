class Player:
    def __init__(self, score, rage):
        self.score = score
        self.rage = rage
        self.units = []

    def __str__(self):
        return "score: " + str(self.score) + "\n" \
                + "rage: " + str(self.rage) + "\n" \
                + "units: " + str(self.units) + "\n"

    def __repr__(self):
        return self.__str__()

    def addUnit(self, unit):
        self.units.append(unit)

    def chooseUnit(self, type):
        for object in self.units:
            object.identity.type == type
            return object
