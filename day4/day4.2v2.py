f = open("input.txt")

result = 0

for line in f:
    data = line.strip()
    a, b = data.split(",")[0].split("-")
    a, b = int(a), int(b)

    x, y = data.split(",")[1].split("-")
    x, y = int(x), int(y)

    list1 = []
    list1.extend(range(a, b+1))

    list2 = []
    list2.extend(range(x, y+1))

    if set(list1).intersection(list2):
        result += 1

print(result)