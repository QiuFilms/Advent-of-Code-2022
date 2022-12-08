f = open("input.txt")
lines = f.readlines()
width, height = [len(lines[0].strip()), len(lines)]

def checkColumn(value, indexValue, index):
    scoreUp = 0
    for x in range(index-1,-1,-1):
        data = lines[x].strip()
        scoreUp += 1
        if int(data[indexValue]) >= value:
            break
    
    scoreDown = 0
    for x in range(index+1, height, 1):
        data = lines[x].strip()
        scoreDown += 1
        if int(data[indexValue]) >= value:
            break

    return scoreUp*scoreDown

def checkRow(value, indexValue, index):
    scoreLeft = 0
    scoreRight = 0
    for x in range(indexValue-1,-1,-1):
        data = lines[index].strip()
        scoreLeft += 1
        if int(data[x]) >= value:
            break

    for x in range(indexValue+1,width,1):
        data = lines[index].strip()
        scoreRight += 1
        if int(data[x]) >= value:
            break
    return scoreLeft*scoreRight

view = []
for i in range(height):
    data = lines[i].strip()
    for x in range(width):
        result = checkColumn(int(data[x]), x, i)*checkRow(int(data[x]), x, i)
        view.append(result)

view.sort(reverse=True)
print(view[0])