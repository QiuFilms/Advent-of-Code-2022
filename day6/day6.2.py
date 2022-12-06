f = open("test.txt")

letters = []
index = 13
for line in f:
    data = line.strip()
    for x in range(len(line)):
        if x < len(line)-13:
            index += 1
            check = list(dict.fromkeys(line[x:x+14]))
            if len(check) == 14:
                break

        

print(index)