def check_low(i, j):
    return all([n < inpt[i][j] for n in neighbors(i, j)])


def neighbors_ind(i, j):
    return (i+1, j), (i-1, j), (i, j+1), (i, j-1)


def neighbors(i, j):
    return inpt[i+1][j], inpt[i-1][j], inpt[i][j+1], inpt[i][j-1]


# with open('test9.txt', 'r') as f:
with open('input9.txt', 'r') as f:
    inpt = [[9] + list(map(int, list(line.strip()))) + [9] for line in f]
inpt.insert(0, len(inpt[0])*[9])
inpt.append(len(inpt[0])*[9])

low_points = []
for i in range(1, len(inpt) - 1):
    for j in range(1, len(inpt[0]) - 1):
        if check_low(i, j):
            low_points.append((i, j))

basins = []
for i, j in low_points:
    basin = {(i, j)}
    basin_next = basin.copy()
    while True:
        for ii, jj in basin:
            for i_n, j_n in neighbors_ind(ii, jj):
                if inpt[i_n][j_n] != 9:
                    basin_next.add((i_n, j_n))
        if len(basin) == len(basin_next):
            break
        basin = basin_next.copy()
    basins.append(basin)
size_basins = sorted(list(map(len, basins)), reverse=True)
print(size_basins[0] * size_basins[1] * size_basins[2])
