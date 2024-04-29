import sys
from bisect import bisect_left

input = lambda: sys.stdin.readline().rstrip()

N, M = map(int, input().split())

call = []
limit = [0] * N

for i in range(N):
    c, l = input().split()
    call.append(c)
    limit[i] = int(l)

for _ in range(M):
    print(call[bisect_left(limit, int(input()))])
