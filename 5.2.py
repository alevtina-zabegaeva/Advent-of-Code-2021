import re
from collections import Counter


# with open('test5.txt', 'r') as f:
with open('input5.txt', 'r') as f:
    inpt = [list(map(int, re.split(r'[ >,\-]+', line.strip()))) for line in f]

vents = Counter()

for line in inpt:
    x1, y1, x2, y2 = line
    factor_x = 1 if x1 < x2 else -1 if x1 > x2 else 0
    factor_y = 1 if y1 < y2 else -1 if y1 > y2 else 0
    for i in range(max(abs(x1 - x2), abs(y1 - y2)) + 1):
        point = ((x1 + i*factor_x, y1 + i*factor_y),)
        vents.update(point)

overlap = vents - Counter(set(vents))
print(len(overlap))

# for i in range(10):
#     for j in range(10):
#         if vents[(j, i)] > 0:
#             print(vents[(j, i)], end='')
#         else:
#             print('.', end='')
#     print()
