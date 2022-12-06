f = open("input.txt")

letters = []
index = 3
for line in f:
    data = line.strip()
    for x in range(len(line)):
        if x < len(line)-3:
            index += 1
            check = list(dict.fromkeys(line[x:x+4]))
            if len(check) == 4:
                break

        

print(index)