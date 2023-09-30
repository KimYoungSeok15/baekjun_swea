import sys
input = sys.stdin.readline
from collections import deque
n, m = map(int, input().split())
board =[list(map(int, input().split())) for _ in range(n)]
wall = []
for i in range(n):
    for j in range(m):
        if board[i][j]:
            wall.append((i,j))
h, w, sr, sc, er, ec = map(lambda x: int(x)-1, input().split())
d = ((0,1), (1,0), (-1,0), (0,-1))
visited = [[0]*m for _ in range(n)]
q = deque([(sr, sc)])
visited[sr][sc] = 1

def check(i,j):
    global h, w
    for row, col in wall:
        if i <= row <= i+h and j <= col <= j+w:
            return False
    return True

while q:
    r, c = q.popleft()
    now = visited[r][c]
    for dr, dc in d:
        nr, nc = r+dr, c+dc
        if 0<= nr < n-h and 0<= nc < m-w and not visited[nr][nc]:
            if not check(nr,nc):
                continue
            if nr == er and nc == ec:
                print(now)
                exit()
            q.append((nr, nc))
            visited[nr][nc] = now + 1
print(-1)