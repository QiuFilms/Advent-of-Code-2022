import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

f = open("input.txt")
lines = f.readlines()

result = 0
for x in range(0,len(lines)-1,3):
    line1 = lines[x].strip()
    line2 = lines[x+1].strip()
    line3 = lines[x+2].strip()

    list1 = set(line1).intersection(line2)
    list2 = set(line2).intersection(line3)
    final = list(list1.intersection(list2))
    result += alphabet.index(final[0])+1

print(result)
