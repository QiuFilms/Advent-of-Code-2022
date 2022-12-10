f = open("input.txt")

cycle = 1
X = 1
xArr = [[1,1]]

for line in f:
    data = line.strip()
    if "addx" in data:
        cycle += 1
        xArr.append([cycle, X])
        cycle += 1

        X += int(data.split(" ")[1])
        xArr.append([cycle, X])
    else:
        cycle += 1
        xArr.append([cycle, X])

screen = []
for i in range(0,6):
    row = list("."*40)
    string=''

    if i == 0:
        for c in range(40*i,40+40*i):
            cycle, sprite = xArr[c]
            if c == sprite or c == sprite-1 or c == sprite+1:
                row[c] = "#"
    else:
        index = 0
        for c in range(40*i,40+40*i+1):
            if c != 240:
                cycle, sprite = xArr[c]
                if index == sprite or index == sprite-1 or index == sprite+1:
                    row[index] = "#"
                index += 1
    screen.append(string.join(row))

for line in screen:
    print(line)