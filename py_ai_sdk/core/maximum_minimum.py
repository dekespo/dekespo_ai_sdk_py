import types

from py_ai_sdk.core.core_utils import checkType, checkNoneValue, eprint, comparisonCheck

def getMaximumMinimumValues(list_dim2Ds, maximiniValue, criteriaFunction, operator, **kwargs):
    checkType(list_dim2Ds, list)
    checkNoneValue(maximiniValue, "maximiniValue")
    checkType(criteriaFunction, types.FunctionType)
    chosen_dim2D = None
    for dim2D in list_dim2Ds:
        localValue = criteriaFunction(dim2D, **kwargs)
        if localValue == "CONTINUE":
            continue
        elif localValue == "BREAK":
            break

        if comparisonCheck(localValue, operator, maximiniValue):
            maximiniValue = localValue
            chosen_dim2D = dim2D
    if not chosen_dim2D:
        eprint("WARNING: chosen_dim2D in getMaximumMinimumValue returns None!")
    return maximiniValue, chosen_dim2D
