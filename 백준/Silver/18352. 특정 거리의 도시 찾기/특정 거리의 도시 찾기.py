import sys
from collections import deque
input = sys.stdin.readline
n, m, k, x = map(int, input().split())
edge = [[] for _ in range(n+1)]
for _ in range(m):
    t1, t2 = map(int, input().split())
    edge[t1].append(t2)
v = [0]*(n+1)
v[x] = 1
q = deque([[x, 0]])
ans = []
while q:
    now, dis = q.popleft()
    if dis == k:
        ans.append(now)
        continue
    for connected in edge[now]:
        if not v[connected]:
            v[connected] = 1
            q.append([connected, dis+1])
if not ans:
    print(-1)
else:
    for city in sorted(ans):
        print(city)
            
        