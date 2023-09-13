import heapq
import sys
input = sys.stdin.readline
h = []
n = int(input())
for i in range(n):
  temp = int(input())
  if temp:
    heapq.heappush(h, temp)
  elif h:
    print(heapq.heappop(h))
  else:
    print(0)
    