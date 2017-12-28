def checkType(instance, classType):
    if not isinstance(instance, classType):
        raise TypeError("Mismatch in types: instance = " + type(instance) + "and class = " + type(classType))

def checkPositiveValue(value):
    if value <= 0:
        raise ArithmeticError("Value " + value + " must be larger than 0")

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)
