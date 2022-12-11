f = open("test.txt")

monkeys = {}

key = ""
modd = 1
for line in f:
    data = line.strip()
    if "Monkey" in data:
        key = data.split(" ")[0] + data.split(" ")[1][0:1]
        monkeys[key] = {}
        monkeys[key]["Inspected"] = 0
    elif data:
        subKey, value  = data.split(":")

        if "Starting" in subKey:
            value = value.strip()
            value = "".join(value.split(" ")).split(",")
            monkeys[key]["Items"] = value

        if "Operation" in subKey:
            value = value.strip().split(" ")
            monkeys[key]["Operation"] = value[-2:]

        if "Test" in subKey:
            monkeys[key]["Test"] = {}
            monkeys[key]["Test"]["Divisible"] = int(value.strip().split(" ")[2])
            modd *= monkeys[key]["Test"]["Divisible"]
        if "If" in subKey:
            value = value.strip().split(" ")
            if "true" in subKey:
                monkeys[key]["Test"]["True"] = value[-1]
            else:
                monkeys[key]["Test"]["False"] = value[-1]

def monkeyTurn(monkey):
    for item in monkey["Items"]:
        monkey["Inspected"] += 1
        worryLevel = calculateWorryLevel(int(item), monkey)
        divideBy = monkey["Test"]["Divisible"]

        worryLevel %= modd
        if worryLevel % divideBy == 0:
            monkeys["Monkey"+monkey["Test"]["True"]]["Items"].append(worryLevel)
        else: 
            monkeys["Monkey"+monkey["Test"]["False"]]["Items"].append(worryLevel)
    monkey["Items"] = []


def calculateWorryLevel(worryLevel, monkey):
    operation, variable = monkey["Operation"] 
    value = worryLevel
    if "old" not in variable:
        value = int(variable)
    
    if "+" in operation:
        return (worryLevel+value)
    if "-" in operation:
        return (worryLevel-value)
    return (worryLevel*value)


rounds = []

for x in range(20):
    for monkey in monkeys.keys():
        monkeyTurn(monkeys[monkey])
    rounds.append(monkeys)

mostActive = []
for r in rounds[-1]:
    mostActive.append(int(monkeys[r]["Inspected"]))

mostActive.sort(reverse=True)
print(mostActive[0]*mostActive[1])