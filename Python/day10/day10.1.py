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


cycles = [20,60,100,140,180,220]

signalStrength = 0
for c in cycles:
    signalStrength += xArr[c-1]*c
print(signalStrength)