f = open("input.txt")

currentHpos = (0,0)
currentTpos = currentHpos
allTails = [(0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0), (0,0)]

def changePositionHead(direction):
    x, y = currentHpos
    tempArray = []
    if "R" in direction:
        pos = (x+1,y)
        for h in range(9):
            if h == 0:
               tempArray.append(checkPositionTail(pos, h, direction)) 
            else:
                tempArray.append(checkPositionTail(tempArray[h-1], h, direction))
        return [pos,tempArray]
    elif "L" in direction:
        pos = (x-1,y)
        for h in range(9):
            if h == 0:
               tempArray.append(checkPositionTail(pos, h, direction)) 
            else:
                tempArray.append(checkPositionTail(tempArray[h-1], h, direction))
        return [pos,tempArray]
    elif "U" in direction:
        pos = (x,y-1)
        for h in range(9):
            if h == 0:
               tempArray.append(checkPositionTail(pos, h, direction)) 
            else:
                tempArray.append(checkPositionTail(tempArray[h-1], h, direction))
        return [pos,tempArray]
    elif "D" in direction:
        pos = (x,y+1)
        for h in range(9):
            if h == 0:
               tempArray.append(checkPositionTail(pos, h, direction)) 
            else:
                tempArray.append(checkPositionTail(tempArray[h-1], h, direction))
        return [pos,tempArray]




def checkPositionTail(position, index, letter):
    x, y = allTails[index]
    for n in range(-1,2,1):  
        if [x+n, y-1] == [position[0],position[1]] or [x+n, y+1] == [position[0],position[1]]:
            return allTails[index]

    for n in range(-1,2,1):     
        if [x+1, y+n] == [position[0],position[1]] or [x-1, y+n] == [position[0],position[1]]:
            return allTails[index] 

    if allTails[index] == position:
        return position

    if index == 0:
        return currentHpos

    nx, ny = (0,0)
    if x > position[0]:
        nx = x - 1
    elif x < position[0]:
        nx = x + 1
    else:
        nx = x
    
    if y > position[1]:
        ny = y-1
    elif y < position[1]:
        ny = y+1
    else:
        ny = y
    
    return (nx,ny) 



arr = []
for line in f:
    data = line.strip().split(" ")
    for c in range(int(data[1])):
        temp = changePositionHead(data[0])
        currentHpos = temp[0]
        allTails = temp[1]
        arr.append(allTails[8])

arr = set(arr)
print(len(arr))

