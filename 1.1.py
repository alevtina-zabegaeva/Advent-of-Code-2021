with open('input1.txt', 'r') as f:
    inpt = [int(line.strip()) for line in f]

summ = 0
for i in range(1, len(inpt)):
    if inpt[i] > inpt[i - 1]:
        summ += 1
print(summ)

ss = [True for i in range(1, len(inpt)) if inpt[i] > inpt[i - 1]]
s = len(ss)
print(s)
