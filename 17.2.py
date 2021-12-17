# Goal:
x_min, x_max = 124, 174
y_min, y_max = -123, -86

# x_min, x_max = 20, 30
# y_min, y_max = -10, -5

goal = []
vx0_min = int((-1 + (1 + 8*x_min)**0.5) / 2)  # min velocity (-1) to reach x = x_min
for vy0 in range(y_min, abs(y_min)):
    for vx0 in range(vx0_min, x_max + 1):
        looking_further = True
        x, y = 0, 0
        vx, vy = vx0, vy0
        while looking_further:
            x += vx
            y += vy
            if vx > 0:
                vx -= 1
            elif vx < 0:
                vx += 1
            vy -= 1
            if x_min <= x <= x_max and y_min <= y <= y_max:  # goal!
                looking_further = False
                goal.append((vx0, vy0))
            elif x <= 0 or x > x_max or y < y_min:  # flew away
                looking_further = False
print(goal)
print(len(goal))

