f = open("input.txt")

result = []
count = 0
for line in f:
    data = line.strip()
    if not data:
        result.append(count)
        count = 0
    else:
        count += int(data)
        
result.sort(reverse=True)
print(sum(result[:3]))