import sys

from py_ai_sdk import ci_utils

def main():
    command = "python -m coverage run --source=py_ai_sdk/core -m unittest discover -s py_ai_sdk/tests"
    returncode = ci_utils.run_process(command, "Coverage")
    command = "python -m coverage report --show-missing --fail-under=80"
    returncode = ci_utils.run_process(command, "Report check")
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
