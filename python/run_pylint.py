import subprocess
import sys
import os

RETURN_CODE_OK = 0

def run_process(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    stdout, _ = process.communicate()
    stdout = stdout.decode('utf-8')
    returncode = process.returncode
    if returncode != RETURN_CODE_OK:
        print(stdout)
    else:
        print("Pylint is OK")
    return returncode

def main():
    base_command = "python -m pylint"
    folders = ["core", "templates", "tests", "."]
    commands = [base_command + " " + next for next in folders]
    for command in commands:
        returncode = run_process(command)
        if returncode != RETURN_CODE_OK:
            break
    print("Retrun code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
