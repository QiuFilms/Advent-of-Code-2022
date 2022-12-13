f = open("input.txt")

points = {
    "X" : 1,
    "Y" : 2,
    "Z" : 3
}


result = 0


for line in f:
    values = line.strip().split(" ")
    if values[0] == "A":
        if values[1] == "X":
            result += points[values[1]] + 3
        elif values[1] == "Y":
            result += points[values[1]] + 6
        elif values[1] == "Z":
            result += points[values[1]]
    elif values[0] == "B":
        if values[1] == "X":
            result += points[values[1]]
        elif values[1] == "Y":
            result += points[values[1]] + 3
        elif values[1] == "Z":
            result += points[values[1]] + 6
    elif values[0] == "C":
        if values[1] == "X":
            result += points[values[1]] + 6
        elif values[1] == "Y":
            result += points[values[1]]
        elif values[1] == "Z":
            result += points[values[1]] + 3
    
print(result)