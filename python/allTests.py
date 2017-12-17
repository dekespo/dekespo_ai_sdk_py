import subprocess
from os import listdir
from os.path import isfile, join

if __name__ == "__main__":
    command = "python "
    path = "tests/"
    fileNames = [file for file in listdir(path) if isfile(join(path, file))] 
    for fileName in fileNames:
        print("Test Name = ", fileName)
        process = subprocess.Popen(["python", path + fileName], stdout=subprocess.PIPE)
        process.communicate()[0]
