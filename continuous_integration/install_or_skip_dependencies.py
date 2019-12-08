import sys

from continuous_integration import utils

def install_or_skip_dependencies():
    pylint_version = "2.3.1"
    coverage_version = "4.5.4"
    command = "sudo pip install pipenv"
    returncode = utils.run_process(command, "Pipenv")
    if returncode != utils.RETURN_CODE_OK:
        sys.exit(-1)
    command = f"pipenv install pylint=={pylint_version}"
    returncode = utils.run_process(command, "Pipenv")
    if returncode != utils.RETURN_CODE_OK:
        sys.exit(-1)
    command = f"pipenv install coverage=={coverage_version}"
    returncode = utils.run_process(command, "Pipenv")
    if returncode != utils.RETURN_CODE_OK:
        sys.exit(-1)
    command = "pipenv install codecov"
    returncode = utils.run_process(command, "Pipenv")
    return returncode
