from collections import defaultdict


def is_small_cave(string):
    return string != 'start' and string != 'end' and string.islower()


def next_steps(prev_way):
    last = prev_way[-1]
    next_way = []
    for cave in graph[last]:
        if cave == 'start':
            continue
        if is_small_cave(cave) and cave in prev_way:
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

new_graph = graph.copy()
while True:
    for point in graph:
        if is_small_cave(point) and len(graph[point]) == 1 and is_small_cave(graph[point][0]):
            new_graph[graph[point][0]].remove(point)
            new_graph.pop(point)
    if len(graph) == len(new_graph):
        break
    graph = new_graph.copy()
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
