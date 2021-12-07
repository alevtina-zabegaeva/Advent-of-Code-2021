def fuel(x):
    f = 0
    for crab in inpt:
        f += abs(crab - x) * (abs(crab - x) + 1) // 2
    return f


# with open('test7.txt', 'r') as f:
with open('input7.txt', 'r') as f:
    inpt = list(map(int, f.read().split(',')))

left, right = min(inpt), max(inpt)
eps = 2
while right - left > eps:
    a = (left * 2 + right) // 3
    b = (left + right * 2) // 3
    if fuel(a) < fuel(b):
        right = b
    else:
        left = a
print(fuel((left + right) // 2))
