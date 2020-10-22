import sys

from continuous_integration import utils

def install_or_skip_dependencies():
    def install_module(command, process_name):
        returncode = utils.run_process(command, process_name)
        if returncode != utils.RETURN_CODE_OK:
            sys.exit(-1)
        return returncode

    pylint_version = "2.3.1"
    coverage_version = "4.5.4"
    mypy_version = "0.790"
    returncode = install_module("sudo pip install pipenv", "pipenv")
    returncode = install_module(f"pipenv install pylint=={pylint_version}", "pylint")
    returncode = install_module(f"pipenv install coverage=={coverage_version}", "coverage")
    returncode = install_module(f"pipenv install mypy=={mypy_version}", "mypy")
    returncode = install_module("pipenv install codecov", "codecov")
    return returncode
