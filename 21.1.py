from itertools import cycle
from collections import deque


def play(start, max_score):
    score = [0, 0]
    dice = cycle(range(1, 101))
    pawn = [deque(range(1, 11)), deque(range(1, 11))]
    pawn[0].rotate(-start[0] + 1)
    pawn[1].rotate(-start[1] + 1)
    t = 0
    while True:
        for player in range(2):
            t += 3
            pawn[player].rotate(-next(dice)-next(dice)-next(dice))
            score[player] += pawn[player][0]
            if score[player] >= max_score:
                return score[player-1], t


# start = [4, 8]
start = [9, 4]

max_score = 1000

score2, time = play(start, max_score)
print(score2 * time)
