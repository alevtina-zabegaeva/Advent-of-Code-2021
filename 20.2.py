from functools import reduce
from copy import deepcopy


def make_list(string):
    return [bi[char] for char in string.strip()]


def add_frame(table, char):
    w = 2
    n, m = len(table), len(table[0])
    table_return = [[char]*w + row + [char]*w for row in table]
    for i in range(w):
        table_return.insert(0, [char]*(m+w*2))
        table_return.append([char] * (m + w * 2))
    return table_return


def image_print(table):
    for row in table:
        for element in row:
            print(ch[element], end='')
        print()
    print()


def output_image(table):
    table_return = []
    n, m = len(table), len(table[0])
    for i in range(1, n - 1):
        table_return.append([])
        for j in range(1, m - 1):
            table_return[-1].append(enhancement[make_index(i, j, table)])
    return table_return


def make_index(ii, jj, table):
    nums = table[ii-1][jj-1:jj+2] + table[ii][jj-1:jj+2] + table[ii+1][jj-1:jj+2]
    return reduce(lambda x, y: (x << 1) + y, nums)


def lit(table):
    return sum(sum(row) for row in table)


bi = {'.': 0, '#': 1}
ch = ('.', '#')

# with open('test20.txt', 'r') as f:
with open('input20.txt', 'r') as f:
    inpt = []
    for i, line in enumerate(f):
        if i == 0:
            enhancement = make_list(line)
        elif line.strip() != '':
            inpt.append(make_list(line))
print(enhancement)
# print(inpt)
# image_print(inpt)

flag = enhancement[0]
steps = 50
for step in range(steps):
    inpt = add_frame(inpt, flag*step % 2)
    outpt = output_image(inpt)
    inpt = deepcopy(outpt)
image_print(inpt)
print(lit(inpt))
