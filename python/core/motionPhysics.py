from dimensions import Dim2D
from utils import *

class MotionPhysics2D:
    def __init__(self, position, velocity, acceleration = None, force = None, momentum = None, mass = None):
        checkType(position, Dim2D)
        self.position = position
        checkType(velocity, Dim2D)
        self.velocity = velocity
        if acceleration:
            checkType(acceleration, Dim2D)
            self.acceleration = acceleration
        if force:
            checkType(force, Dim2D)
            self.force = force
        if momentum:
            checkType(momentum, Dim2D)
            self.momentum = momentum
        if mass:
            checkPositiveValue(mass)
            self.mass = mass

# TODO: Add normalise the units for these variables
# TODO: Add input conditions for which ones should be accessible(for example, if we have mass and acceleration, we don't need force and momentum)
    def __str__(self):
        string = "Position: " + self.position
        string += "\nVelocity" + self.velocity
        if self.acceleration:
            string += "\nAcceleration" + self.acceleration
        if self.force:
            string += "\nForce" + self.force
        if self.momentum:
            string += "\nMomentum" + self.momentum
        if self.mass:
            string += "\nMass" + self.mass
        return string

    def __repr__(self):
        return self.__str__()
