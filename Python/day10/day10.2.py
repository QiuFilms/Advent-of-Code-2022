f = open("input.txt")

cycle = 1
X = 1
xArr = [X]

for line in f:
    data = line.strip()
    if "addx" in data:
        xArr.append(X)

        X += int(data.split(" ")[1])
        xArr.append(X)
    else:
        xArr.append(X)

screen = []
for i in range(0,6):
    row = list("."*40)
    string=''

    index = 0
    for c in range(40*i,40+40*i):
        sprite = xArr[c]
        if index == sprite or index == sprite-1 or index == sprite+1:
            row[index] = "#"
        index += 1
    screen.append(string.join(row))

for line in screen:
    print(line)