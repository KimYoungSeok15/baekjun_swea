import sys
from collections import deque
input = sys.stdin.readline
n,m,v = map(int, input().split())
edge = sorted([list(map(int, input().split())) for _ in range(m)])
visited = [0]*(n+1)
ans = []
def dfs(s):
    visited[s] = 1
    ans.append(s)
    temp = []
    for e in edge:
        if e[0] == s and not visited[e[1]]:
            temp.append(e[1])
        elif e[1] == s and not visited[e[0]]:
            temp.append(e[0])
    temp.sort()
    for t in temp:
        if not visited[t]:
            dfs(t)
    
dfs(v)
print(*ans)
ans = []
q = deque([v])
visited = [0]*(n+1)
while q:
    now = q.popleft()
    ans.append(now)
    visited[now] = 1
    temp = []
    for e in edge:
        if e[0] == now and not visited[e[1]]:
            temp.append(e[1])
            visited[e[1]] = 1
        if e[1] == now and not visited[e[0]]:
            temp.append(e[0])
            visited[e[0]] = 1
    temp.sort()
    q.extend(temp)
print(*ans)