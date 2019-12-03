from core.utils import check_positive_value, error_print
from core.shapes import Shape2D

# pylint: disable=too-many-instance-attributes
class Motion2D:
    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position):
        self._position = position

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, velocity):
        self._velocity = velocity

    @property
    def acceleration(self):
        return self._acceleration

    @acceleration.setter
    def acceleration(self, acceleration):
        self._acceleration = acceleration

    @property
    def force(self):
        return self._force

    @force.setter
    def force(self, force):
        self._force = force

    @property
    def momentum(self):
        return self._momentum

    @momentum.setter
    def momentum(self, momentum):
        self._momentum = momentum

    @property
    def mass(self):
        return self._mass

    @mass.setter
    def mass(self, mass):
        check_positive_value(mass)
        self._mass = mass

    def __init__(self, shape: Shape2D):
        self.shape = shape
        self._position = shape.get_position()
        self._velocity = None
        self._acceleration = None
        self._force = None
        self._momentum = None
        self._mass = None

    def __str__(self):
        string = "Position: " + self.position
        if self.velocity:
            string += "\nVelocity: " + self.velocity
        if self.acceleration:
            string += "\nAcceleration: " + self.acceleration
        if self.force:
            string += "\nForce: " + self.force
        if self.momentum:
            string += "\nMomentum: " + self.momentum
        if self.mass:
            string += "\nMass: " + self.mass
        return string

    def __repr__(self):
        return self.__str__()

    def update(self):
        def update_velocity():
            if not self.velocity:
                error_print("Velocity does not exist. Cannot update the velocity")
                return
            if self.acceleration:
                self.velocity += self.acceleration

        def update_position():
            if self.velocity:
                self.position += self.velocity

        update_velocity()
        update_position()
        return self.position
