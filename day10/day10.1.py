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


cycles = [20,60,100,140,180,220]

signalStrength = 0
for c in cycles:
    signalStrength += xArr[c-1][1]*c
print(signalStrength)