class Identity:
    def __init__(self, id_, type_, player):
        self.id_ = id_
        self.type_ = type_
        self.player = player

    def __str__(self):
        return f"id: {self.id_}, type: {self.type_}, player: {self.player}"

    def __repr__(self):
        return self.__str__()
