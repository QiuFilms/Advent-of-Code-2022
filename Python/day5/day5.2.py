f = open("input.txt")

result = ""
stack = [
    ["G","J","W","R","F","T","Z"],
    ["M","W","G"],
    ["G","H","N","J"],
    ["W","N","C","R","J"],
    ["M","V","Q","G","B","S","F","W"],
    ["C","W","V","D","T","R","S"],
    ["V","G","Z","D","C","N","B","H"],
    ["C","G","M","N","J","S"],
    ["L","D","J","C","W","N","P","G"]
]


for line in f:
    data = line.strip()
    arr = data.split(" ")

    count = int(arr[1])
    moveFrom = int(arr[3])-1
    moveTo = int(arr[5])-1
    for x in range(0, count, 1):
        stack[moveTo].insert(x,stack[moveFrom][0])
        stack[moveFrom].remove(stack[moveFrom][0])

for create in stack:
    result += create[0]
print(result)