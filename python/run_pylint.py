import sys

import ci_utils

def main():
    base_command = "python -m pylint"
    folders = ["core", "templates", "tests", "."]
    commands = [base_command + " " + next for next in folders]
    for command in commands:
        returncode = ci_utils.run_process(command, "Pylint")
        if returncode != ci_utils.RETURN_CODE_OK:
            break
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
