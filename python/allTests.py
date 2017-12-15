import subprocess

if __name__ == "__main__":
    command = "python "
    path = "tests/"
    fileNames = [
        "dimensionsTest",
        "shapesTest"
    ]
    for name in fileNames:
        print("Test Name = ", name)
        process = subprocess.Popen(["python", path + name + ".py"], stdout=subprocess.PIPE)
        process.communicate()[0]
