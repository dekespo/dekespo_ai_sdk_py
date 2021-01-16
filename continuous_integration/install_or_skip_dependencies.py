import sys

from continuous_integration import utils


def install_or_skip_dependencies():
    def install_module(command: str, process_name: str) -> int:
        returncode = utils.run_process(command, process_name)
        if returncode != utils.RETURN_CODE_OK:
            sys.exit(-1)
        return returncode

    black_version = "20.8b1"
    coverage_version = "5.3.1"
    mypy_version = "0.790"
    pylint_version = "2.6.0"
    xenon_version = "0.7.1"
    returncode = install_module("pip install pipenv", "pipenv")
    returncode = install_module(f"pipenv install black=={black_version}", "black")
    returncode = install_module("pipenv install codecov", "codecov")
    returncode = install_module(
        f"pipenv install coverage=={coverage_version}", "coverage"
    )
    returncode = install_module(f"pipenv install mypy=={mypy_version}", "mypy")
    returncode = install_module(f"pipenv install pylint=={pylint_version}", "pylint")
    returncode = install_module(f"pipenv install xenon=={xenon_version}", "xenon")
    return returncode
