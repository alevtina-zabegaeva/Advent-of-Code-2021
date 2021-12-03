from collections import Counter


def char_count(lst, index):
    counts = Counter({'0': 0, '1': 0})
    for number in lst:
        counts.update(list(number[index]))
    return counts


def make_rating(rating, char0, char1, place):
    for i in range(length):
        if len(rating) <= 1:
            break
        count_i = char_count(rating, i)
        rating_i = char0
        if (count_i.most_common()[place][0] == char1 and
                count_i.most_common()[0][1] != count_i.most_common()[1][1]):
            rating_i = char1
        for line in rating.copy():
            if not line[i] == rating_i:
                rating.remove(line)


# with open('test3.txt', 'r') as f:
with open('input3.txt', 'r') as f:
    inputs = [line.strip() for line in f]

length = len(inputs[0])

oxygen_generator_rating = inputs.copy()
make_rating(oxygen_generator_rating, '1', '0', 0)

CO2_scrubber_rating = inputs.copy()
make_rating(CO2_scrubber_rating, '0', '1', -1)

print(oxygen_generator_rating, CO2_scrubber_rating)
print(int(oxygen_generator_rating[0], 2), int(CO2_scrubber_rating[0], 2))
print(int(oxygen_generator_rating[0], 2) * int(CO2_scrubber_rating[0], 2))
