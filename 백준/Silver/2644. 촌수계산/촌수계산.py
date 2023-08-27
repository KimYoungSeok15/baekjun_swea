from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
a, b = map(lambda x: int(x)-1, input().split())
child = [[] for _ in range(n)]
for _ in range(int(input())):
  x, y = map(lambda x: int(x)-1, input().split())
  child[x].append(y)
  child[y].append(x)
visited = [0]*n
visited[a] = 1
q = deque([a])
while q:
  now = q.popleft()
  v = visited[now]
  for c in child[now]:
    if not visited[c]:
      q.append(c)
      visited[c] = v + 1
print(visited[b]-1)