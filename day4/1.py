#!/usr/bin/env python3
import re

# first version got the right answer even though it 
# didn't check horizontal wins correctly lol

def ver(l):
    start = [0, 1, 2, 3, 4]
    if len(l) < 5 or not any(i in l for i in start):
        return False
    c = 1
    for i in start:
        if i in l:
            for n in range(5, 21, 5):
                if (n + i) in l:
                    c += 1
        if c == 5:
            return True
        else:
            c = 1
    return False

def hor(l):
    start = [0, 5, 10, 15, 20]
    if len(l) < 5 or not any(i in l for i in start):
        return False
    for i in start:
        if i in l:
            try:
                test = l[l.index(i) + 4]
                sub = l[l.index(i) : l.index(test)]
                if sub == list(range(min(sub), max(sub) + 1)):
                    return True
            except IndexError:
                continue
    return False

with open("input.txt") as f:
    order = f.readline().strip().split(",")
    grids = f.read().split("\n\n")

# boards as 2d-list
boards = []
for g in grids:
    g = re.sub(r"\n", " ", g)
    boards.append(g.split())

d = {i: [] for i in range(0, len(boards))}

for num in order:
    for i in range(0, len(boards)):
        b = boards[i]
        if num in b:
            index = b.index(num)
            d[i].append(index)
            d[i].sort()
            if ver(d[i]) or hor(d[i]):
                for rm in reversed(d[i]):
                    del b[rm]
                b = [int(x) for x in b]
                print(sum(b) * int(num))
                quit()
