from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
visited = [0]*(n+1)
node = [[] for _ in range(n+1)]
for i in range(m):
  node[edge[i][0]].append(edge[i][1])
  node[edge[i][1]].append(edge[i][0])

ans = 0

for j in range(1,n+1):
  if not visited[j]:
    ans += 1
    q = deque([j])
    while q:
      now = q.popleft()
      for k in node[now]:
        if not visited[k]:
          visited[k] = 1
          q.append(k)

print(ans)