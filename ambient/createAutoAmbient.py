import os

current_path = os.getcwd()
dir_paths = list(map(lambda x: os.path.join(current_path, x), ["src", "resources"]))

for path in dir_paths:
    isExist = os.path.exists(path)
    if not isExist:
        os.makedirs(path)
        print(f"{path} is created")

filePaths = list(
    map(lambda x: os.path.join(current_path, x), ["mainModel.py", "runModel.py"])
)
for path in filePaths:
    adress = os.path.join(dir_paths[0], path.replace("Model", ""))
    with open(path, "rb") as Modelf:
        with open(adress, "w") as f:
            # write the content of the file in the new file
            f.write(Modelf.read().decode("utf-8"))
