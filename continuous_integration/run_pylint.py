from continuous_integration import utils

def run_pylint():
    modules = utils.get_common_modules()
    command = f"python -m pylint {modules} --rcfile=.pylintrc"
    returncode = utils.run_process(command, "Pylint")
    return returncode
