from itertools import product


with open('input24.txt', 'r') as f:
    commands = [line.strip().split() for line in f]

inputs = product(range(9, 0, -1), repeat=14)

variable = [0, 0, 0, 0]
ind = {'w': 0, 'x': 1, 'y': 2, 'z': 3}
# for input in inputs:
input = '34171911181211'
i = 0
crush = False
for command in commands:
    ind_a = ind[command[1]]
    if command[0] == 'inp':
        print(f'w = {variable[0]}, x = {variable[1]}, y = {variable[2]}, z = {variable[3]}')
        variable[ind_a] = int(input[i])
        i += 1
    else:
        try:
            b = int(command[2])
        except:
            b = variable[ind[command[2]]]
        if command[0] == 'add':
            variable[ind_a] += b
        elif command[0] == 'mul':
            variable[ind_a] *= b
        elif command[0] == 'div':
            if b == 0:
                crush = True
            else:
                variable[ind_a] //= b
        elif command[0] == 'mod':
            if b <= 0 or variable[ind_a] < 0:
                crush = True
            else:
                variable[ind_a] %= b
        else:
            variable[ind_a] = 1 if variable[ind_a] == b else 0
print(f'w = {variable[0]}, x = {variable[1]}, y = {variable[2]}, z = {variable[3]}')
