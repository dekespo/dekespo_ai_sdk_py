import sys

from py_ai_sdk import ci_utils

def main():
    command = "python -m pylint py_ai_sdk --rcfile=py_ai_sdk/.pylintrc"
    returncode = ci_utils.run_process(command, "Pylint")
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
