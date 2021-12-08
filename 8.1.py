# with open('test8.txt', 'r') as f:
with open('input8.txt', 'r') as f:
    inpt = []
    for line in f:
        line = line.split(' | ')
        inpt.append((line[0].split(), line[1].split()))

# inpt = [(['acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab', 'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'],
#          ['cdfeb', 'fcadb', 'cdfeb', 'cdbaf'])]

print(inpt)
otpt = []
for line in inpt:
    for word in line[1]:
        if len(word) == 2 or len(word) == 4 or len(word) == 3 or len(word) == 7:
            otpt.append(word)
print(len(otpt))
