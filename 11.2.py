def neighbors_ind(i, j):
    return ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
            (i + 1, j + 1), (i - 1, j - 1), (i - 1, j + 1), (i + 1, j - 1))


def neighbors(i, j):
    return [inpt[ii][jj] for (ii, jj) in neighbors_ind(i, j)]


def print_octopus():
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            print(f'{inpt[i][j]:2}', end='')
        print()
    print()


# with open('test11.txt', 'r') as f:
with open('input11.txt', 'r') as f:
    inpt = [[10] + list(map(int, list(line.strip()))) + [10] for line in f]
n, m = len(inpt), len(inpt[0]) - 2
inpt.insert(0, (m+2) * [10])
inpt.append((m+2) * [10])

print_octopus()
steps = 1000
flashes_sum = 0
for k in range(steps):
    current_flashes = set()
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            inpt[i][j] += 1
            if inpt[i][j] == 10:
                current_flashes.add((i, j))
    flashes_sum += len(current_flashes)
    all_flashes = current_flashes.copy()
    while len(current_flashes) != 0:
        new_flashes = set()
        for i, j in current_flashes:
            for ii, jj in neighbors_ind(i, j):
                if (ii, jj) not in all_flashes:
                    inpt[ii][jj] += 1
                    if inpt[ii][jj] > 9 and 0 < ii <= n and 0 < jj <= m:
                        new_flashes.add((ii, jj))
        current_flashes = new_flashes - all_flashes
        all_flashes |= current_flashes
        flashes_sum += len(current_flashes)
    for i, j in all_flashes:
        inpt[i][j] = 0
    print('Step', k + 1, len(all_flashes), all_flashes)
    print_octopus()
    if len(all_flashes) == n*m:
        break
print(flashes_sum)
