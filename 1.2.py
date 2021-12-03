with open('input1.txt', 'r') as f:
    inpt = [int(line.strip()) for line in f]

step = 3
summ = 0
for i in range(step, len(inpt)):
    if inpt[i] > inpt[i - step]:
        summ += 1
print(summ)

ss = [True for i in range(step, len(inpt)) if inpt[i] > inpt[i - step]]
s = len(ss)
print(s)
