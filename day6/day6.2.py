f = open("input.txt")

searched = 14
index = searched-1
for line in f:
    data = line.strip()
    for x in range(len(line)):
        if x < len(line)-searched-1:
            index += 1
            check = list(dict.fromkeys(line[x:x+searched]))
            if len(check) == searched:
                break

print(index)