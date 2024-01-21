import sys
from itertools import permutations
input = sys.stdin.readline
n = int(input())
possible = []
for case in permutations(('1','2','3','4','5','6','7','8','9'), 3):
    possible.append(''.join(case))

pos_idx = [1]*len(possible)

for _ in range(n):
    num, s, b = input().rstrip().split()
    s, b = int(s), int(b)
    
    for i in range(len(pos_idx)):
            
        if pos_idx[i]:
            strike, ball = 0, 0
            for j in range(3):
                if possible[i][j] == num[j]:
                    strike += 1
                elif num.count(possible[i][j]) == 1:
                    ball += 1
            if not (strike == s and ball == b):
                pos_idx[i] = 0
    
print(pos_idx.count(1))