with open('input2.txt', 'r') as f:
    inpt = [line.strip().split() for line in f]

depth = 0
horizontal_position = 0

for i in range(len(inpt)):
    if inpt[i][0] == 'forward':
        horizontal_position += int(inpt[i][1])
    elif inpt[i][0] == 'down':
        depth += int(inpt[i][1])
    else:
        depth -= int(inpt[i][1])
print(horizontal_position, depth, horizontal_position*depth)
