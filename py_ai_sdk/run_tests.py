import sys

from py_ai_sdk import ci_utils

def main():
    command = "python -m unittest discover py_ai_sdk/tests"
    returncode = ci_utils.run_process(command, "Unit tests")
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
