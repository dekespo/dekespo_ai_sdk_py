import subprocess

RETURN_CODE_OK = 0
RETURN_CODE_ERROR = 1


def run_process(command, process_name):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    stdout = stdout.decode("utf-8")
    returncode = process.returncode
    if returncode != RETURN_CODE_OK:
        print(stdout)
    else:
        print(process_name + " -> OK")
    return returncode


# TODO: Delete this function?
def remove_extension_if_exists(string, extension):
    if string.endswith(extension):
        return string[: -len(extension)]
    return string


def get_common_modules() -> str:
    return " ".join(
        [
            "dekespo_ai_sdk",
            "tests",
            "continuous_integration",
        ]
    )
