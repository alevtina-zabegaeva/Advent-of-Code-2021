import re


def is_intersected(c1, c2):
    x11, x12, y11, y12, z11, z12 = c1
    x21, x22, y21, y22, z21, z22 = c2
    return (x11 <= x22 and x21 <= x12 and
            y11 <= y22 and y21 <= y12 and
            z11 <= z22 and z21 <= z12)


def find_intersection(c1, c2):
    x11, x12, y11, y12, z11, z12 = c1
    x21, x22, y21, y22, z21, z22 = c2
    return (max(x11, x21), min(x12, x22),
            max(y11, y21), min(y12, y22),
            max(z11, z21), min(z12, z22))  # cuboid


def sub_intersection(c1, c2):
    x11, x12, y11, y12, z11, z12 = c1
    x21, x22, y21, y22, z21, z22 = c2
    candidate = [(x11, x12, y11, y12, z11, z21-1), (x11, x12, y11, y12, z22+1, z12),
                 (x11, x12, y11, y21-1, z21, z22), (x11, x12, y22+1, y12, z21, z22),
                 (x11, x21-1, y21, y22, z21, z22), (x22+1, x12, y21, y22, z21, z22)]
    to_return = []
    for cuboid in candidate:
        if cuboid[0] <= cuboid[1] and cuboid[2] <= cuboid[3] and cuboid[4] <= cuboid[5]:
            to_return.append(cuboid)
    return to_return  # list of cuboids


def sub_cuboid(c1, c2):
    if not is_intersected(c1, c2):
        return [c1]
    c3 = find_intersection(c1, c2)  # cuboid
    c4 = sub_intersection(c1, c3)  # list of cuboids
    return c4  # list of cuboids


def cubes(list_of_cuboids):
    sum = 0
    for c in list_of_cuboids:
        sum += (c[1] - c[0] + 1) * (c[3] - c[2] + 1) * (c[5] - c[4] + 1)
    return sum


def addition(list_of_cuboids, c0):
    sum_cuboids = []
    for c in list_of_cuboids:
        sum_cuboids.extend(sub_cuboid(c, c0))
    sum_cuboids.append(c0)
    return sum_cuboids


def subtraction(list_of_cuboids, c0):
    sum_cuboids = []
    for c in list_of_cuboids:
        sum_cuboids.extend(sub_cuboid(c, c0))
    return sum_cuboids


# with open('test22.2.txt', 'r') as f:
with open('input22.txt', 'r') as f:
    inpt = []
    for line in f:
        line = line.strip().split(' x=')
        line[1] = tuple(map(int, re.split(r'[,xyz=\.]+', line[1])))
        inpt.append(line)

print(inpt)
result = [inpt[0][1]]
for i in range(1, len(inpt)):
    if inpt[i][0] == 'on':
        result = addition(result, inpt[i][1])
    else:
        result = subtraction(result, inpt[i][1])
    # print(result)
print(cubes(result))
