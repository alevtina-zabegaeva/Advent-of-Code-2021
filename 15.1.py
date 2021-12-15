from collections import defaultdict

# with open('test15.txt', 'r') as f:
with open('input15.txt', 'r') as f:
    inpt = [list(map(int, list(line.strip()))) for line in f]

n, m = len(inpt), len(inpt[0])

ways = defaultdict(int)
#     i  j    sum
ways[(0, 0)] = 0
steps = ((1, 0), (-1, 0), (0, 1), (0, -1))
for k in range(n*m):
    new_ways = ways.copy()
    for way, s in ways.items():
        for step in steps:
            ii, jj = way[0] + step[0], way[1] + step[1]
            if 0 <= ii < n and 0 <= jj < m:
                new_s = s + inpt[ii][jj]
                if ((ii, jj) in new_ways and new_s < new_ways[(ii, jj)] or
                        (ii, jj) not in new_ways):
                    new_ways[(ii, jj)] = new_s
    if ways == new_ways:
        break
    ways = new_ways.copy()
    # print(k+1, len(ways), ways)
print(ways[(n-1, m-1)])

"""
import matplotlib.pyplot as plt
import numpy as np
inpt = np.array(inpt)

z = inpt
nrows, ncols = z.shape
x = np.linspace(0, ncols - 1, ncols)
y = np.linspace(0, nrows - 1, nrows)
x, y = np.meshgrid(x, y)

# ax = fig.add_subplot(projection='3d')
# ax.plot_surface(x, y, z)
fig, ax = plt.subplots()
im = ax.imshow(z)
# for i in range(len(x)):
#     for j in range(len(y)):
#         text = ax.text(j, i, z[i, j],
#                        ha="center", va="center", color="w")

fig.tight_layout()
plt.show()
"""
