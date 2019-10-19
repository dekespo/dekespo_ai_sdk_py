from py_ai_sdk.core.core_utils import check_positive_value, error_print

class MotionPhysics2D:
    @property
    def position(self):
        return self._position

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

    def __init__(self, position):
        self._position = position

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

    def update(self, position, newForce, newMass, friction, newAcceleration):
        if friction:
            check_positive_value(friction)
        try:
            if self.force:
                self.force = newForce
        except AttributeError:
            error_print("Exception: There is no force!")
        try:
            if self.mass:
                if newMass:
                    check_positive_value(newMass)
                    self.mass = newMass
                self.acceleration = self.force.constant_divide(self.mass)
        except AttributeError:
            error_print("Exception: There is no mass!")
        try:
            if self.acceleration:
                self.acceleration += newAcceleration
                self.velocity += self.acceleration
                if self.mass:
                    try:
                        if self.momentum:
                            self.momentum = self.velocity.constant_multiply(self.mass)
                    except AttributeError:
                        error_print("Exception: There is no momentum!")
        except AttributeError:
            error_print("Exception: There is no acceleration!")
        return position + self.velocity
