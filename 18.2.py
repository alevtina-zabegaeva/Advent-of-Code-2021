import re
from itertools import product


def explode(n):
    found = False
    count = 0
    for i, char in enumerate(n):
        if char == '[':
            count += 1
        elif char == ']':
            count -= 1
        if count >= 5:
            found = True
            break
    if found:
        start = i
        end = n[start:].find(']') + i + 1
        n0 = n[start:end][1:-1].split(',')
        n1, n2 = int(n0[0]), int(n0[1])
        n_left, n_right = n[:start], n[end:]

        def repl_r(matchobj):
            return str(int(matchobj.group()) + n2)

        n_right = re.sub('\d+', repl_r, n_right, count=1)

        def repl_l(matchobj):
            return str(int(matchobj.group()[::-1]) + n1)[::-1]

        n_left = re.sub('\d+', repl_l, n_left[::-1], count=1)[::-1]

        n = f'{n_left}0{n_right}'
    return n


def split(n):
    match = re.search('\d{2,}', n)
    if match:
        n0 = int(match.group())
        n = f'{n[:match.start()]}[{n0//2},{n0-n0//2}]{n[match.end():]}'
    return n


def magnitude(n):
    while True:
        match = re.search('\[[^[\]]+]', n)
        if match:
            n0 = match.group()[1:-1].split(',')
            n1, n2 = int(n0[0]), int(n0[1])
            n = f'{n[:match.start()]}{3 * n1 + n2 * 2}{n[match.end():]}'
        else:
            n = int(n)
            return n


def add_str(n1, n2):
    return f'[{n1},{n2}]'


def snail_addition(n1, n2):
    n = add_str(n1, n2)
    exploded, splitted = True, True
    while exploded or splitted:
        exploded, splitted = False, False
        while True:
            n_next = explode(n)
            if n_next == n:
                break
            exploded = True
            n = n_next
        n_next = split(n)
        if n_next != n:
            splitted = True
            n = n_next
    return n


# with open('test18.txt', 'r') as f:
with open('input18.txt', 'r') as f:
    inpt = [line.strip() for line in f]
print(inpt)

max_magnitude = 0
for number1, number2 in product(inpt, inpt):
    snail_number = snail_addition(number1, number2)
    max_magnitude = max(max_magnitude, magnitude(snail_number))

print(max_magnitude)
