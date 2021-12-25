import re
from itertools import product


def cuboid(n):
    x1, x2, y1, y2, z1, z2 = n
    m = 50
    if x2 < -m or y2 < -m or z2 < -m or x1 > m or y1 > m or z1 > m:
        return set()
    x1, x2 = max(x1, -m), min(x2, m)
    y1, y2 = max(y1, -m), min(y2, m)
    z1, z2 = max(z1, -m), min(z2, m)
    return set(product(range(x1, x2+1), range(y1, y2+1), range(z1, z2+1)))


# with open('test22.txt', 'r') as f:
with open('input22.txt', 'r') as f:
    inpt = []
    for line in f:
        line = line.strip().split(' x=')
        line[1] = tuple(map(int, re.split(r'[,xyz=\.]+', line[1])))
        inpt.append(line)

cubes = set()
print(inpt)
for line in inpt:
    cube = cuboid(line[1])
    if line[0] == 'on':
        cubes |= cube
    else:
        cubes -= cube
print(len(cubes))
