def check_low(i, j):
    return all([n < inpt[i][j] for n in neighbors(i, j)])


def neighbors(i, j):
    return inpt[i+1][j], inpt[i-1][j], inpt[i][j+1], inpt[i][j-1]


# with open('test9.txt', 'r') as f:
with open('input9.txt', 'r') as f:
    inpt = [[9] + list(map(int, list(line.strip()))) + [9] for line in f]
inpt.insert(0, len(inpt[0]) * [9])
inpt.append(len(inpt[0]) * [9])

summ = 0
for i in range(1, len(inpt) - 1):
    for j in range(1, len(inpt[0]) - 1):
        if check_low(i, j):
            summ += inpt[i][j] + 1
print(summ)
