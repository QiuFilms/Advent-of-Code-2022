import string
alphabet = list(string.ascii_lowercase) + list(string.ascii_uppercase)

f = open("input.txt")

result = 0
for line in f:
    data = line.strip()
    compartment_1 = data[:int(len(data)/2)]
    compartment_2 = data[int(len(data)/2):len(data)]
    letter = list(set(compartment_1).intersection(compartment_2))
    result += alphabet.index(letter[0])+1

print(result)