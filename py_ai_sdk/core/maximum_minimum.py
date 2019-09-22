from py_ai_sdk.core.core_utils import checkType, checkNoneValue, eprint, comparisonCheck

import types

def getMaximumMinimumValues(listOfObjects, maximiniValue, criteriaFunction, operator, **kwargs):
    checkType(listOfObjects, list)
    checkNoneValue(maximiniValue, "maximiniValue")
    checkType(criteriaFunction, types.FunctionType)
    chosenObject = None
    for object in listOfObjects:
        localValue = criteriaFunction(object, **kwargs)
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
