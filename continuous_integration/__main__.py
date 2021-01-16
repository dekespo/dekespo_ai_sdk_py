import argparse
import sys

from continuous_integration.install_or_skip_dependencies import (
    install_or_skip_dependencies,
)
from continuous_integration import utils

MODULES = utils.get_common_modules()


def check_all_code_analysis() -> int:
    # The order matters here
    returncode = utils.RETURN_CODE_OK
    returncode = returncode or run_black()
    returncode = returncode or run_pylint()
    returncode = returncode or run_xenon()
    returncode = returncode or run_mypy()
    return returncode


def parse_argurments() -> argparse.Namespace:
    parser = argparse.ArgumentParser("Continous Integration Tools")
    parser.add_argument("--black", action="store_true")
    parser.add_argument("--check_all_code_analysis", action="store_true")
    parser.add_argument("--install_or_skip_dependencies", action="store_true")
    parser.add_argument("--mypy", action="store_true")
    parser.add_argument("--pylint", action="store_true")
    parser.add_argument("--tests", action="store_true")
    parser.add_argument("--xenon", action="store_true")
    return parser.parse_args()


def run_black() -> int:
    command = f"black --check {MODULES}"
    returncode = utils.run_process(command, "black")
    return returncode


def run_mypy() -> int:
    command = f"mypy {MODULES}"
    returncode = utils.run_process(command, "mypy")
    return returncode


def run_pylint() -> int:
    command = f"pylint {MODULES} --rcfile=.pylintrc"
    returncode = utils.run_process(command, "Pylint")
    return returncode


def run_tests() -> int:
    command = "coverage run --source=dekespo_ai_sdk -m unittest"
    returncode = utils.run_process(command, "Tests with Coverage")
    command = "coverage report --show-missing --fail-under=90"
    returncode = utils.run_process(command, "Coverage Report check")
    return returncode


def run_xenon() -> int:
    command = f"xenon -bB -mA -aA {MODULES}"
    returncode = utils.run_process(command, "xenon")
    return returncode


def main():
    arguments = parse_argurments()
    returncode = utils.RETURN_CODE_ERROR
    if arguments.black:
        returncode = run_black()
    elif arguments.check_all_code_analysis:
        returncode = check_all_code_analysis()
    elif arguments.install_or_skip_dependencies:
        returncode = install_or_skip_dependencies()
    elif arguments.mypy:
        returncode = run_mypy()
    elif arguments.pylint:
        returncode = run_pylint()
    elif arguments.tests:
        returncode = run_tests()
    elif arguments.xenon:
        returncode = run_xenon()
    print("Return code is ", returncode)
    sys.exit(returncode)


if __name__ == "__main__":
    main()
