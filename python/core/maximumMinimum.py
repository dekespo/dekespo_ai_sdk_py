from utils import *

import types

def getMaximumMinimumValues(listOfObjects, maximiniValue, criteriaFunction, operator):
    checkType(listOfObjects, list)
    checkNoneValue(maximiniValue, "maximiniValue")
    checkType(criteriaFunction, types.FunctionType)
    chosenObject = None
    for object in listOfObjects:
        localValue = criteriaFunction(object)
        if localValue == "CONTINUE":
            continue
        elif localValue == "BREAK":
            break

        if comparisonCheck(localValue, operator, maximiniValue):
            maximiniValue = localValue
            chosenObject = object
    if not chosenObject:
        eprint("WARNING: chosenObject in getMaximumMinimumValue returns None!")
    return maximiniValue, chosenObject
