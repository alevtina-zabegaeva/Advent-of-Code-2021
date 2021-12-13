from collections import defaultdict


def is_small_cave(string):
    return string != 'start' and string != 'end' and string.islower()


def has_2_small_caves(lst):
    for i in range(len(lst) - 1):
        if is_small_cave(lst[i]) and lst[i] in lst[i + 1:]:
            return True
    return False


def next_steps(prev_way):
    last = prev_way[-1]
    next_way = []
    for cave in graph[last]:
        if cave == 'start':
            continue
        if is_small_cave(cave) and has_2_small_caves(prev_way) and cave in prev_way:
            continue
        next_way.append(prev_way + [cave])
    return next_way


# with open('test12.3.txt', 'r') as f:
with open('input12.txt', 'r') as f:
    graph = defaultdict(list)
    for line in f:
        line_lst = line.strip().split('-')
        graph[line_lst[0]].append(line_lst[1])
        graph[line_lst[1]].append(line_lst[0])

# print(graph)

paths = []
way = [['start']]
while len(way) > 0:
    way2 = []
    for w in way:
        next_s = next_steps(w)
        if len(next_s) > 0:
            way2.extend(next_s)
    way = way2.copy()
    for w in way2:
        if w[-1] == 'end':
            paths.append(w)
            way.remove(w)

print(len(paths))
