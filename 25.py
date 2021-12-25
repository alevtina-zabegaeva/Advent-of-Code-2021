from copy import deepcopy


def print_map(input_map):
    for row in input_map:
        for char in row:
            print(char, end='')
        print()
    print()


def copy_map(input_map, c):
    new_map = []
    for row in input_map:
        new_map.append([])
        for char in row:
            if char == c:
                new_map[-1].append(char)
            else:
                new_map[-1].append('.')
    return new_map


# with open('test25.txt', 'r') as f:
with open('input25.txt', 'r') as f:
    cucumbers = [list(line.strip()) for line in f]

print_map(cucumbers)
n, m = len(cucumbers), len(cucumbers[0])

step = 0
move = True
while move:
    move = False
    new_cucumbers = copy_map(cucumbers, 'v')
    for i, row in enumerate(cucumbers):
        for j, char in enumerate(row):
            if char == '>':
                next_j = (j+1) % m
                if row[next_j] == '.':
                    new_cucumbers[i][next_j] = '>'
                    move = True
                else:
                    new_cucumbers[i][j] = '>'
    cucumbers = deepcopy(new_cucumbers)
    new_cucumbers = copy_map(cucumbers, '>')
    for i, row in enumerate(cucumbers):
        for j, char in enumerate(row):
            if char == 'v':
                next_i = (i+1) % n
                if cucumbers[next_i][j] == '.':
                    new_cucumbers[next_i][j] = 'v'
                    move = True
                else:
                    new_cucumbers[i][j] = 'v'
    cucumbers = deepcopy(new_cucumbers)
    step += 1

print(f'After step {step}')
print_map(cucumbers)
