from collections import Counter


# with open('test14.txt', 'r') as f:
with open('input14.txt', 'r') as f:
    rules = {}
    polymer_template = []
    read_next = False
    for line in f:
        line = line.strip()
        if line == '':
            read_next = True
        elif not read_next:
            polymer_template = list(line)
        else:
            line = line.split(' -> ')
            rules[line[0]] = line[1]

print(rules)
print(polymer_template)

steps = 10
for step in range(steps):
    new_template = [polymer_template[0]]
    for i in range(len(polymer_template) - 1):
        new_template.append(rules[polymer_template[i] + polymer_template[i + 1]])
        new_template.append(polymer_template[i + 1])
    polymer_template = new_template.copy()
    # print(step + 1, ''.join(polymer_template))

count = Counter(polymer_template)
count = count.most_common()
print(count[0][1] - count[-1][1])

