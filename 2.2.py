with open('input2.txt', 'r') as f:
    inpt = []
    for line in f:
        command, X = line.strip().split()
        inpt.append((command, int(X)))

depth = 0
horizontal_position = 0
aim = 0

for line in inpt:
    if line[0] == 'forward':
        horizontal_position += line[1]
        depth += aim * line[1]
    elif line[0] == 'down':
        aim += line[1]
    else:
        aim -= line[1]
print(horizontal_position, depth, horizontal_position*depth)
