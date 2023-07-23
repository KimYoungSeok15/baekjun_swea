from collections import deque
n = int(input())
c = int(input())
con = [[] for _ in range(n+1)]
for _ in range(c):
    temp = list(map(int, input().split()))
    con[temp[0]].append(temp[1])
    con[temp[1]].append(temp[0])
visited = [0]*(n+1)
q = deque([1])
ans = 0
while q:
    now = q.popleft()
    visited[now] = 1
    for edge in con[now]:
        if not visited[edge]:
            q.append(edge)
            visited[edge] = 1
            ans += 1

print(ans)
