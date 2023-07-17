import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int, input().split())
edge = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    edge[a].append(b)
    edge[b].append(a)
for e in edge:
    e.sort()
visited = [0]*(n+1)
def dfs(x):
    visited[x] = 1
    print(x, end=' ')
    for n in edge[x]:
        if not visited[n]:
            dfs(n)
dfs(v)
print()
visited = [0]*(n+1)
q = deque([v])
while q:
    now = q.popleft()
    if visited[now]:
        continue
    visited[now] = 1
    print(now, end=' ')
    q.extend(edge[now])
print()