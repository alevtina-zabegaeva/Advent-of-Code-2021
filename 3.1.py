from collections import Counter


def char_count(lst, _length):
    counts = [Counter() for _ in range(_length)]
    for number in lst:
        for k, cipher in enumerate(number):
            counts[k].update(list(cipher))
    return counts


# with open('test3.txt', 'r') as f:
with open('input3.txt', 'r') as f:
    inputs = [line.strip() for line in f]

length = len(inputs[0])
inputs_count = char_count(inputs, length)

gamma_rate, epsilon_rate = '', ''

for c in inputs_count:
    gamma_rate += c.most_common()[0][0]
    epsilon_rate += c.most_common()[1][0]

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
