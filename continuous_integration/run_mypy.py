from continuous_integration import utils

def run_mypy():
    modules = utils.get_common_modules()
    command = f"mypy {modules}"
    returncode = utils.run_process(command, "mypy")
    return returncode
