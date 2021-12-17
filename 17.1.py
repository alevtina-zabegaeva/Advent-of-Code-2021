# Goal:
x_min, x_max = 124, 174
y_min, y_max = -123, -86

# x_min, x_max = 20, 30
# y_min, y_max = -10, -5

vy00 = y_min                  # min velocity when crossing x = 0
vy0 = -vy00 - 1               # then the initial velocity that was at t = 0
h_max = (vy0*vy0 + vy0) // 2  # maximum height depending on initial velocity
print('Maximum height =', h_max)
