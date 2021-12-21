#!/usr/bin/env python

with open("day17/input.txt") as f:
    line = f.read().split()
    x, y = line[2].replace("x=", "").replace(",", ""), line[3].replace("y=", "")
    x_a, y_a = [int(n) for n in x.split("..")], [int(n) for n in y.split("..")]
    x, xx = min(x_a), max(x_a)
    y, yy = min(y_a), max(y_a)

# based on examples when y_vel > 0 (which it should always be) --> y = -y_vel - 1
# y_min = -y_vel - 1 --> y_vel = -y_min - 1
y_vel = -y - 1

# sum of an arithmetic series
top = 0
while y_vel:
    top += y_vel
    y_vel -= 1

print(top)
