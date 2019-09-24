from numbers import Number

import sys
import operator

def checkNumberValue(value):
    if not isinstance(value, Number):
        raise TypeError("Value type " + type(value).__name__ + " is not a Number type")

def checkType(instance, classType):
    if not isinstance(instance, classType):
        raise TypeError("Mismatch in types: instance = " + type(instance).__name__ \
            + " and class = " + classType.__name__)

def checkPositiveValue(value):
    checkNumberValue(value)
    if value <= 0:
        raise ArithmeticError("Value " + str(value) + " must be larger than 0")

def checkNoneValue(value, valueName):
    if not value:
        checkType(valueName, str)
        raise AssertionError(valueName, " cannot be None!")

def checkValidation(value, valueName, validValues):
    checkType(validValues, tuple)
    if value not in validValues:
        raise AssertionError(valueName, " is ", value, ", which is not valid." \
            " The valid list is: ", validValues)

def comparisonCheck(first, relate, second):
    operators = {
        '>': operator.gt,
        '<': operator.lt,
        '>=': operator.ge,
        '<=': operator.le,
        '==': operator.eq
    }
    checkValidation(relate, "relate", tuple(operators.keys()))
    return operators[relate](first, second)

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
