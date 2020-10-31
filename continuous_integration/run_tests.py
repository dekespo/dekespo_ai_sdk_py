from continuous_integration import utils


def run_tests():
    command = f"python -m coverage run --source=dekespo_ai_sdk -m unittest "
    returncode = utils.run_process(command, "Tests with Coverage")
    command = "python -m coverage report --show-missing --fail-under=90"
    returncode = utils.run_process(command, "Coverage Report check")
    return returncode
