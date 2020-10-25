from continuous_integration import utils


def run_black():
    modules = utils.get_common_modules()
    command = f"black --check {modules}"
    returncode = utils.run_process(command, "black")
    return returncode
