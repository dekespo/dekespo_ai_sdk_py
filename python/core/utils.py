from numbers import Number

def checkNumberValue(value):
    if not isinstance(value, Number):
        raise TypeError("Value type ", type(value), " is not a Number type")

def checkType(instance, classType):
    if not isinstance(instance, classType):
        raise TypeError("Mismatch in types: instance = " + type(instance) + "and class = " + type(classType))

def checkPositiveValue(value):
    checkNumberValue(value)
    if value <= 0:
        raise ArithmeticError("Value " + value + " must be larger than 0")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
