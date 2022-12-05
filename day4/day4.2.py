f = open("input.txt")

result = 0

for line in f:
    data = line.strip()
    a, b = data.split(",")[0].split("-")
    a, b = int(a), int(b)

    x, y = data.split(",")[1].split("-")
    x, y = int(x), int(y)
    if x <= b and y >= a:
        result += 1


print(result)