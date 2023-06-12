from collections import deque
from itertools import permutations
import sys
from copy import deepcopy
# 8 9 10
# 1 2 8 9 10
input = sys.stdin.readline
cap = list(map(int, input().split()))
memory = [[0,0,cap[2]]]
temp1 = [[0,0,cap[2]]]
while 1:
    temp2 = []
    for t in temp1:
        for from_, to in permutations(range(3),2):
            temp3 = [t[0],t[1],t[2]]
            mass = min(temp3[from_], cap[to] - temp3[to])
            temp3[from_] -= mass
            temp3[to] += mass
            if temp3 not in temp1 and temp3 not in temp2 and temp3 not in memory:
                temp2.append(temp3)
    temp1 = deepcopy(temp2)
    memory.extend(temp1)
    if not temp1:
        break
memory.sort(key=lambda x:x[-1])
for case in memory:
    if case[0] == 0:
        print(case[2], end=' ')