from collections import Counter, deque


# with open('test6.txt', 'r') as f:
with open('input6.txt', 'r') as f:
    for line in f:
        inpt = list(map(int, line.split(',')))

counter = Counter(inpt)
fishes = deque([counter[i] for i in range(9)])
print(fishes)
days = 256

for day in range(1, days + 1):
    fishes.rotate(-1)
    fishes[6] += fishes[8]
    print(day, fishes)

print()
print(sum(fishes))
