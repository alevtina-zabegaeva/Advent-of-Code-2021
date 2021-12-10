pairs = ('()', '[]', '{}', '<>')
opens = ('(', '[', '{', '<')
closes = (')', ']', '}', '>')
points = {')': 3, ']': 57, '}': 1197, '>': 25137}


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


def find_error(string):
    for i in opens:
        for j in closes:
            f = string.find(i+j)
            if f != -1:
                return j

# with open('test10.txt', 'r') as f:
with open('input10.txt', 'r') as f:
    inpt = [line.strip() for line in f]

print(inpt)

summ = 0
for line in inpt:
    rline = reduce(line)
    if not isincomplete(rline):
        summ += points[find_error(rline)]
print(summ)
