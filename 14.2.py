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
            polymer_template = line
        else:
            line = line.split(' -> ')
            rules[line[0]] = line[1]
print(polymer_template)

pairs = Counter()
for i in range(len(polymer_template) - 1):
    pairs.update([polymer_template[i] + polymer_template[i + 1]])
print('pairs =', pairs)

rules_pairs = {}
for pair, letter in rules.items():
    rules_pairs[pair] = (pair[0] + letter, letter + pair[1])
print('rules_pairs =', rules_pairs)

steps = 40
for step in range(steps):
    pairs_next = Counter()
    for pair, count in pairs.items():
        for p in rules_pairs[pair]:
            pairs_next[p] += count
    pairs = pairs_next.copy()
print('pairs =', pairs)

letters = Counter()
for pair, count in pairs.items():
    letters[pair[0]] += count
    letters[pair[1]] += count
print('letters = ', letters)
for letter, count in letters.items():
    letters[letter] //= 2
    if letter == polymer_template[0] or letter == polymer_template[-1]:
        letters[letter] += 1
print('correct letters = ', letters)
count = letters.most_common()
print(count[0][1] - count[-1][1])
