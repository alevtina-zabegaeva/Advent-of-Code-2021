def print_paper():
    n, m = 0, 0
    for d in dots:
        n = max(n, d[0])
        m = max(m, d[1])
    for i in range(m + 1):
        for j in range(n + 1):
            if (j, i) in dots:
                print('#', end='')
            else:
                print('.', end='')
        print()
    print()


# with open('test13.txt', 'r') as f:
with open('input13.txt', 'r') as f:
    dots = set()
    commands = []
    read_next = False
    for line in f:
        line = line.strip()
        if line == '':
            read_next = True
        elif read_next:
            commands.append(line[11:].split('='))
        else:
            dots.add(tuple(map(int, line.split(','))))

print(len(dots), dots)
print(commands)
# print_paper()
command = commands[0]
along_axis = 0 if command[0] == 'x' else 1
along_value = int(command[1])
new_dots = dots.copy()
for dot in dots:
    if dot[along_axis] > along_value:
        new_dots.remove(dot)
        new_dot = list(dot)
        new_dot[along_axis] = 2*along_value - dot[along_axis]
        new_dots.add(tuple(new_dot))
dots = new_dots.copy()
# print_paper()
print(len(dots))
