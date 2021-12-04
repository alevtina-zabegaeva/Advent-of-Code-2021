import numpy as np


def check_win(matrix):
    for j in range(tables.shape[1]):
        if sum(matrix[j, :]) == 0:
            return True
    for k in range(tables.shape[2]):
        if sum(matrix[:, k]) == 0:
            return True
    return False


# with open('test4.txt', 'r') as f:
with open('input4.txt', 'r') as f:
    inputs = [[]]
    i = 0
    for line in f:
        if line == '\n':
            i += 1
            inputs.append([])
            continue
        inputs[i].append(line.strip())

numbers = list(map(int, inputs.pop(0)[0].split(',')))
for i, table in enumerate(inputs):
    inputs[i] = [list(map(int, line.split())) for line in table]
tables = np.array(inputs)
marked = np.full(tables.shape, True)
not_win_tables = np.full(tables.shape[0], True)

is_end = False
for n, number in enumerate(numbers):
    for i in range(tables.shape[0]):
        for j in range(tables.shape[1]):
            for k in range(tables.shape[2]):
                if tables[i, j, k] == number:
                    marked[i, j, k] = False
                    if check_win(marked[i]):
                        not_win_tables[i] = False
                        if np.sum(not_win_tables) == 0:
                            is_end = True
                    break
            if is_end:
                break
        if is_end:
            break
    if is_end:
        break

print(np.sum(tables[i] * marked[i]) * number)
