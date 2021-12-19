from itertools import product


def dist(s1, s2):
    return sum(abs(s1[i] - s2[i]) for i in range(3))


def rotate(vector):
    vx, vy, vz = vector[0], vector[1], vector[2]
    r = [(vx, vy, vz), (vx, vz, -vy), (vx, -vy, -vz), (vx, -vz, vy),
         (-vx, -vy, vz), (-vx, vz, vy), (-vx, vy, -vz), (-vx, -vz, -vy)]
    for ii in range(len(r)*2):
        r.append((r[ii][1], r[ii][2], r[ii][0]))
    return r


def match(points1, original_points2):
    for v in range(24):
        points2 = [rotate(o_point2)[v] for o_point2 in original_points2]
        for point2 in points2:
            for point1 in points1:
                move = tuple(point1[k] - point2[k] for k in range(3))
                new_points2 = set(tuple(p2[k] + move[k] for k in range(3)) for p2 in points2)
                inter = set(points1).intersection(new_points2)
                if len(inter) >= 12:
                    return points2, move
    return False


# with open('test19.txt', 'r') as f:
with open('input19.txt', 'r') as f:
    inpt = []
    for line in f:
        if line.strip() == '':
            continue
        elif line.startswith('---'):
            inpt.append([])
        else:
            inpt[-1].append(tuple(map(int, line.strip().split(','))))
print(inpt)

n = len(inpt)
scanners_move = [(0, 0, 0)]*n
rotated_scanners = {0}
checked = set()
while len(rotated_scanners) < n:
    for i in range(n):
        if i not in rotated_scanners:
            continue
        for j in range(1, n):
            if j in rotated_scanners or i == j or (i, j) in checked:
                continue
            result = match(inpt[i], inpt[j])
            checked.add((i, j))
            if result:
                inpt[j] = result[0].copy()
                scanners_move[j] = tuple(scanners_move[i][k] + result[1][k] for k in range(3))
                rotated_scanners.add(j)
print(scanners_move)

dist_max = 0
for s1, s2 in product(scanners_move, scanners_move):
    dist_max = max(dist_max, dist(s1, s2))
print(dist_max)
