class Identity:
    def __init__(self, id, type, player):
        self.id = id
        self.type = type
        self.player = player

    def __str__(self):
        return "id: " + str(self.id) + ", type: " + str(self.type) + ", player: " + str(self.player)

    def __repr__(self):
        return self.__str__()
