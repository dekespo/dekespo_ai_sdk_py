import sys

from py_ai_sdk import ci_utils

def main():
    sources = ",".join([
        "py_ai_sdk/core",
        "py_ai_sdk/algorithms"
    ])
    command = f"python -m coverage run --source={sources} -m unittest " \
    "discover -s py_ai_sdk/tests"
    # "discover -s py_ai_sdk/tests/algorithms"
    returncode = ci_utils.run_process(command, "Tests with Coverage")
    command = "python -m coverage report --show-missing --fail-under=80"
    returncode = ci_utils.run_process(command, "Coverage Report check")
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
