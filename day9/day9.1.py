f = open("test.txt")

currentHpos = (0,0)
currentTpos = currentHpos

def changePositionHead(direction):
    x, y = currentHpos
    if "R" in direction:
        pos = (x+1,y)
        return [pos,checkPositionTail(pos)]
    elif "L" in direction:
        pos = (x-1,y)
        checkPositionTail(pos)
        return [pos,checkPositionTail(pos)]
    elif "U" in direction:
        pos = (x,y-1)
        checkPositionTail(pos)
        return [pos,checkPositionTail(pos)]
    elif "D" in direction:
        pos = (x,y+1)
        return [pos,checkPositionTail(pos)]
        


def checkPositionTail(position):
    x, y = currentTpos
    for n in range(-1,2,1):  
        if [x+n, y-1] == [position[0],position[1]] or [x+n, y+1] == [position[0],position[1]]:
            return currentTpos

    for n in range(-1,2,1):     
        if [x+1, y+n] == [position[0],position[1]] or [x-1, y+n] == [position[0],position[1]]:
            return currentTpos 

    if  currentTpos == position:
        return position

    return currentHpos  

arr = []
for line in f:
    data = line.strip().split(" ")
    for c in range(int(data[1])):
        temp = changePositionHead(data[0])
        currentHpos = temp[0]
        currentTpos = temp[1]
        print(currentHpos)
        arr.append(currentTpos)

arr = set(arr)
print(len(arr))


for aa in range(9):
    print(aa)