from continuous_integration import utils

def run_mypy():
    modules = utils.get_common_modules()
    # TODO: Ignore the applications folder for now
    modules = modules.replace("applications", "")
    # TODO: Ignore the missing imports due to the structure of this repo
    command = f"mypy --ignore-missing-imports {modules}"
    returncode = utils.run_process(command, "mypy")
    return returncode
