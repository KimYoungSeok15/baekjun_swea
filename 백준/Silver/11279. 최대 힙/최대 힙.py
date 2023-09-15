import sys
import heapq
input = sys.stdin.readline
n = int(input())
h = []
cnt = 0
for i in range(n):
  t = -int(input())
  if not t:
    try:
      print(-heapq.heappop(h))
    except:
      print(0)
  else:
    heapq.heappush(h, t)
 