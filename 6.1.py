# with open('test6.txt', 'r') as f:
with open('input6.txt', 'r') as f:
    for line in f:
        inpt = list(map(int, line.split(',')))

print(inpt)
days = 80
for day in range(1, days + 1):
    i = 0
    while i < len(inpt):
        if inpt[i] == 0:
            inpt[i] = 6
            inpt.append(9)
        else:
            inpt[i] -= 1
        i += 1
    print(day, inpt)

print(len(inpt))
