from continuous_integration import utils

def run_pylint():
    modules = " ".join([
        "core",
        "tests",
        "templates",
        "draw",
        "applications",
        "continuous_integration",
        "physics",
        "algorithms"
    ])
    command = f"python -m pylint {modules} --rcfile=.pylintrc"
    returncode = utils.run_process(command, "Pylint")
    return returncode
