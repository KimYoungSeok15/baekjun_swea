import sys
from collections import deque
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
ans = 0
heap = []
for _ in range(n):
    heappush(heap, int(input()))
for i in range(n-1):
    now = heappop(heap) + heappop(heap)
    ans += now
    heappush(heap, now)
print(ans)