f = open("input.txt")

points = {
    "A" : 1,
    "B" : 2,
    "C" : 3
}


result = 0


for line in f:
    values = line.strip().split(" ")
    
    
    if values[1] == "X":
        if values[0] == "A":
            result += points["C"]
        elif values[0] == "B":
            result += points["A"]
        elif values[0] == "C":
            result += points["B"]
    elif values[1] == "Y":
        if values[0] == "A":
            result += points[values[0]]
        elif values[0] == "B":
            result += points[values[0]]
        elif values[0] == "C":
            result += points[values[0]]
        result += 3
    elif values[1] == "Z":
        if values[0] == "A":
            result += points["B"]
        elif values[0] == "B":
            result += points["C"]
        elif values[0] == "C":
            result += points["A"]
        result += 6
    
print(result)