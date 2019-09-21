import sys
import os

from py_ai_sdk import ci_utils

def main():
    path = "py_ai_sdk/tests/"
    base_command = "python -m unittest " + path.replace("/", ".")
    file_names = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    commands = [base_command + ci_utils.remove_extension_if_exists(file,".py") for file in file_names]
    for command in commands:
        print(command)
        returncode = ci_utils.run_process(command, "Test")
        if returncode != ci_utils.RETURN_CODE_OK:
            break
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
