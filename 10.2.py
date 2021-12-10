pairs = ('()', '[]', '{}', '<>')
opens = ('(', '[', '{', '<')
closes = (')', ']', '}', '>')
points = {'(': 1, '[': 2, '{': 3, '<': 4}

def reduce(string):
    found = True
    while found:
        found = False
        for pair in pairs:
            f = string.find(pair)
            if f != -1:
                string = string[:f] + string[f+2:]
                found = True
    return string


def isincomplete(string):
    return all(string.find(char) == -1 for char in closes)


# with open('test10.txt', 'r') as f:
with open('input10.txt', 'r') as f:
    inpt = [line.strip() for line in f]

print(inpt)

scores = []
for line in inpt:
    rline = reduce(line)
    if isincomplete(rline):
        score = 0
        for char in reversed(rline):
            score *= 5
            score += points[char]
        scores.append(score)
scores.sort()
print(scores[len(scores)//2])
