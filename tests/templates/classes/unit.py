class Unit:
    def __init__(self, identity, physics):
        self.identity = identity
        self.physics = physics

    def __str__(self):
        return (
            "identity: "
            + str(self.identity)
            + "\n"
            + "physics: "
            + str(self.physics)
            + "\n"
        )

    def __repr__(self):
        return self.__str__()
