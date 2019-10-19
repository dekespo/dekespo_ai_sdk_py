from py_ai_sdk.core.core_utils import check_positive_value, error_print

# This class should be used in a class with position
class MotionPhysics2D:
    def __init__(self, velocity, acceleration=None, force=None, momentum=None, mass=None):
        self.velocity = velocity
        if acceleration:
            self.acceleration = acceleration
        if force:
            self.force = force
        if momentum:
            self.momentum = momentum
        if mass:
            check_positive_value(mass)
            self.mass = mass

        if not acceleration:
            if force and mass:
                self.acceleration = force.constant_divide(mass)
        if not force:
            if acceleration and mass:
                self.force = acceleration.constant_multiply(mass)
        if not momentum:
            if mass:
                self.momentum = velocity.constant_multiply(mass)
        if not mass:
            if acceleration and force:
                self.mass = force.vectoral_divide(acceleration)
                self.mass = self.mass.x
                if not momentum:
                    self.momentum = velocity.constant_multiply(self.mass)
            elif momentum:
                self.mass = momentum.vectoral_divide(velocity)
                self.mass = self.mass.x
                if not acceleration and force:
                    self.acceleration = force.constant_divide(self.mass)

    def __str__(self):
        string = "Velocity: " + self.velocity
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
