f = open("input.txt")
tree = {"files":[]}

currentDir = tree
currentDirNames = []

def getPrevious():
    result = tree
    for letter in currentDirNames:
        result = result[letter]
    return result


for line in f:
    data = line.strip()
    if "$ cd" in data:
        key = data.split(" ")[2]
        if "/" in data:
            currentDir = tree
        elif ".." in data:
            currentDirNames.pop()
            currentDir = getPrevious()
        else:
            if key not in currentDir:
                currentDir[key] = {}
                currentDirNames.append(key)

            currentDir = currentDir[key]
    elif "$ ls" not in data and "dir" not in data:
        if "files" not in currentDir:
            currentDir["files"] = []
        currentDir["files"].append([data.split(" ")[1], data.split(" ")[0]])

dirs = []
def countDirSize(param):
    size = 0
    for key in param:
        if "files" in key:
            for file in param["files"]:
                size += int(file[1])
        else:
            num = countDirSize(param[key])
            size += num
            dirs.append([key, num])
    return size           

space = 30000000
total = 70000000
free = 70000000 - countDirSize(tree)
needed = 30000000 - free

result = 0
sorted(dirs,  key=lambda x: x[1])
for line in dirs:
    if line[1] >= needed:
        result += line[1]
        break

print(result)
