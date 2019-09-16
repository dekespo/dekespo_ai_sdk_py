import sys
import os

import utils

def main():
    base_command = "python"
    path = "tests/"
    file_names = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))] 
    commands = [base_command + " " + path + next for next in file_names]
    for command in commands:
        returncode = utils.run_process(command, "Test")
        if returncode != utils.RETURN_CODE_OK:
            break
    print("Return code is ", returncode)
    sys.exit(returncode)

if __name__ == "__main__":
    main()
