from collections import deque
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
shark = []
inf = 50**2
visited = [[inf]*m for _ in range(n)]
d = ((1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1))
for i in range(n):
    for j in range(m):
        if board[i][j]:
            shark.append((i,j))
for s in shark:
    q = deque([(s[0],s[1])])
    visited[s[0]][s[1]] = 0
    while q:
        r, c = q.popleft()
        now = visited[r][c]
        for dr, dc in d:
            if 0<=r+dr<n and 0<=c+dc<m and visited[r+dr][c+dc] > now + 1:
                visited[r+dr][c+dc] = now + 1
                q.append((r+dr,c+dc))
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans,visited[i][j])
print(ans)