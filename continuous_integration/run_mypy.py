from continuous_integration import utils


def run_mypy():
    command = "mypy dekespo_ai_sdk"
    returncode = utils.run_process(command, "mypy")
    return returncode
