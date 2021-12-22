from itertools import cycle
from collections import Counter



def play(start, max_score):
    wins = [0, 0]
    dice = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}  # sum of 3: times
    state = [Counter({(0, start[0]): 1}),  # (score, pawn): quantity
             Counter({(0, start[1]): 1})]
    players = cycle((0, 1))
    step = 0
    for player in players:
        step += 1
        next_state = Counter()
        for st, t1 in state[player].items():
            for d, t2 in dice.items():
                next_pawn = (st[1] + d - 1) % 10 + 1
                next_score = st[0] + next_pawn
                if next_score >= max_score:
                    wins[player] += t1 * t2 * sum(state[player-1].values())
                else:
                    next_state.update({(next_score, next_pawn): t1 * t2})
        state[player] = next_state
        print(f'Player {player + 1}, step {step} {next_state}')
        if len(state[0]) == 0 and len(state[1]) == 0:
            return wins


# start = [4, 8]  # test
start = [9, 4]

max_score = 21

win = play(start, max_score)
print(max(win))
