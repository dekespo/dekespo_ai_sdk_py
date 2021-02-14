import subprocess

RETURN_CODE_OK: int = 0

def run_process(command: str, process_name: str) -> int:
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    stdout, stderr = process.communicate()
    stdout = stdout.decode("utf-8")
    returncode = process.returncode
    if returncode != RETURN_CODE_OK:
        print(stdout)
        print(stderr)
    else:
        print(process_name + " -> OK")
    return returncode

def main():
    returncode: int = RETURN_CODE_OK
    command: str = "rm -rf build dist dekespo_ai_sdk.egg-info"
    returncode = returncode or run_process(command, "clean pypi leftover")
    command = "pipenv run python setup.py sdist bdist_wheel"
    returncode = returncode or run_process(command, "Create the new SDK version")
    # TODO: Make sure to communicate via subprocess for twine
    # command = "pipenv run python -m twine upload dist/*"
    # returncode = returncode or run_process(command, "Upload the new SDK version")
    return returncode

# TODO: Install Twine module beforehand
if __name__ == '__main__':
    if main() != RETURN_CODE_OK:
        print("Error in uploading SDK")
    else:
        print("Run 'pipenv run python -m twine upload dist/*' to complete the upload")
