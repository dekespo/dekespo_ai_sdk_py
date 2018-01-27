from dimensions import Dim2D
from utils import *

# This class should be used in a class with position
class MotionPhysics2D:
    def __init__(self, velocity, acceleration = None, force = None, momentum = None, mass = None):
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

        if not acceleration:
            if force and mass:
                self.acceleration = force.constantDivide(mass)
        if not force:
            if acceleration and mass:
                self.force = acceleration.constantMultiply(mass)
        if not momentum:
            if mass:
                self.momentum = velocity.constantMultiply(mass)
        if not mass:
            if acceleration and force:
                self.mass = force.vectoralDivide(acceleration)
                self.mass = Dim2D.toNumberValue(self.mass)
                if not momentum:
                    self.momentum = velocity.constantMultiply(self.mass)
            elif momentum:
                self.mass = momentum.vectoralDivide(velocity)
                self.mass = Dim2D.toNumberValue(self.mass)
                if not acceleration and force:
                    self.acceleration = force.constantDivide(self.mass)

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
            checkPositiveValue(friction)
        try:
            if self.force:
                self.force = newForce
        except AttributeError:
            eprint("Exception: There is no force!")
        try:
            if self.mass:
                if newMass:
                    checkPositiveValue(newMass)
                    self.mass = newMass
                self.acceleration = self.force.constantDivide(self.mass)
        except AttributeError:
            eprint("Exception: There is no mass!")
        try:
            if self.acceleration:
                self.acceleration += newAcceleration
                self.velocity += self.acceleration
                if self.mass:
                    try:
                        if self.momentum:
                            self.momentum = self.velocity.constantMultiply(self.mass)
                    except AttributeError:
                        eprint("Exception: There is no momentum!")
        except AttributeError:
            pass
            eprint("Exception: There is no acceleration!")
        return position + self.velocity
