f = open("input.txt")
lines = f.readlines()
width, height = [len(lines[0].strip()), len(lines)]

def checkColumn(value, indexValue, index):
    isVisibleTop = True
    isVisibleBottom = True
    for x in range(height):
        data = lines[x].strip()
        if int(data[indexValue]) >= value and index < x:
            isVisibleTop = False
        elif int(data[indexValue]) >= value and index > x:
            isVisibleBottom = False
    return isVisibleTop or isVisibleBottom


def checkRow(value, indexValue, index):
    isVisibleLeft = True
    isVisibleRight = True
    for x in range(width):
        data = lines[index].strip()
        if int(data[x]) >= value and x < indexValue:
            isVisibleLeft = False
        elif int(data[x]) >= value and x > indexValue:
            isVisibleRight = False
    return isVisibleLeft or isVisibleRight

visible = width*2+height*2-4
print(visible)

for i in range(1 , height-1, 1):
    data = lines[i].strip()
    for x in range(1, width-1, 1):
        if checkColumn(int(data[x]), x, i):
            visible += 1
        elif checkRow(int(data[x]), x, i):
            visible += 1


print(visible)