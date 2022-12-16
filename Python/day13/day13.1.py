f = open("input.txt")
file = f.readlines()

pairs = list()
for index, line in enumerate(file):
    line = line.strip()

    if not line:
        continue

    if index == 0:
        pairs.append([line])
    else:
        if len(pairs[-1]) != 2:
            pairs[-1].append(line)
        else:
            pairs.append([line])

def compareSimple(a, b):
    if a < b:
        return True
    return False


def compareComplex(a, b):
    if isinstance(a, int) and isinstance(b, list):
        a = [a]

    if isinstance(a, list) and isinstance(b, int):
        b = [b]
    
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return True 
        if a == b:
            return -1   
        return False
    
    if isinstance(a, list) and isinstance(b, list):
        i = 0
        while i < len(a) and i < len(b):
            test = compareComplex(a[i], b[i])
            if test == True:
                return True
            if test == False:
                return False

            i += 1

        if i == len(a):
            if len(a) == len(b):
                return -1
            return True
        return False

r = 0

for index, pair in enumerate(pairs):
    a, b = map(eval, pair) 
    value = compareComplex(a, b)
    print(a, b, value)
    if value:
        print(index+1)
        r += index+1
print(r)