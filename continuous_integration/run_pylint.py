from continuous_integration import utils

def run_pylint():
    command = "python -m pylint py_ai_sdk --rcfile=.pylintrc"
    returncode = utils.run_process(command, "Pylint")
    return returncode
