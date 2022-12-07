f = open("test.txt")
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
    dirSize = 0
    for key in param:
        if "files" in key:
            for file in param["files"]:
                size += int(file[1])
        else:
            num = countDirSize(param[key])
            size += num
            dirSize = num
            dirs.append([key, dirSize])
    return size           

countDirSize(tree)
print(countDirSize(tree))


result = 0
for line in dirs:
    if line[1] <= 100000:
        result += line[1]

print(result)