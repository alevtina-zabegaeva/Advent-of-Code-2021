# with open('test8.txt', 'r') as f:
with open('input8.txt', 'r') as f:
    inpt = []
    for line in f:
        line = line.split(' | ')
        inpt.append([list(map(set, line[0].split())),
                     list(map(set, line[1].split()))])

# for line in inpt:
#     print(line)

numbers = 0
for line in inpt:
    digits = [''] * 10
    remaining_digits = line[0].copy()
    for word in line[0]:   # _1__4__78_
        if len(word) == 2:
            digits[1] = word
            remaining_digits.remove(word)
        elif len(word) == 4:
            digits[4] = word
            remaining_digits.remove(word)
        elif len(word) == 3:
            digits[7] = word
            remaining_digits.remove(word)
        elif len(word) == 7:
            digits[8] = word
            remaining_digits.remove(word)
    for word in remaining_digits:   # 0_23_56__9
        if len(word | digits[1]) == 7:
            digits[6] = word
        elif len(word - digits[1]) == 3:
            digits[3] = word
        elif len(word) == 6 and len(word - digits[4]) == 2:
            digits[9] = word
        elif len(word) == 6:
            digits[0] = word
        elif len(word - digits[4]) == 3:
            digits[2] = word
        else:
            digits[5] = word
    number = 0
    for i in range(1, 5):
        number += digits.index(line[1][-i]) * 10 ** (i - 1)
    numbers += number
print(numbers)
