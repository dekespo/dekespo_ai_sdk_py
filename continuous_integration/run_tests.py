from continuous_integration import utils

def run_tests():
    sources = ",".join([
        "py_ai_sdk/core",
        "py_ai_sdk/algorithms"
    ])
    command = f"python -m coverage run --source={sources} -m unittest " \
    "discover -s py_ai_sdk/tests"
    returncode = utils.run_process(command, "Tests with Coverage")
    command = "python -m coverage report --show-missing --fail-under=90"
    returncode = utils.run_process(command, "Coverage Report check")
    return returncode
