#!/usr/bin/env python3
from collections import Counter

def ol(list, l):
    i = 0
    while i < l and len(list) > 1:
        temp = []
        for b in list:
            temp.append(b[i])
        data = Counter(temp)
        # prefer 1
        if len(data) > 1 and data.most_common(2)[0][1] == data.most_common(2)[1][1]:
            m = "1"
        else:
            m = data.most_common(1)[0][0]
        # qualify by m
        for b in list:
            if b[i] != m:
                list.remove(b)
        i += 1
    return int(list[0], 2)

def sl(list, l):
    i = 0
    while i < l and len(list) > 1:
        temp = []
        for b in list:
            temp.append(b[i])
        data = Counter(temp)
        # prefer 0
        if len(data) > 1:
            if data.most_common(2)[0][1] == data.most_common(2)[1][1]:
                m = "0"
            else:
                m = data.most_common(2)[1][0]
        else:
            m = data.most_common(1)[0][0]
        # qualify by m
        for b in list:
            if b[i] != m:
                print("removed: " + b + " when m=" + str(m))
                list.remove(b)
        i += 1
    return int(list[0], 2)

with open("input.txt") as f:
    list = f.read().splitlines()

l = len(list[0])
oxy = ol(list.copy(), l)
scrub = sl(list.copy(), l)

print(bin(oxy))
print(bin(scrub))

print(oxy * scrub)
