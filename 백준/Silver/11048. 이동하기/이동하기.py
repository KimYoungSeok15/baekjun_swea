from collections import deque
n , m =map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
d = ((1,0),(0,1))
v = [[-1]*m for _ in range(n)]
v[0][0] = board[0][0]
q = deque([[0,0]])
while q:
    r, c = q.popleft()
    now = v[r][c]
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<=nr<n and 0<=nc<m and now+board[nr][nc] > v[nr][nc]:
            q.append([nr,nc])
            v[nr][nc] = now+board[nr][nc]
print(v[n-1][m-1])